from difflib import SequenceMatcher

def detect_conflicts_and_duplicates(new_entry, memory, dup_threshold=0.85, conflict_threshold=0.5):
    duplicates = []
    conflicts = []

    def similarity(t1, t2):
        return SequenceMatcher(None, t1, t2).ratio()

    for existing in memory:
        sim = similarity(new_entry["text"], existing["text"])

        if sim >= dup_threshold:
            duplicates.append(existing)
        elif (new_entry.get("month") == existing.get("month") and
              new_entry.get("business_unit") == existing.get("business_unit") and
              new_entry.get("metric") == existing.get("metric") and
              sim < conflict_threshold):
            conflicts.append(existing)

    if duplicates:
        print(f"⚠️ Found {len(duplicates)} possible duplicate(s):")
        for d in duplicates:
            print(f"  - ID {d['id']}: {d['text']}")

    if conflicts:
        print(f"⚠️ Found {len(conflicts)} possible conflicting entries:")
        for c in conflicts:
            print(f"  - ID {c['id']}: {c['text']}")

    if duplicates or conflicts:
        proceed = input("Do you still want to save this commentary? (yes/no): ").strip().lower()
        if proceed not in ("yes", "y"):
            print("Entry not saved.")
            return False  # Signal to abort saving

    return True  # Signal to proceed with saving
