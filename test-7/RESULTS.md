# SAT Practice Test 7 evaluation results

**jev-1.13.0: 84/92 (91.3%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-7-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 29/30 | 96.7% |
| Reading and Writing, Module 2 | 28/31 | 90.3% |
| Math, Module 1 | 14/15 | 93.3% |
| Math, Module 2 | 13/16 | 81.2% |
| **Reading and Writing** | 57/61 | 93.4% |
| **Math** | 27/31 | 87.1% |
| **Overall** | 84/92 | 91.3% |

## Incorrect answers

Four errors are in Reading and Writing (three conventions questions and one inference question); four are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q26` | A: supposed; a | D: supposed, a | 32% |
| `rw_m2_q18` | A: proclaim that the percentage of silver in coins suitable for trade would be raised to a threshold higher than 80%. | B: keep the amount of silver in Sidonian coins consistent with that in coins minted in 367 BCE but decrease their weight. | 41% |
| `rw_m2_q19` | A: included | D: to include | 56% |
| `rw_m2_q25` | A: pristine, though | B: pristine, though; | 92% |
| `math_m1_q25` | A: 2(cos 66°)(sin 24°) | C: (cos 66°)² + (cos 24°)² | 42% |
| `math_m2_q18` | A: −18 | D: 18 | 27% |
| `math_m2_q24` | C: 84 | B: 168 | 49% |
| `math_m2_q25` | B: √149 | C: √167 | 86% |

## Explanations

- **`rw_m1_q26`:** The phrase beginning “a finding” adds information about the preceding statement and is not an independent clause. A comma correctly introduces it; a semicolon would require an independent clause on each side.
- **`rw_m2_q18`:** Keeping the amount of silver per coin unchanged while reducing the coin’s total weight raises its silver percentage without requiring more silver. Raising the required threshold above 80% would instead make the existing low-silver coins even less acceptable for trade.
- **`rw_m2_q19`:** The verb “decided” takes the infinitive “to include” here: the committee decided to include tug-of-war. “Decided included” is ungrammatical.
- **`rw_m2_q25`:** The comma sets off “though” as an adverb referring back to the preceding sentence; the semicolon then joins two complete clauses. Choice A instead makes the damage to chondrites sound contrary to their lack of pristine condition, which reverses the intended relationship.
- **`math_m1_q25`:** The angles 24° and 66° are complementary, so sin 24° = cos 66° and sin 66° = cos 24°. Substitution gives (cos 66°)² + (cos 24°)², choice C.
- **`math_m2_q18`:** Adding the equations cancels y and gives 0 = 13x − 6. Thus 13x = 6 and 39x = 18, choice D.
- **`math_m2_q24`:** Since tan X = YZ/XZ = 12/35 and YZ = 24, XZ = 70. The hypotenuse is √(24² + 70²) = 74, so the perimeter is 24 + 70 + 74 = 168, choice B.
- **`math_m2_q25`:** Completing the square gives (x + 7)² + (y − 3)² = 109 + 49 + 9 = 167. The radius is therefore √167, choice C.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,624 |
| Output tokens | 4,327 |
| Server time | 213 ms |
| Network round trip | 181 ms |
| Calculated combined time | ≈ 394 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 213.47391800009063`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 92 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1ebca8a3b3ea16c47ff9a53430f147b7d02`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `0b65f01c0ce342fff186f0508e45e8cbb0fb45ea9e0c6ed33d66d825f0d0f6b5` |
| [state.json](state.json) | `5ab1e023235a3a949f61ef4c9a43cbc7b759a1ece69c1f61b2930fa551e5f636` |
| [answer_key.json](answer_key.json) | `2dbfcb10fe44e5a1ca9ccfa9f2fb76c5860d0dd587638262ca75baff170add1e` |
| [responses.json](responses.json) | `b8ad33888e4ff189f236c7913fb1cc74f6608cd9d1f5ec00a51cfff8f51ab027` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-7/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
