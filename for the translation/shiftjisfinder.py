import os

ENCODINGS = [
    "utf-8",
    "utf-8-sig",
    "shift_jis",
    "cp932"
]


def search_word_in_file(file_path, search_word):
    for enc in ENCODINGS:
        try:
            with open(file_path, "r", encoding=enc) as f:
                for line_number, line in enumerate(f, start=1):
                    if search_word in line:
                        print(f"\nFile: {file_path}")
                        print(f"Line {line_number}: {line.rstrip()}")
                return True  # Successfully read with this encoding
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return False

    print(f"Skipped (unsupported encoding): {file_path}")
    return False


def search_word_in_txt(search_root, search_word):
    total_files = 0

    for root, _, files in os.walk(search_root):
        for file in files:
            if file.lower().endswith(".txt"):
                total_files += 1
                search_word_in_file(os.path.join(root, file), search_word)

    print(f"\nSearch finished. TXT files scanned: {total_files}")


if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.abspath(__file__))

    word = input("Enter the word to search for: ").strip()

    if not word:
        print("Search word cannot be empty.")
    else:
        print(f"Searching in: {script_folder}")
        search_word_in_txt(script_folder, word)
