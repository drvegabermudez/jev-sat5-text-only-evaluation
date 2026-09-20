# Jev SAT text-only evaluations

Official SAT practice tests prepared as TypeSafe Choice questions, with original A–D options and complete text context. Each test’s inputs, grading references, and available results live in its own folder.

| Test | Questions | Status | Files |
|---|---:|---|---|
| SAT Practice Test 1 | 97 | Jev 1.13.0: **89/97 (91.8%)** | [Test overview](test-1/README.md) · [Results](test-1/RESULTS.md) · [Model card](test-1/MODEL_CARD.md) |
| SAT Practice Test 2 | 93 | Jev 1.13.0: **85/93 (91.4%)** | [Test overview](test-2/README.md) · [Results](test-2/RESULTS.md) · [Model card](test-2/MODEL_CARD.md) |
| SAT Practice Test 3 | 94 | Jev 1.13.0: **84/94 (89.4%)** | [Test overview](test-3/README.md) · [Results](test-3/RESULTS.md) · [Model card](test-3/MODEL_CARD.md) |
| SAT Practice Test 4 | 92 | Jev 1.13.0: **87/92 (94.6%)** | [Test overview](test-4/README.md) · [Results](test-4/RESULTS.md) · [Model card](test-4/MODEL_CARD.md) |
| SAT Practice Test 5 | 91 | Jev 1.13.0: **81/91 (89.0%)** | [Test overview](test-5/README.md) · [Results](test-5/RESULTS.md) · [Model card](test-5/MODEL_CARD.md) |
| SAT Practice Test 6 | 88 | Jev 1.13.0: **81/88 (92.0%)** | [Test overview](test-6/README.md) · [Results](test-6/RESULTS.md) · [Model card](test-6/MODEL_CARD.md) |
| SAT Practice Test 7 | 92 | Jev 1.13.0: **84/92 (91.3%)** | [Test overview](test-7/README.md) · [Results](test-7/RESULTS.md) · [Model card](test-7/MODEL_CARD.md) |
| SAT Practice Test 8 | 91 | Ready to run | [Test overview](test-8/README.md) · [Questions](test-8/questions.json) · [State](test-8/state.json) |
| SAT Practice Test 9 | 93 | Ready to run | [Test overview](test-9/README.md) · [Questions](test-9/questions.json) · [State](test-9/state.json) |
| SAT Practice Test 10 | 91 | Ready to run | [Test overview](test-10/README.md) · [Questions](test-10/questions.json) · [State](test-10/state.json) |
| SAT Practice Test 11 | 87 | Ready to run | [Test overview](test-11/README.md) · [Questions](test-11/questions.json) · [State](test-11/state.json) |

Across Tests 1–7, Jev 1.13.0 answered **591/647 (91.3%)** correctly: **397/431 (92.1%)** in Reading and Writing and **194/216 (89.8%)** in Math. This pools one response export per test and weights each included question equally; it is raw subset accuracy, not an official SAT scaled score.

For each run, send the test’s `questions.json` and `state.json` to Jev. The `answer_key.json` contains the correct answers for grading; `responses.json`, when present, contains the model’s actual output. Keep answer keys out of model inputs.

Tests 8–11 add **362 questions ready for evaluation**; their responses and results are pending. Each test documents its source and omissions. The selected sets for Tests 1–7 have no exact duplicates after normalizing whitespace, underlining markers, and equivalent notation. The new sets contain repeated questions: the same comparison of stems and answer texts, allowing reordered options, finds **51 in Test 8, 37 in Test 9, and 45 in Test 10** matching earlier folders, and **none in Test 11**. Matches are listed in each new test overview. Repeated items remain in their original tests; future pooled results should account for this overlap. Similar templates and partial text overlap may remain. Question IDs are local to their test folders.

## Reported timing

| Test | Server time | Network round trip | Calculated combined time |
|---|---:|---:|---:|
| Test 1 | 216 ms | 67 ms | ≈ 283 ms |
| Test 2 | 253 ms | 120 ms | ≈ 373 ms |
| Test 3 | 183 ms | 57 ms | ≈ 240 ms |
| Test 4 | 198 ms | 107 ms | ≈ 305 ms |
| Test 5 | 249 ms | 125 ms | ≈ 374 ms |
| Test 6 | 182 ms | 153 ms | ≈ 335 ms |
| Test 7 | 213 ms | 181 ms | ≈ 394 ms |

Server times come from the response exports; network timings are user-reported. Combined times are their sums, not separate end-to-end measurements. Each test uses a different question set and a single response export.

## Reproduce results

Python 3.9 or newer is sufficient; no external packages or model calls are required.

```bash
python3 test-1/evaluate.py --check
python3 test-2/evaluate.py --check
python3 test-3/evaluate.py --check
python3 test-4/evaluate.py --check
python3 test-5/evaluate.py --check
python3 test-6/evaluate.py --check
python3 test-7/evaluate.py --check
```

Completed test folders contain the model output, grading key, results, and model evaluation card. The evaluators for Tests 1–4, 6, and 7 generate both reports directly from their respective input, answer-key, and response files.

SAT content is owned by College Board and the respective passage rights holders. These independent evaluations are not affiliated with or endorsed by College Board or TypeSafe. Scores are raw subset accuracy, not official SAT scaled scores.
