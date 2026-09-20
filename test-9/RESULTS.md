# SAT Practice Test 9 evaluation results

**jev-1.13.0: 82/93 (88.2%) correct.**

The [official College Board scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-9-digital.pdf), page 4, supplies the answer letters recorded in [answer_key.json](answer_key.json). Each correct answer receives one point; omitted questions are not scored.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 24/28 | 85.7% |
| Reading and Writing, Module 2 | 29/33 | 87.9% |
| Math, Module 1 | 16/17 | 94.1% |
| Math, Module 2 | 13/15 | 86.7% |
| **Reading and Writing** | 53/61 | 86.9% |
| **Math** | 29/32 | 90.6% |
| **Overall** | 82/93 | 88.2% |

## Incorrect answers

Eight errors are in Reading and Writing: seven test Standard English conventions and one tests a logical transition. Three errors are in Math. Confidence below is the exported `confidence` field, distinct from the probability assigned to the selected option.

| Question | Jev answered | Correct answer | Confidence |
|---|---|---|---:|
| `rw_m1_q22` | D: nickname; however, | C: nickname, however, | 58% |
| `rw_m1_q24` | A: emerged | C: emerged: | 63% |
| `rw_m1_q25` | C: suggests | A: suggesting | 91% |
| `rw_m1_q30` | C: Specifically, | B: By contrast, | 60% |
| `rw_m2_q23` | C: content in that era, | B: content; in that era, | 43% |
| `rw_m2_q24` | A: compound, aluminum oxide | D: compound aluminum oxide | 64% |
| `rw_m2_q25` | A: are highly prized | C: highly prized | 56% |
| `rw_m2_q26` | B: conservation; though | C: conservation, though; | 20% |
| `math_m1_q19` | A: −9 | D: 18 | 45% |
| `math_m2_q04` | A: −3 | B: 6 | 22% |
| `math_m2_q26` | C: I and II | D: Neither I nor II | 31% |

## Explanations

- **`rw_m1_q22`:** Commas bracket “however.” The following “feeling” phrase explains Scott-Heron’s resistance but is not an independent clause that can follow a semicolon.
- **`rw_m1_q24`:** The colon introduces an explanation of the divergent strategies. Without punctuation after “emerged,” the complete introductory statement runs into the explanation.
- **`rw_m1_q25`:** The main clause is “This hypothesis … cannot stand.” “Suggesting” describes the hypothesis; “suggests” adds an incompatible second main verb.
- **`rw_m1_q30`:** The second sentence contrasts oxygen intake stopping, and the glow ending, with oxygen intake starting the glow. “By contrast” expresses that relationship.
- **`rw_m2_q23`:** The semicolon separates two independent clauses. A comma after “in that era” sets off the introductory phrase within the second clause.
- **`rw_m2_q24`:** “Aluminum oxide” identifies which chemical compound was used. It belongs directly after “compound,” with no separating commas.
- **`rw_m2_q25`:** “Its vehicles highly prized …” adds a descriptive phrase. Inserting “are” creates a second independent clause joined to the first by only a comma.
- **`rw_m2_q26`:** “Though” belongs to the preceding claim, contrasting it with the initial expectation. The semicolon then introduces the explanation of increased resource use.
- **`math_m1_q19`:** The first equation simplifies to 4x − 18y = 5. With h = 18, the second becomes 4x − 18y = −2: parallel, distinct lines with no solution.
- **`math_m2_q04`:** Adding 3x = 12 and −3x + y = −6 cancels x and gives y = 6.
- **`math_m2_q26`:** At x = 0, the intercept is a(1 + 2.2^b) = a + m. Form I displays k = 2.2^b, and form II displays m = a·2.2^b; neither displays the entire intercept as a constant or coefficient.

## Overlap with earlier tests

The [test overview](README.md#overlap-and-question-ids) identifies 37 questions with the same normalized stem and answer texts in Tests 1–8. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. These are retained in the full Test 9 score.

| Test 9 cohort | Correct | Accuracy |
|---|---:|---:|
| Matches an earlier selected question | 34/37 | 91.9% |
| No exact earlier match found | 48/56 | 85.7% |

This comparison does not establish novelty relative to model training data or rule out similar templates and partial text overlap. A pooled score across Tests 1–9 counts repeated questions more than once unless an explicit deduplication rule is applied.

## Reported usage and timing

| Metric | Value |
|---|---:|
| Input tokens | 18,677 |
| Output tokens | 4,374 |
| Server time | 206 ms |
| Network round trip | 100 ms |
| Calculated combined time | ≈ 306 ms |

Token counts and server time come from the service export (`evaluation_time_ms = 205.641459004255`). The user confirmed the server-time interpretation and reported the network round-trip time. The combined time adds these two values; it is not a separate end-to-end measurement.

## Validation and provenance

All 93 expected answers are present, with no unexpected IDs. Every answer uses an original A–D option. All probabilities and confidence values lie between 0 and 1, and every selected answer has the highest reported probability. Answer-key text matches the corresponding original option. Of the 93 probability distributions, 92 sum to 1. The distribution for `math_m2_q24` totals 0.99 (A: 0.93, B: 0, C: 0.05, D: 0.01). The export is preserved without normalization. Choice A is correct; grading by selected answer is unaffected. The evaluator permits this specific recorded total and rejects any other unexpected total.

Request identifier: `playground_1eb819d1b60f49349f497facace04149b23`. The [response export](responses.json) is preserved byte-for-byte. Prepared inputs and the grading key are unchanged. These hashes identify the evaluated artifacts:

| File | SHA-256 |
|---|---|
| [questions.json](questions.json) | `06d37cdb9d77064cbaca768f4170030104b164ed418c26b4f4daeb939109b347` |
| [state.json](state.json) | `ef0f0f82b4726b989fc7ab285e7334f5a97e3c0a40e614a596ed9056f8010532` |
| [answer_key.json](answer_key.json) | `5cb12d05480f2ad2f74b7bfa1c105a902f37d3f0c7134b7a8531d4dde8bb311a` |
| [responses.json](responses.json) | `3fc2d8db9845e6a30d910808aab9c27c6902a8c90cfe9cff291c1e909d38522d` |

The export does not embed the original request, execution timestamp, or sampling settings; exact remote inputs cannot be independently verified from it. The score is raw accuracy on the selected subset, not an official SAT scaled score. See the [model evaluation card](MODEL_CARD.md) for scope and limitations.

## Reproduce the results

Run `python3 evaluate.py --check` from this folder, or `python3 test-9/evaluate.py --check` from the repository root. The script verifies the artifact hashes, checks all responses with the documented probability-total exception, recalculates the grade and overlap-cohort scores, and checks both reports. No external packages, credentials, or model calls are required.

Generated by `python3 evaluate.py --write`.
