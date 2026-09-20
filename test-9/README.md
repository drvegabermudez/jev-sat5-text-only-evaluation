# SAT Practice Test 9: Jev evaluation

**Jev 1.13.0 scored 82/93 (88.2%)** on the selected questions: **53/61 Reading and Writing** and **29/32 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 93 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, overlap cohorts, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, overlap, and file identification |

Keep the answer key out of model inputs. Reported server time is **206 ms** and the user-reported network round trip is **100 ms**, for a calculated combined time of **approximately 306 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-9/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #9**, the 56-page nonadaptive paper form for the digital SAT. The test, scoring guide, and answer explanations are available from College Board’s [practice-test page](https://satsuite.collegeboard.org/practice/practice-tests/paper).

- [Test PDF](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-9-digital.pdf)
- [Scoring guide](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-9-digital.pdf), answer key on PDF page 4
- [Answer explanations](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-9-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 5 | 28 |
| Reading and Writing 2 | 33 | 0 | 33 |
| Math 1 | 27 | 10 | 17 |
| Math 2 | 27 | 12 | 15 |
| **Total** | **120** | **27** | **93** |

There are 15 visual exclusions and 12 additional numerical-response exclusions. 2 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q11` | 7 | Table of recordings of dolphins with their calves. |
| `rw_m1_q12` | 7 | Table of maximum maple-tree heights and native ranges. |
| `rw_m1_q13` | 8 | Graph of plant metal content with and without kanamycin. |
| `rw_m1_q14` | 9 | Table of torpor bouts and arousal episodes. |
| `rw_m1_q15` | 10 | Graph of nonhexagonal cells in honeybee nests. |
| `math_m1_q06` | 34 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q12` | 36 | Circle diagram with diameters and labeled arcs. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 36 | Frequency table of data values; also a numerical-response item. |
| `math_m1_q17` | 37 | Answer choices are tables of x and y values. |
| `math_m1_q20` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q26` | 39 | Table of poll results. |
| `math_m1_q27` | 39 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q03` | 42 | Table of residents by age and location. |
| `math_m2_q06` | 43 | Diagram of parallel lines and a transversal; also a numerical-response item. |
| `math_m2_q07` | 43 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q08` | 43 | Table of x and y values. |
| `math_m2_q11` | 44 | Table of savings-account balances. |
| `math_m2_q13` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q17` | 45 | Dot plots of glue-stick counts for two classes. |
| `math_m2_q20` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q22` | 47 | Answer choices are tables of x and y values. |
| `math_m2_q27` | 48 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized text comparison found **37 of the 93 included questions** with the same stem and answer texts in earlier test folders. These items are retained to preserve the source test. The comparison ignores whitespace, underlining markers, equivalent typography, and answer-choice order; each question retains the order printed in this test. The table lists all detected matches.

| This test | Earlier test question |
|---|---|
| `rw_m1_q03` | [Test 2, `rw_m1_q02`](../test-2/questions.json) |
| `rw_m1_q10` | [Test 3, `rw_m2_q09`](../test-3/questions.json) |
| `rw_m1_q17` | [Test 1, `rw_m1_q18`](../test-1/questions.json) |
| `rw_m1_q18` | [Test 1, `rw_m2_q17`](../test-1/questions.json) |
| `rw_m1_q19` | [Test 3, `rw_m1_q20`](../test-3/questions.json) |
| `rw_m1_q20` | [Test 1, `rw_m1_q26`](../test-1/questions.json) |
| `rw_m1_q22` | [Test 3, `rw_m1_q25`](../test-3/questions.json) |
| `rw_m1_q23` | [Test 1, `rw_m2_q27`](../test-1/questions.json) |
| `rw_m1_q27` | [Test 2, `rw_m2_q27`](../test-2/questions.json) |
| `rw_m1_q29` | [Test 3, `rw_m2_q30`](../test-3/questions.json) |
| `rw_m1_q31` | [Test 2, `rw_m1_q29`](../test-2/questions.json) |
| `rw_m1_q33` | [Test 3, `rw_m1_q30`](../test-3/questions.json) |
| `rw_m2_q03` | [Test 3, `rw_m2_q02`](../test-3/questions.json) |
| `rw_m2_q05` | [Test 1, `rw_m1_q02`](../test-1/questions.json) |
| `rw_m2_q07` | [Test 2, `rw_m1_q08`](../test-2/questions.json) |
| `rw_m2_q08` | [Test 1, `rw_m1_q08`](../test-1/questions.json) |
| `rw_m2_q11` | [Test 3, `rw_m1_q11`](../test-3/questions.json) |
| `rw_m2_q16` | [Test 3, `rw_m1_q16`](../test-3/questions.json) |
| `rw_m2_q17` | [Test 2, `rw_m1_q17`](../test-2/questions.json) |
| `rw_m2_q19` | [Test 1, `rw_m1_q21`](../test-1/questions.json) |
| `rw_m2_q22` | [Test 2, `rw_m1_q28`](../test-2/questions.json) |
| `rw_m2_q24` | [Test 3, `rw_m2_q27`](../test-3/questions.json) |
| `rw_m2_q27` | [Test 1, `rw_m2_q30`](../test-1/questions.json) |
| `rw_m2_q29` | [Test 1, `rw_m2_q31`](../test-1/questions.json) |
| `rw_m2_q33` | [Test 2, `rw_m2_q33`](../test-2/questions.json) |
| `math_m1_q04` | [Test 1, `math_m1_q04`](../test-1/questions.json) |
| `math_m1_q05` | [Test 3, `math_m2_q08`](../test-3/questions.json) |
| `math_m1_q08` | [Test 2, `math_m2_q02`](../test-2/questions.json) |
| `math_m1_q09` | [Test 3, `math_m1_q05`](../test-3/questions.json) |
| `math_m1_q23` | [Test 3, `math_m1_q23`](../test-3/questions.json) |
| `math_m2_q04` | [Test 1, `math_m2_q03`](../test-1/questions.json) |
| `math_m2_q09` | [Test 1, `math_m2_q10`](../test-1/questions.json) |
| `math_m2_q15` | [Test 3, `math_m1_q17`](../test-3/questions.json) |
| `math_m2_q16` | [Test 1, `math_m2_q18`](../test-1/questions.json) |
| `math_m2_q19` | [Test 2, `math_m2_q18`](../test-2/questions.json) |
| `math_m2_q23` | [Test 1, `math_m1_q23`](../test-1/questions.json) |
| `math_m2_q25` | [Test 3, `math_m1_q25`](../test-3/questions.json) |

This is a text-overlap check, not evidence of independent tested skills or absence from model training data. Future results pooled across all tests should distinguish repeated items from distinct questions. IDs preserve the source section, module, and question number and are local to each test folder; identify an item by its test number and question ID together.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `06d37cdb9d77064cbaca768f4170030104b164ed418c26b4f4daeb939109b347` |
| `state.json` | `ef0f0f82b4726b989fc7ab285e7334f5a97e3c0a40e614a596ed9056f8010532` |
| `answer_key.json` | `5cb12d05480f2ad2f74b7bfa1c105a902f37d3f0c7134b7a8531d4dde8bb311a` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-9-digital.pdf` | `ff929c946ebfa8d8d7f199e52e1eb12d7cf7d68256b894846725df0da87a6d69` |
| `scoring-sat-practice-test-9-digital.pdf` | `928485b854d73384d7570ec4383a2581b2ad0c24fa78164049cb7931846c74fa` |
| `sat-practice-test-9-answers-digital.pdf` | `5c06af4bd2379763fbaabdae16f9cd03e14cabc7ee041131ba6b2837f5bf4696` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
