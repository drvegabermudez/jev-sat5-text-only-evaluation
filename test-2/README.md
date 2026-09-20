# SAT Practice Test 2: Jev evaluation

**Jev 1.13.0 scored 85/93 (91.4%)** on the selected questions: **58/62 Reading and Writing** and **27/31 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 93 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, and file identification |

Keep the answer key out of model inputs. Reported server time is **253 ms** and the user-reported network round trip is **120 ms**, for a calculated combined time of **approximately 373 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-2/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #2**, the 56-page nonadaptive paper form for the digital SAT. College Board’s test and scoring guide are preserved on APCORE’s public mirror; the answer explanations are preserved on Binju’s Education’s public mirror.

- [Test PDF](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/sat-practice-test-2-digital.pdf)
- [Scoring guide](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-2-digital.pdf), answer key on page 4
- [Answer explanations](https://www.binjuseducation.com/wp-content/uploads/2025/09/sat-practice-test-2-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 1 | 32 |
| Reading and Writing 2 | 33 | 3 | 30 |
| Math 1 | 27 | 13 | 14 |
| Math 2 | 27 | 10 | 17 |
| **Total** | **120** | **27** | **93** |

There are 13 visual exclusions and 14 additional numerical-response exclusions. 0 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q14` | 9 | Graph of individuals reporting directly to CEOs. |
| `rw_m2_q10` | 22 | Graph of political orientation and probability of voting. |
| `rw_m2_q11` | 23 | Graph of spider population counts. |
| `rw_m2_q16` | 26 | Graph of power-conversion efficiency and electron-transport layers. |
| `math_m1_q01` | 34 | Line graph of used cars by model year. |
| `math_m1_q03` | 34 | Diagram of parallel lines and a transversal. |
| `math_m1_q04` | 35 | Graph used to identify a y-intercept. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q17` | 37 | Circle diagram with labeled diameters and arcs. |
| `math_m1_q20` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q22` | 38 | Answer choices are tables of x and y values. |
| `math_m1_q24` | 39 | Graph of a translated function. |
| `math_m1_q27` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q03` | 44 | Scatterplot with a line of best fit. |
| `math_m2_q04` | 45 | Graph used to evaluate a function. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q13` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q20` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q26` | 49 | Histograms of two data sets. |
| `math_m2_q27` | 49 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized question stems were compared across the selected sets for Tests 1–7; no exact duplicates were found. Similar math templates remain, with different equations, values, or requested quantities. No items were excluded for duplication. This checks text overlap, not independence of tested skills or absence from model training data.

IDs preserve the source section, module, and question number. They are local to each test folder: `rw_m1_q01` identifies a different question in each test.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `a944c25ddb43f17f63191f8f3377d48b13e849bd2992585c8fe796b3465cbf09` |
| `state.json` | `a90d86cabef79b232ce069b96e382e4e8cbc6634148167049ef0977cc3af4f08` |
| `answer_key.json` | `f80a39685cb5d6ede29f33ac142eced52c509a9ba12efc762ecf4996870063b1` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-2-digital.pdf` | `bd13cb36a1b95c4ed0488f2dd0f6213373e2bbd8884125327f9161de9e7c1fc8` |
| `scoring-sat-practice-test-2-digital.pdf` | `c6b493879135d37235f76ffa07cdae4464e2b0ad3ac16087977efe3874b2c58c` |
| `sat-practice-test-2-answers-digital.pdf` | `7b7197d54ab49f5d7d8d49f660f9ef28a143ba2affedcad708bca80ddf090527` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
