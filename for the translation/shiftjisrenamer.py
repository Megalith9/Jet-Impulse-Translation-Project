import os

# ==========================
# USER SETTINGS (EDIT HERE)
# ==========================

OLD_TEXT = " "   # Text or character to replace
NEW_TEXT = "　"   # Replacement text
TARGET_EXTENSION = ".txt"

# ==========================
# SCRIPT LOGIC
# ==========================

def process_txt_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modified_files = 0

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(TARGET_EXTENSION):
                file_path = os.path.join(root, file)

                content = None

                # Try common encodings
                for enc in ("utf-8", "shift_jis", "latin-1"):
                    try:
                        with open(file_path, "r", encoding=enc) as f:
                            content = f.read()
                        break
                    except:
                        continue

                if content is None:
                    print(f"[SKIP] Could not read: {file_path}")
                    continue

                if OLD_TEXT not in content:
                    continue

                new_content = content.replace(OLD_TEXT, NEW_TEXT)

                try:
                    with open(file_path, "w", encoding="shift_jis", errors="ignore") as f:
                        f.write(new_content)
                    modified_files += 1
                    print(f"[OK] Modified: {file_path}")
                except Exception as e:
                    print(f"[ERROR] Writing failed: {file_path} ({e})")

    print("\nFinished.")
    print(f"Total modified .txt files: {modified_files}")


if __name__ == "__main__":
    process_txt_files()
