# Tollywood Movie Script Translation Evaluation

This project evaluates different Large Language Models (LLMs) for translating Tollywood movie scripts into international languages. Specifically, it evaluates how well different LLMs perform at translating a sample script (based on "RRR") into German and Polish.

## [Google Colab Link](https://colab.research.google.com/drive/1fqY9RkePMC-dzhF36WsGHxDcerYmRqV6?usp=sharing)

## Overview

Dubbing and subtitling are crucial for expanding the reach of Tollywood films to international audiences. This project aims to identify which LLM provides the best translation quality for this purpose.

## Features

- Evaluates translations from three different LLMs:
  - LLama 3.1 405B
  - Perplexity
  - mMERT
- Targets two languages for evaluation:
  - German
  - Polish
- Uses appropriate metrics for evaluation:
  - BLEU score (4-gram)
  - ROUGE-L F1 score
- Ground Truth
  - ChatGPT-4
- Calculates Mean Win Rate to rank the models

## Project Structure

```
.
├── README.md
├── main.py                   # Main script for running the evaluation
├── translation_utils.py      # Utilities for handling translations
├── visualization.py          # Functions for visualizing results
├── create_sample_script.py   # Helper to create sample script data
├── requirements.txt
├── script.txt                # Sample script for testing
└── results/
    ├── score_comparison.png
```


## Setup and Execution

1. Install dependencies:
   ```
   git clone https://github.com/mitesh-kr/LLM-based-Movie-Script-Translation-Evaluation.git
   cd LLM-based-Movie-Script-Translation-Evaluation
   pip install -r requirements.txt
   ```

2. Place your English script in `data/english_script.txt` or use the default sample.

3. Run the main script:
   ```
   python main.py
   ```

## Task Details

### a) Selected LLMs
- LLama 3.1 405B
- Perplexity
- mBERT (Facebook's mBART-large-50-many-to-many-mmt)

### b) Target Languages
- German
- Polish

### c) Evaluation Metrics
- BLEU Score (4-gram)
- ROUGE-L F1 Score

### d) Mean Win Rate Results
The Mean Win Rate metric is calculated by:
1. Counting the number of wins for each model across all metrics and languages
2. Dividing by the total number of comparisons
3. Expressing as a percentage

### e) Rationale for Choices

**LLM Selection:**
- LLama 3.1 405B and Perplexity were chosen as they are widely used, open-source LLMs with strong performance
- mBERT was selected specifically for its multilingual capabilities and prior success in translation tasks

**Language Choice:**
- German and Polish represent significant markets for translated media
- These languages offer different linguistic challenges, providing a good test of model robustness

**Evaluation Metrics:**
- BLEU Score measures similarity between translations using n-grams (groups of 4 words)
- ROUGE-L F1 Score focuses on capturing key information through longest common subsequence matching
- These complementary metrics provide a comprehensive evaluation of translation quality

## Results


| Task | LLM | BLEU Score | ROUGE Score | BLEU Win | ROUGE Win | Total Wins | Total Comparisons | Mean Win Rate (%) |
|------|-----|------------|-------------|----------|-----------|------------|-------------------|-------------------|
| German Translation | LLama 3.1 405B | 0.5268 | 0.7643 | 0 | 0 | 0 | 2 | 0% |
| | Perplexity | 0.5915 | 0.8036 | 1 | 1 | 2 | 2 | 100% |
| | mMERT | 0.3556 | 0.6444 | 0 | 0 | 0 | 2 | 0% |
| Polish Translation | LLama 3.1 405B | 0.4744 | 0.7394 | 0 | 0 | 0 | 2 | 0% |
| | Perplexity | 0.5995 | 0.8083 | 1 | 1 | 2 | 2 | 100% |
| | mMERT | 0.2726 | 0.5755 | 0 | 0 | 0 | 2 | 0% |

The performance comparison visualizations can be found in the `results/` directory after running the main script.
## Interpretation
perplexity has the highest Mean Win Rate of 1 for both translation tasks,
indicating it performed the best across all tasks and metrics. Both LLama
3.1 405B and mMERT have a Mean Win Rate of 0, as they didn't win in any
category.
This metric clearly shows that perplexity outperformed the other two LLMs
followed byLLama 3.1 405B and mMERT in both translation tasks and for
both BLEU and ROUGE scores.

LLM Selection: LLama 3.1 and perplexity are the most used llms for any
type of work and are easily available open source for use . MERT was
chosen because it’s one of the llm speciality used for translation and it
shows strong results in other translation benchmarks.

Language Choice: German and Polish were chosen because both
languages represent significant markets for translated media, particularly
Tollywood films. Evaluating translation performance in these languages
helps ensure that models can handle translation tasks relevant to
real-world demands and cultural preferences in media consumption.

Evaluation Metrics: BLEU and ROUGE were chosen because they are
commonly used to evaluate translation quality. BLEU measures how similar
the translated text is to the reference by checking groups of words
(n-grams), and in this case, we are using groups of 4 words. ROUGE
focuses on recall, which checks if the important parts of the original text are
included in the translation. This helps make sure the translation captures
the key information.
For this dubbing task i have chosen, three LLM LLama 3.1 405B,
perplexity and mMERT. For ground truth translation from ChatGPT is being
used.
An initial 100 sentences are being used for this evaluation task.
For the Blue score 4-gram score has been considered and the rouge L F1
score has been considered.

## Notes
- ChatGPT translations are used as ground truth for evaluation
- The script processes at least the first 100 sentences of the movie script as required

