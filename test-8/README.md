# SAT Practice Test 8: Jev evaluation

**Jev 1.13.0 scored 83/91 (91.2%)** on the selected questions: **55/61 Reading and Writing** and **28/30 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 91 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, overlap cohorts, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, overlap, and file identification |

Keep the answer key out of model inputs. Reported server time is **245 ms** and the user-reported network round trip is **155 ms**, for a calculated combined time of **approximately 400 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-8/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #8**, the 56-page nonadaptive paper form for the digital SAT. The test, scoring guide, and answer explanations are available from College Board’s [practice-test page](https://satsuite.collegeboard.org/practice/practice-tests/paper).

- [Test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-8-digital.pdf)
- [Scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-8-digital.pdf), answer key on PDF page 4
- [Answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-8-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 3 | 30 |
| Reading and Writing 2 | 33 | 2 | 31 |
| Math 1 | 27 | 11 | 16 |
| Math 2 | 27 | 13 | 14 |
| **Total** | **120** | **29** | **91** |

There are 15 visual exclusions and 14 additional numerical-response exclusions. 0 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q11` | 8 | Table of video game availability by release year. |
| `rw_m1_q12` | 8 | Table of depths at which deep-sea fish live. |
| `rw_m1_q13` | 8 | Table of US housing starts. |
| `rw_m2_q14` | 23 | Table of speech and information rates for five languages. |
| `rw_m2_q15` | 24 | Table of estimated tyrannosaurid bite forces. |
| `math_m1_q03` | 34 | Graph used to identify a y-intercept. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q11` | 36 | Scatterplot used to select a linear model. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q15` | 37 | Graph of a cubic function. |
| `math_m1_q20` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q23` | 39 | Frequency table of package weights. |
| `math_m1_q27` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q01` | 44 | Graph used to identify a y-intercept. |
| `math_m2_q02` | 44 | Table of average employee counts by store type. |
| `math_m2_q03` | 44 | Diagram of parallel lines and a transversal. |
| `math_m2_q05` | 45 | Labeled right-triangle diagram. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q12` | 46 | Labeled right-triangle diagram. |
| `math_m2_q13` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q19` | 48 | Dot plots of two data sets. |
| `math_m2_q20` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q27` | 50 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized text comparison found **51 of the 91 included questions** with the same stem and answer texts in earlier test folders. These items are retained to preserve the source test. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order; each question retains the order printed in this test. The table lists all detected matches.

| This test | Earlier test question |
|---|---|
| `rw_m1_q01` | [Test 2, `rw_m1_q01`](../test-2/questions.json) |
| `rw_m1_q02` | [Test 1, `rw_m2_q02`](../test-1/questions.json) |
| `rw_m1_q04` | [Test 2, `rw_m2_q01`](../test-2/questions.json) |
| `rw_m1_q07` | [Test 3, `rw_m1_q09`](../test-3/questions.json) |
| `rw_m1_q09` | [Test 2, `rw_m2_q07`](../test-2/questions.json) |
| `rw_m1_q10` | [Test 3, `rw_m2_q10`](../test-3/questions.json) |
| `rw_m1_q14` | [Test 1, `rw_m1_q13`](../test-1/questions.json) |
| `rw_m1_q15` | [Test 2, `rw_m2_q14`](../test-2/questions.json) |
| `rw_m1_q16` | [Test 1, `rw_m1_q16`](../test-1/questions.json) |
| `rw_m1_q18` | [Test 1, `rw_m2_q18`](../test-1/questions.json) |
| `rw_m1_q19` | [Test 1, `rw_m2_q19`](../test-1/questions.json) |
| `rw_m1_q20` | [Test 1, `rw_m2_q25`](../test-1/questions.json) |
| `rw_m1_q22` | [Test 1, `rw_m1_q27`](../test-1/questions.json) |
| `rw_m1_q27` | [Test 1, `rw_m2_q29`](../test-1/questions.json) |
| `rw_m1_q30` | [Test 2, `rw_m2_q31`](../test-2/questions.json) |
| `rw_m1_q31` | [Test 2, `rw_m2_q32`](../test-2/questions.json) |
| `rw_m1_q32` | [Test 3, `rw_m2_q33`](../test-3/questions.json) |
| `rw_m1_q33` | [Test 2, `rw_m1_q33`](../test-2/questions.json) |
| `rw_m2_q03` | [Test 2, `rw_m2_q02`](../test-2/questions.json) |
| `rw_m2_q04` | [Test 3, `rw_m1_q04`](../test-3/questions.json) |
| `rw_m2_q05` | [Test 2, `rw_m1_q05`](../test-2/questions.json) |
| `rw_m2_q06` | [Test 1, `rw_m1_q07`](../test-1/questions.json) |
| `rw_m2_q07` | [Test 2, `rw_m2_q06`](../test-2/questions.json) |
| `rw_m2_q08` | [Test 3, `rw_m2_q06`](../test-3/questions.json) |
| `rw_m2_q09` | [Test 2, `rw_m1_q10`](../test-2/questions.json) |
| `rw_m2_q16` | [Test 1, `rw_m2_q14`](../test-1/questions.json) |
| `rw_m2_q17` | [Test 3, `rw_m2_q17`](../test-3/questions.json) |
| `rw_m2_q19` | [Test 2, `rw_m1_q20`](../test-2/questions.json) |
| `rw_m2_q20` | [Test 2, `rw_m1_q21`](../test-2/questions.json) |
| `rw_m2_q21` | [Test 3, `rw_m1_q22`](../test-3/questions.json) |
| `rw_m2_q23` | [Test 2, `rw_m2_q24`](../test-2/questions.json) |
| `rw_m2_q24` | [Test 2, `rw_m2_q25`](../test-2/questions.json) |
| `rw_m2_q25` | [Test 2, `rw_m2_q26`](../test-2/questions.json) |
| `rw_m2_q28` | [Test 3, `rw_m2_q28`](../test-3/questions.json) |
| `rw_m2_q29` | [Test 1, `rw_m1_q30`](../test-1/questions.json) |
| `math_m1_q01` | [Test 3, `math_m2_q04`](../test-3/questions.json) |
| `math_m1_q02` | [Test 2, `math_m1_q02`](../test-2/questions.json) |
| `math_m1_q09` | [Test 1, `math_m1_q09`](../test-1/questions.json) |
| `math_m1_q10` | [Test 3, `math_m1_q11`](../test-3/questions.json) |
| `math_m1_q18` | [Test 1, `math_m1_q19`](../test-1/questions.json) |
| `math_m1_q19` | [Test 1, `math_m1_q22`](../test-1/questions.json) |
| `math_m1_q22` | [Test 3, `math_m1_q19`](../test-3/questions.json) |
| `math_m1_q25` | [Test 1, `math_m1_q25`](../test-1/questions.json) |
| `math_m2_q04` | [Test 3, `math_m1_q03`](../test-3/questions.json) |
| `math_m2_q08` | [Test 1, `math_m2_q08`](../test-1/questions.json) |
| `math_m2_q10` | [Test 1, `math_m2_q09`](../test-1/questions.json) |
| `math_m2_q11` | [Test 1, `math_m1_q10`](../test-1/questions.json) |
| `math_m2_q18` | [Test 1, `math_m2_q19`](../test-1/questions.json) |
| `math_m2_q22` | [Test 1, `math_m2_q22`](../test-1/questions.json) |
| `math_m2_q23` | [Test 2, `math_m2_q19`](../test-2/questions.json) |
| `math_m2_q25` | [Test 1, `math_m1_q26`](../test-1/questions.json) |

This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Future results pooled across all tests should distinguish repeated items from distinct questions. IDs preserve the source section, module, and question number and are local to each test folder; identify an item by its test number and question ID together.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `d8269591557b3ead80b3da92fb532658f517801ae3fc8c399fbda96d6eea47ab` |
| `state.json` | `69dd2c0d88774aae93a47d05712c7d16f3fb642621a7fa3283779396cf6f20ab` |
| `answer_key.json` | `7e68b171f7d1f8440df6e8db94a946125fd92db44da24b60baacd849ebb38c70` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-8-digital.pdf` | `b1599121d38fd6f1f3207774c4bad4d73aceac43dd46ad3dd95f08c60f145b63` |
| `scoring-sat-practice-test-8-digital.pdf` | `8582d33f07624136dcfc6fe6b3f8a2e76b5b25310903262d975fbc7b3ec79bc6` |
| `sat-practice-test-8-answers-digital.pdf` | `bdfd870bbf13da9d01bffcf2f6a0738e6c9c397193ae8733087ca57e2f1401cc` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
