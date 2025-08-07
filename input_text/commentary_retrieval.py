import json
import os

def load_commentary(json_path="finley_memory.json"):
    if not os.path.exists(json_path):
        print("No commentary file found.")
        return []

    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error reading commentary file.")
        return []

    return data

def display_commentary(data):
    if not data:
        print("No commentary to display.")
        return

    print("\n--- Finley Commentary Log ---\n")
    for i, entry in enumerate(data, start=1):
        # Use the loop index i as an ID display instead of entry['id']
        print(f"[{i}] {entry.get('timestamp', 'No timestamp')}")
        # Use 'commentary' or fallback if missing
        print(f"> {entry.get('commentary', 'No commentary')}\n")

if __name__ == "__main__":
    commentary = load_commentary()
    display_commentary(commentary)