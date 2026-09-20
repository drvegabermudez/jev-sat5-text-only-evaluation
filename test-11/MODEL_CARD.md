# Model evaluation card: Jev 1.13.0 on SAT Practice Test 11

**jev-1.13.0: 79/87 (90.8%) correct.**

## Evaluation overview

| Field | Value |
|---|---|
| Model | `jev-1.13.0`, as reported in the export |
| Interface | TypeSafe Choice questions with original A–D options |
| Task | English-language SAT Reading and Writing and Math |
| Dataset | 87 original multiple-choice questions: 62 Reading and Writing and 25 Math |
| Evaluated response exports | 1 |
| Request identifier | `playground_1eb65253354de17407eb4f9c2b853e2f2b1` |
| Response artifact | [responses.json](responses.json), preserved byte-for-byte |

## Data and method

The source is College Board’s [SAT Practice Test #11](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-11-digital.pdf), the 52-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 87 are included. Twenty visual items and thirteen additional numerical-response items are excluded; one visual exclusion also requires a numerical response. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.

Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 87 expected IDs. The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-11-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 30/32 | 93.8% |
| Reading and Writing, Module 2 | 25/30 | 83.3% |
| Math, Module 1 | 14/14 | 100.0% |
| Math, Module 2 | 10/11 | 90.9% |
| **Reading and Writing** | 55/62 | 88.7% |
| **Math** | 24/25 | 96.0% |
| **Overall** | 79/87 | 90.8% |

The eight incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Seven errors are in Reading and Writing and one is in Math.

## Overlap with earlier tests

No exact matches of normalized question stems and answer texts were found against the selected sets for Tests 1–10. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. All 87 selected Test 11 questions therefore contribute to the distinct-question aggregate under this matching rule.

This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Similar templates and partial text overlap may remain. See the [test overview](README.md#overlap-and-question-ids) for the comparison method.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,317 |
| Output tokens | 4,092 |
| Server time | 253 ms |
| Network round trip | 169 ms |
| Calculated combined time | ≈ 422 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 252.8140020003775`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Scope and limitations

- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.
- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.
- **Public questions:** Training overlap, retrieval, and memorization have not been investigated. No exact matches were found against selected questions in Tests 1–10, but this does not establish independence from training data or tested skills.
- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.
- **Confidence and probability totals:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation. The probabilities for `math_m2_q26` total 0.99; all other distributions total 1. The original values are preserved, and this anomaly does not affect grading by selected answer.
- **Model details:** Architecture, parameter count, training data, training cutoff, and serving hardware are not established by the available evidence.

## Reproducibility

Run `python3 evaluate.py --check` from this folder, or `python3 test-11/evaluate.py --check` from the repository root. The script verifies the artifact hashes, checks all responses with the documented probability-total exception, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required. [RESULTS.md](RESULTS.md) records the input, answer-key, and response hashes.

This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. It does not establish general model reliability or suitability for decisions about individual students.

Generated by `python3 evaluate.py --write`.
