# Instructions for the coding agent

This repository is a diary of solved problems. Your job is usually to add one entry. Follow these rules exactly.

## Before anything else

1. Run `git pull` before creating or editing any file, and before every commit.
2. Read `diario/DEVICES.md` and `diario/_TEMPLATE.md`.

## Where an entry goes

- Path: `diario/{device-slug}/YYYY-MM-DD-short-title.md`
- `{device-slug}` comes from `diario/DEVICES.md`. Use the slug listed there.
- If the device is not listed, add it to `diario/DEVICES.md` (official name + slug), then create the entry.
- Problems that belong to no device go in `diario/general/`.
- `short-title`: lowercase, words separated by hyphens, no accents, describing the symptom or error, not just the fix.

## Entry format

- Follow `diario/_TEMPLATE.md`. Keep the headings exactly as they are (they are fixed English labels; the content is in the user's language).
- Keep only what worked. Do not add failed attempts. The optional `Do not` section is one line, only when the mistake is easy to repeat.
- Keep concrete details: exact error messages, commands, paths, versions, device names.
- Use the exact device name from `diario/DEVICES.md` in the `Device` field.

## Never write secrets

Never write passwords, tokens, API keys, recovery codes or private keys in an entry. If one appears in the content you were given, replace it with a note saying where it is stored (for example "key stored in the password manager") and tell the user.

## Commit

- Add one entry per commit. Do not modify other entries unless explicitly asked.
- Commit message: `diary: {device} - {short title}`
- Run `git pull` again if the push is rejected, then push.
