import matplotlib.pyplot as plt
import numpy as np
import os

def visualize_results(results, win_rates):
    """
    Visualize evaluation results
    
    Args:
        results (dict): Dictionary containing evaluation results
        win_rates (dict): Dictionary containing win rate results
    """
    # Create directory for results if it doesn't exist
    os.makedirs("results", exist_ok=True)
    
    # Create figure for performance comparison
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    # Models and metrics
    models = list(results["German"].keys())
    metrics = ["BLEU", "ROUGE"]
    
    # Set width of bars
    bar_width = 0.35
    
    # Set position of bars on x-axis
    r1 = np.arange(len(models))
    r2 = [x + bar_width for x in r1]
    
    # Create bars for German
    for i, metric in enumerate(metrics):
        position = r1 if i == 0 else r2
        values = [results["German"][model][metric] for model in models]
        axes[0].bar(position, values, width=bar_width, 
                    label=f'{metric} Score', color=f'C{i}')
    
    # Add labels and title for German
    axes[0].set_xlabel('Models')
    axes[0].set_ylabel('Score')
    axes[0].set_title('German Translation Performance')
    axes[0].set_xticks([r + bar_width/2 for r in range(len(models))])
    axes[0].set_xticklabels(models)
    axes[0].legend()
    
    # Create bars for Polish
    for i, metric in enumerate(metrics):
        position = r1 if i == 0 else r2
        values = [results["Polish"][model][metric] for model in models]
        axes[1].bar(position, values, width=bar_width, 
                    label=f'{metric} Score', color=f'C{i}')
    
    # Add labels and title for Polish
    axes[1].set_xlabel('Models')
    axes[1].set_ylabel('Score')
    axes[1].set_title('Polish Translation Performance')
    axes[1].set_xticks([r + bar_width/2 for r in range(len(models))])
    axes[1].set_xticklabels(models)
    axes[1].legend()
    
    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig("results/performance_comparison.png")
    plt.close()
    
    # Create figure for win rate comparison
    plt.figure(figsize=(10, 6))
    
    # Win rate data
    models = list(win_rates.keys())
    win_rates_values = [win_rates[model]["mean_win_rate"] for model in models]
    
    # Create bars
    plt.bar(models, win_rates_values, color=['skyblue', 'lightgreen', 'salmon'])
    
    # Add labels and title
    plt.xlabel('Models')
    plt.ylabel('Mean Win Rate (%)')
    plt.title('Model Performance: Mean Win Rate Comparison')
    
    # Add values on top of bars
    for i, v in enumerate(win_rates_values):
        plt.text(i, v + 2, f"{v:.1f}%", ha='center')
    
    # Save figure
    plt.tight_layout()
    plt.savefig("results/win_rate_comparison.png")
    plt.close()
