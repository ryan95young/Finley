import json
from datetime import datetime
from commentary_sanitize_text import sanitize_text
from commentary_detect_conflicts_and_duplicates import detect_conflicts_and_duplicates
from supabase import create_client
import uuid
import os

SUPABASE_URL = "https://wvhydcduidfgmswawkud.supabase.co"
SUPABASE_KEY = "sb_publishable_xzumVoItFr43myzD6Qle_w_fyI8W6Q6"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_commentary(json_path="finley_memory.json"):
    # Load existing data if the file exists
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
    else:
        data = []

    # Get user input
    text = input("Enter your commentary:\n").strip()

     # Sanitize the commentary text
    text = sanitize_text(text)
    
    # Get tags as comma-separated string, then split into list
    tags_input = input("Enter tags (comma-separated, optional): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

    # Optionally, add other metadata here (e.g., month, category)

    new_entry = {
        "id": len(data) + 1,
        "text": text,
        "tags": tags,
        "timestamp": datetime.now().isoformat()
    }

    # Detect duplicates and conflicts
    proceed = detect_conflicts_and_duplicates(new_entry, data)
    if not proceed:
        return  # abort saving if user says no

    data.append(new_entry)

    # Save back to JSON file
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    # Save to Supabase
    new_id = str(uuid.uuid4())
    response = supabase.table("Finley Testing").insert({
    "id": new_id,
    "user_id": "ryan-young",
    "timestamp": datetime.utcnow().isoformat(),
    "raw_json": text
}).execute()

    print("✅ Commentary with tags saved.")

if __name__ == "__main__":
    save_commentary()