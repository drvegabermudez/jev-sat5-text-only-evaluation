# SAT Practice Test 6: ready for Jev

**88 original multiple-choice questions:** 61 Reading and Writing and 27 Math. No model responses have been recorded yet.

## Send to Jev

Use [questions.json](questions.json) as the Choice question map and [state.json](state.json) as the shared state. Both files are ready to paste into the corresponding TypeSafe fields. Send only those two files to the model.

[answer_key.json](answer_key.json) is for grading after the response arrives. It contains the official answer letter, answer text, and source PDF page for each included question. Save Jev’s unmodified output as `responses.json` in this folder when available.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 88 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference; not a model input |
| README.md | Sources, selection, omissions, and overlap check |

## Source and selection

The source is College Board’s **The SAT Practice Test #6**, © 2024, 56-page nonadaptive paper form, with cover identifiers `WX4P0010` and `6VSL02`.

- [Official test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-6-digital.pdf)
- [Official scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-6-digital.pdf), answer key on page 4
- [Official answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-6-answers-digital.pdf)

The question set preserves the source wording and original choices, with line wrapping normalized for text. Underlining is marked explicitly; fractions, roots, and exponents are represented with Unicode symbols and grouped linear notation. All selected items were checked against rendered source pages. Their answer letters agree in both official answer documents.

Only multiple-choice items whose complete context is in text are included. All items containing a graph, diagram, or table are excluded, including items with visual answer choices. Numerical-response items are excluded without adding artificial choices. Geometry questions remain when the original item supplies all relationships in text and has no accompanying figure.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 3 | 30 |
| Reading and Writing 2 | 33 | 2 | 31 |
| Math 1 | 27 | 15 | 12 |
| Math 2 | 27 | 12 | 15 |
| **Total** | **120** | **32** | **88** |

There are 20 exclusions with graphs, diagrams, or tables and 12 additional numerical-response exclusions. Two visual exclusions are also numerical-response items, so all 14 original numerical-response questions are excluded.

## Overlap with Test 5

The 88 selected questions were compared with the 91 questions in [Test 5](../test-5/questions.json), using normalized stems and all four options. There were **no identical questions**. A word-sequence similarity check also found no shared passage spans of 18 or more consecutive tokens in the stems. This is a text-overlap check, not evidence about model training exposure or complete independence of the skills tested.

Question IDs retain their source section, module, and number. IDs are local to each test: for example, `rw_m1_q01` identifies different questions in Test 5 and Test 6. Keep files from different tests in their respective folders.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q11` | 8 | Table of annual US car production. |
| `rw_m1_q14` | 10 | Graph of attentiveness scores by leave condition. |
| `rw_m1_q15` | 11 | Graph of lizard speeds when pursuing prey or escaping predators. |
| `rw_m2_q13` | 23 | Graph of national-park recreation visits. |
| `rw_m2_q15` | 24 | Table of patient ratings after 21 days. |
| `math_m1_q02` | 35 | Scatterplot and graphical answer choices. |
| `math_m1_q05` | 36 | Graph of an object’s height over time. |
| `math_m1_q06` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q11` | 38 | Answer choices are tables. |
| `math_m1_q13` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 38 | Right-triangle diagram; also a numerical-response item. |
| `math_m1_q15` | 39 | Graph of active projects over time. |
| `math_m1_q19` | 40 | Table of employee counts by restaurant. |
| `math_m1_q20` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 40 | Graph of a quadratic function; also a numerical-response item. |
| `math_m1_q23` | 41 | Includes a circle graph explicitly referenced as “shown.” |
| `math_m1_q24` | 41 | Right-triangle diagram with angle and side labels. |
| `math_m1_q26` | 42 | Table of function values. |
| `math_m1_q27` | 42 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q02` | 46 | Includes an intersecting-lines diagram explicitly referenced in the text. |
| `math_m2_q04` | 46 | Graph used to classify a function. |
| `math_m2_q05` | 47 | Graph used to read a y-intercept. |
| `math_m2_q06` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q13` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q19` | 50 | Table of train capacities. |
| `math_m2_q20` | 50 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 50 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q26` | 52 | Scatterplot with a line of best fit. |
| `math_m2_q27` | 52 | Original question requires a numerical response and has no A–D choices. |

## File identification

SHA-256 hashes identify the exact prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `90165a44f9070de0a157365579815b7d0ee7cd6f9d2cb9cd61b4fa57d109f300` |
| `state.json` | `403a01dcd56408533f88aed02f7172ed54cb2404d3caac514d61f614a6613949` |
| `answer_key.json` | `0e74b92d8396721c989e556046f1ad1d71d6333a319de979489f0b682e404561` |

## Attribution and reporting

SAT content is © 2024 College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

After Jev returns its answers, report raw accuracy on these 88 questions and section/module breakdowns. This selected subset does not produce an official SAT scaled score.
