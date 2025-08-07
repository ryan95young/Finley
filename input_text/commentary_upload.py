import json
from datetime import datetime
from commentary_sanitize_text import sanitize_text
from commentary_detect_conflicts_and_duplicates import detect_conflicts_and_duplicates
import os

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

    print("✅ Commentary with tags saved.")

if __name__ == "__main__":
    save_commentary()