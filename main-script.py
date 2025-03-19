import os
from translator import translate_with_llama, translate_with_perplexity, translate_with_mbert
from evaluator import calculate_bleu_score, calculate_rouge_score
from visualizer import visualize_results
from utils import read_text_file, count_sentences, preprocess_text

def main():
    # Create necessary directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    
    # Read the English script
    english_script = read_text_file("data/english_script.txt")
    if not english_script:
        # Sample script if file doesn't exist
        english_script = """THE STORY

Swinging off branches, playing in valleys.....
Should I be pampered in mother's lap every day.....
"""
        with open("data/english_script.txt", "w") as f:
            f.write(english_script)
    
    # Ensure we're working with at least 100 sentences as required
    sentence_count = count_sentences(english_script)
    print(f"English script contains {sentence_count} sentences.")
    if sentence_count < 100:
        print("WARNING: Script contains fewer than 100 sentences. Consider using a longer script.")
    
    # Target languages
    target_languages = ["German", "Polish"]
    
    # Translate with different models
    print("Translating with ChatGPT (ground truth)...")
    # Note: In a real setup, you'd interface with the ChatGPT API
    # For this assignment, we'll use provided sample translations
    chatgpt_german = read_text_file("data/chatgpt_german.txt")
    chatgpt_polish = read_text_file("data/chatgpt_polish.txt")
    
    # If the ground truth files don't exist, create samples
    if not chatgpt_german:
        chatgpt_german = """DIE GESCHICHTE

Schwingend von Ästen, spielend in Tälern
Sollte ich jeden Tag auf dem Schoß meiner Mutter verwöhnt werden......"""
        with open("data/chatgpt_german.txt", "w") as f:
            f.write(chatgpt_german)
    
    if not chatgpt_polish:
        chatgpt_polish = """HISTORIA

Huśtając się z gałęzi, bawiąc się w dolinach
Powinienem być codziennie tulony na kolanach matki........"""
        with open("data/chatgpt_polish.txt", "w") as f:
            f.write(chatgpt_polish)
    
    # Translate with LLama 3.1
    print("Translating with LLama 3.1 405B...")
    llama_german = translate_with_llama(english_script, "German")
    llama_polish = translate_with_llama(english_script, "Polish")
    
    # Translate with Perplexity
    print("Translating with Perplexity...")
    perplexity_german = translate_with_perplexity(english_script, "German")
    perplexity_polish = translate_with_perplexity(english_script, "Polish")
    
    # Translate with mBERT
    print("Translating with mBERT...")
    mbert_german = translate_with_mbert(english_script, "en_XX", "de_DE")
    mbert_polish = translate_with_mbert(english_script, "en_XX", "pl_PL")
    
    # Save translations
    with open("data/llama_german.txt", "w") as f:
        f.write(llama_german)
    with open("data/llama_polish.txt", "w") as f:
        f.write(llama_polish)
    with open("data/perplexity_german.txt", "w") as f:
        f.write(perplexity_german)
    with open("data/perplexity_polish.txt", "w") as f:
        f.write(perplexity_polish)
    with open("data/mbert_german.txt", "w") as f:
        f.write(mbert_german)
    with open("data/mbert_polish.txt", "w") as f:
        f.write(mbert_polish)
    
    # Evaluate translations
    print("Evaluating translations...")
    results = {
        "German": {
            "LLama 3.1 405B": {
                "BLEU": calculate_bleu_score(chatgpt_german, llama_german, language="german"),
                "ROUGE": calculate_rouge_score(chatgpt_german, llama_german)["rougeL"].fmeasure
            },
            "Perplexity": {
                "BLEU": calculate_bleu_score(chatgpt_german, perplexity_german, language="german"),
                "ROUGE": calculate_rouge_score(chatgpt_german, perplexity_german)["rougeL"].fmeasure
            },
            "mBERT": {
                "BLEU": calculate_bleu_score(chatgpt_german, mbert_german, language="german"),
                "ROUGE": calculate_rouge_score(chatgpt_german, mbert_german)["rougeL"].fmeasure
            }
        },
        "Polish": {
            "LLama 3.1 405B": {
                "BLEU": calculate_bleu_score(chatgpt_polish, llama_polish, language="polish"),
                "ROUGE": calculate_rouge_score(chatgpt_polish, llama_polish)["rougeL"].fmeasure
            },
            "Perplexity": {
                "BLEU": calculate_bleu_score(chatgpt_polish, perplexity_polish, language="polish"),
                "ROUGE": calculate_rouge_score(chatgpt_polish, perplexity_polish)["rougeL"].fmeasure
            },
            "mBERT": {
                "BLEU": calculate_bleu_score(chatgpt_polish, mbert_polish, language="polish"),
                "ROUGE": calculate_rouge_score(chatgpt_polish, mbert_polish)["rougeL"].fmeasure
            }
        }
    }
    
    # Calculate Mean Win Rate
    win_rates = calculate_mean_win_rate(results)
    
    # Display results
    print("\nEvaluation Results:")
    for language in results:
        print(f"\n{language} Translation Results:")
        print(f"{'Model':<15} {'BLEU Score':<15} {'ROUGE Score':<15}")
        print("-" * 45)
        for model, scores in results[language].items():
            print(f"{model:<15} {scores['BLEU']:<15.4f} {scores['ROUGE']:<15.4f}")
    
    print("\nMean Win Rate Results:")
    print(f"{'Model':<15} {'BLEU Wins':<15} {'ROUGE Wins':<15} {'Total Wins':<15} {'Comparisons':<15} {'Mean Win Rate (%)':<20}")
    print("-" * 90)
    for model, rates in win_rates.items():
        print(f"{model:<15} {rates['BLEU_wins']:<15} {rates['ROUGE_wins']:<15} {rates['total_wins']:<15} {rates['total_comparisons']:<15} {rates['mean_win_rate']:<20.2f}")
    
    # Visualize results
    visualize_results(results, win_rates)
    
    print("\nResults visualization saved to 'results/performance_comparison.png'")
    print("Win rate visualization saved to 'results/win_rate_comparison.png'")

def calculate_mean_win_rate(results):
    models = ["LLama 3.1 405B", "Perplexity", "mBERT"]
    win_rates = {model: {"BLEU_wins": 0, "ROUGE_wins": 0, "total_wins": 0, "total_comparisons": 0, "mean_win_rate": 0.0} for model in models}
    
    for language in results:
        # Find best BLEU score
        best_bleu = max(results[language].items(), key=lambda x: x[1]["BLEU"])
        win_rates[best_bleu[0]]["BLEU_wins"] += 1
        
        # Find best ROUGE score
        best_rouge = max(results[language].items(), key=lambda x: x[1]["ROUGE"])
        win_rates[best_rouge[0]]["ROUGE_wins"] += 1
        
        # Update total comparisons
        for model in models:
            win_rates[model]["total_comparisons"] += 2  # 2 metrics per language
    
    # Calculate total wins and mean win rate
    for model in models:
        win_rates[model]["total_wins"] = win_rates[model]["BLEU_wins"] + win_rates[model]["ROUGE_wins"]
        win_rates[model]["mean_win_rate"] = (win_rates[model]["total_wins"] / win_rates[model]["total_comparisons"]) * 100
    
    return win_rates

if __name__ == "__main__":
    main()
