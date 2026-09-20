# SAT Practice Test 2 evaluation results

**jev-1.13.0: 85/93 (91.4%) correct.**

The [College Board scoring guide mirrored by APCORE](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-2-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 31/32 | 96.9% |
| Reading and Writing, Module 2 | 27/30 | 90.0% |
| Math, Module 1 | 12/14 | 85.7% |
| Math, Module 2 | 15/17 | 88.2% |
| **Reading and Writing** | 58/62 | 93.5% |
| **Math** | 27/31 | 87.1% |
| **Overall** | 85/93 | 91.4% |

## Incorrect answers

Four errors are in Reading and Writing, all testing Standard English conventions; four are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q25` | D: materialism” | C: materialism,” | 20% |
| `rw_m2_q19` | D: lifelike, but | C: lifelike, | 48% |
| `rw_m2_q22` | C: there are many critics who have focused on Kurosawa’s use of Western literary sources, but they | A: many critics have focused on Kurosawa’s use of Western literary sources but | 30% |
| `rw_m2_q23` | B: Basic; in 2009, an online television network, | C: Basic, in 2009; an online television network, | 28% |
| `math_m1_q11` | A: 40 | B: 48 | 42% |
| `math_m1_q18` | B: 9 | C: 12 | 36% |
| `math_m2_q16` | D: 9 | C: 1/9 | 77% |
| `math_m2_q24` | B: (x − 8)² + (y − 4)² = 16 | C: (x − 4)² + (y − 9)² = 16 | 54% |

## Explanations

- **`rw_m1_q25`:** The phrase beginning “an apt assessment” comments on the preceding observation and must be set off with a comma. Choice D omits that required boundary punctuation.
- **`rw_m2_q19`:** The opening clause begins with “While” and must be separated from the main clause, “others look to the past,” by a comma. Adding “but” at that boundary leaves no independent main clause.
- **`rw_m2_q22`:** The introductory phrase “In assessing the films…” must modify the people doing the assessing. Choice A places “many critics” directly after it; choice C begins with “there,” leaving the modifier dangling.
- **`rw_m2_q23`:** Semicolons separate the three projects because each list item already contains commas. The first item ends with its date, 2009, so the semicolon belongs after “2009”; commas set off the app and network names.
- **`math_m1_q11`:** The requested expression is four times the given left-hand side: 16x + 8 = 4(4x + 2) = 4 × 12 = 48, choice B.
- **`math_m1_q18`:** Let c be the number of children, so there are 21 − c adults. Then 80(21 − c) + 60c = 1,440, giving 1,680 − 20c = 1,440 and c = 12, choice C. The selected value, 9, is the number of adults.
- **`math_m2_q16`:** Rearranging 2y + 18x = 9 gives y = −9x + 9/2, so line p has slope −9. A perpendicular line has slope −1/(−9) = 1/9, choice C.
- **`math_m2_q24`:** At the y-axis, x = 0. In choice C, substitution gives 16 + (y − 9)² = 16, so y = 9 is the only intersection. Choices A and B have no y-axis intersections; choice D has two.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,910 |
| Output tokens | 4,374 |
| Server time | 253 ms |
| Network round trip | 120 ms |
| Calculated combined time | ≈ 373 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 252.52049599657767`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 93 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1eb3d3c0b684e274fbda72a15131ee83b6e`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `a944c25ddb43f17f63191f8f3377d48b13e849bd2992585c8fe796b3465cbf09` |
| [state.json](state.json) | `a90d86cabef79b232ce069b96e382e4e8cbc6634148167049ef0977cc3af4f08` |
| [answer_key.json](answer_key.json) | `f80a39685cb5d6ede29f33ac142eced52c509a9ba12efc762ecf4996870063b1` |
| [responses.json](responses.json) | `fd7b93a9a832760b4d8e6aa9deb39b3527275de68e36de2de1d49ec3dcc1b9cd` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-2/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
