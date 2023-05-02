import os
import random
import sys
import re

def is_valid_entry(line):
    return 'schema#comment' in line

def extract_text(line):
    match = re.search(r'"(.*?)"@en', line)
    return match.group(1) if match else None

def get_random_entries(file_path, n):
    selected_entries = []

    # Get file size
    file_size = os.path.getsize(file_path)

    with open(file_path, 'r') as rdf_file:
        for _ in range(n):
            while True:
                # Move to a random position in the file
                random_pos = random.randint(0, file_size)
                rdf_file.seek(random_pos)

                # Read one line (potentially partial) and discard
                rdf_file.readline()

                # Read the next complete line
                line = rdf_file.readline()

                # Check if it is a valid entry and not a comment
                if line and is_valid_entry(line):
                    text = extract_text(line)
                    if text:
                        selected_entries.append(text)
                        break

    return selected_entries

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_rdf_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = 10  # Number of random entries to select

    random_entries = get_random_entries(file_path, n)
    for entry in random_entries:
        print(entry)
