# SAT Practice Test 6 evaluation results

**jev-1.13.0: 81/88 (92.0%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-6-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 27/30 | 90.0% |
| Reading and Writing, Module 2 | 28/31 | 90.3% |
| Math, Module 1 | 12/12 | 100.0% |
| Math, Module 2 | 14/15 | 93.3% |
| **Reading and Writing** | 55/61 | 90.2% |
| **Math** | 26/27 | 96.3% |
| **Overall** | 81/88 | 92.0% |

## Incorrect answers

Six errors are in Standard English conventions; one is in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q22` | B: do people perceive acts of kindness? | D: people perceive acts of kindness. | 45% |
| `rw_m1_q24` | B: microsculptures, creations | C: microsculptures. Creations | 39% |
| `rw_m1_q25` | D: works: it’s because | B: works. Because | 36% |
| `rw_m2_q23` | A: leaves, man-made trash: | B: leaves; man-made trash, | 42% |
| `rw_m2_q24` | D: competitions; however, | A: competitions, however: | 35% |
| `rw_m2_q26` | C: increases | B: increase | 37% |
| `math_m2_q23` | C: 46 | A: 16 | 56% |

## Explanations

- **`rw_m1_q22`:** The sentence reports what the researchers investigated. This indirect question uses subject–verb order (“people perceive”) and ends with a period.
- **`rw_m1_q24`:** A period ends the first complete sentence. “Creations so small that they are best viewed through a microscope” then introduces and describes the subject of the next sentence, “Wigan’s sculptures.” A comma after “microsculptures” does not properly separate the two complete sentences.
- **`rw_m1_q25`:** “A ray diagram reveals how this works” is a complete sentence. The next sentence begins with “Because,” introducing the reason for the statement that follows. Choice D leaves a comma splice within the explanation.
- **`rw_m2_q23`:** Semicolons separate the three list items because each contains an internal comma: natural debris, man-made trash, and traditional art supplies. A comma before “such as plastic bags” introduces the example within the second item.
- **`rw_m2_q24`:** “However” closes the statement contrasting the many Latin American dances with the five included in competition. A colon then introduces the list of five dances. The list is not an independent clause that could follow the semicolon in choice D.
- **`rw_m2_q26`:** The subject of the main clause is plural, “the toxins,” so the verb is “increase.” The singular “organism” belongs to the intervening clause and does not control the main verb.
- **`math_m2_q23`:** Rewrite (1.84)^(x/4) as ((1.84)^(1/4))^x. Thus 1 + p/100 = (1.84)^(1/4), giving p = 100((1.84)^(1/4) − 1) ≈ 16.47. The closest choice is A, 16.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,103 |
| Output tokens | 4,139 |
| Server time | 182 ms |
| Network round trip to us-west | 153 ms |
| Calculated combined time | ≈ 335 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 182.25066499144305`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 88 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1ebcdc90e6da9094330ad8ca45511fed2aa`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `90165a44f9070de0a157365579815b7d0ee7cd6f9d2cb9cd61b4fa57d109f300` |
| [state.json](state.json) | `403a01dcd56408533f88aed02f7172ed54cb2404d3caac514d61f614a6613949` |
| [answer_key.json](answer_key.json) | `0e74b92d8396721c989e556046f1ad1d71d6333a319de979489f0b682e404561` |
| [responses.json](responses.json) | `121fd1e39783409408b4effbb1a4cebd6b9c8d830e5422d8269d551e90f16c29` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-6/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
