# SAT Practice Test 11 evaluation results

**jev-1.13.0: 79/87 (90.8%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-11-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

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

## Incorrect answers

Seven errors are in Reading and Writing: five test Standard English conventions, one tests inference, and one tests a logical transition. One error is in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q22` | D: 1804 | B: 1804, | 29% |
| `rw_m1_q25` | B: swimming is | D: swimming, | 28% |
| `rw_m2_q18` | D: inconsistencies across the model’s simulations of Titan’s precipitation and humidity could be attributable to variations in the moon’s methane mole fraction. | A: some disagreements between the model’s simulations of Titan’s precipitation and humidity and the moon’s actual precipitation and humidity are to be expected. | 42% |
| `rw_m2_q20` | A: create | B: to create | 66% |
| `rw_m2_q25` | B: the most highly skilled soccer players responding to hypothetical match scenarios have electrograms that show | A: electrograms show that while responding to hypothetical match scenarios, the most highly skilled soccer players have | 26% |
| `rw_m2_q26` | A: searched | B: searching | 72% |
| `rw_m2_q29` | A: nevertheless, | C: indeed, | 96% |
| `math_m2_q26` | B: 3/4 | D: 4/3 | 58% |

## Explanations

- **`rw_m1_q22`:** The comma after “1804” closes the parenthetical phrase “ratified in 1804,” matching the comma after “amendment.” The main clause then continues with “separated.”
- **`rw_m1_q25`:** The main clause is “Helical swimming … bestows similar advantages.” The comma starts the intervening description. Adding “is” creates an incompatible second main verb.
- **`rw_m2_q18`:** A uniform methane value simplifies an uncertain real distribution, so differences between simulated and observed weather are expected. Choice D instead discusses inconsistencies among simulations, which the passage does not establish.
- **`rw_m2_q20`:** The construction is “enables someone to do something”: ArcGIS enables cartographers to create maps. The bare verb “create” does not fit.
- **`rw_m2_q25`:** The opening description refers to recordings, so “electrograms” must immediately follow it. Choice B incorrectly attaches that description to soccer players.
- **`rw_m2_q26`:** The main clause says that scientists adapted the test. “Searching” describes those scientists; “searched” improperly adds another main verb without a conjunction.
- **`rw_m2_q29`:** The usual 20–50 km heights support the claim that jets reaching about 80 km are outliers. “Indeed” introduces that support; “nevertheless” incorrectly signals a contrast.
- **`math_m2_q26`:** In right triangle XYW, tan Y = WX/WY = 429/572 = 3/4. Since Y and Z are complementary angles, tan Z = 1/tan Y = 4/3, choice D.

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

## Validation and provenance

All 87 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option. Of the 87 probability distributions, 86 sum to 1. The distribution for `math_m2_q26` totals 0.99 (A: 0.04, B: 0.68, C: 0.08, D: 0.19). The export is preserved without normalization. The selected answer B is incorrect; the official answer is D. Grading by selected answer is unaffected by the probability total. The evaluator permits this specific recorded total and rejects any other unexpected total.

Request identifier: `playground_1eb65253354de17407eb4f9c2b853e2f2b1`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `bbaefe864750788e4094d6032acfe663f843845617525ee17be7a87651284984` |
| [state.json](state.json) | `847e427f00270c39015e8a749763a750907ec77a3eaf58ae074578fdeae1cf70` |
| [answer_key.json](answer_key.json) | `ba67bca064be38a7b3119f690243b8ebe69de7fd0c0051f31f42dbfd474dc39a` |
| [responses.json](responses.json) | `aa581bc42b8c7450873f3cc23c67d3f911f996e171482f7f6f0a3c0a3e682e70` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-11/evaluate.py --check` from the repository root. The script verifies the artifact hashes, checks all responses with the documented probability-total exception, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
