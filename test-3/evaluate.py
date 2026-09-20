#!/usr/bin/env python3
"""Reproduce the 94-question Test 3 evaluation using Python's standard library."""

import argparse
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_HASHES = {'questions.json': 'c406ecac593620e51e2603f4b52bc8995fc98ea4bfee0edb29343b42491b02ca',
 'state.json': 'daed71323f5b6037f50ec96aeb3116e4da763600845fac70c938fa95a1727eb1',
 'answer_key.json': '9df538cb37011d82b75f7d23b768cee657d5a2d09407b30ad80d731f050b627f',
 'responses.json': 'e8edc25f497a7772f58bc37e66490c75c31d2039490047093fc4866555e7282e'}
# Network timing supplied by the user for this response export.
NETWORK_ROUND_TRIP_MS = 57
MODULE_COUNTS = {'rw_m1': 32, 'rw_m2': 30, 'math_m1': 15, 'math_m2': 17}
MODULE_NAMES = {
    'rw_m1': 'Reading and Writing, Module 1',
    'rw_m2': 'Reading and Writing, Module 2',
    'math_m1': 'Math, Module 1',
    'math_m2': 'Math, Module 2',
}
EXPLANATIONS = {'rw_m1_q23': 'The clause beginning “whenever” specifies the condition under which a leap second '
              'is added. It follows “is added” directly without a comma, semicolon, or period, so '
              'choice D is correct.',
 'rw_m1_q25': 'Commas set off “however,” while the phrase beginning “feeling” explains why '
              'Scott-Heron resisted the nickname. That phrase is not an independent clause, so the '
              'semicolon in choice D cannot introduce it.',
 'rw_m1_q26': '“The stitching barely visible…” is a supplementary phrase, not an independent '
              'clause. A comma attaches that description to the statement that the portraits are '
              'quilts; adding “and” does not produce a grammatical continuation.',
 'rw_m1_q28': 'The requested answer must both describe the rocking chair and introduce its maker '
              'to an unfamiliar audience. Choice A describes the chair and identifies Sam Maloof '
              'as an American woodworker. Choice D describes the chair but does not introduce '
              'Maloof.',
 'rw_m2_q21': 'The clause beginning “while” supplies contrasting information about the rougheye '
              'rockfish. A comma connects it to the main clause; a semicolon cannot separate a '
              'main clause from this dependent clause.',
 'rw_m2_q22': 'The introductory phrase “Powered with energy collected by solar panels during the '
              'day” needs a comma before the main clause beginning “the blinking LEDs.” Choice B '
              'omits that comma.',
 'rw_m2_q26': 'The passage contains two complete sentences: Nehmé traveled to study the tombs; the '
              'burial chambers seem to blend with nature. Choice A supplies a period, and “Built '
              'into the rocky outcrops…” opens the second sentence as a modifier of the burial '
              'chambers. Choice B creates a comma splice.',
 'rw_m2_q27': '“Aluminum oxide” identifies which chemical compound was used and is essential to '
              'the meaning. It therefore stays directly beside “chemical compound” without commas, '
              'as in choice D.',
 'math_m1_q18': 'Let n be the smaller integer. Then n(2n + 11) = 546, or (n − 14)(2n + 39) = 0. '
                'The positive solution is n = 14, and the other integer is 39; 14 × 39 = 546. Thus '
                'choice B is correct.',
 'math_m2_q25': 'If each leg has length L, the hypotenuse is L√2 and the perimeter is L(2 + √2). '
                'With L = 47√2, this equals 94√2 + 94, exactly the given perimeter. Thus the leg '
                'length is 47√2 inches, choice B.'}


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
    require(len(questions) == 94, 'Expected 94 questions')
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
    source = 'The [College Board scoring guide mirrored by APCORE](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-3-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.'
    reproduction = 'Run `python3 evaluate.py --check` from this folder, or `python3 test-3/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.'
    errors = [row for row in rows if not row['correct']]
    results = [
        '# SAT Practice Test 3 evaluation results', '', headline, '', source, '',
        '## Performance', '', *score_table(rows), '',
        '## Incorrect answers', '',
        'Eight errors are in Reading and Writing: seven test Standard English conventions and one tests synthesis of notes for a specified audience. Two errors are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.', '',
        '| Question | Jev answered | Correct answer | Confidence |', '|---|---|---|---:|',
    ]
    for row in errors:
        results.append(f"| `{row['id']}` | {row['selected']}: {cell(row['selected_text'])} | {row['expected']}: {cell(row['expected_text'])} | {row['confidence']:.0%} |")
    results += ['', '## Explanations', '']
    results += [f"- **`{row['id']}`:** {EXPLANATIONS[row['id']]}" for row in errors]
    results += ['', *timing_lines(response),
        '## Validation and provenance', '',
        'All 94 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.', '',
        f"Request identifier: `{response['request_id']}`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:", '',
        '| File | SHA-256 |', '|---|---|',
    ]
    results += [f'| [{name}]({name}) | `{digest}` |' for name, digest in EXPECTED_HASHES.items()]
    results += ['', 'The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.', '',
        '## Reproduce the results', '', reproduction, '', 'Generated by `python3 evaluate.py --write`.', '',
    ]
    card = [
        '# Model evaluation card: Jev 1.13.0 on SAT Practice Test 3', '', headline, '',
        '## Evaluation overview', '',
        '| Field | Value |', '|---|---|',
        f"| Model | `{response['model']}`, as reported in the export |",
        '| Interface | TypeSafe Choice questions with original A–D options |',
        '| Task | English-language SAT Reading and Writing and Math |',
        '| Dataset | 94 original multiple-choice questions: 62 Reading and Writing and 32 Math |',
        '| Evaluated response exports | 1 |',
        f"| Request identifier | `{response['request_id']}` |",
        '| Response artifact | [responses.json](responses.json), preserved byte-for-byte |', '',
        '## Data and method', '',
        'The source is College Board’s [SAT Practice Test #3](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/sat-practice-test-3-digital.pdf), the 56-page nonadaptive paper form for the digital SAT, preserved on APCORE’s public mirror. Of its 120 original questions, 94 are included. Thirteen visual items and thirteen additional numerical-response items are excluded; one visual exclusion also requires a numerical response. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.', '',
        'Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 94 expected IDs. ' + source, '',
        '## Performance', '', *score_table(rows), '',
        'The ten incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Eight errors are in Reading and Writing and two are in Math.', '',
        *timing_lines(response),
        '## Scope and limitations', '',
        '- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.',
        '- **Single evaluated export:** This test does not measure repeated-run reliability. Tests 1, 2, 3, 5, 6, and 7 contain different selected questions, so their scores and timings do not isolate a change in model capability or speed.',
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
    print('All 94 responses validated. ' + ('Committed reports match.' if args.check else 'Reports regenerated.' if args.write else 'No files changed.'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
