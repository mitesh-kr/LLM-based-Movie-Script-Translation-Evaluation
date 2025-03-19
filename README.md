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
    ├── translation_scores.csv
    ├── translation_scores.md
    ├── win_rates.csv
    ├── win_rates.md
    ├── score_comparison.png
    ├── win_rates.png
    └── comparison_table.html
```


## Setup and Execution

1. Install dependencies:
   ```
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

The performance comparison visualizations can be found in the `results/` directory after running the main script.

## Notes
- ChatGPT translations are used as ground truth for evaluation
- The script processes at least the first 100 sentences of the movie script as required

