# SAT Practice Test 8 evaluation results

**jev-1.13.0: 83/91 (91.2%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-8-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

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

## Incorrect answers

Six errors are in Reading and Writing, all testing Standard English conventions. Two errors are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q20` | A: creates | B: create | 94% |
| `rw_m1_q22` | C: equations. Though, | A: equations, though: | 48% |
| `rw_m1_q23` | A: attests | D: attest | 37% |
| `rw_m1_q24` | D: antiquity; however, | C: antiquity, however; | 100% |
| `rw_m1_q25` | A: works were | C: works, | 48% |
| `rw_m2_q22` | B: bounds, helping | A: bounds helped | 33% |
| `math_m1_q25` | A: −481/4 | C: −319/4 | 54% |
| `math_m2_q11` | B: 5 | C: 15 | 60% |

## Explanations

- **`rw_m1_q20`:** “Would” governs both verbs: the lock would increase salinity and create a barrier. “Creates” cannot follow that shared modal.
- **`rw_m1_q22`:** “Though” concludes the contrast in the first clause. The colon then introduces Hopper’s programming work as an explanation of her broader career.
- **`rw_m1_q23`:** The subject is the plural “accomplishments,” so the verb must be “attest.” The intervening description of Goldin does not change that agreement.
- **`rw_m1_q24`:** “However” modifies the claim that neoclassical writers were not first. The Renaissance example supports that claim, so the semicolon belongs after “however.”
- **`rw_m1_q25`:** Commas enclose the descriptive phrase beginning “much admired.” The main clause already has “had … been … gathering,” so adding “were” breaks its structure.
- **`rw_m2_q22`:** The compound subject—Ashford’s gestures and habit—needs the main verb “helped.” “Helping” leaves the sentence without a main verb.
- **`math_m1_q25`:** A horizontal line meets this downward-opening parabola once only at its vertex. Completing the square gives y = −(x − 9/2)² − 319/4, so c = −319/4.
- **`math_m2_q11`:** Substitute y = −3x into 4x + y = 15: 4x − 3x = 15, so x = 15.

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

## Validation and provenance

All 91 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1eb3d5ab79224974a58b5b1d6cc34f644a6`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `d8269591557b3ead80b3da92fb532658f517801ae3fc8c399fbda96d6eea47ab` |
| [state.json](state.json) | `69dd2c0d88774aae93a47d05712c7d16f3fb642621a7fa3283779396cf6f20ab` |
| [answer_key.json](answer_key.json) | `7e68b171f7d1f8440df6e8db94a946125fd92db44da24b60baacd849ebb38c70` |
| [responses.json](responses.json) | `aa85b3e7347d97d3157bb1b52b9a97f3c4143a90704e0bb951f7237cc0e631cc` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-8/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
