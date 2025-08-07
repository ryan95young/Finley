import json
import os

def load_commentary(json_path="finley_memory.json"):
    if not os.path.exists(json_path):
        print("No commentary file found.")
        return []
    with open(json_path, "r") as f:
        return json.load(f)

def search_by_tag(commentary, tag):
    tag = tag.lower()
    results = [entry for entry in commentary if tag in (t.lower() for t in entry.get("tags", []))]
    return results

def search_by_keyword(commentary, keyword):
    keyword = keyword.lower()
    results = [entry for entry in commentary if keyword in entry.get("text", "").lower()]
    return results

def main():
    commentary = load_commentary()
    if not commentary:
        return

    choice = input("Search by (1) tag or (2) keyword? Enter 1 or 2: ").strip()
    if choice == "1":
        tag = input("Enter tag to search for: ").strip()
        results = search_by_tag(commentary, tag)
    elif choice == "2":
        keyword = input("Enter keyword to search for: ").strip()
        results = search_by_keyword(commentary, keyword)
    else:
        print("Invalid choice.")
        return

    if not results:
        print("No matching commentary found.")
        return

    print(f"\nFound {len(results)} matching entries:\n")
    for entry in results:
        print(f"ID: {entry['id']} | Tags: {entry.get('tags', [])} | Timestamp: {entry['timestamp']}")
        print(f"Text: {entry['text']}\n{'-'*40}")

if __name__ == "__main__":
    main()