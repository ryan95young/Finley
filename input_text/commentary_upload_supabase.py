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
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print(os.getenv("OPEN_API_KEY"))

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
