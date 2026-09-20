# Jev on SAT Practice Test 5

**Jev 1.13.0 scored 81/91 correct (89.0%)** on a text-only subset of College Board’s SAT Practice Test #5.

| Section | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing | 56/61 | 91.8% |
| Math | 25/30 | 83.3% |
| **Total** | **81/91** | **89.0%** |

[Full results](RESULTS.md) · [Model card](MODEL_CARD.md) · [Omitted questions](OMISSIONS.md)

## Test and selection

The source is **The SAT Practice Test #5**, © 2024 College Board: the 56-page nonadaptive paper form with cover identifiers `WX4P0001` and `6VSL01`.

- [Official test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-5-digital.pdf)
- [Official scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-5-digital.pdf), answer key on page 4

Of the 120 source questions, this dataset includes **91 original multiple-choice questions**: 61 Reading and Writing and 30 Math. Each includes its complete text context and original A–D options. Original question numbers are preserved.

The 29 exclusions consist of 17 questions requiring graphs, diagrams, or tables and 12 other questions requiring numerical responses. [OMISSIONS.md](OMISSIONS.md) lists every exclusion and its reason. Geometry questions are included when their equations and relationships are fully specified in text.

## Files

| File | Purpose |
|---|---|
| [state.json](state.json) | Shared context for the evaluation |
| [questions.json](questions.json) | 91 questions in TypeSafe Choice format |
| [responses.json](responses.json) | Unmodified Jev response export |
| [answer_key.json](answer_key.json) | Official answer letters and answer text for the 91 questions |
| [RESULTS.md](RESULTS.md) | Section and module scores, incorrect answers, and explanations |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, performance, and limitations |
| [results/](results/) | Machine-readable summary and per-question grading |
| [OMISSIONS.md](OMISSIONS.md) / [omitted_questions.csv](omitted_questions.csv) | Excluded questions and reasons |
| [question_manifest.json](question_manifest.json) | Question identifiers and source pages |
| [official_answer_key.json](official_answer_key.json) | Official answers for all 120 source questions |
| [provenance.json](provenance.json) | Source identifiers, response metadata, and artifact hashes |
| [evaluate.py](evaluate.py) / [validate.py](validate.py) | Reproducible grading and dataset validation |

Use `state.json` and `questions.json` as the evaluation inputs. Answer keys and results are for grading. The response export contains all 91 expected answers; it does not include the original service request or sampling settings.

## Reproduce the grade

Python 3.9 or newer is sufficient. No external packages, credentials, or model calls are required.

```bash
git clone https://github.com/drvegabermudez/jev-sat5-text-only-evaluation.git
cd jev-sat5-text-only-evaluation
python3 evaluate.py --check
```

Expected output:

```text
Overall: 81/91 (89.0%)
Reading and Writing: 56/61 (91.8%)
Math: 25/30 (83.3%)
Incorrect answers: 10.
Response validation passed. Committed results match.
```

The command validates artifact hashes, question coverage, answer keys, probability fields, and confidence ranges, then recalculates the results. `python3 evaluate.py --write` regenerates the reports; `python3 validate.py` checks the dataset separately.

This is raw accuracy on a selected subset, not an official SAT scaled score.

## Attribution

SAT content is © 2024 College Board, with passages attributable to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. See [third-party notices](THIRD_PARTY_NOTICES.md).
