import json
from datetime import datetime
import os

def save_commentary(text, json_path="finley_memory.json"):
    # Load existing data if the file exists
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            data = json.load(f)
    else:
        data = []

    new_entry = {
        "id": len(data) + 1,
        "text": text.strip(),
        "timestamp": datetime.now().isoformat()
    }

    data.append(new_entry)

    # Save back to JSON file
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)

    print("Commentary saved.")