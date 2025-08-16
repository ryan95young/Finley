import json
from datetime import datetime
from input_text.commentary_sanitize_text import sanitize_text
from supabase import create_client
import uuid
import os
from openai import OpenAI

# Supabase client
SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#OpenAI client
OpenAI_client = OpenAI(api_key=os.getenv("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"))

def save_commentary(comment):

    embedding_response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=comment
    )

    embedding = embedding_response.data[0].embedding

    # Save to Supabase
    new_id = str(uuid.uuid4())
    utc_timestamp = datetime.utcnow().isoformat() + "Z"
    comment_json = {"text": comment}
    response = supabase.table("Finley_Testing").insert({
        "id": new_id,
        "user_id": "ryan-young",
        "timestamp": utc_timestamp,
        "raw_json": comment_json, 
        "embedding": embedding
}).execute()
