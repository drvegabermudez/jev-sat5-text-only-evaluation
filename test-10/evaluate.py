#!/usr/bin/env python3
"""Reproduce the 91-question Test 10 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {'questions.json': '3c5a989e53063c688ccdbf0f21ae41d3fd54ba985e6a2f9097084ef5d79801e6',
 'state.json': 'fb11e919adb591e66a830ed703028088550cf895974410fa8a4c8e5a9b17eb53',
 'answer_key.json': '3dd740f947c03c9856283d6fcc4553c1c18187246bc1bb909c2a4b86bc0b58c9',
 'responses.json': '4f36c3296d614c14b4c7db6cfa827e188ca8ec9e5cb201c628e5c9a01ddfc974'}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 118
MODULE_COUNTS = {'rw_m1': 32, 'rw_m2': 29, 'math_m1': 14, 'math_m2': 16}
MODULE_NAMES = {'rw_m1': 'Reading and Writing, Module 1', 'rw_m2': 'Reading and Writing, Module 2', 'math_m1': 'Math, Module 1', 'math_m2': 'Math, Module 2'}
# Matches to Tests 1–9, using the normalized text comparison documented in README.md.
REPEATED_IDS = frozenset(['rw_m1_q02',
 'rw_m1_q03',
 'rw_m1_q04',
 'rw_m1_q08',
 'rw_m1_q09',
 'rw_m1_q10',
 'rw_m1_q12',
 'rw_m1_q14',
 'rw_m1_q15',
 'rw_m1_q16',
 'rw_m1_q19',
 'rw_m1_q20',
 'rw_m1_q21',
 'rw_m1_q22',
 'rw_m1_q23',
 'rw_m1_q24',
 'rw_m1_q28',
 'rw_m1_q33',
 'rw_m2_q01',
 'rw_m2_q02',
 'rw_m2_q03',
 'rw_m2_q09',
 'rw_m2_q10',
 'rw_m2_q17',
 'rw_m2_q18',
 'rw_m2_q19',
 'rw_m2_q20',
 'rw_m2_q21',
 'rw_m2_q22',
 'rw_m2_q25',
 'rw_m2_q26',
 'rw_m2_q30',
 'rw_m2_q31',
 'math_m1_q03',
 'math_m1_q05',
 'math_m1_q10',
 'math_m1_q11',
 'math_m1_q15',
 'math_m1_q18',
 'math_m1_q23',
 'math_m1_q24',
 'math_m2_q10',
 'math_m2_q17',
 'math_m2_q23',
 'math_m2_q24'])
EXPLANATIONS = {'rw_m1_q22': '“Forcing” introduces a phrase describing the consequence of food becoming '
              'unavailable. The main clause already has its verb, so “forces” cannot be added this '
              'way.',
 'rw_m1_q23': 'A comma separates the introductory “While” clause from “others look to the past.” '
              'The contrast is already established by “While”; adding “but” breaks that structure.',
 'rw_m1_q26': '“Their” refers back to the plural “types of pop culture references.” The singular '
              '“its” does not agree with that antecedent.',
 'math_m1_q10': 'The requested expression is four times the given one: 16x + 8 = 4(4x + 2) = 4(12) '
                '= 48, choice B.',
 'math_m1_q23': 'All four circles have radius 4. A circle touches the y-axis once when its center '
                'is exactly 4 units from that axis. Choice C has center (4, 9) and touches at (0, '
                '9); choice B has center (8, 4) and misses the y-axis.',
 'math_m1_q25': 'An increase of 1,800% adds 18x to the original x. Thus 19x = 684 and x = 36, '
                'choice D. Dividing by 18 instead gives the selected 38.'}


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
    require(len(REPEATED_IDS) == 45 and REPEATED_IDS <= set(questions), 'Invalid overlap cohort')
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
        'The [test overview](README.md#overlap-and-question-ids) identifies 45 questions with the same normalized stem and answer texts in Tests 1–9. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 10 score.', '',
        '| Test 10 cohort | Correct | Accuracy |', '|---|---:|---:|',
        *[f"| {name} | {sum(row['correct'] for row in group)}/{len(group)} | {100 * sum(row['correct'] for row in group) / len(group):.1f}% |" for name, group in [('Matches an earlier selected question', repeated), ('No exact earlier match found', remaining)]], '',
        'This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–10 counts repeated questions more than once unless an explicit deduplication rule is applied.', '',
    ]


def reports(rows, response):
    headline = f"**{response['model']}: {score(rows)} correct.**"
    source = 'The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-10-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-10/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 10 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Three errors are in Reading and Writing, all testing Standard English conventions. Three errors are in Math. All six errors are in Module 1 of their respective sections. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *overlap_lines(rows), *timing_lines(response),
        '## Validation and provenance', '',
        'All 91 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer is among the options with the highest reported probability. Answer-key text matches the corresponding original option. For `math_m1_q10`, A and B each have a reported probability of 0.48. The export selects A; the correct answer is B, so this item is graded incorrect. Tied probabilities do not override the exported selection.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 10', '', headline, '',
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
        'The source is College Board’s [SAT Practice Test #10](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-10-digital.pdf), the 56-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 91 are included. Fifteen visual items and fourteen numerical-response items are excluded, with no overlap between these exclusion groups. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 91 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The six incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Three errors are in Reading and Writing and three are in Math; both Module 2 subsets were answered entirely correctly.', '',
        *overlap_lines(rows), *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.',
        '- **Public and repeated questions:** Training overlap, retrieval, and memorization have not been investigated. Forty-five selected questions repeat earlier test content under the documented normalization, so pooled results must account for repeated items.',
        '- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.',
        '- **Confidence and ties:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation. For `math_m1_q10`, the incorrect selected answer A and the correct answer B both have reported probability 0.48. Grading uses the exported choice A without overriding the selection.',
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
