#!/usr/bin/env python3
"""Validate the current original-choice dataset and the provenance of its supplied response export."""

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_keys)


def validate_dataset(verbose=True):
    provenance = load(ROOT / 'provenance.json')
    for name, expected in provenance['sha256'].items():
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        require(actual == expected, f'Artifact hash mismatch: {name}')
    questions = load(ROOT / 'questions.json')
    key = load(ROOT / 'answer_key.json')
    official = load(ROOT / 'official_answer_key.json')
    manifest = load(ROOT / 'question_manifest.json')
    require(manifest['dataset_version'] == provenance['dataset_version'], 'Dataset identifiers differ')
    require(len(questions) == 91, 'Expected 91 questions')
    require(set(key) == set(questions), 'Key/question IDs differ')
    entries = {row['id']: row for row in manifest['questions']}
    require(len(manifest['questions']) == len(entries) == 91 and set(entries) == set(questions), 'Manifest/question IDs differ')
    with (ROOT / 'omitted_questions.csv').open(newline='', encoding='utf-8') as stream:
        omissions = list(csv.DictReader(stream))
    omitted_ids = {row['id'] for row in omissions}
    require(len(omissions) == len(omitted_ids) == 29, 'Expected 29 distinct omissions')
    require(omitted_ids == set(manifest['omitted_question_ids']), 'Omission CSV/manifest differ')
    require(not omitted_ids & set(questions), 'An omitted question is still included')
    expected_source_ids = {f'{section}_m{module}_q{number:02d}' for section, count in [('rw', 33), ('math', 27)] for module in (1, 2) for number in range(1, count + 1)}
    require(set(official) == expected_source_ids == omitted_ids | set(questions), 'Included and omitted IDs must partition all 120 source questions')
    require(Counter(row['category'] for row in omissions) == {'source_visual_or_table': 17, 'original_numerical_response': 12}, 'Unexpected omission categories')
    modules = Counter(qid.rsplit('_', 1)[0] for qid in questions)
    require(modules == manifest['counts']['by_module'] == {'rw_m1':31, 'rw_m2':30, 'math_m1':15, 'math_m2':15}, 'Module counts differ')

    underlined_count = 0
    for qid, question in questions.items():
        require(question['type'] == 'choice', f'{qid}: unexpected question type')
        require(list(question['criteria']) == list('ABCD'), f'{qid}: original A–D order changed')
        require(all(isinstance(value, str) and value.strip() for value in question['criteria'].values()), f'{qid}: empty option')
        stem = question['instructions']
        require(isinstance(stem, str) and stem.strip(), f'{qid}: empty stem')
        require(not re.search(r'(graph|figure|diagram|table|scatterplot)\s+(shown|above|below)', stem, re.I), f'{qid}: possible unresolved visual reference')
        require(stem.count('[UNDERLINED]') == stem.count('[/UNDERLINED]'), f'{qid}: incomplete underlining markers')
        underlined_count += stem.count('[UNDERLINED]')
        answer = key[qid]
        require(answer['choice'] == answer['official_answer'] == official[qid], f'{qid}: official answer mismatch')
        require(answer['answer'] == question['criteria'][answer['choice']], f'{qid}: answer text mismatch')
        require(answer['original_format'] == entries[qid]['original_format'] == 'multiple_choice', f'{qid}: nonoriginal format')
        require(answer['added_choices'] is False and entries[qid]['added_choices'] is False, f'{qid}: added choices remain')
        require(entries[qid]['requires_external_visual'] is False, f'{qid}: unresolved visual dependency')
    require(underlined_count == 6, 'Expected six preserved underlined spans')
    paired = questions['rw_m2_q08']['instructions']
    require('Text 1\n' in paired and 'Text 2\n' in paired, 'Paired-passage context missing')
    evaluation = provenance['evaluation']
    require(evaluation['status'] == 'graded' and evaluation['response_file'] == 'responses.json', 'Evaluation metadata does not identify the response')
    require('responses.json' in provenance['sha256'], 'Response hash is missing')
    response = load(ROOT / evaluation['response_file'])
    require(set(response['answers']) == set(questions), 'Response does not cover exactly the 91 question IDs')
    require(response['model'] == evaluation['model'] and response['request_id'] == evaluation['request_id'], 'Response identity differs from provenance')
    require(evaluation['input_sha256'] == {name: provenance['sha256'][name] for name in ['state.json', 'questions.json']}, 'Prepared input hashes differ from recorded evaluation inputs')
    correct = sum(response['answers'][qid]['choice'] == key[qid]['choice'] for qid in questions)
    require(evaluation['score'] == {'correct': correct, 'total': len(questions), 'accuracy_percent': round(100 * correct / len(questions), 4)}, 'Recorded score differs from the answers')
    if verbose:
        print('Dataset: 91 original multiple-choice questions (61 Reading and Writing, 30 Math).')
        print('Exclusions: 17 visual/table questions + 12 additional numerical-response questions = 29.')
        print('Answer key, question coverage, underlining, paired passages, and artifact hashes verified.')
        print(f'Response identity and prepared-input hashes verified; score: {correct}/{len(questions)}.')
    return questions, key, manifest, provenance, response


if __name__ == '__main__':
    try:
        validate_dataset()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}') from error
