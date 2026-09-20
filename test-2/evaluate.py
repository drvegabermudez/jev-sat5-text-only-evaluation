#!/usr/bin/env python3
"""Reproduce the 93-question Test 2 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {'questions.json': 'a944c25ddb43f17f63191f8f3377d48b13e849bd2992585c8fe796b3465cbf09',
 'state.json': 'a90d86cabef79b232ce069b96e382e4e8cbc6634148167049ef0977cc3af4f08',
 'answer_key.json': 'f80a39685cb5d6ede29f33ac142eced52c509a9ba12efc762ecf4996870063b1',
 'responses.json': 'fd7b93a9a832760b4d8e6aa9deb39b3527275de68e36de2de1d49ec3dcc1b9cd'}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 120
MODULE_COUNTS = {'rw_m1': 32, 'rw_m2': 30, 'math_m1': 14, 'math_m2': 17}
MODULE_NAMES = {
    'rw_m1': 'Reading and Writing, Module 1',
    'rw_m2': 'Reading and Writing, Module 2',
    'math_m1': 'Math, Module 1',
    'math_m2': 'Math, Module 2',
}
EXPLANATIONS = {'rw_m1_q25': 'The phrase beginning “an apt assessment” comments on the preceding observation and '
              'must be set off with a comma. Choice D omits that required boundary punctuation.',
 'rw_m2_q19': 'The opening clause begins with “While” and must be separated from the main clause, '
              '“others look to the past,” by a comma. Adding “but” at that boundary leaves no '
              'independent main clause.',
 'rw_m2_q22': 'The introductory phrase “In assessing the films…” must modify the people doing the '
              'assessing. Choice A places “many critics” directly after it; choice C begins with '
              '“there,” leaving the modifier dangling.',
 'rw_m2_q23': 'Semicolons separate the three projects because each list item already contains '
              'commas. The first item ends with its date, 2009, so the semicolon belongs after '
              '“2009”; commas set off the app and network names.',
 'math_m1_q11': 'The requested expression is four times the given left-hand side: 16x + 8 = 4(4x + '
                '2) = 4 × 12 = 48, choice B.',
 'math_m1_q18': 'Let c be the number of children, so there are 21 − c adults. Then 80(21 − c) + '
                '60c = 1,440, giving 1,680 − 20c = 1,440 and c = 12, choice C. The selected value, '
                '9, is the number of adults.',
 'math_m2_q16': 'Rearranging 2y + 18x = 9 gives y = −9x + 9/2, so line p has slope −9. A '
                'perpendicular line has slope −1/(−9) = 1/9, choice C.',
 'math_m2_q24': 'At the y-axis, x = 0. In choice C, substitution gives 16 + (y − 9)² = 16, so y = '
                '9 is the only intersection. Choices A and B have no y-axis intersections; choice '
                'D has two.'}


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
    require(len(questions) == 93, 'Expected 93 questions')
    require(set(questions) == set(key) == set(response['answers']), 'Missing or unexpected question IDs')
    require(isinstance(files['state.json'], dict) and files['state.json'], 'Expected nonempty state')
    require(in_range(response['evaluation_time_ms'], 0, float('inf')), 'Invalid server time')
    require(in_range(NETWORK_ROUND_TRIP_MS, 0, float('inf')), 'Invalid network time')
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


def reports(rows, response):
    headline = f"**{response['model']}: {score(rows)} correct.**"
    source = 'The [College Board scoring guide mirrored by APCORE](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-2-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-2/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 2 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Four errors are in Reading and Writing, all testing Standard English conventions; four are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *timing_lines(response),
        '## Validation and provenance', '',
        'All 93 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 2', '', headline, '',
        '## Evaluation overview', '',
        '| Field | Value |', '|---|---|',
        f"| Model | `{response['model']}`, as reported in the export |",
        '| Interface | TypeSafe Choice questions with original A–D options |',
        '| Task | English-language SAT Reading and Writing and Math |',
        '| Dataset | 93 original multiple-choice questions: 62 Reading and Writing and 31 Math |',
        '| Evaluated response exports | 1 |',
        f"| Request identifier | `{response['request_id']}` |",
        '| Response artifact | [responses.json](responses.json), preserved byte-for-byte |', '',
        '## Data and method', '',
        'The source is College Board’s [SAT Practice Test #2](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/sat-practice-test-2-digital.pdf), the 56-page nonadaptive paper form for the digital SAT, preserved on APCORE’s public mirror. Of its 120 original questions, 93 are included. Thirteen visual items and fourteen numerical-response items are excluded, with no overlap between these two groups. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 93 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The eight incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Four errors are in Reading and Writing and four are in Math.', '',
        *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Tests 1, 2, 5, 6, and 7 contain different selected questions, so their scores and timings do not isolate a change in model capability or speed.',
        '- **Public test:** Training overlap, retrieval, and memorization have not been investigated. A normalized text-overlap check across Tests 1–7 found no identical selected question stems; that does not establish independence from training data.',
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
    print('All 93 responses validated. ' + ('Committed reports match.' if args.check else 'Reports regenerated.' if args.write else 'No files changed.'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
