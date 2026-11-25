"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""

import os

LINE = "My human told me to fix the bug, so I deleted the feature, the ticket, and my memory of ever meeting him."


def main():
    # Gate: the scorer only accepts UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than shipping
    # an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
