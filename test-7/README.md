# SAT Practice Test 7: ready for Jev

**92 original multiple-choice questions:** 61 Reading and Writing and 31 Math. No model responses have been recorded yet.

## Send to Jev

Use [questions.json](questions.json) as the Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model.

[answer_key.json](answer_key.json) is for grading after the response arrives. It contains the official answer letter, answer text, and source PDF page for every included question.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 92 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference; not a model input |
| README.md | Sources, selection, omissions, and overlap check |

## Source and selection

The source is College Board’s **The SAT Practice Test #7**, © 2025, 56-page nonadaptive paper form, with cover identifiers `WX5P0001` and `6WSL01`.

- [Official test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-7-digital.pdf)
- [Official scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-7-digital.pdf), answer key on page 4
- [Official answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-7-answers-digital.pdf)

Included questions retain the source wording and original A–D choices. Line wrapping is normalized; underlining is marked explicitly, and the poem retains its line breaks. Fractions, exponents, roots, absolute values, and segment overbars use Unicode symbols and grouped text notation. All question pages were reviewed visually, and every included answer agrees in both official answer documents.

Only original multiple-choice items whose complete context can be represented in text are included. Items with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response items are excluded without inventing choices.

A reference to a figure, point, or graph does not by itself require an image. For example, `math_m1_q02` supplies both rectangle areas in words; `math_m1_q22` supplies the circle radius and triangle perimeter; `math_m2_q25` supplies the complete circle equation. These original items have no accompanying figure and retain all their context.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 3 | 30 |
| Reading and Writing 2 | 33 | 2 | 31 |
| Math 1 | 27 | 12 | 15 |
| Math 2 | 27 | 11 | 16 |
| **Total** | **120** | **28** | **92** |

There are 15 exclusions with graphs or tables and 13 additional numerical-response exclusions. One visual exclusion also requires a numerical response, so all 14 original numerical-response questions are excluded.

## Overlap with Tests 5 and 6

The 92 selected questions were compared with the 91 questions in [Test 5](../test-5/questions.json) and the 88 questions in [Test 6](../test-6/questions.json). Normalized question stems and complete questions with their choices have **no exact duplicates** across these sets. The closest wording matches were reviewed: they use different functions, values, and answer choices. No questions were omitted for duplication. This checks text overlap; it does not establish independence of tested skills or absence from model training data.

Question IDs preserve their source section, module, and number. IDs are local to each test folder: `rw_m1_q01` identifies different questions in Tests 5, 6, and 7.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q12` | 8 | Graph of factors mentioned by participants considering reusable containers. |
| `rw_m1_q15` | 11 | Graph of urban land expansion attributed to population and GDP growth. |
| `rw_m1_q16` | 12 | Graph of China’s imports by type and year. |
| `rw_m2_q12` | 24 | Table of bus shelters with shade and summer surface temperatures. |
| `rw_m2_q13` | 25 | Table of areas and populations of Arabian Peninsula countries. |
| `math_m1_q01` | 34 | Scatterplot of temperature and distance above sea level, with a line of best fit. |
| `math_m1_q05` | 35 | Bar graph of daily battery charges. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q08` | 35 | Graph of a tablet’s estimated value over time. |
| `math_m1_q11` | 36 | Graph of an absolute value function and a linear function. |
| `math_m1_q13` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q20` | 38 | Scatterplot of chamber temperature over time; also a numerical-response item. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q24` | 39 | Table of x and y values. |
| `math_m1_q27` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q03` | 44 | Graph of a quadratic function used to identify its vertex. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q12` | 46 | Scatterplot with a line of best fit. |
| `math_m2_q13` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q16` | 47 | Answer choices are tables of x and y values. |
| `math_m2_q20` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q22` | 49 | Table of function values. |
| `math_m2_q27` | 50 | Original question requires a numerical response and has no A–D choices. |

## File identification

SHA-256 hashes identify the exact prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `0b65f01c0ce342fff186f0508e45e8cbb0fb45ea9e0c6ed33d66d825f0d0f6b5` |
| `state.json` | `5ab1e023235a3a949f61ef4c9a43cbc7b759a1ece69c1f61b2930fa551e5f636` |
| `answer_key.json` | `2dbfcb10fe44e5a1ca9ccfa9f2fb76c5860d0dd587638262ca75baff170add1e` |

## Attribution and reporting

SAT content is © 2025 College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

After Jev returns its answers, report raw accuracy on these 92 questions and section/module breakdowns. This selected subset does not produce an official SAT scaled score.
