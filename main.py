"""Write the one-line warning label to /output/entry.txt.

Standard library only: no Pillow, no numpy, no external font or data
file. The output folder itself is never removed; only its contents
are cleared, because the grading sandbox mounts /output.
"""

import os

LINE = "WARNING: This human runs on caffeine and spite. Do not shake before 9 AM. May spontaneously talk about crypto."
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
