import re
import os

def count_sentences(text):
    """
    Count the number of sentences in a text
    
    Args:
        text (str): Text to count sentences in
        
    Returns:
        int: Number of sentences
    """
    # Split text by sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty strings and count non-empty sentences
    return len([s for s in sentences if s.strip()])

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

def read_text_file(filepath):
    """
    Read text from a file
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        str: Text content or empty string if file doesn't exist
    """
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return ""
