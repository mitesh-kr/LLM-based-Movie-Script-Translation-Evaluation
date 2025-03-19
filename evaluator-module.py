import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.tokenize import word_tokenize
from rouge_score import rouge_scorer
import re

# Download necessary NLTK data
try:
    nltk.download('punkt')
except:
    print("NLTK download failed. Make sure you have internet connection.")

def preprocess_text(text):
    """
    Preprocess text for evaluation
    
    Args:
        text (str): Text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    # Remove punctuation except apostrophes
    text = re.sub(r"[^\w\s']", '', text)
    
    # Handle apostrophes
    text = re.sub(r"\s'\s|'\s|\s'", ' ', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Convert to lowercase
    return text.lower()

def calculate_bleu_score(reference, candidate, language='english'):
    """
    Calculate BLEU score between reference and candidate texts
    
    Args:
        reference (str): Reference text
        candidate (str): Candidate text
        language (str): Language for tokenization
        
    Returns:
        float: BLEU score
    """
    # Preprocess texts
    reference = preprocess_text(reference)
    candidate = preprocess_text(candidate)
    
    # Tokenize texts
    reference_tokens = word_tokenize(reference, language=language)
    candidate_tokens = word_tokenize(candidate, language=language)
    
    # Apply smoothing function
    smoothing_function = SmoothingFunction().method1
    
    # Calculate BLEU score with equal weights for 1-4 grams
    bleu_score = sentence_bleu(
        [reference_tokens], 
        candidate_tokens,
        weights=(0.25, 0.25, 0.25, 0.25),
        smoothing_function=smoothing_function
    )
    
    return bleu_score

def calculate_rouge_score(reference, candidate):
    """
    Calculate ROUGE scores between reference and candidate texts
    
    Args:
        reference (str): Reference text
        candidate (str): Candidate text
        
    Returns:
        dict: Dictionary containing ROUGE scores
    """
    # Preprocess texts
    reference = preprocess_text(reference)
    candidate = preprocess_text(candidate)
    
    # Initialize ROUGE scorer
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    
    # Calculate scores
    scores = scorer.score(reference, candidate)
    
    return scores
