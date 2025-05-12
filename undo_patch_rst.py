import os
import re

# Configuration
RST_DIR = "docs"  # Directory containing your .rst files
SUB_FILE = "_substitutions.rst"
INCLUDE_DIRECTIVE = f".. include:: {SUB_FILE}"
SUB_KEY = "|imgpath|"
RAW_PATH = "../../../version-0.2/nucleardatapy_samples/figs"

# Regex to match variants like ":scale: 70%", ":scale:70 %", etc.
scale_pattern = re.compile(r'^(\s*):scale:\s*70\s*%')

def process_rst_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    new_lines = []

    for line in lines:
        original_line = line

        # Remove include directive line
        if INCLUDE_DIRECTIVE in line.strip():
            modified = True
            continue

        # Replace |imgpath| with raw path
        if SUB_KEY in line:
            line = line.replace(SUB_KEY, RAW_PATH)
            modified = True

        # Replace ":scale: 70%" with ":width: 70%"
        if scale_pattern.match(line):
            indent = scale_pattern.match(line).group(1)
            line = f"{indent}:width: 70%\n"
            modified = True

        new_lines.append(line)

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")

def main():
    for root, _, files in os.walk(RST_DIR):
        for file in files:
            if file.endswith(".rst"):
                process_rst_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
