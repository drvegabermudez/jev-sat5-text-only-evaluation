# Jev SAT text-only evaluations

Official SAT practice tests prepared as TypeSafe Choice questions, with original A–D options and complete text context. Each test’s inputs, grading references, and available results live in its own folder.

| Test | Questions | Status | Files |
|---|---:|---|---|
| SAT Practice Test 5 | 91 | Jev 1.13.0: **81/91 (89.0%)** | [Test overview](test-5/README.md) · [Results](test-5/RESULTS.md) · [Model card](test-5/MODEL_CARD.md) |
| SAT Practice Test 6 | 88 | Jev 1.13.0: **81/88 (92.0%)** | [Test overview](test-6/README.md) · [Results](test-6/RESULTS.md) · [Model card](test-6/MODEL_CARD.md) |
| SAT Practice Test 7 | 92 | Jev 1.13.0: **84/92 (91.3%)** | [Test overview](test-7/README.md) · [Results](test-7/RESULTS.md) · [Model card](test-7/MODEL_CARD.md) |

For each run, send the test’s `questions.json` and `state.json` to Jev. The `answer_key.json` contains the correct answers for grading; `responses.json`, when present, contains the model’s actual output. Keep answer keys out of model inputs.

Each test documents its source and omissions. The selected question sets have no exact duplicates across Tests 5, 6, and 7. Question IDs are local to their test folders.

## Reported timing

| Test | Server time | Network round trip | Calculated combined time |
|---|---:|---:|---:|
| Test 5 | 249 ms | 125 ms | ≈ 374 ms |
| Test 6 | 182 ms | 153 ms | ≈ 335 ms |
| Test 7 | 213 ms | 181 ms | ≈ 394 ms |

Server times come from the response exports; network timings are user-reported. Combined times are their sums, not separate end-to-end measurements. Each test uses a different question set and a single response export.

## Reproduce results

Python 3.9 or newer is sufficient; no external packages or model calls are required.

```bash
python3 test-5/evaluate.py --check
python3 test-6/evaluate.py --check
python3 test-7/evaluate.py --check
```

Each test folder contains its model output, grading key, results, and model evaluation card. The evaluators for Tests 6 and 7 generate both reports directly from their respective input, answer-key, and response files.

SAT content is owned by College Board and the respective passage rights holders. These independent evaluations are not affiliated with or endorsed by College Board or TypeSafe. Scores are raw subset accuracy, not official SAT scaled scores.
