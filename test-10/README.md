# SAT Practice Test 10: ready for Jev

**91 original text-only multiple-choice questions** are ready to run: **61 Reading and Writing** and **30 Math**. No Jev response has been recorded for this test yet.

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 91 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| README.md | Sources, selection, omissions, overlap, and file identification |

Keep the answer key out of model inputs. The model’s response export, results, timing, and model evaluation card can be added after the run.

## Source and selection

The source is College Board’s **The SAT Practice Test #10**, the 56-page nonadaptive paper form for the digital SAT. The test, scoring guide, and answer explanations are available from College Board’s [practice-test page](https://satsuite.collegeboard.org/practice/practice-tests/paper).

- [Test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-10-digital.pdf)
- [Scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-10-digital.pdf), answer key on PDF page 4
- [Answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-10-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 1 | 32 |
| Reading and Writing 2 | 33 | 4 | 29 |
| Math 1 | 27 | 13 | 14 |
| Math 2 | 27 | 11 | 16 |
| **Total** | **120** | **29** | **91** |

There are 15 visual exclusions and 14 additional numerical-response exclusions. 0 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q17` | 11 | Graph of fruit-fly survival following infection. |
| `rw_m2_q11` | 22 | Graph of wild-mammal biomass by species. |
| `rw_m2_q12` | 23 | Table of clamshell tools by cave depth. |
| `rw_m2_q13` | 24 | Graph of power-conversion efficiency and electron-transport layers. |
| `rw_m2_q14` | 25 | Table of employment by sector in France and the United States. |
| `math_m1_q01` | 34 | Line graph of used cars by model year. |
| `math_m1_q02` | 34 | Graph of a system of linear equations. |
| `math_m1_q04` | 36 | Graph of a translated function and graphical answer choices on the following page. |
| `math_m1_q06` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q08` | 38 | Table of mascot votes by grade level. |
| `math_m1_q13` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q17` | 40 | Table of plant height and time. |
| `math_m1_q19` | 40 | Answer choices are tables of x and y values. |
| `math_m1_q20` | 41 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 41 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q27` | 42 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q02` | 46 | Scatterplot with a line of best fit. |
| `math_m2_q03` | 46 | Graph of a linear relationship and tabular answer choices. |
| `math_m2_q06` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q13` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q16` | 49 | Graph of shares of stock that can be purchased. |
| `math_m2_q20` | 50 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 50 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q26` | 52 | Histograms of two data sets. |
| `math_m2_q27` | 52 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized text comparison found **45 of the 91 included questions** with the same stem and answer texts in earlier test folders. These items are retained to preserve the source test. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order; each question retains the order printed in this test. The table lists all detected matches.

| This test | Earlier test question |
|---|---|
| `rw_m1_q02` | [Test 1, `rw_m2_q01`](../test-1/questions.json) |
| `rw_m1_q03` | [Test 1, `rw_m1_q01`](../test-1/questions.json) |
| `rw_m1_q04` | [Test 1, `rw_m1_q04`](../test-1/questions.json) |
| `rw_m1_q08` | [Test 2, `rw_m2_q08`](../test-2/questions.json) |
| `rw_m1_q09` | [Test 3, `rw_m1_q10`](../test-3/questions.json) |
| `rw_m1_q10` | [Test 3, `rw_m2_q08`](../test-3/questions.json) |
| `rw_m1_q12` | [Test 2, `rw_m2_q09`](../test-2/questions.json) |
| `rw_m1_q14` | [Test 1, `rw_m2_q12`](../test-1/questions.json) |
| `rw_m1_q15` | [Test 3, `rw_m2_q11`](../test-3/questions.json) |
| `rw_m1_q16` | [Test 2, `rw_m2_q12`](../test-2/questions.json) |
| `rw_m1_q19` | [Test 3, `rw_m1_q19`](../test-3/questions.json) |
| `rw_m1_q20` | [Test 1, `rw_m2_q20`](../test-1/questions.json) |
| `rw_m1_q21` | [Test 3, `rw_m1_q21`](../test-3/questions.json) |
| `rw_m1_q22` | [Test 1, `rw_m2_q21`](../test-1/questions.json) |
| `rw_m1_q23` | [Test 2, `rw_m2_q19`](../test-2/questions.json) |
| `rw_m1_q24` | [Test 2, `rw_m1_q23`](../test-2/questions.json) |
| `rw_m1_q28` | [Test 2, `rw_m2_q28`](../test-2/questions.json) |
| `rw_m1_q33` | [Test 3, `rw_m1_q32`](../test-3/questions.json) |
| `rw_m2_q01` | [Test 3, `rw_m1_q01`](../test-3/questions.json) |
| `rw_m2_q02` | [Test 1, `rw_m2_q03`](../test-1/questions.json) |
| `rw_m2_q03` | [Test 1, `rw_m2_q07`](../test-1/questions.json) |
| `rw_m2_q09` | [Test 3, `rw_m1_q12`](../test-3/questions.json) |
| `rw_m2_q10` | [Test 1, `rw_m2_q11`](../test-1/questions.json) |
| `rw_m2_q17` | [Test 2, `rw_m1_q19`](../test-2/questions.json) |
| `rw_m2_q18` | [Test 1, `rw_m1_q19`](../test-1/questions.json) |
| `rw_m2_q19` | [Test 1, `rw_m2_q22`](../test-1/questions.json) |
| `rw_m2_q20` | [Test 3, `rw_m2_q18`](../test-3/questions.json) |
| `rw_m2_q21` | [Test 1, `rw_m2_q23`](../test-1/questions.json) |
| `rw_m2_q22` | [Test 3, `rw_m2_q20`](../test-3/questions.json) |
| `rw_m2_q25` | [Test 1, `rw_m1_q24`](../test-1/questions.json) |
| `rw_m2_q26` | [Test 3, `rw_m1_q27`](../test-3/questions.json) |
| `rw_m2_q30` | [Test 1, `rw_m1_q31`](../test-1/questions.json) |
| `rw_m2_q31` | [Test 3, `rw_m2_q32`](../test-3/questions.json) |
| `math_m1_q03` | [Test 1, `math_m1_q03`](../test-1/questions.json) |
| `math_m1_q05` | [Test 1, `math_m2_q04`](../test-1/questions.json) |
| `math_m1_q10` | [Test 2, `math_m1_q11`](../test-2/questions.json) |
| `math_m1_q11` | [Test 2, `math_m2_q05`](../test-2/questions.json) |
| `math_m1_q15` | [Test 2, `math_m1_q16`](../test-2/questions.json) |
| `math_m1_q18` | [Test 2, `math_m1_q19`](../test-2/questions.json) |
| `math_m1_q23` | [Test 2, `math_m2_q24`](../test-2/questions.json) |
| `math_m1_q24` | [Test 2, `math_m2_q25`](../test-2/questions.json) |
| `math_m2_q10` | [Test 2, `math_m2_q11`](../test-2/questions.json) |
| `math_m2_q17` | [Test 2, `math_m2_q15`](../test-2/questions.json) |
| `math_m2_q23` | [Test 1, `math_m2_q24`](../test-1/questions.json) |
| `math_m2_q24` | [Test 3, `math_m2_q26`](../test-3/questions.json) |

The answer choices for `rw_m1_q09` are ordered differently from Test 3’s `rw_m1_q10`; the answer key follows Test 10’s original order.

This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Future results pooled across all tests should distinguish repeated items from distinct questions. IDs preserve the source section, module, and question number and are local to each test folder; identify an item by its test number and question ID together.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `3c5a989e53063c688ccdbf0f21ae41d3fd54ba985e6a2f9097084ef5d79801e6` |
| `state.json` | `fb11e919adb591e66a830ed703028088550cf895974410fa8a4c8e5a9b17eb53` |
| `answer_key.json` | `3dd740f947c03c9856283d6fcc4553c1c18187246bc1bb909c2a4b86bc0b58c9` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-10-digital.pdf` | `4dda8203caba0f4a377f6b0ff72b194799483cd39e3145e96f68dfc872d1cc2c` |
| `scoring-sat-practice-test-10-digital.pdf` | `d33ca9d96e78888d26b4685d099e0598e56cc8122703b3f4e8e5b9d1ac3e35c2` |
| `sat-practice-test-10-answers-digital.pdf` | `50ef64c8c9dd47e63eef7a247ef09f258451dabd68e93ea2f0dca5674f5f2d6f` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results will report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
