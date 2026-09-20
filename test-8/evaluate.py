#!/usr/bin/env python3
"""Reproduce the 91-question Test 8 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {'questions.json': 'd8269591557b3ead80b3da92fb532658f517801ae3fc8c399fbda96d6eea47ab',
 'state.json': '69dd2c0d88774aae93a47d05712c7d16f3fb642621a7fa3283779396cf6f20ab',
 'answer_key.json': '7e68b171f7d1f8440df6e8db94a946125fd92db44da24b60baacd849ebb38c70',
 'responses.json': 'aa85b3e7347d97d3157bb1b52b9a97f3c4143a90704e0bb951f7237cc0e631cc'}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 155
MODULE_COUNTS = {'rw_m1': 30, 'rw_m2': 31, 'math_m1': 16, 'math_m2': 14}
MODULE_NAMES = {'rw_m1': 'Reading and Writing, Module 1', 'rw_m2': 'Reading and Writing, Module 2', 'math_m1': 'Math, Module 1', 'math_m2': 'Math, Module 2'}
# Matches to Tests 1–7, using the normalized text comparison documented in README.md.
REPEATED_IDS = frozenset(['rw_m1_q01',
 'rw_m1_q02',
 'rw_m1_q04',
 'rw_m1_q07',
 'rw_m1_q09',
 'rw_m1_q10',
 'rw_m1_q14',
 'rw_m1_q15',
 'rw_m1_q16',
 'rw_m1_q18',
 'rw_m1_q19',
 'rw_m1_q20',
 'rw_m1_q22',
 'rw_m1_q27',
 'rw_m1_q30',
 'rw_m1_q31',
 'rw_m1_q32',
 'rw_m1_q33',
 'rw_m2_q03',
 'rw_m2_q04',
 'rw_m2_q05',
 'rw_m2_q06',
 'rw_m2_q07',
 'rw_m2_q08',
 'rw_m2_q09',
 'rw_m2_q16',
 'rw_m2_q17',
 'rw_m2_q19',
 'rw_m2_q20',
 'rw_m2_q21',
 'rw_m2_q23',
 'rw_m2_q24',
 'rw_m2_q25',
 'rw_m2_q28',
 'rw_m2_q29',
 'math_m1_q01',
 'math_m1_q02',
 'math_m1_q09',
 'math_m1_q10',
 'math_m1_q18',
 'math_m1_q19',
 'math_m1_q22',
 'math_m1_q25',
 'math_m2_q04',
 'math_m2_q08',
 'math_m2_q10',
 'math_m2_q11',
 'math_m2_q18',
 'math_m2_q22',
 'math_m2_q23',
 'math_m2_q25'])
EXPLANATIONS = {'rw_m1_q20': '“Would” governs both verbs: the lock would increase salinity and create a barrier. '
              '“Creates” cannot follow that shared modal.',
 'rw_m1_q22': '“Though” concludes the contrast in the first clause. The colon then introduces '
              'Hopper’s programming work as an explanation of her broader career.',
 'rw_m1_q23': 'The subject is the plural “accomplishments,” so the verb must be “attest.” The '
              'intervening description of Goldin does not change that agreement.',
 'rw_m1_q24': '“However” modifies the claim that neoclassical writers were not first. The '
              'Renaissance example supports that claim, so the semicolon belongs after “however.”',
 'rw_m1_q25': 'Commas enclose the descriptive phrase beginning “much admired.” The main clause '
              'already has “had … been … gathering,” so adding “were” breaks its structure.',
 'rw_m2_q22': 'The compound subject—Ashford’s gestures and habit—needs the main verb “helped.” '
              '“Helping” leaves the sentence without a main verb.',
 'math_m1_q25': 'A horizontal line meets this downward-opening parabola once only at its vertex. '
                'Completing the square gives y = −(x − 9/2)² − 319/4, so c = −319/4.',
 'math_m2_q11': 'Substitute y = −3x into 4x + y = 15: 4x − 3x = 15, so x = 15.'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for name, value in pairs:
        require(name not in result, f'Duplicate JSON key: {name}')
        result[name] = value
    return result


def in_range(value, low, high):
    return type(value) in (int, float) and math.isfinite(value) and low <= value <= high


def evaluate():
    files = {}
    for name, expected in EXPECTED_HASHES.items():
        content = (ROOT / name).read_bytes()
        require(hashlib.sha256(content).hexdigest() == expected, f'Artifact hash mismatch: {name}')
        files[name] = json.loads(content, object_pairs_hook=unique_object)
    questions, key, response = (files[name] for name in ('questions.json', 'answer_key.json', 'responses.json'))
    require(len(questions) == 91, 'Expected 91 questions')
    require(set(questions) == set(key) == set(response['answers']), 'Missing or unexpected question IDs')
    require(isinstance(files['state.json'], dict) and files['state.json'], 'Expected nonempty state')
    require(in_range(response['evaluation_time_ms'], 0, float('inf')), 'Invalid server time')
    require(in_range(NETWORK_ROUND_TRIP_MS, 0, float('inf')), 'Invalid network time')
    require(len(REPEATED_IDS) == 51 and REPEATED_IDS <= set(questions), 'Invalid overlap cohort')
    require(isinstance(response['model'], str) and response['model'], 'Missing model identifier')
    require(isinstance(response['request_id'], str) and response['request_id'], 'Missing request identifier')
    require(all(type(response['usage'][k]) is int and response['usage'][k] >= 0 for k in ('input_tokens', 'output_tokens')), 'Invalid usage')
    rows = []
    for qid, question in questions.items():
        answer = response['answers'][qid]
        criteria = question['criteria']
        require(question['type'] == answer['type'] == 'choice', f'{qid}: expected Choice format')
        require(isinstance(question['instructions'], str) and question['instructions'].strip(), f'{qid}: empty question')
        require(set(criteria) == set('ABCD'), f'{qid}: expected original A–D options')
        require(all(isinstance(value, str) and value.strip() for value in criteria.values()), f'{qid}: empty option')
        correct = key[qid]['choice']
        selected = answer['choice']
        require(correct in criteria and key[qid]['answer'] == criteria[correct], f'{qid}: answer key does not match option text')
        require(selected in criteria, f'{qid}: invalid selected choice')
        probabilities = answer['probabilities']
        require(set(probabilities) == set(criteria), f'{qid}: unexpected probability labels')
        require(all(in_range(value, 0, 1) for value in probabilities.values()), f'{qid}: invalid probability')
        require(math.isclose(sum(probabilities.values()), 1, rel_tol=0, abs_tol=1e-8), f'{qid}: probabilities do not sum to one')
        require(probabilities[selected] == max(probabilities.values()), f'{qid}: selected choice is not a probability maximum')
        require(in_range(answer['confidence'], 0, 1), f'{qid}: invalid confidence')
        rows.append({
            'id': qid,
            'module': qid.rsplit('_', 1)[0],
            'selected': selected,
            'expected': correct,
            'selected_text': criteria[selected],
            'expected_text': criteria[correct],
            'correct': selected == correct,
            'confidence': answer['confidence'],
        })
    for module, count in MODULE_COUNTS.items():
        require(sum(row['module'] == module for row in rows) == count, f'{module}: unexpected question count')
    require({row['id'] for row in rows if not row['correct']} == set(EXPLANATIONS), 'Explanations do not match incorrect answers')
    return rows, response


def score(rows):
    return f"{sum(row['correct'] for row in rows)}/{len(rows)} ({100 * sum(row['correct'] for row in rows) / len(rows):.1f}%)"


def score_table(rows):
    groups = [(name, [row for row in rows if row['module'] == module]) for module, name in MODULE_NAMES.items()]
    groups += [
        ('**Reading and Writing**', [row for row in rows if row['module'].startswith('rw_')]),
        ('**Math**', [row for row in rows if row['module'].startswith('math_')]),
        ('**Overall**', rows),
    ]
    return ['| Group | Correct | Accuracy |', '|---|---:|---:|'] + [
        f"| {name} | {sum(row['correct'] for row in group)}/{len(group)} | {100 * sum(row['correct'] for row in group) / len(group):.1f}% |"
        for name, group in groups
    ]


def timing_lines(response):
    server = response['evaluation_time_ms']
    return [
        '## Reported usage and timing', '',
        '| Metric | Value |', '|---|---:|',
        f"| Input tokens | {response['usage']['input_tokens']:,} |",
        f"| Output tokens | {response['usage']['output_tokens']:,} |",
        f'| Server time | {server:.0f} ms |',
        f'| Network round trip | {NETWORK_ROUND_TRIP_MS} ms |',
        f'| Calculated combined time | ≈ {server + NETWORK_ROUND_TRIP_MS:.0f} ms |', '',
        f'Token counts and server time come from the service export (`evaluation_time_ms = {server}`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.', '',
    ]


def cell(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def overlap_lines(rows):
    repeated = [row for row in rows if row['id'] in REPEATED_IDS]
    remaining = [row for row in rows if row['id'] not in REPEATED_IDS]
    return [
        '## Overlap with earlier tests', '',
        'The [test overview](README.md#overlap-and-question-ids) identifies 51 questions with the same normalized stem and answer texts in Tests 1–7. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 8 score.', '',
        '| Test 8 cohort | Correct | Accuracy |', '|---|---:|---:|',
        *[f"| {name} | {sum(row['correct'] for row in group)}/{len(group)} | {100 * sum(row['correct'] for row in group) / len(group):.1f}% |" for name, group in [('Matches an earlier selected question', repeated), ('No exact earlier match found', remaining)]], '',
        'This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–8 counts repeated questions more than once unless an explicit deduplication rule is applied.', '',
    ]


def reports(rows, response):
    headline = f"**{response['model']}: {score(rows)} correct.**"
    source = 'The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-8-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-8/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 8 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Six errors are in Reading and Writing, all testing Standard English conventions. Two errors are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *overlap_lines(rows), *timing_lines(response),
        '## Validation and provenance', '',
        'All 91 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 8', '', headline, '',
        '## Evaluation overview', '',
        '| Field | Value |', '|---|---|',
        f"| Model | `{response['model']}`, as reported in the export |",
        '| Interface | TypeSafe Choice questions with original A–D options |',
        '| Task | English-language SAT Reading and Writing and Math |',
        '| Dataset | 91 original multiple-choice questions: 61 Reading and Writing and 30 Math |',
        '| Evaluated response exports | 1 |',
        f"| Request identifier | `{response['request_id']}` |",
        '| Response artifact | [responses.json](responses.json), preserved byte-for-byte |', '',
        '## Data and method', '',
        'The source is College Board’s [SAT Practice Test #8](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-8-digital.pdf), the 56-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 91 are included. Fifteen visual items and fourteen numerical-response items are excluded, with no overlap between these exclusion groups. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 91 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The eight incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Six errors are in Reading and Writing and two are in Math.', '',
        *overlap_lines(rows), *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.',
        '- **Public and repeated questions:** Training overlap, retrieval, and memorization have not been investigated. Fifty-one selected questions repeat earlier test content under the documented normalization, so pooled results must account for repeated items.',
        '- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.',
        '- **Confidence:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation.',
        '- **Model details:** Architecture, parameter count, training data, training cutoff, and serving hardware are not established by the available evidence.', '',
        '## Reproducibility', '', reproduction + ' [RESULTS.md](RESULTS.md) records the input, answer-key, and response hashes.', '',
        'This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. It does not establish general model reliability or suitability for decisions about individual students.', '',
        'Generated by `python3 evaluate.py --write`.', '',
    ]
    return {'RESULTS.md': '\n'.join(results).encode(), 'MODEL_CARD.md': '\n'.join(card).encode()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true', help='Verify the committed reports against a fresh calculation')
    mode.add_argument('--write', action='store_true', help='Regenerate RESULTS.md and MODEL_CARD.md')
    args = parser.parse_args()
    rows, response = evaluate()
    for name, content in reports(rows, response).items():
        path = ROOT / name
        if args.write:
            path.write_bytes(content)
        elif args.check:
            require(path.is_file() and path.read_bytes() == content, f'Report differs from recalculation: {name}')
    for label, group in [('Overall', rows), ('Reading and Writing', [r for r in rows if r['module'].startswith('rw_')]), ('Math', [r for r in rows if r['module'].startswith('math_')])]:
        print(f'{label}: {score(group)}')
    print('All 91 responses validated. ' + ('Committed reports match.' if args.check else 'Reports regenerated.' if args.write else 'No files changed.'))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
