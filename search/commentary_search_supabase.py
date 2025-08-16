from supabase import create_client
import os

SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def search_commentary(search_text):
    """
    Search the 'Finley_Testing' table for case-insensitive matches
    in the 'text' field inside raw_json, and return as a single string.
    """
    if not search_text.strip():
        return ""

    response = (
        supabase.table("Finley_Testing")
        .select("*")
        .filter("raw_json->>text", "ilike", f"%{search_text}%")
        .execute()
    )

    if not response.data:
        return "No matching commentary found."

    # Convert each JSON row into a single line of text
    lines = []
    for row in response.data:
        json_data = row.get("raw_json", {})
        text = json_data.get("text", "")
        lines.append(text.replace("\n", " "))  # remove newlines inside each commentary

    return "\n".join(lines)  # one line per row

