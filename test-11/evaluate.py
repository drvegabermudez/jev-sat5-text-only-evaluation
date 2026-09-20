#!/usr/bin/env python3
"""Reproduce the 87-question Test 11 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {'questions.json': 'bbaefe864750788e4094d6032acfe663f843845617525ee17be7a87651284984',
 'state.json': '847e427f00270c39015e8a749763a750907ec77a3eaf58ae074578fdeae1cf70',
 'answer_key.json': 'ba67bca064be38a7b3119f690243b8ebe69de7fd0c0051f31f42dbfd474dc39a',
 'responses.json': 'aa581bc42b8c7450873f3cc23c67d3f911f996e171482f7f6f0a3c0a3e682e70'}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 169
# The original export totals 0.99 for this item; preserve it without normalization.
PROBABILITY_SUM_EXCEPTIONS = {'math_m2_q26': 0.99}
MODULE_COUNTS = {'rw_m1': 32, 'rw_m2': 30, 'math_m1': 14, 'math_m2': 11}
MODULE_NAMES = {'rw_m1': 'Reading and Writing, Module 1', 'rw_m2': 'Reading and Writing, Module 2', 'math_m1': 'Math, Module 1', 'math_m2': 'Math, Module 2'}

EXPLANATIONS = {'rw_m1_q22': 'The comma after “1804” closes the parenthetical phrase “ratified in 1804,” matching '
              'the comma after “amendment.” The main clause then continues with “separated.”',
 'rw_m1_q25': 'The main clause is “Helical swimming … bestows similar advantages.” The comma '
              'starts the intervening description. Adding “is” creates an incompatible second main '
              'verb.',
 'rw_m2_q18': 'A uniform methane value simplifies an uncertain real distribution, so differences '
              'between simulated and observed weather are expected. Choice D instead discusses '
              'inconsistencies among simulations, which the passage does not establish.',
 'rw_m2_q20': 'The construction is “enables someone to do something”: ArcGIS enables cartographers '
              'to create maps. The bare verb “create” does not fit.',
 'rw_m2_q25': 'The opening description refers to recordings, so “electrograms” must immediately '
              'follow it. Choice B incorrectly attaches that description to soccer players.',
 'rw_m2_q26': 'The main clause says that scientists adapted the test. “Searching” describes those '
              'scientists; “searched” improperly adds another main verb without a conjunction.',
 'rw_m2_q29': 'The usual 20–50 km heights support the claim that jets reaching about 80 km are '
              'outliers. “Indeed” introduces that support; “nevertheless” incorrectly signals a '
              'contrast.',
 'math_m2_q26': 'In right triangle XYW, tan Y = WX/WY = 429/572 = 3/4. Since Y and Z are '
                'complementary angles, tan Z = 1/tan Y = 4/3, choice D.'}


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
    require(len(questions) == 87, 'Expected 87 questions')
    require(set(questions) == set(key) == set(response['answers']), 'Missing or unexpected question IDs')
    require(isinstance(files['state.json'], dict) and files['state.json'], 'Expected nonempty state')
    require(in_range(response['evaluation_time_ms'], 0, float('inf')), 'Invalid server time')
    require(in_range(NETWORK_ROUND_TRIP_MS, 0, float('inf')), 'Invalid network time')
    require(set(PROBABILITY_SUM_EXCEPTIONS) <= set(questions), 'Invalid probability exception ID')
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
        expected_total = PROBABILITY_SUM_EXCEPTIONS.get(qid, 1.0)
        require(math.isclose(sum(probabilities.values()), expected_total, rel_tol=0, abs_tol=1e-8), f'{qid}: unexpected probability total')
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
    return [
        '## Overlap with earlier tests', '',
        'No exact matches of normalized question stems and answer texts were found against the selected sets for Tests 1–10. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. All 87 selected Test 11 questions therefore contribute to the distinct-question aggregate under this matching rule.', '',
        'This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Similar templates and partial text overlap may remain. See the [test overview](README.md#overlap-and-question-ids) for the comparison method.', '',
    ]


def reports(rows, response):
    headline = f"**{response['model']}: {score(rows)} correct.**"
    source = 'The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-11-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-11/evaluate.py --check` from the repository root. The script verifies the artifact hashes, checks all responses with the documented probability-total exception, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 11 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Seven errors are in Reading and Writing: five test Standard English conventions, one tests inference, and one tests a logical transition. One error is in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *overlap_lines(rows), *timing_lines(response),
        '## Validation and provenance', '',
        'All 87 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option. Of the 87 probability distributions, 86 sum to 1. The distribution for `math_m2_q26` totals 0.99 (A: 0.04, B: 0.68, C: 0.08, D: 0.19). The export is preserved without normalization. The selected answer B is incorrect; the official answer is D. Grading by selected answer is unaffected by the probability total. The evaluator permits this specific recorded total and rejects any other unexpected total.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 11', '', headline, '',
        '## Evaluation overview', '',
        '| Field | Value |', '|---|---|',
        f"| Model | `{response['model']}`, as reported in the export |",
        '| Interface | TypeSafe Choice questions with original A–D options |',
        '| Task | English-language SAT Reading and Writing and Math |',
        '| Dataset | 87 original multiple-choice questions: 62 Reading and Writing and 25 Math |',
        '| Evaluated response exports | 1 |',
        f"| Request identifier | `{response['request_id']}` |",
        '| Response artifact | [responses.json](responses.json), preserved byte-for-byte |', '',
        '## Data and method', '',
        'The source is College Board’s [SAT Practice Test #11](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-11-digital.pdf), the 52-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 87 are included. Twenty visual items and thirteen additional numerical-response items are excluded; one visual exclusion also requires a numerical response. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 87 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The eight incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Seven errors are in Reading and Writing and one is in Math.', '',
        *overlap_lines(rows), *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.',
        '- **Public questions:** Training overlap, retrieval, and memorization have not been investigated. No exact matches were found against selected questions in Tests 1–10, but this does not establish independence from training data or tested skills.',
        '- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.',
        '- **Confidence and probability totals:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation. The probabilities for `math_m2_q26` total 0.99; all other distributions total 1. The original values are preserved, and this anomaly does not affect grading by selected answer.',
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
    print('All 87 responses checked; one probability-total anomaly documented. ' + ('Committed reports match.' if args.check else 'Reports regenerated.' if args.write else 'No files changed.'))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
