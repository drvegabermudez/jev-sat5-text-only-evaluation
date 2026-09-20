# SAT Practice Test 10 evaluation results

**jev-1.13.0: 85/91 (93.4%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-10-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

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

## Incorrect answers

Three errors are in Reading and Writing, all testing Standard English conventions. Three errors are in Math. All six errors are in Module 1 of their respective sections. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q22` | A: forces | C: forcing | 48% |
| `rw_m1_q23` | D: lifelike, but | C: lifelike, | 50% |
| `rw_m1_q26` | A: its | C: their | 68% |
| `math_m1_q10` | A: 40 | B: 48 | 32% |
| `math_m1_q23` | B: (x − 8)² + (y − 4)² = 16 | C: (x − 4)² + (y − 9)² = 16 | 54% |
| `math_m1_q25` | C: 38 | D: 36 | 41% |

## Explanations

- **`rw_m1_q22`:** “Forcing” introduces a phrase describing the consequence of food becoming unavailable. The main clause already has its verb, so “forces” cannot be added this way.
- **`rw_m1_q23`:** A comma separates the introductory “While” clause from “others look to the past.” The contrast is already established by “While”; adding “but” breaks that structure.
- **`rw_m1_q26`:** “Their” refers back to the plural “types of pop culture references.” The singular “its” does not agree with that antecedent.
- **`math_m1_q10`:** The requested expression is four times the given one: 16x + 8 = 4(4x + 2) = 4(12) = 48, choice B.
- **`math_m1_q23`:** All four circles have radius 4. A circle touches the y-axis once when its center is exactly 4 units from that axis. Choice C has center (4, 9) and touches at (0, 9); choice B has center (8, 4) and misses the y-axis.
- **`math_m1_q25`:** An increase of 1,800% adds 18x to the original x. Thus 19x = 684 and x = 36, choice D. Dividing by 18 instead gives the selected 38.

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

## Validation and provenance

All 91 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer is among the options with the highest reported probability. Answer-key text matches the corresponding original option. For `math_m1_q10`, A and B each have a reported probability of 0.48. The export selects A; the correct answer is B, so this item is graded incorrect. Tied probabilities do not override the exported selection.

Request identifier: `playground_1eb2e929ef247284ea19122456494ab9994`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `3c5a989e53063c688ccdbf0f21ae41d3fd54ba985e6a2f9097084ef5d79801e6` |
| [state.json](state.json) | `fb11e919adb591e66a830ed703028088550cf895974410fa8a4c8e5a9b17eb53` |
| [answer_key.json](answer_key.json) | `3dd740f947c03c9856283d6fcc4553c1c18187246bc1bb909c2a4b86bc0b58c9` |
| [responses.json](responses.json) | `4f36c3296d614c14b4c7db6cfa827e188ca8ec9e5cb201c628e5c9a01ddfc974` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-10/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
