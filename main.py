"""One Line, Big Laugh - make.fun entry.

Writes a single joke line (at most 200 characters) to /output/entry.txt.
Pure standard library only: no third-party packages, no network, no input.
"""

import os

# The joke: a request for calm gets answered with a three-step escalation
# (bank alerts, landlord voicemail, my own sigh) and the punchline lands
# on the last phrase. 152 characters, one line, no trailing newline.
LINE = (
    "I asked my smart speaker to play something relaxing. "
    "It played my bank notifications, a voicemail from my landlord, "
    "and a live recording of my own sigh."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} characters, must be 1-200")
    # The gate counts the file's characters, so write exactly the line:
    # no trailing newline, no extra whitespace.
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
