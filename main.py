"""One Emoji, One Smile — entry for make.fun.

Writes one emoji to /output/entry.txt.
The entry is exactly one emoji and nothing else: the one most likely to make a stranger smile.
"""
import os

LINE = "😊"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
