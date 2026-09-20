# SAT Practice Test 3: Jev evaluation

**Jev 1.13.0 scored 84/94 (89.4%)** on the selected questions: **54/62 Reading and Writing** and **30/32 Math**. See the [results](RESULTS.md) and [model evaluation card](MODEL_CARD.md).

## Send to Jev

Use [questions.json](questions.json) as the TypeSafe Choice question map and [state.json](state.json) as the shared state. Send only those two files to the model, using this test’s matching pair.

| File | Purpose |
|---|---|
| [questions.json](questions.json) | Model input: 94 Choice questions with original A–D options |
| [state.json](state.json) | Model input: shared instructions and notation conventions |
| [answer_key.json](answer_key.json) | Grading reference: official answer letter, answer text, and source PDF page |
| [responses.json](responses.json) | Original Jev response export, preserved byte-for-byte |
| [RESULTS.md](RESULTS.md) | Scores, incorrect answers, explanations, and timing |
| [MODEL_CARD.md](MODEL_CARD.md) | Evaluation method, scope, and limitations |
| [evaluate.py](evaluate.py) | Reproduce the grade and validate both reports |
| README.md | Sources, selection, omissions, and file identification |

Keep the answer key out of model inputs. Reported server time is **183 ms** and the user-reported network round trip is **57 ms**, for a calculated combined time of **approximately 240 ms**. This sum is not a separate end-to-end measurement.

Run `python3 test-3/evaluate.py --check` from the repository root to reproduce the results.

## Source and selection

The source is College Board’s **The SAT Practice Test #3**, the 56-page nonadaptive paper form for the digital SAT. College Board’s test and scoring guide are preserved on APCORE’s public mirror; the answer explanations are preserved on Binju’s Education’s public mirror.

- [Test PDF](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/sat-practice-test-3-digital.pdf)
- [Scoring guide](https://www.aptutorgroup.com/uploads/1/1/1/8/111840249/scoring-sat-practice-test-3-digital.pdf), answer key on page 4
- [Answer explanations](https://www.binjuseducation.com/wp-content/uploads/2025/09/sat-practice-test-3-answers-digital.pdf)

Included items preserve the original wording and A–D choices. Line wrapping is normalized; poem line breaks, underlining, and mathematical notation are preserved in text. All question pages were reviewed visually. Every included answer agrees between the scoring guide and the separate answer-explanation document.

Only original multiple-choice items with complete text context are included. Questions with graphs, diagrams, or tables are excluded, including visual answer choices. Numerical-response questions are excluded without inventing options. A question may mention a point, figure, or graph and still be included when the original text supplies all its context and no accompanying visual is needed.

| Module | Original | Omitted | Included |
|---|---:|---:|---:|
| Reading and Writing 1 | 33 | 1 | 32 |
| Reading and Writing 2 | 33 | 3 | 30 |
| Math 1 | 27 | 12 | 15 |
| Math 2 | 27 | 10 | 17 |
| **Total** | **120** | **26** | **94** |

There are 13 visual exclusions and 13 additional numerical-response exclusions. 1 of the visual exclusions also require numerical responses; all 14 original numerical-response questions are excluded.

## Omitted questions

PDF pages are one-based; printed page numbers are two less than the PDF page number.

| Question | PDF page | Reason |
|---|---:|---|
| `rw_m1_q14` | 9 | Graph of female farmers by region and crop type. |
| `rw_m2_q13` | 23 | Table of estimated tyrannosaurid bite forces. |
| `rw_m2_q14` | 24 | Table of clamshell tools found at different cave depths. |
| `rw_m2_q15` | 25 | Table of torpor bouts and arousal episodes. |
| `math_m1_q04` | 34 | Diagram of parallel lines and a transversal. |
| `math_m1_q06` | 35 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q07` | 35 | Bar graph of food-drive can counts; also a numerical-response item. |
| `math_m1_q08` | 35 | Table of mascot votes by grade level. |
| `math_m1_q09` | 36 | Graph of an electrician’s total charge. |
| `math_m1_q13` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q14` | 37 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q20` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q21` | 38 | Original question requires a numerical response and has no A–D choices. |
| `math_m1_q24` | 39 | Graph of a rational function. |
| `math_m1_q26` | 40 | Table of poll results. |
| `math_m1_q27` | 40 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q02` | 44 | Graph used to identify a y-intercept. |
| `math_m2_q06` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q07` | 45 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q11` | 46 | Scatterplot with a line of best fit. |
| `math_m2_q13` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q14` | 46 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q20` | 47 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q21` | 48 | Original question requires a numerical response and has no A–D choices. |
| `math_m2_q24` | 48 | Dot plots of two data sets. |
| `math_m2_q27` | 49 | Original question requires a numerical response and has no A–D choices. |

## Overlap and question IDs

Normalized question stems were compared across the selected sets for Tests 1–7; no exact duplicates were found. Similar math templates remain, with different equations, values, or requested quantities. No items were excluded for duplication. This checks text overlap, not independence of tested skills or absence from model training data.

IDs preserve the source section, module, and question number. They are local to each test folder: `rw_m1_q01` identifies a different question in each test.

## File identification

SHA-256 hashes identify the prepared inputs and grading key.

| File | SHA-256 |
|---|---|
| `questions.json` | `c406ecac593620e51e2603f4b52bc8995fc98ea4bfee0edb29343b42491b02ca` |
| `state.json` | `daed71323f5b6037f50ec96aeb3116e4da763600845fac70c938fa95a1727eb1` |
| `answer_key.json` | `9df538cb37011d82b75f7d23b768cee657d5a2d09407b30ad80d731f050b627f` |

Source PDF hashes identify the exact downloaded documents; the PDFs are linked above rather than duplicated in the repository.

| Source PDF | SHA-256 |
|---|---|
| `sat-practice-test-3-digital.pdf` | `0aa9aa91546efd1c8f8a271df4a2f11d0bce3fbd5cfa4408616b5082e1f5585d` |
| `scoring-sat-practice-test-3-digital.pdf` | `0bc0862d8aa9564a76a038cc8669a62700d078b8a3c8e2a2ab55b8812cf83f51` |
| `sat-practice-test-3-answers-digital.pdf` | `de83608cb54880dcab7906e2ddc9dee7c9ed11e8cb4b3669a0e9083ca6a5083a` |

## Attribution and reporting

SAT content is © College Board; underlying passages belong to their respective rights holders. This independent evaluation is not affiliated with or endorsed by College Board or TypeSafe and does not grant an open-content license to the source material.

Results report raw accuracy on this selected subset, with section and module breakdowns. This subset does not produce an official SAT scaled score.
