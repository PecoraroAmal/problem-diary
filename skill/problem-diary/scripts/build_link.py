#!/usr/bin/env python3
"""Build a claude.ai/code link that prefills a prompt and a repository
for saving one problem-diary entry.

Exit codes: 0 ok, 2 link too long (use the file path instead),
3 the entry looks like it contains a secret (fix it and run again).
"""
import argparse
import re
import sys
from urllib.parse import quote

PROMPT = """Follow the instructions in CLAUDE.md. Run git pull, then create the file `{path}` with exactly the content below. If the device is missing from diario/DEVICES.md, add it. Commit with message "diary: {device} - {title}" and push.

---
{entry}"""

# Conservative limit: long URLs are cut or rejected by browsers and servers.
DEFAULT_MAX_URL = 3000

SECRET_PATTERNS = [
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"sk-ant-[A-Za-z0-9_-]{10,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"(?i)\b(password|passwd|token|secret|api[_-]?key)\s*[:=]\s*\S{6,}",
]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", required=True, help="owner/name of the diary repo")
    p.add_argument("--path", required=True, help="path of the new entry in the repo")
    p.add_argument("--device", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--entry-file", required=True)
    p.add_argument("--max-url", type=int, default=DEFAULT_MAX_URL)
    a = p.parse_args()

    with open(a.entry_file, encoding="utf-8") as f:
        entry = f.read().strip()

    for pattern in SECRET_PATTERNS:
        if re.search(pattern, entry):
            print("The entry seems to contain a secret. Replace it with a note on "
                  "where it is stored, then run again.", file=sys.stderr)
            sys.exit(3)

    prompt = PROMPT.format(path=a.path, device=a.device, title=a.title, entry=entry)
    url = ("https://claude.ai/code?prompt=" + quote(prompt, safe="")
           + "&repositories=" + quote(a.repo, safe="/"))

    if len(url) > a.max_url:
        print(f"Link too long ({len(url)} chars, limit {a.max_url}). "
              "Use the file path instead.", file=sys.stderr)
        sys.exit(2)

    print(url)
    print(f"({len(url)} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
