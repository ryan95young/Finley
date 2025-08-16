from supabase import create_client
import os

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
