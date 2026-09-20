#!/usr/bin/env python3
"""Reproduce the current 91-question Jev evaluation using only Python's standard library."""

import argparse
import csv
import io
import json
import math

from validate import ROOT, load, require, validate_dataset


def score(rows):
    correct = sum(row['correct'] for row in rows)
    return {'correct': correct, 'total': len(rows), 'accuracy_percent': round(100 * correct / len(rows), 4)}


def grade(questions, key, manifest, response):
    require(set(response['answers']) == set(questions), 'Missing or unexpected response IDs')
    entries = {row['id']: row for row in manifest['questions']}
    rows = []
    for qid, question in questions.items():
        answer = response['answers'][qid]
        require(answer['type'] == 'choice', f'{qid}: expected Choice response')
        selected = answer['choice']
        require(selected in question['criteria'], f'{qid}: invalid selected choice')
        probabilities = answer['probabilities']
        require(set(probabilities) == set(question['criteria']), f'{qid}: probability labels differ from choices')
        require(all(type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1 for value in probabilities.values()), f'{qid}: invalid probability')
        require(math.isclose(sum(probabilities.values()), 1, abs_tol=1e-8), f'{qid}: probabilities do not sum to one')
        require(probabilities[selected] == max(probabilities.values()), f'{qid}: selected choice is not a probability maximum')
        confidence = answer['confidence']
        require(type(confidence) in (int, float) and math.isfinite(confidence) and 0 <= confidence <= 1, f'{qid}: invalid confidence')
        correct_choice = key[qid]['choice']
        rows.append({
            'question_id': qid,
            'section': 'Reading and Writing' if qid.startswith('rw_') else 'Math',
            'module': entries[qid]['module'],
            'original_question_number': entries[qid]['number'],
            'jev_choice': selected,
            'correct_choice': correct_choice,
            'correct': selected == correct_choice,
            'jev_answer_text': question['criteria'][selected],
            'correct_answer_text': question['criteria'][correct_choice],
            'confidence': confidence,
            'selected_option_probability': probabilities[selected],
            'correct_option_probability': probabilities[correct_choice],
        })
    return rows


def summarize(rows, response, provenance):
    timing_context = provenance['evaluation']['timing_context']
    server_time_ms = response['evaluation_time_ms']
    network_round_trip_ms = timing_context['network_round_trip_ms']
    require(all(type(value) in (int, float) and math.isfinite(value) and value >= 0 for value in (server_time_ms, network_round_trip_ms)), 'Invalid timing value')
    return {
        'dataset_version': provenance['dataset_version'],
        'model': response['model'],
        'request_id': response['request_id'],
        'overall': score(rows),
        'sections': {section: score([row for row in rows if row['section'] == section]) for section in ['Reading and Writing', 'Math']},
        'modules': {module: score([row for row in rows if row['question_id'].startswith(module)]) for module in ['rw_m1','rw_m2','math_m1','math_m2']},
        'wrong_question_ids': [row['question_id'] for row in rows if not row['correct']],
        'validation': {
            'all_91_expected_answers_present': True,
            'all_choices_valid': True,
            'all_probability_sums_equal_one': True,
            'all_choices_are_probability_maxima': True,
            'all_confidences_in_range': True,
            'all_keys_match_official_original_choices': True,
            'prepared_inputs_and_response_hashes_verified': True,
        },
        'input_sha256': provenance['evaluation']['input_sha256'],
        'response_sha256': provenance['sha256']['responses.json'],
        'reported_usage': response.get('usage'),
        'reported_evaluation_time_ms': response.get('evaluation_time_ms'),
        'timing': {
            'server_time_ms': server_time_ms,
            'server_time_source': provenance['evaluation']['evaluation_time_semantics'],
            **timing_context,
            'calculated_combined_time_ms': server_time_ms + network_round_trip_ms,
        },
        'limitations': [
            'The supplied response export does not embed the submitted request or sampling settings.',
            'One evaluated response export; not an official SAT scaled score.',
            'Service-reported evaluation time is not independently measured end-to-end latency.',
            'Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation.',
        ],
    }


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def artifacts(rows, summary, explanations):
    errors = [row for row in rows if not row['correct']]
    require(set(explanations) == {row['question_id'] for row in errors}, 'Error explanations do not match the current errors')
    for row in rows:
        row['explanation_if_wrong'] = explanations.get(row['question_id'], '')
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    total = summary['overall']
    report = [
        '# SAT Practice Test 5 evaluation results', '',
        f"**{summary['model']}: {total['correct']}/{total['total']} correct ({total['accuracy_percent']:.1f}%).**", '',
        'The response export contains all 91 expected answers. The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-5-digital.pdf), page 4, supplies the answer letters. Each correct answer receives one point; excluded questions are not scored.', '',
    ]
    for title, groups in [('Sections', summary['sections']), ('Modules', summary['modules'])]:
        report.extend([f'## {title}', '', '| Group | Correct | Accuracy |', '|---|---:|---:|'])
        for name, result in groups.items():
            report.append(f"| {name} | {result['correct']}/{result['total']} | {result['accuracy_percent']:.1f}% |")
        report.append('')
    report.extend(['## Incorrect answers', '', 'Confidence is the reported `confidence` field, distinct from the probability assigned to the selected option.', '', '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|'])
    for row in errors:
        report.append(f"| `{row['question_id']}` | {row['jev_choice']}: {cell(row['jev_answer_text'])} | {row['correct_choice']}: {cell(row['correct_answer_text'])} | {row['confidence']:.0%} |")
    report.extend(['', '## Explanations', ''])
    for row in errors:
        report.append(f"- **`{row['question_id']}`:** {explanations[row['question_id']]}")
    timing = summary['timing']
    report.extend(['', '## Reported usage and timing', '',
        f"The service reports {summary['reported_usage']['input_tokens']:,} input tokens and {summary['reported_usage']['output_tokens']:,} output tokens.", '',
        '| Timing | Value |', '|---|---:|',
        f"| Server time | {timing['server_time_ms']:.0f} ms |",
        f"| Network round trip to {timing['network_region']} | {timing['network_round_trip_ms']:.0f} ms |",
        f"| Calculated combined time | ≈ {timing['calculated_combined_time_ms']:.0f} ms |", '',
        f"Server time is the exported `evaluation_time_ms = {summary['reported_evaluation_time_ms']}`, with its meaning confirmed by the user. Network time is user-reported. The combined time adds these two values; it is not a separate end-to-end measurement.", '',
        '## Provenance and reproduction', '',
        'The supplied export is preserved byte-for-byte in [responses.json](responses.json). Its question IDs exactly match the dataset. Input and response hashes are recorded in [provenance.json](provenance.json). The export does not include the original service request or sampling settings.', '',
        'Run `python3 evaluate.py --check` to reproduce and verify the committed results. See [all 91 grading records](results/per_question.csv), the [machine-readable summary](results/summary.json), and the [model evaluation card](MODEL_CARD.md). This is raw subset accuracy, not an official SAT scaled score.', '',
        'Generated by `python3 evaluate.py --write`.', '',
    ])
    return {
        'results/summary.json': (json.dumps(summary, indent=2, ensure_ascii=False) + '\n').encode(),
        'results/per_question.csv': stream.getvalue().encode(),
        'RESULTS.md': '\n'.join(report).encode(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Verify that committed results match a fresh calculation')
    mode.add_argument('--write', action='store_true', help='Regenerate result JSON, CSV, and RESULTS.md')
    args = parser.parse_args()
    questions, key, manifest, provenance, response = validate_dataset(verbose=False)
    rows = grade(questions, key, manifest, response)
    summary = summarize(rows, response, provenance)
    require(summary['overall'] == provenance['evaluation']['score'], 'Calculated score differs from provenance')
    outputs = artifacts(rows, summary, load(ROOT / 'results/error_explanations.json'))
    for name, content in outputs.items():
        path = ROOT / name
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        elif args.check:
            require(path.is_file() and path.read_bytes() == content, f'Stored results differ from recalculation: {name}')
    for name, result in [('Overall', summary['overall']), *summary['sections'].items()]:
        print(f"{name}: {result['correct']}/{result['total']} ({result['accuracy_percent']:.1f}%)")
    print(f"Incorrect answers: {len(summary['wrong_question_ids'])}.")
    print('Response validation passed. ' + ('Committed results match.' if args.check else 'Results regenerated.' if args.write else 'No files changed.'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
