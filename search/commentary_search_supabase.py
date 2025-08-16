from supabase import create_client
import os

SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def search_commentary(search_text):
    """
    Search the 'Finley Testing' table for case-insensitive matches
    in the raw_json field.
    """
    if not search_text.strip():
        return []

    response = (
        supabase.table("Finley Testing")
        .select("*")
        .ilike("raw_json", f"%{search_text}%")
        .execute()
    )

    return response.data if response.data else []
