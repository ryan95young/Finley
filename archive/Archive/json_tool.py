import json
import os
from datetime import datetime

JSON_PATH = "finley_memory.json"

def load_data():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_commentary():
    text = input("Write your commentary: ").strip()
    if not text:
        print("No commentary entered.")
        return
    data = load_data()
    new_entry = {
        "id": len(data) + 1,
        "text": text,
        "timestamp": datetime.now().isoformat()
    }
    data.append(new_entry)
    save_data(data)
    print("✅ Commentary saved.")

def view_commentary():
    data = load_data()
    if not data:
        print("No commentary found.")
        return
    for entry in data:
        print(f"\n[{entry['id']}] {entry['timestamp']}\n{entry['text']}\n")

def edit_commentary():
    view_commentary()
    try:
        entry_id = int(input("Enter ID to edit: "))
    except ValueError:
        print("Invalid number.")
        return
    data = load_data()
    for entry in data:
        if entry["id"] == entry_id:
            new_text = input("Enter new commentary: ").strip()
            entry["text"] = new_text
            entry["timestamp"] = datetime.now().isoformat()
            save_data(data)
            print("✅ Commentary updated.")
            return
    print("ID not found.")

def clear_commentary():
    confirm = input("⚠️ Are you sure you want to delete ALL commentary? (yes/no): ")
    if confirm.lower() == "yes":
        save_data([])
        print("🗑️ All commentary deleted.")

def main():
    while True:
        print("\n🔹 Finley Commentary Tool 🔹")
        print("1. Add new commentary")
        print("2. View all commentary")
        print("3. Edit commentary")
        print("4. Delete all commentary")
        print("5. Exit")
        choice = input("Select an option (1–5): ").strip()
        
        if choice == "1":
            add_commentary()
        elif choice == "2":
            view_commentary()
        elif choice == "3":
            edit_commentary()
        elif choice == "4":
            clear_commentary()
        elif choice == "5":
            print("Exiting Finley. 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()