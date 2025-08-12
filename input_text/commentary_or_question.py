import re
submission_final_reply = []
submission_commentary_reply = "I'll remember that for you."
submission_question_reply = "Thank you for the question. [Reply]"

def classify_submission(text: str) -> str:
    """
    Classifies text as either 'question' or 'commentary'.
    
    Rules:
    - If text contains a '?' → likely a question
    - If it starts with question words like who/what/why/how/etc. → question
    - Otherwise → commentary
    """
    
    if not text or not text.strip():
       submission_final_reply = submission_commentary_reply 
        
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
        submission_final_reply = submission_question_reply
    
    # Rule 2: If starts with question word → question
    if any(text_clean.startswith(qw + " ") for qw in question_words):
        submission_final_reply = submission_question_reply
    
    # Rule 3: If ends with a question mark after stripping punctuation → question
    if re.match(r".+\?$", text.strip()):
        submission_final_reply = submission_question_reply
    
    # Default: commentary
    submission_final_reply = submission_commentary_reply  # default for empty submissions