---
name: problem-diary
description: Save a solved technical problem as a reusable entry in the user's GitHub problem diary (date, device, problem, the steps that worked, conclusion). Use whenever the user says "close and save", "chiudi e salva", "save this solution", "add it to the diary", "salva nel diario", or signals that a problem is solved and worth keeping, even if they never mention the diary or GitHub. Also use when a long troubleshooting conversation ends with a working fix. Produces a prefilled claude.ai/code link (short entries) or a ready-to-upload .md file (long entries), and writes directly when already inside Claude Code.
---

# Problem Diary

Turn a solved problem into a short diary entry stored in the user's own GitHub repo, so that future conversations find the answer in fewer requests. An entry is only useful if someone searching by symptom, device or error message can land on it and reuse it, so specific and findable beats complete.

## Configuration (edit once)

```
REPO: owner/repo-name
```

Replace `owner/repo-name` with the diary repository. If it is still the placeholder, ask the user for the real name once, reuse it for the rest of the conversation, and suggest they edit this line.

## When to run

Run when the user asks to close and save, or clearly signals that a problem is solved and worth keeping. Skip trivial questions that a quick search would answer. If unsure whether the problem deserves an entry, ask in one short line.

## Workflow

### 1. Write the entry

Read `assets/entry-template.md` and fill it in. The reasons behind each rule matter more than the rules, so apply them with judgment:

- **Keep only what worked.** Failed attempts are noise when the entry is reread months later. Add the optional "Do not" line only when the mistake is easy to repeat.
- **Use exact commands, paths, versions and error messages.** The reader will copy them. A vague note such as "fixed the boot" cannot be reused.
- **Title the entry with the symptom or error**, not the fix. People search for what they saw.
- **Keep the headings in English and the content in the user's language.** Fixed labels keep search and grep reliable across entries.
- **Leave secrets out.** The diary lives in git history for good and may be shared one day. Replace a password, token or key with a note on where it is stored ("key kept in the password manager"), and tell the user what you replaced.

### 2. Decide device, path and date

- Use the official device name from `diario/DEVICES.md` when that file is readable in the project knowledge. If the device is unclear or not listed, ask once.
- Path: `diario/{device-slug}/YYYY-MM-DD-short-title.md`, with the slug in lowercase, hyphens, no accents.
- Problems tied to no single device (a website, a shared service) go in `diario/general/`.
- Use today's date.

### 3. Pick the delivery path

1. **Inside Claude Code** (git is available in the repo): follow the repo's `CLAUDE.md` and write the file yourself: `git pull`, create the file, commit, push directly to `main` (no other branch, no pull request). No length limit.
2. **From chat, short entry:** Path A, the prefilled link.
3. **From chat, long entry:** Path B, a file to upload. Choose this as well whenever Path A reports the link is too long.

## Path A: prefilled link

Save the entry to a temporary file, then run the script from this skill's folder:

```
python scripts/build_link.py --repo <REPO> --path <PATH> --device "<DEVICE>" --title "<TITLE>" --entry-file entry.md
```

The script URL-encodes the prompt, which is easy to get wrong by hand, and it also checks two things:

- exit code 2: the link is too long for a reliable URL, so switch to Path B
- exit code 3: the entry seems to contain a secret; fix the entry and run again

Give the resulting link to the user as a clickable link and say what happens: they open it, check the prompt, press Enter. The link only prefills the form, so nothing runs until they send it. They need Claude Code on the web connected to GitHub with the repo authorized.

If code execution is not available, build the link by hand with the same prompt skeleton that is in the script (`PROMPT` in `scripts/build_link.py`), URL-encode everything, and keep the entry under about 1,000 characters.

## Path B: file to upload

Create the entry as a `.md` file named exactly as decided in step 2 and present it. State clearly where it goes, because the wrong folder is the most likely mistake:

> Put this file in the folder `diario/<device-slug>/` of your repo (on github.com open the folder, then *Add file > Upload files*, and commit).

If file creation is unavailable, show the entry in a code block titled with its full path so the user can paste it into a new file.

## After saving

Remind the user once, in one line, to press the Sync icon in the Claude Project so chats see the new entry. Do not repeat the reminder later in the same conversation.

## Example

Input: after a long chat, the user writes "ok funziona, chiudi e salva". The fix was reinstalling a Wi-Fi driver on a laptop after a kernel update.

Output (entry text, content in Italian because the user writes Italian):

```
# Wi-Fi assente dopo l'aggiornamento del kernel (iwlwifi non carica)

- **Date:** 2026-10-12
- **Device:** Example Laptop
- **Tags:** #wifi #kernel #driver

## Context
Ubuntu 24.04, kernel aggiornato da 6.8 a 6.11, scheda Intel.

## Problem
Dopo il riavvio l'interfaccia wlp2s0 non esisteva. `dmesg` mostrava: `iwlwifi: probe failed`.

## Solution
1. `sudo apt install --reinstall linux-firmware`
2. `sudo modprobe -r iwlwifi && sudo modprobe iwlwifi`
3. Riavviare e verificare con `ip link`.

## Conclusion
Il firmware non era stato aggiornato insieme al kernel; reinstallarlo ha risolto.
```

Then Path A: path `diario/example-laptop/2026-10-12-wifi-assente-dopo-aggiornamento-kernel.md`.
