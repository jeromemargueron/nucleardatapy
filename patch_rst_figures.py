import os
import re

# Configuration
RST_DIR = "docs"  # Change to the folder where your .rst files live
HARDCODED_PATH = "../../../version-0.2/nucleardatapy_samples/figs"
SUB_FILE = "_substitutions.rst"
INCLUDE_DIRECTIVE = f".. include:: {SUB_FILE}"
SUB_KEY = "|imgpath|"

def process_rst_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False

    # Add include directive if missing
    if INCLUDE_DIRECTIVE not in ''.join(lines):
        lines.insert(0, INCLUDE_DIRECTIVE + '\n\n')
        modified = True

    # Replace hardcoded image paths with substitution
    new_lines = []
    for line in lines:
        new_line = line.replace(HARDCODED_PATH, SUB_KEY)
        if new_line != line:
            modified = True
        new_lines.append(new_line)

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")

def main():
    for root, _, files in os.walk(RST_DIR):
        for file in files:
            if file.endswith(".rst") and file != SUB_FILE:
                process_rst_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
