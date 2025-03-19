# Tollywood Movie Script Translation Evaluation

This project evaluates different Large Language Models (LLMs) for translating Tollywood movie scripts into international languages. Specifically, it evaluates how well different LLMs perform at translating a sample script (based on "RRR") into German and Polish.

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

## Rationale

### LLM Selection

- **LLama 3.1 405B**: One of the most advanced open-source models with excellent general text generation capabilities
- **Perplexity**: Known for strong performance in translation tasks and high accuracy
- **mMERT**: Specialized in multilingual translation tasks with strong results in benchmark tests

### Language Choice

- **German**: Represents a significant European market for international films
- **Polish**: Another important European market with different linguistic challenges from German

### Evaluation Metrics

- **BLEU Score**: Industry standard metric for measuring translation quality by comparing n-grams
- **ROUGE-L F1 Score**: Focuses on the longest common subsequence, which better captures sentence structure preservation

## Installation

```bash
# Clone the repository
git clone https://github.com/mitesh-kr/tollywood-translation-evaluation.git
cd tollywood-translation-evaluation

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. First, generate a sample script (if you don't have a real one):

```bash
python create_sample_script.py --sentences 100 --output script.txt
```

2. Run the evaluation:

```bash
python main.py --input script.txt --languages German Polish --llms LLama_3.1_405B perplexity mMERT --num_sentences 100 --output_dir results
```

## Results

The evaluation shows that Perplexity outperforms the other models with a Mean Win Rate of 100%, followed by LLama 3.1 405B and mMERT. Detailed results can be found in the `results` directory.

## Citation

If you use this code or methodology in your work, please cite:

```
@misc{tollywood-translation-evaluation,
  author = {Your Name},
  title = {Evaluation of LLMs for Tollywood Movie Script Translation},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/yourusername/tollywood-translation-evaluation}
}
```

## License

MIT License
