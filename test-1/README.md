# SAT Practice Test 1: Jev evaluation

**Jev 1.13.0 scored 89/97 (91.8%)** on the selected questions: **58/62 Reading and Writing** and **31/35 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 97 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, and file identification |

Keep the answer key out of model inputs. Reported server time is **216 ms** and the user-reported network round trip is **67 ms**, for a calculated combined time of **approximately 283 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-1/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #1**, the 56-page nonadaptive paper form for the digital SAT. College Board’s test and scoring guide are preserved on APCORE’s public mirror; the answer explanations are preserved on Binju’s Education’s public mirror.

- [Test PDF](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/sat-practice-test-1-digital.pdf)
- [Scoring guide](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-1-digital.pdf), answer key on page 4
- [Answer explanations](https://www.binjuseducation.com/wp-content/uploads/2025/09/sat-practice-test-1-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 2 | 31 |
| Reading and Writing 2 | 33 | 2 | 31 |
| Math 1 | 27 | 11 | 16 |
| Math 2 | 27 | 8 | 19 |
| **Total** | **120** | **23** | **97** |

There are 12 visual exclusions and 11 additional numerical-response exclusions. 3 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q14` | 9 | Table of credited film output. |
| `rw_m1_q15` | 10 | Table of juvenile plants growing on bare ground and in vegetation patches. |
| `rw_m2_q13` | 23 | Table of speech and information rates for five languages. |
| `rw_m2_q15` | 24 | Table of employment by sector in France and the United States. |
| `math_m1_q06` | 34 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q11` | 35 | Scatterplot used to select a linear model. |
| `math_m1_q12` | 36 | Graph of a cubic function. |
| `math_m1_q13` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 36 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q18` | 37 | Graph of shares of stock that can be purchased. |
| `math_m1_q20` | 38 | Frequency table of data values; also a numerical-response item. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q24` | 39 | Table of x and y values for a line. |
| `math_m1_q27` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q05` | 45 | Labeled right-triangle diagram. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Graph used to identify an x-intercept; also a numerical-response item. |
| `math_m2_q13` | 47 | Diagram of parallel lines and a transversal; also a numerical-response item. |
| `math_m2_q14` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q20` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q27` | 50 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized question stems were compared across the selected sets for Tests 1–7; no exact duplicates were found. Similar math templates remain, with different equations, values, or requested quantities. No items were excluded for duplication. This checks text overlap, not independence of tested skills or absence from model training data.

IDs preserve the source section, module, and question number. They are local to each test folder: `rw_m1_q01` identifies a different question in each test.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `98daf68aa46a90b1b9043de13a7a2a41d2616bf26b49f182d28fcff429245269` |
| `state.json` | `7576f7d93db15deb11e64d7c9bc756d3028a85fc15911e60093af4fbd5ac930d` |
| `answer_key.json` | `1321242e34cec467b2c05960e35524bfdfce17acc08ee8b0dce5798d7096a663` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-1-digital.pdf` | `697295ed8349c4c188a366c0c614073e3e384294119a5a83c6c3a19686cd97ed` |
| `scoring-sat-practice-test-1-digital.pdf` | `43f1386763e4fedb35e0231f59e4b5b4cc873ad508b1d242f98d2bea79ec4893` |
| `sat-practice-test-1-answers-digital.pdf` | `a4fa09584678472531d1d7c45dd842d034724b71e7e86bc37fe1735a4d922594` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
