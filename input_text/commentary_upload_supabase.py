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
    comment_json = {"text": comment}
    response = supabase.table("Finley_Testing").insert({
    "id": new_id,
    "user_id": "ryan-young",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "raw_json": comment_json
}).execute()
