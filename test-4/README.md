# SAT Practice Test 4: Jev evaluation

**Jev 1.13.0 scored 87/92 (94.6%)** on the selected questions: **59/62 Reading and Writing** and **28/30 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 92 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, and file identification |

Keep the answer key out of model inputs. Reported server time is **198 ms** and the user-reported network round trip is **107 ms**, for a calculated combined time of **approximately 305 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-4/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #4**, the 56-page nonadaptive paper form for the digital SAT. The test and scoring guide are hosted by College Board.

- [Test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf)
- [Scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-4-digital.pdf), answer key on page 4
- [Answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 3 | 30 |
| Reading and Writing 2 | 33 | 1 | 32 |
| Math 1 | 27 | 12 | 15 |
| Math 2 | 27 | 12 | 15 |
| **Total** | **120** | **28** | **92** |

There are 15 visual exclusions and 13 additional numerical-response exclusions. 1 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q13` | 10 | Graph of organic farms by US state. |
| `rw_m1_q15` | 11 | Table of ablation rates for cosmic dust. |
| `rw_m1_q17` | 12 | Table of plant growth with mycorrhizal fungi. |
| `rw_m2_q13` | 23 | Graph of economic policy uncertainty. |
| `math_m1_q01` | 34 | Bar graph of students’ votes for activities. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q08` | 35 | Table of a linear function’s values. |
| `math_m1_q09` | 35 | Diagram of two labeled right triangles. |
| `math_m1_q10` | 36 | Scatterplot used to select a linear model. |
| `math_m1_q12` | 36 | Graph used to identify a line’s equation. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q20` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q27` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q01` | 42 | Line graph of estimated chipmunk populations. |
| `math_m2_q06` | 43 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 43 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q08` | 43 | Answer choices are tables of function values. |
| `math_m2_q13` | 44 | Table of tile colors and shapes; also a numerical-response item. |
| `math_m2_q14` | 44 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q16` | 45 | Diagram of parallel lines and a transversal. |
| `math_m2_q20` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q22` | 46 | Graph of a system of linear equations. |
| `math_m2_q24` | 47 | Dot plot of a data set. |
| `math_m2_q27` | 48 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized question stems were compared across the selected sets for Tests 1–7; no exact duplicates were found. Similar math templates remain, with different equations, values, or requested quantities. No items were excluded for duplication. This checks text overlap, not independence of tested skills or absence from model training data.

IDs preserve the source section, module, and question number. They are local to each test folder: `rw_m1_q01` identifies a different question in each test.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `83558559495c9397c41081f42f6ef6500f5bc48d69df297990dcf73c9691c973` |
| `state.json` | `7faa96ec775640751d1e98d9d82eafe2100ac8f0421f14b23e69d2fae8c90e0d` |
| `answer_key.json` | `4fd4e72052d0afe062cd956d0fa6fb3fdd326d313d79f75384a56f6c26ff9222` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-4-digital.pdf` | `5d4a55e241f46beec90c6f273c346be6b6d5231127d73068083d881aa2a37d7a` |
| `scoring-sat-practice-test-4-digital.pdf` | `c518fd9af053b94417040a90f74e9f85763e0be759a5efdf3c86b13f60566262` |
| `sat-practice-test-4-answers-digital.pdf` | `ee2ed6b3a5d77994b6e6ad460137f6959c5b142695ae20e0bb28089171649b56` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
