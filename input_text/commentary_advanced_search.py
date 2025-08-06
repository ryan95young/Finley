import json
import os
from datetime import datetime
from rapidfuzz import fuzz, process

def load_commentary(json_path="finley_memory.json"):
    if not os.path.exists(json_path):
        print("No commentary file found.")
        return []
    with open(json_path, "r") as f:
        return json.load(f)

def filter_by_date_range(commentary, start_date=None, end_date=None):
    filtered = []
    for entry in commentary:
        timestamp = entry.get("timestamp")
        if not timestamp:
            continue
        entry_date = datetime.fromisoformat(timestamp)
        if start_date and entry_date < start_date:
            continue
        if end_date and entry_date > end_date:
            continue
        filtered.append(entry)
    return filtered

def filter_by_tags(commentary, tags, logic="and"):
    """
    tags: list of tags to filter by
    logic: "and" = must have all tags, "or" = any tag matches
    """
    tags = [t.lower() for t in tags]
    results = []
    for entry in commentary:
        entry_tags = [t.lower() for t in entry.get("tags", [])]
        if logic == "and" and all(tag in entry_tags for tag in tags):
            results.append(entry)
        elif logic == "or" and any(tag in entry_tags for tag in tags):
            results.append(entry)
    return results

def search_by_keyword_fuzzy(commentary, keyword, threshold=70):
    """
    Use fuzzy matching to find commentary text with similarity >= threshold
    """
    results = []
    keyword = keyword.lower()
    for entry in commentary:
        text = entry.get("text", "").lower()
        score = fuzz.partial_ratio(keyword, text)
        if score >= threshold:
            results.append(entry)
    return results

def parse_date(date_str):
    try:
        return datetime.fromisoformat(date_str)
    except Exception:
        print(f"Invalid date format: {date_str}. Use YYYY-MM-DD.")
        return None

def main():
    commentary = load_commentary()
    if not commentary:
        return

    print("Filter commentary by:")
    start_date_str = input("Start date (YYYY-MM-DD) or leave blank: ").strip()
    end_date_str = input("End date (YYYY-MM-DD) or leave blank: ").strip()
    start_date = parse_date(start_date_str) if start_date_str else None
    end_date = parse_date(end_date_str) if end_date_str else None

    filtered = filter_by_date_range(commentary, start_date, end_date)

    tags_input = input("Enter tags to filter by (comma-separated) or leave blank: ").strip()
    if tags_input:
        tags = [t.strip() for t in tags_input.split(",")]
        logic = input("Match all tags (AND) or any tag (OR)? Enter AND/OR: ").strip().lower()
        logic = "and" if logic != "or" else "or"
        filtered = filter_by_tags(filtered, tags, logic)

    keyword = input("Enter keyword for fuzzy search or leave blank: ").strip()
    if keyword:
        filtered = search_by_keyword_fuzzy(filtered, keyword)

    if not filtered:
        print("No commentary matched the filters.")
        return

    print(f"\nFound {len(filtered)} matching entries:\n")
    for entry in filtered:
        print(f"ID: {entry['id']} | Tags: {entry.get('tags', [])} | Timestamp: {entry['timestamp']}")
        print(f"Text: {entry['text']}\n{'-'*40}")

if __name__ == "__main__":
    main() 