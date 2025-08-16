import json
from datetime import datetime
from input_text.commentary_sanitize_text import sanitize_text
from supabase import create_client
import uuid
import os

SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_commentary(comment):

    # Save to Supabase
    new_id = str(uuid.uuid4())
    response = supabase.table("Finley Testing").insert({
    response = supabase.table("Finley_Testing").insert({
    "id": new_id,
    "user_id": "ryan-young",
    "timestamp": datetime.utcnow().isoformat(),
    "raw_json": comment_json
}).execute()
