# Model evaluation card: Jev 1.13.0 on SAT Practice Test 9

**jev-1.13.0: 82/93 (88.2%) correct.**

## Evaluation overview

| Field | Value |
|---|---|
| Model | `jev-1.13.0`, as reported in the export |
| Interface | TypeSafe Choice questions with original A–D options |
| Task | English-language SAT Reading and Writing and Math |
| Dataset | 93 original multiple-choice questions: 61 Reading and Writing and 32 Math |
| Evaluated response exports | 1 |
| Request identifier | `playground_1eb819d1b60f49349f497facace04149b23` |
| Response artifact | [responses.json](responses.json), preserved byte-for-byte |

## Data and method

The source is College Board’s [SAT Practice Test #9](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-9-digital.pdf), the 56-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 93 are included. Fifteen visual items and twelve additional numerical-response items are excluded; two visual exclusions also require numerical responses. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.

Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 93 expected IDs. The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-9-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 24/28 | 85.7% |
| Reading and Writing, Module 2 | 29/33 | 87.9% |
| Math, Module 1 | 16/17 | 94.1% |
| Math, Module 2 | 13/15 | 86.7% |
| **Reading and Writing** | 53/61 | 86.9% |
| **Math** | 29/32 | 90.6% |
| **Overall** | 82/93 | 88.2% |

The eleven incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Eight errors are in Reading and Writing and three are in Math.

## Overlap with earlier tests

The [test overview](README.md#overlap-and-question-ids) identifies 37 questions with the same normalized stem and answer texts in Tests 1–8. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 9 score.

| Test 9 cohort | Correct | Accuracy |
|---|---:|---:|
| Matches an earlier selected question | 34/37 | 91.9% |
| No exact earlier match found | 48/56 | 85.7% |

This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–9 counts repeated questions more than once unless an explicit deduplication rule is applied.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,677 |
| Output tokens | 4,374 |
| Server time | 206 ms |
| Network round trip | 100 ms |
| Calculated combined time | ≈ 306 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 205.641459004255`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Scope and limitations

- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.
- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.
- **Public and repeated questions:** Training overlap, retrieval, and memorization have not been investigated. Thirty-seven selected questions repeat earlier test content under the documented normalization, so pooled results must account for repeated items.
- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.
- **Confidence and probability totals:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation. The probabilities for `math_m2_q24` total 0.99; all other distributions total 1. The original values are preserved, and this anomaly does not affect grading by selected answer.
- **Model details:** Architecture, parameter count, training data, training cutoff, and serving hardware are not established by the available evidence.

## Reproducibility

Run `python3 evaluate.py --check` from this folder, or `python3 test-9/evaluate.py --check` from the repository root. The script verifies the artifact hashes, checks all responses with the documented probability-total exception, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required. [RESULTS.md](RESULTS.md) records the input, answer-key, and response hashes.

This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. It does not establish general model reliability or suitability for decisions about individual students.

Generated by `python3 evaluate.py --write`.
