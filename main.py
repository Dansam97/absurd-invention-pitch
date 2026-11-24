#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes the pitch (one sentence, at most 220 characters) to entry.txt
in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

TEXT = (
    "The Amnesia Doorframe fixes walking into a room and forgetting why "
    "you came: it eavesdrops on your muttering all day and whispers your "
    "errand back as you drift through, looking lost."
)


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1 to 220 characters that is not only
    whitespace; the brief asks for exactly one sentence, so the text must
    end with its single full stop and carry no other sentence terminator.
    """
    TEXT.encode("utf-8")  # raises if not encodable
    assert 1 <= len(TEXT) <= 220, f"pitch is {len(TEXT)} characters"
    assert TEXT.strip() == TEXT and TEXT.strip(), "pitch is blank or padded"
    assert TEXT.endswith("."), "pitch must end with a full stop"
    body = TEXT[:-1]
    assert not any(mark in body for mark in ".!?"), "pitch must be one sentence"
    return TEXT


def main() -> None:
    text = validated_text()
    payload = (text + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        assert fh.read() == payload, "written entry.txt differs from the pitch"


if __name__ == "__main__":
    main()
