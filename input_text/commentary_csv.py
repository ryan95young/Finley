import pandas as pd
import json
import os
from datetime import datetime
from uuid import uuid4
from commentary_sanitize_text import sanitize_text  # uses your existing function

# === Settings ===
json_path = "finley_memory.json"

# === Load or initialize JSON memory ===
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = []

# === Choose CSV to upload ===
csv_path = input("Enter path to commentary CSV file: ").strip('"')
df = pd.read_csv(csv_path, sep=",", engine="python")
df.columns = df.columns.str.strip().str.lower()

# === Process each row ===

for _, row in df.iterrows():
    # Sanitize all values in the row
    sanitized_row = {
        col: sanitize_text(str(val)) if pd.notna(val) else "" 
        for col, val in row.items()
    }

    # Check if any column was changed after sanitization
    sanitized = any(
        sanitize_text(str(val)) != str(val)
        for col, val in row.items()
        if pd.notna(val)
    )

    # Required fields
    entry = {
        "id": str(uuid4()),  # unique identifier for each entry
        "month": sanitized_row.get("month", ""),
        "business_unit": sanitized_row.get("business_unit", ""),
        "metric": sanitized_row.get("metric", ""),
        "commentary": sanitized_row.get("commentary", ""),
        "sanitized": sanitized,
        "uploaded_by": sanitized_row.get("uploaded_by", ""),
        "timestamp": datetime.now().isoformat(timespec="seconds")
    }

    memory.append(entry)

# === Save back to JSON ===
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

print(f"✅ {len(df)} entries added to Finley memory.")
