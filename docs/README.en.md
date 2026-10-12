# Problem Diary

**A tiny, AI-agnostic system to keep a searchable diary of the problems you have solved, so your AI assistant stops forgetting.**

Languages: [all languages](../README.md)

## The idea

If you talk to an AI assistant every day, you solve the same kinds of problems again and again, on many devices and projects. The assistant does not remember the details, and you spend several requests rebuilding context.

This project keeps a plain-Markdown diary in a Git repository. When a problem is solved, the assistant writes a short entry: **what the problem was, the steps that actually worked, and the conclusion** (not the whole chat, and not the failed attempts). Next time, the assistant reads the diary first and finds the answer in fewer requests.

It is useful if you have many projects and devices. If you only ask quick one-off questions, you do not need it.

## How it works

```
 chat with Claude ──"close and save"──▶ prefilled link ──▶ Claude Code on the web ──▶ commit + push
        ▲                                                                                  │
        └──────────── Claude Project (GitHub repo as knowledge, press Sync) ◀──────────────┘
```

- **Writing:** Claude Code (terminal or web) creates the entry, runs `git pull`, commits and pushes.
- **Reading:** the repo is added to a Claude Project as knowledge. After each new entry, press the Sync icon.
- **No server, no tokens in chat.** The diary is just files in your own repo, so it works with any tool that can read Markdown.

## Requirements

- Your own GitHub repository (private is fine) created from this template.
- A Claude Pro, Max or Team account (needed for Claude Code on the web).
- GitHub connected at [claude.ai/code](https://claude.ai/code), with the Claude app authorised on your diary repo.
- GitHub connected to claude.ai (the GitHub integration) so a Project can read the repo.
- For long entries created from chat: code execution and file creation enabled in Claude settings.

## Setup

1. Create a **private** repo from this template and clone or upload these files.
2. Connect GitHub at claude.ai/code and authorise the repo (grant access to this repo only).
3. Create a Claude **Project**. In its knowledge section press **+**, choose **GitHub**, select your repo and the files to include.
4. Install the skill in `skill/problem-diary/` and edit its `REPO:` line with your `owner/repo-name`.
5. List your devices in `diario/DEVICES.md` using one official name per device.

## Daily use

When a problem is solved, tell the assistant **"close and save"**. Depending on length, one of three paths is used:

| Situation | What happens |
|---|---|
| Short entry, from chat | The skill prepares a `claude.ai/code` link with the prompt and repo already filled in. Open it and press Enter. |
| Long entry, from chat | The skill creates the `.md` file with the right name and tells you the exact folder. Upload it from the GitHub website (*Add file > Upload files*). |
| You are already in Claude Code | It writes the file directly: `git pull`, commit, push. No length limit. |

Then press **Sync** in the Claude Project, so chats see the new entry.

## Repository structure

```
README.md                          index of the translated READMEs
CLAUDE.md                          instructions for the coding agent
docs/README.{lang}.md              README in each language
diario/
  DEVICES.md                       official device names (one name per device)
  _TEMPLATE.md                     entry template
  {device-slug}/
    YYYY-MM-DD-short-title.md      one file per solved problem
skill/problem-diary/               the "close and save" skill
  SKILL.md                         workflow and rules
  scripts/build_link.py            builds the prefilled link, checks length and secrets
  assets/entry-template.md         entry template used by the skill (keep in sync with diario/_TEMPLATE.md)
```

Problems that belong to no single device (a website, a shared service) go in `diario/general/`.

## Entry format

Each entry has the same fixed headings, so grep and AI search work reliably: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus optional **Do not**, and **Related**. The content is written in your own language. See `diario/_TEMPLATE.md`.

## Limits and privacy

- A link carries the entry inside the URL, so only short entries use it. Longer ones use the file path.
- Opening the link and pressing Enter stays manual: it is not fully automatic, and no entry is saved without you seeing it.
- Each saved entry starts a Claude Code web session, which counts toward your subscription usage.
- Keep the repo private. Entries describe your systems in detail.
- **Never put passwords, tokens or keys in an entry.** Write where they are stored instead.
- The whole repo counts toward the Project knowledge capacity. Short entries fit by the hundreds.
- GitHub sync in Projects can occasionally lag or fail. If chat does not see a new entry, press Sync again and check.

## License

Choose a license for your fork (MIT is a common choice for a project like this).
