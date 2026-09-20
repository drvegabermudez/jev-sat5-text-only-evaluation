# Model evaluation card: Jev 1.13.0 on SAT Practice Test 10

**jev-1.13.0: 85/91 (93.4%) correct.**

## Evaluation overview

| Field | Value |
|---|---|
| Model | `jev-1.13.0`, as reported in the export |
| Interface | TypeSafe Choice questions with original A–D options |
| Task | English-language SAT Reading and Writing and Math |
| Dataset | 91 original multiple-choice questions: 61 Reading and Writing and 30 Math |
| Evaluated response exports | 1 |
| Request identifier | `playground_1eb2e929ef247284ea19122456494ab9994` |
| Response artifact | [responses.json](responses.json), preserved byte-for-byte |

## Data and method

The source is College Board’s [SAT Practice Test #10](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-10-digital.pdf), the 56-page nonadaptive paper form for the digital SAT. Of its 120 original questions, 91 are included. Fifteen visual items and fourteen numerical-response items are excluded, with no overlap between these exclusion groups. The [test overview](README.md) lists every omission and links the separate answer explanations used to verify the key.

Inputs are [questions.json](questions.json) and [state.json](state.json). Included items preserve the original wording and choices in text notation. The response contains all 91 expected IDs. The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-10-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 29/32 | 90.6% |
| Reading and Writing, Module 2 | 29/29 | 100.0% |
| Math, Module 1 | 11/14 | 78.6% |
| Math, Module 2 | 16/16 | 100.0% |
| **Reading and Writing** | 58/61 | 95.1% |
| **Math** | 27/30 | 90.0% |
| **Overall** | 85/91 | 93.4% |

The six incorrect answers and their explanations are listed in [RESULTS.md](RESULTS.md). Three errors are in Reading and Writing and three are in Math; both Module 2 subsets were answered entirely correctly.

## Overlap with earlier tests

The [test overview](README.md#overlap-and-question-ids) identifies 45 questions with the same normalized stem and answer texts in Tests 1–9. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 10 score.

| Test 10 cohort | Correct | Accuracy |
|---|---:|---:|
| Matches an earlier selected question | 41/45 | 91.1% |
| No exact earlier match found | 44/46 | 95.7% |

This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–10 counts repeated questions more than once unless an explicit deduplication rule is applied.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 17,955 |
| Output tokens | 4,280 |
| Server time | 203 ms |
| Network round trip | 118 ms |
| Calculated combined time | ≈ 321 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 203.38128799994593`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Scope and limitations

- **Selected subset:** Visual and numerical-response items are excluded. These results are raw subset accuracy, not official SAT scaled scores or a measure of the complete adaptive test.
- **Single evaluated export:** This test does not measure repeated-run reliability. Different test sets and serving conditions prevent these runs from isolating changes in model capability or speed.
- **Public and repeated questions:** Training overlap, retrieval, and memorization have not been investigated. Forty-five selected questions repeat earlier test content under the documented normalization, so pooled results must account for repeated items.
- **Request evidence:** The export does not include the submitted request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.
- **Confidence and ties:** Reported confidence and option probabilities are separate outputs and are not established to be calibrated by this evaluation. For `math_m1_q10`, the incorrect selected answer A and the correct answer B both have reported probability 0.48. Grading uses the exported choice A without overriding the selection.
- **Model details:** Architecture, parameter count, training data, training cutoff, and serving hardware are not established by the available evidence.

## Reproducibility

Run `python3 evaluate.py --check` from this folder, or `python3 test-10/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required. [RESULTS.md](RESULTS.md) records the input, answer-key, and response hashes.

This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe. It does not establish general model reliability or suitability for decisions about individual students.

Generated by `python3 evaluate.py --write`.
