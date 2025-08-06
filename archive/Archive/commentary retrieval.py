from docx import Document
import os

def pull_all_lines(docx_path="finley_memory.docx"):
    if not os.path.exists(docx_path):
        print("No commentary memory found.")
        return []

    doc = Document(docx_path)
    lines = [para.text for para in doc.paragraphs]
    return lines

# Example usage:
all_lines = pull_all_lines()
for i, line in enumerate(all_lines, 1):
    print(f"{i}: {line}")