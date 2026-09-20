# Model evaluation card: Jev 1.13.0 on SAT Practice Test 8

**jev-1.13.0: 83/91 (91.2%) correct.**

## Evaluation overview

| Field | Value |
|---|---|
| Model | `jev-1.13.0`, as reported in the export |
| Interface | TypeSafe Choice questions with original A–D options |
| Task | English-language SAT Reading and Writing and Math |
| Dataset | 91 original multiple-choice questions: 61 Reading and Writing and 30 Math |
| Evaluated response exports | 1 |
| Request identifier | `playground_1eb3d5ab79224974a58b5b1d6cc34f644a6` |
| Response artifact | [responses.json](responses.json), preserved byte-for-byte |

## Data and method

The source is College Board’s [SAT Practice Test #8](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-8-digital.pdf), the 56-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 91 are included. Fifteen visual items and fourteen numerical-response items are excluded, with no overlap between these exclusion groups. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.

Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 91 expected IDs. The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-8-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 25/30 | 83.3% |
| Reading and Writing, Module 2 | 30/31 | 96.8% |
| Math, Module 1 | 15/16 | 93.8% |
| Math, Module 2 | 13/14 | 92.9% |
| **Reading and Writing** | 55/61 | 90.2% |
| **Math** | 28/30 | 93.3% |
| **Overall** | 83/91 | 91.2% |

The eight incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Six errors are in Reading and Writing and two are in Math.

## Overlap with earlier tests

The [test overview](README.md#overlap-and-question-ids) identifies 51 questions with the same normalized stem and answer texts in Tests 1–7. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 8 score.

| Test 8 cohort | Correct | Accuracy |
|---|---:|---:|
| Matches an earlier selected question | 47/51 | 92.2% |
| No exact earlier match found | 36/40 | 90.0% |

This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–8 counts repeated questions more than once unless an explicit deduplication rule is applied.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,222 |
| Output tokens | 4,280 |
| Server time | 245 ms |
| Network round trip | 155 ms |
| Calculated combined time | ≈ 400 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 245.0090429992997`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Scope and limitations

- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.
- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.
- **Public and repeated questions:** Training overlap, retrieval, and memorization have not been investigated. Fifty-one selected questions repeat earlier test content under the documented normalization, so pooled results must account for repeated items.
- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.
- **Confidence:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation.
- **Model details:** Architecture, parameter count, training data, training cutoff, and serving hardware are not established by the available evidence.

## Reproducibility

Run `python3 evaluate.py --check` from this folder, or `python3 test-8/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required. [RESULTS.md](RESULTS.md) records the input, answer-key, and response hashes.

This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. It does not establish general model reliability or suitability for decisions about individual students.

Generated by `python3 evaluate.py --write`.
