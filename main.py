#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry 200.

Writes a single Wi-Fi network name of at most 32 characters to
/output/entry.txt. Pure Python standard library, no network, fully
deterministic: every run produces the exact same bytes.

The name: "WiFi Went Out, So Did My Wife" (29 characters).
The joke lands on first read — the Wi-Fi dropped, and so did the wife —
and the few words imply a whole story: a household, a marriage, and the
night the internet went down and she walked out with it.
"""

import os

NAME = "WiFi Went Out, So Did My Wife"

MAX_CHARS = 32


def main() -> None:
    if not NAME or not NAME.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(NAME) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(NAME)} characters, over the {MAX_CHARS} limit"
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(NAME)
    print(f"wrote {len(NAME)} characters to {path}")


if __name__ == "__main__":
    main()
