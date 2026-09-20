# SAT Practice Test 11: ready for Jev

**87 original text-only multiple-choice questions** are ready to run: **62 Reading and Writing** and **25 Math**. No Jev response has been recorded for this test yet.

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 87 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| README.md | Sources, selection, omissions, overlap, and file identification |

Keep the answer key out of model inputs. The model’s response export, results, timing, and model evaluation card can be added after the run.

## Source and selection

The source is College Board’s **The SAT Practice Test #11**, the 52-page nonadaptive paper form for the digital SAT. The test, scoring guide, and answer explanations are available from College Board’s [practice-test page](https://satsuite.collegeboard.org/practice/practice-tests/paper).

- [Test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-11-digital.pdf)
- [Scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-11-digital.pdf), answer key on PDF page 4
- [Answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-11-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 1 | 32 |
| Reading and Writing 2 | 33 | 3 | 30 |
| Math 1 | 27 | 13 | 14 |
| Math 2 | 27 | 16 | 11 |
| **Total** | **120** | **33** | **87** |

There are 20 visual exclusions and 13 additional numerical-response exclusions. 1 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q15` | 10 | Graph of energy density for four fuels. |
| `rw_m2_q11` | 22 | Graph of census populations for four Canadian cities. |
| `rw_m2_q12` | 22 | Graph of animal groups represented in drawings. |
| `rw_m2_q13` | 23 | Graph of US Congress members who identified as veterans. |
| `math_m1_q01` | 34 | Labeled triangle diagram. |
| `math_m1_q05` | 35 | Table of sandwich choices. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q15` | 37 | Scatterplot with a line of best fit. |
| `math_m1_q18` | 38 | Answer choices are graphs of a system of equations. |
| `math_m1_q19` | 39 | Labeled right-triangle diagram. |
| `math_m1_q20` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q23` | 40 | Graph of a transformed exponential function. |
| `math_m1_q27` | 41 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q02` | 44 | Dot plot of sea-star diameters. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q09` | 45 | Graph used to classify a function. |
| `math_m2_q10` | 46 | Shaded coordinate graph used to identify an inequality. |
| `math_m2_q13` | 47 | Labeled right-triangle diagram; also a numerical-response item. |
| `math_m2_q14` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q15` | 47 | Graph of boiling point and molecular weight. |
| `math_m2_q17` | 48 | Table of a linear function’s values. |
| `math_m2_q18` | 48 | Table of a quadratic function’s values. |
| `math_m2_q19` | 49 | Graph relating numbers of two types of stars. |
| `math_m2_q20` | 49 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 49 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q23` | 50 | Diagram of intersecting segments and triangles. |
| `math_m2_q25` | 50 | Histogram of points scored by players. |
| `math_m2_q27` | 51 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

No exact matches of normalized stems and answer texts were found against the selected sets for Tests 1–10. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order. Similar question templates or partial text overlap may remain.

This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Future results pooled across all tests should distinguish repeated items from distinct questions. IDs preserve the source section, module, and question number and are local to each test folder; identify an item by its test number and question ID together.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `bbaefe864750788e4094d6032acfe663f843845617525ee17be7a87651284984` |
| `state.json` | `847e427f00270c39015e8a749763a750907ec77a3eaf58ae074578fdeae1cf70` |
| `answer_key.json` | `ba67bca064be38a7b3119f690243b8ebe69de7fd0c0051f31f42dbfd474dc39a` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-11-digital.pdf` | `c5376d25a691f6774fa328a83516c068c226b33e3683055a0873e2fb7b0bd428` |
| `scoring-sat-practice-test-11-digital.pdf` | `8cf577b00d2ee8dd9d0c5bdb15b98bd2802cfdb9409ce2b51b41a59c0d92d3cd` |
| `sat-practice-test-11-answers-digital.pdf` | `049ecb1ea0fe13557964803a724b279f58243bd8ada18c0d794654c54a86ea4d` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results will report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
