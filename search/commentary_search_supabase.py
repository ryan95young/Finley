from supabase import create_client
import os

SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def search_commentary(search_text):

    # Step 1: get all commentary from Supabase
    response = supabase.table("Finley_Testing").select("*").execute()
    if not response.data:
        return "No commentary stored yet."

    # Step 2: lowercase for simple keyword matching
    question_words = set(comment.lower().split())
    matches = []

    for row in response.data:
        text = row["raw_json"]["text"]
        text_words = set(text.lower().split())
        # simple overlap scoring
        overlap = len(question_words & text_words)
        if overlap > 0:
            matches.append((overlap, text))
    
    if not matches:
        return "No matching commentary found."

    # Step 3: sort matches by highest overlap
    matches.sort(reverse=True, key=lambda x: x[0])
    # return top 5 matches
    return "\n\n".join([m[1] for m in matches[:5]])

