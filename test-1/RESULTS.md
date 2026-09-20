# SAT Practice Test 1 evaluation results

**jev-1.13.0: 89/97 (91.8%) correct.**

The [College Board scoring guide mirrored by APCORE](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-1-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 29/31 | 93.5% |
| Reading and Writing, Module 2 | 29/31 | 93.5% |
| Math, Module 1 | 14/16 | 87.5% |
| Math, Module 2 | 17/19 | 89.5% |
| **Reading and Writing** | 58/62 | 93.5% |
| **Math** | 31/35 | 88.6% |
| **Overall** | 89/97 | 91.8% |

## Incorrect answers

Four errors are in Reading and Writing, all testing Standard English conventions; four are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q20` | C: soul”; positing | A: soul,” positing | 32% |
| `rw_m1_q27` | C: equations. Though, | A: equations, though: | 50% |
| `rw_m2_q21` | A: forces | C: forcing | 58% |
| `rw_m2_q25` | A: creates | B: create | 96% |
| `math_m1_q10` | B: 5 | C: 15 | 76% |
| `math_m1_q25` | A: −481/4 | C: −319/4 | 51% |
| `math_m2_q03` | A: −3 | B: 6 | 29% |
| `math_m2_q26` | A: 10x + 7y = 1 ax − 2by = 1 | B: 10x + 7y = 1 ax + 2by = 1 | 17% |

## Explanations

- **`rw_m1_q20`:** The phrase beginning “positing” explains Epicurus’s definition and attaches to the main clause with a comma. A semicolon would require an independent clause after it, which “positing…” is not.
- **`rw_m1_q27`:** The comma attaches “though” to the statement that Hopper’s career involved more than equations. The colon then introduces an explanation of that statement: her work helped usher in the digital age. Starting the next sentence with “Though” creates an illogical contrast.
- **`rw_m2_q21`:** “Forcing” introduces a phrase describing the consequence of food becoming unavailable. “Forces” supplies another finite verb without a grammatical connection to the preceding clause.
- **`rw_m2_q25`:** The modal “would” governs both coordinated verbs: the lock would increase salinity and create a barrier. Both verbs must take the base form, so “create” is correct.
- **`math_m1_q10`:** Substitute y = −3x into 4x + y = 15 to obtain 4x − 3x = 15. Therefore x = 15, choice C.
- **`math_m1_q25`:** A horizontal line intersects this downward-opening parabola once only at its vertex. Completing the square gives y = −(x − 9/2)² − 319/4, so c = −319/4, choice C.
- **`math_m2_q03`:** Add the two equations: 3x + (−3x + y) = 12 − 6, giving y = 6, choice B.
- **`math_m2_q26`:** The original slopes are −5/7 and −a/b, whose product is −1. In choice B, the first slope doubles to −10/7 and the second halves to −a/(2b), preserving their product of −1 and therefore perpendicularity.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,204 |
| Output tokens | 4,562 |
| Server time | 216 ms |
| Network round trip | 67 ms |
| Calculated combined time | ≈ 283 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 215.5186719901394`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 97 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1ebca40d9fb46b24b5483cf1e4cd7f7a010`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `98daf68aa46a90b1b9043de13a7a2a41d2616bf26b49f182d28fcff429245269` |
| [state.json](state.json) | `7576f7d93db15deb11e64d7c9bc756d3028a85fc15911e60093af4fbd5ac930d` |
| [answer_key.json](answer_key.json) | `1321242e34cec467b2c05960e35524bfdfce17acc08ee8b0dce5798d7096a663` |
| [responses.json](responses.json) | `75d317c9a29988b302dcf4662cdfc82d84550b663dc0499f2c1557569f97977e` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-1/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
