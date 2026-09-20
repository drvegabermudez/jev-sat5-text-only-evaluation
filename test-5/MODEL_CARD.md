# Model evaluation card: Jev 1.13.0

**81/91 correct (89.0%)** on a text-only multiple-choice subset of SAT Practice Test #5.

## Evaluation overview

| Field | Value |
|---|---|
| Model | `jev-1.13.0`, as reported in the response export |
| Interface | TypeSafe Choice questions with original A–D options |
| Task | Answer English-language SAT Reading and Writing and Math questions |
| Dataset | `sat5-text-only-91`: 61 Reading and Writing and 30 Math questions |
| Evaluated response exports | 1 |
| Request identifier | `playground_1eb7e826737bce1415582b8cb649e90c78a` |
| Response artifact | [responses.json](responses.json), preserved byte-for-byte |

This independent evaluation card describes the supplied output. Model architecture, parameter count, training data, and training cutoff are not established by the available evidence.

## Data and method

The source is College Board’s [SAT Practice Test #5](https://satsuite.collegeboard.org/media/pdf/sat-practice-test-5-digital.pdf), © 2024, nonadaptive paper form, cover identifiers `WX4P0001` and `6VSL01`. Its 120 questions comprise 66 Reading and Writing and 54 Math questions.

The evaluation includes 91 original multiple-choice questions whose context and A–D options are represented in text. It excludes 17 questions requiring graphs, diagrams, or tables and 12 other numerical-response questions. Two visual exclusions also require numerical responses. The [omission list](OMISSIONS.md) gives each exclusion and reason; the [manifest](question_manifest.json) records source pages.

Inputs are [state.json](state.json) and [questions.json](questions.json). The supplied response export covers all 91 question IDs. Each selected letter is compared with the [official College Board answer key](https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-5-digital.pdf), page 4. Correct answers receive one point; excluded questions do not enter the denominator. Answer keys are grading artifacts.

## Performance

| Group | Correct | Accuracy |
|---|---:|---:|
| Reading and Writing, Module 1 | 29/31 | 93.5% |
| Reading and Writing, Module 2 | 27/30 | 90.0% |
| **Reading and Writing** | **56/61** | **91.8%** |
| Math, Module 1 | 12/15 | 80.0% |
| Math, Module 2 | 13/15 | 86.7% |
| **Math** | **25/30** | **83.3%** |
| **Overall** | **81/91** | **89.0%** |

The ten incorrect answers and explanations are listed in [RESULTS.md](RESULTS.md). [Per-question grading](results/per_question.csv) includes every response, correct answer, confidence, and option probability.

## Reported usage

| Export field | Value |
|---|---:|
| Input tokens | 17,637 |
| Output tokens | 4,280 |
| `evaluation_time_ms` | 249.01150100049563 |

These are service-reported values. The timing field is not an independently measured end-to-end latency; its scope and the serving hardware are unspecified.

## Scope and limitations

- **Selected subset:** Visual and numerical-response items are excluded. The result is not an official SAT scaled score and does not establish performance on the full or adaptive SAT.
- **Single evaluated export:** This evaluation does not measure repeated-run reliability or performance across other test forms and models.
- **Public test:** Training overlap, retrieval, and memorization have not been investigated.
- **Request evidence:** The export does not include the original service request, execution timestamp, or sampling settings. Exact remote inputs cannot be independently verified from the export alone.
- **Text and confidence:** PDF layout is represented as text. Reported confidence and option probabilities have not been established to be calibrated by this evaluation.

The repository supports reproducing this grade and inspecting model responses. It does not establish general model reliability or suitability for decisions about individual students.

## Reproducibility

Run `python3 evaluate.py --check` to validate the dataset and response, recalculate the scores, and verify the committed reports. [provenance.json](provenance.json) records source details and artifact hashes. Regrading requires no credentials, network access, or model calls.
