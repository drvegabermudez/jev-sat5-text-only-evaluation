# SAT Practice Test 3 evaluation results

**jev-1.13.0: 84/94 (89.4%) correct.**

The [College Board scoring guide mirrored by APCORE](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-3-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 28/32 | 87.5% |
| Reading and Writing, Module 2 | 26/30 | 86.7% |
| Math, Module 1 | 14/15 | 93.3% |
| Math, Module 2 | 16/17 | 94.1% |
| **Reading and Writing** | 54/62 | 87.1% |
| **Math** | 30/32 | 93.8% |
| **Overall** | 84/94 | 89.4% |

## Incorrect answers

Eight errors are in Reading and Writing: seven test Standard English conventions and one tests synthesis of notes for a specified audience. Two errors are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q23` | A: added, whenever | D: added whenever | 39% |
| `rw_m1_q25` | D: nickname; however, | C: nickname, however, | 50% |
| `rw_m1_q26` | A: quilts, and the | B: quilts, the | 25% |
| `rw_m1_q28` | D: The rocking chair is made from walnut, and it has been shaped such that its armrests and seat are sleek and contoured. | A: With its sleek, contoured armrests and seat, the walnut rocking chair in Boston’s Museum of Fine Arts is just one piece of furniture created by American woodworker Sam Maloof. | 41% |
| `rw_m2_q21` | C: decade; while | D: decade, while | 30% |
| `rw_m2_q22` | B: energy collected by solar panels during the day | C: energy collected by solar panels during the day, | 88% |
| `rw_m2_q26` | B: tombs, built | A: tombs. Built | 20% |
| `rw_m2_q27` | A: compound, aluminum oxide | D: compound aluminum oxide | 64% |
| `math_m1_q18` | A: 7 | B: 14 | 44% |
| `math_m2_q25` | C: 94 | B: 47√2 | 40% |

## Explanations

- **`rw_m1_q23`:** The clause beginning “whenever” specifies the condition under which a leap second is added. It follows “is added” directly without a comma, semicolon, or period, so choice D is correct.
- **`rw_m1_q25`:** Commas set off “however,” while the phrase beginning “feeling” explains why Scott-Heron resisted the nickname. That phrase is not an independent clause, so the semicolon in choice D cannot introduce it.
- **`rw_m1_q26`:** “The stitching barely visible…” is a supplementary phrase, not an independent clause. A comma attaches that description to the statement that the portraits are quilts; adding “and” does not produce a grammatical continuation.
- **`rw_m1_q28`:** The requested answer must both describe the rocking chair and introduce its maker to an unfamiliar audience. Choice A describes the chair and identifies Sam Maloof as an American woodworker. Choice D describes the chair but does not introduce Maloof.
- **`rw_m2_q21`:** The clause beginning “while” supplies contrasting information about the rougheye rockfish. A comma connects it to the main clause; a semicolon cannot separate a main clause from this dependent clause.
- **`rw_m2_q22`:** The introductory phrase “Powered with energy collected by solar panels during the day” needs a comma before the main clause beginning “the blinking LEDs.” Choice B omits that comma.
- **`rw_m2_q26`:** The passage contains two complete sentences: Nehmé traveled to study the tombs; the burial chambers seem to blend with nature. Choice A supplies a period, and “Built into the rocky outcrops…” opens the second sentence as a modifier of the burial chambers. Choice B creates a comma splice.
- **`rw_m2_q27`:** “Aluminum oxide” identifies which chemical compound was used and is essential to the meaning. It therefore stays directly beside “chemical compound” without commas, as in choice D.
- **`math_m1_q18`:** Let n be the smaller integer. Then n(2n + 11) = 546, or (n − 14)(2n + 39) = 0. The positive solution is n = 14, and the other integer is 39; 14 × 39 = 546. Thus choice B is correct.
- **`math_m2_q25`:** If each leg has length L, the hypotenuse is L√2 and the perimeter is L(2 + √2). With L = 47√2, this equals 94√2 + 94, exactly the given perimeter. Thus the leg length is 47√2 inches, choice B.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,128 |
| Output tokens | 4,421 |
| Server time | 183 ms |
| Network round trip | 57 ms |
| Calculated combined time | ≈ 240 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 182.77623199901427`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 94 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, probability distributions sum to 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option.

Request identifier: `playground_1eb2be9e6464e504a209ec12345bb2104da`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `c406ecac593620e51e2603f4b52bc8995fc98ea4bfee0edb29343b42491b02ca` |
| [state.json](state.json) | `daed71323f5b6037f50ec96aeb3116e4da763600845fac70c938fa95a1727eb1` |
| [answer_key.json](answer_key.json) | `9df538cb37011d82b75f7d23b768cee657d5a2d09407b30ad80d731f050b627f` |
| [responses.json](responses.json) | `e8edc25f497a7772f58bc37e66490c75c31d2039490047093fc4866555e7282e` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-3/evaluate.py --check` from the repository root. The script verifies the artifact hashes, validates all responses, recalculates the grade, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
