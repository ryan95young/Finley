import json
from commentary_sanitize_text import sanitize_text
import os

def load_commentary(json_path="finley_memory.json"):
    """Loads commentary entries from JSON."""
    if not os.path.exists(json_path):
        print("❌ File not found:", json_path)
        return []

    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("❌ Error reading JSON file.")
        return []

def edit_commentary(entries):
    """Prompt user to edit each commentary entry."""
    updated_entries = []
    for entry in entries:
        print(f"\n[{entry['id']}] {entry['timestamp']}")
        print(f"Current: {entry['text']}")
        choice = input("Do you want to edit this? (Y/N): ").strip().lower()

        if choice == "y":
            new_text = input("Enter your revised commentary:\n").strip()
            sanitized_text = sanitize_text(new_text)
            entry['text'] = sanitized_text 

        updated_entries.append(entry)
    return updated_entries

def save_commentary(entries, json_path="finley_memory.json"):
    """Saves updated entries back to JSON."""
    with open(json_path, "w") as f:
        json.dump(entries, f, indent=2)
    print(f"\n✅ Commentary updated and saved to {json_path}")

def main():
    json_path = "finley_memory.json"
    print(f"\n📂 Loading commentary from: {json_path}")
    entries = load_commentary(json_path)

    if not entries:
        print("No commentary found.")
        return

    print(f"\n📝 Found {len(entries)} commentary items.")
    updated = edit_commentary(entries)
    save_commentary(updated, json_path)

if __name__ == "__main__":
    main()