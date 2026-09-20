# Jev SAT text-only evaluations

Official SAT practice tests prepared as TypeSafe Choice questions, with original A–D options and complete text context. Each test’s inputs, grading references, and available results live in its own folder.

| Test | Questions | Status | Files |
|---|---:|---|---|
| SAT Practice Test 5 | 91 | Jev 1.13.0: **81/91 (89.0%)** | [Test overview](test-5/README.md) · [Results](test-5/RESULTS.md) · [Model card](test-5/MODEL_CARD.md) |
| SAT Practice Test 6 | 88 | **Ready to send to Jev** | [Questions](test-6/questions.json) · [State](test-6/state.json) · [Test overview](test-6/README.md) |

For each run, send the test’s `questions.json` and `state.json` to Jev. The `answer_key.json` contains the correct answers for grading; `responses.json`, when present, contains the model’s actual output. Keep answer keys out of model inputs.

Each test documents its source and omissions. Test 6’s selected questions have no exact duplicates in the evaluated Test 5 set. Question IDs are local to their test folders.

## Reproduce Test 5 results

Python 3.9 or newer is sufficient; no external packages or model calls are required.

```bash
python3 test-5/evaluate.py --check
```

Test 6 has no model output or score yet. Its folder contains only questions, state, one grading key, and a README.

SAT content is owned by College Board and the respective passage rights holders. These independent evaluations are not affiliated with or endorsed by College Board or TypeSafe. Scores are raw subset accuracy, not official SAT scaled scores.
