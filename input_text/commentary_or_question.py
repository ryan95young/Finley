import re

submission_commentary_reply = "Commentary"
submission_question_reply = "Question"

def classify_submission(text: str) -> str:
    """
    Classifies text as either 'question' or 'commentary'.
    Returns the appropriate reply string.
    """
    if not text or not text.strip():
        return submission_commentary_reply
        return submission_commentary_reply_path
        
    text_clean = text.strip().lower()
    
    question_words = [
        "who", "what", "when", "where", "why", "how",
        "is", "are", "was", "were", "do", "does", "did",
        "can", "could", "would", "should", "will", "may", "might"
    ]
    
    # Rule 1: Contains a question mark anywhere → question
    if "?" in text_clean:
        return submission_question_reply
    
    # Rule 2: Starts with question word → question
    if any(text_clean.startswith(qw + " ") for qw in question_words):
        return submission_question_reply
    
    # Rule 3: Ends with question mark → question
    if re.match(r".+\?$", text.strip()):
        return submission_question_reply
    
    # Default → commentary
    return submission_commentary_reply
