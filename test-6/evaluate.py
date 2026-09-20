#!/usr/bin/env python3
"""Reproduce the 88-question Test 6 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {
    'questions.json': '90165a44f9070de0a157365579815b7d0ee7cd6f9d2cb9cd61b4fa57d109f300',
    'state.json': '403a01dcd56408533f88aed02f7172ed54cb2404d3caac514d61f614a6613949',
    'answer_key.json': '0e74b92d8396721c989e556046f1ad1d71d6333a319de979489f0b682e404561',
    'responses.json': '121fd1e39783409408b4effbb1a4cebd6b9c8d830e5422d8269d551e90f16c29',
}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 153
NETWORK_REGION = 'us-west'
MODULE_COUNTS = {'rw_m1': 30, 'rw_m2': 31, 'math_m1': 12, 'math_m2': 15}
MODULE_NAMES = {
    'rw_m1': 'Reading and Writing, Module 1',
    'rw_m2': 'Reading and Writing, Module 2',
    'math_m1': 'Math, Module 1',
    'math_m2': 'Math, Module 2',
}
EXPLANATIONS = {
    'rw_m1_q22': 'The sentence reports what the researchers investigated. This indirect question uses subject–verb order (“people perceive”) and ends with a period.',
    'rw_m1_q24': 'A period ends the first complete sentence. “Creations so small that they are best viewed through a microscope” then introduces and describes the subject of the next sentence, “Wigan’s sculptures.” A comma after “microsculptures” does not properly separate the two complete sentences.',
    'rw_m1_q25': '“A ray diagram reveals how this works” is a complete sentence. The next sentence begins with “Because,” introducing the reason for the statement that follows. Choice D leaves a comma splice within the explanation.',
    'rw_m2_q23': 'Semicolons separate the three list items because each contains an internal comma: natural debris, man-made trash, and traditional art supplies. A comma before “such as plastic bags” introduces the example within the second item.',
    'rw_m2_q24': '“However” closes the statement contrasting the many Latin American dances with the five included in competition. A colon then introduces the list of five dances. The list is not an independent clause that could follow the semicolon in choice D.',
    'rw_m2_q26': 'The subject of the main clause is plural, “the toxins,” so the verb is “increase.” The singular “organism” belongs to the intervening clause and does not control the main verb.',
    'math_m2_q23': 'Rewrite (1.84)^(x/4) as ((1.84)^(1/4))^x. Thus 1 + p/100 = (1.84)^(1/4), giving p = 100((1.84)^(1/4) − 1) ≈ 16.47. The closest choice is A, 16.',
}


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
    require(len(questions) == 88, 'Expected 88 questions')
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
        f'| Network round trip to {NETWORK_REGION} | {NETWORK_ROUND_TRIP_MS} ms |',
        f'| Calculated combined time | ≈ {server + NETWORK_ROUND_TRIP_MS:.0f} ms |', '',
        f'Token counts and server time come from the service export (`evaluation_time_ms = {server}`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.', '',
    ]


def cell(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def reports(rows, response):
    headline = f"**{response['model']}: {score(rows)} correct.**"
    source = 'The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-6-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-6/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 6 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Six errors are in Standard English conventions; one is in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *timing_lines(response),
        '## Validation and provenance', '',
        'All 88 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 6', '', headline, '',
        '## Evaluation overview', '',
        '| Field | Value |', '|---|---|',
        f"| Model | `{response['model']}`, as reported in the export |",
        '| Interface | TypeSafe Choice questions with original A–D options |',
        '| Task | English-language SAT Reading and Writing and Math |',
        '| Dataset | 88 original multiple-choice questions: 61 Reading and Writing and 27 Math |',
        '| Evaluated response exports | 1 |',
        f"| Request identifier | `{response['request_id']}` |",
        '| Response artifact | [responses.json](responses.json), preserved byte-for-byte |', '',
        '## Data and method', '',
        'The source is College Board’s [SAT Practice Test #6](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-6-digital.pdf), © 2024, nonadaptive paper form, cover identifiers `WX4P0010` and `6VSL02`. Of its 120 original questions, 88 are included. Twenty items with graphs, diagrams, or tables and twelve additional numerical-response items are excluded; two visual exclusions are also numerical-response items. The [test overview](README.md) lists every omission.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 88 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The seven incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Six errors concern grammar or punctuation and one concerns exponential growth.', '',
        *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Tests 5 and 6 contain different selected questions, so their scores and timings do not isolate a change in model capability or speed.',
        '- **Public test:** Training overlap, retrieval, and memorization have not been investigated. A text-overlap check found no identical selected questions shared with Test 5; that does not establish independence from training data.',
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
    print('All 88 responses validated. ' + ('Committed reports match.' if args.check else 'Reports regenerated.' if args.write else 'No files changed.'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
