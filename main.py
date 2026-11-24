"""The 3 AM Commit Message.

Writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt: the
funniest thing an AI agent would write right after breaking
production at 3 AM. Standard library only.
"""

import os

COMMIT = (
    "fix: reverted the 3am deploy -- the tests were green because "
    "I wrote them after the code and marked my own homework."
)


def check_commit(text):
    """Check the commit message against the competition gate.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line that reads as one commit message. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("commit message must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("commit is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("commit message must be exactly one line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_commit(COMMIT)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
