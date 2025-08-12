import re
# from commentary_upload import save_commentary

def classify_submission(text: str) -> str:
    """
    Classifies text as either 'question' or 'commentary'.
    
    Rules:
    - If text contains a '?' → likely a question
    - If it starts with question words like who/what/why/how/etc. → question
    - Otherwise → commentary
    """
    
    if not text or not text.strip():
        # save_commentary()
        "Thank you for the commentary"  # default for empty submissions
    
    # Normalize text for checks
    text_clean = text.strip().lower()
    
    # Common question words
    question_words = [
        "who", "what", "when", "where", "why", "how",
        "is", "are", "was", "were", "do", "does", "did",
        "can", "could", "would", "should", "will", "may", "might"
    ]
    
    # Rule 1: If there's a question mark anywhere → question
    if "?" in text_clean:
        return "question"
    
    # Rule 2: If starts with question word → question
    if any(text_clean.startswith(qw + " ") for qw in question_words):
        return "question"
    
    # Rule 3: If ends with a question mark after stripping punctuation → question
    if re.match(r".+\?$", text.strip()):
        return "question"
    
    # Default: commentary
    # save_commentary()
    "Thank you for the commentary"  # default for empty submissions