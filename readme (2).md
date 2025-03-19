# Tollywood Script Translation Evaluation

This project evaluates the performance of different Large Language Models (LLMs) in translating/dubbing a Tollywood script from English to multiple target languages for international markets.

## Project Structure

```
.
├── data/                   # Directory for script data
│   ├── english_script.txt  # Original English script
│   ├── chatgpt_german.txt  # ChatGPT German translation (ground truth)
│   ├── chatgpt_polish.txt  # ChatGPT Polish translation (ground truth)
│   └── ...                 # Other translation files
├── results/                # Directory for evaluation results
│   ├── performance_comparison.png  # Performance visualization
│   └── win_rate_comparison.png     # Win rate visualization
├── main.py                 # Main execution script
├── translator.py           # Translation functions
├── evaluator.py            # Evaluation metrics
├── visualizer.py           # Visualization functions
├── utils.py                # Utility functions
├── requirements.txt        # Package dependencies
└── README.md               # Project documentation
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
