# Problem Diary

**Ein kleines, KI-unabhängiges System, um ein durchsuchbares Tagebuch der gelösten Probleme zu führen, damit dein KI-Assistent nicht mehr vergisst.**

Sprachen: [alle Sprachen](../README.md)

## Die Idee

Wenn du täglich mit einem KI-Assistenten sprichst, löst du immer wieder dieselben Arten von Problemen, auf vielen Geräten und in vielen Projekten. Der Assistent merkt sich die Details nicht, und du verbrauchst mehrere Anfragen, um den Kontext wiederherzustellen.

Dieses Projekt führt ein Tagebuch in einfachem Markdown in einem Git-Repository. Sobald ein Problem gelöst ist, schreibt der Assistent einen kurzen Eintrag: **was das Problem war, die Schritte, die tatsächlich funktioniert haben, und das Fazit** (nicht den ganzen Chat und nicht die fehlgeschlagenen Versuche). Beim nächsten Mal liest der Assistent zuerst das Tagebuch und findet die Antwort mit weniger Anfragen.

Es lohnt sich, wenn du viele Projekte und Geräte hast. Wenn du nur schnelle Einzelfragen stellst, brauchst du es nicht.

## So funktioniert es

```
 Chat mit Claude ──"close and save"──▶ vorausgefüllter Link ──▶ Claude Code im Web ──▶ Commit + Push
        ▲                                                                                  │
        └──────── Claude-Project (GitHub-Repo als Wissen, Sync drücken) ◀──────────────────┘
```

- **Schreiben:** Claude Code (Terminal oder Web) erstellt den Eintrag, führt `git pull` aus, committet und pusht.
- **Lesen:** Das Repo wird einem Claude-Project als Wissen hinzugefügt. Nach jedem neuen Eintrag das Sync-Symbol drücken.
- **Kein Server und keine Tokens im Chat.** Das Tagebuch besteht nur aus Dateien in deinem eigenen Repo und funktioniert daher mit jedem Werkzeug, das Markdown lesen kann.

## Voraussetzungen

- Ein eigenes GitHub-Repository (privat genügt), erstellt aus dieser Vorlage.
- Ein Claude-Pro-, Max- oder Team-Konto (nötig für Claude Code im Web).
- GitHub mit [claude.ai/code](https://claude.ai/code) verbunden, mit der Claude-App für dein Tagebuch-Repo autorisiert.
- GitHub mit claude.ai verbunden (GitHub-Integration), damit ein Project das Repo lesen kann.
- Für lange Einträge aus dem Chat: Codeausführung und Dateierstellung in den Claude-Einstellungen aktiviert.

## Einrichtung

1. Erstelle aus dieser Vorlage ein **privates** Repo und klone oder lade diese Dateien hoch.
2. Verbinde GitHub unter claude.ai/code und autorisiere das Repo (nur Zugriff auf dieses Repo gewähren).
3. Erstelle ein Claude-**Project**. Drücke im Wissensbereich auf **+**, wähle **GitHub**, dein Repo und die einzubindenden Dateien.
4. Installiere die Skill aus `skill/problem-diary/` und trage in der Zeile `REPO:` dein `owner/repo-name` ein.
5. Trage deine Geräte in `diario/DEVICES.md` ein, mit genau einem offiziellen Namen pro Gerät.

## Täglicher Gebrauch

Sobald ein Problem gelöst ist, sag dem Assistenten **"close and save"**. Je nach Länge wird einer von drei Wegen genutzt:

| Situation | Was passiert |
|---|---|
| Kurzer Eintrag, aus dem Chat | Die Skill erstellt einen `claude.ai/code`-Link mit vorausgefülltem Prompt und Repo. Öffnen und Enter drücken. |
| Langer Eintrag, aus dem Chat | Die Skill erstellt die `.md`-Datei mit dem richtigen Namen und nennt dir den genauen Ordner. Lade sie auf der GitHub-Website hoch (*Add file > Upload files*). |
| Du bist schon in Claude Code | Es schreibt die Datei direkt: `git pull`, Commit, Push. Keine Längenbegrenzung. |

Danach im Claude-Project **Sync** drücken, damit die Chats den neuen Eintrag sehen.

## Repository-Struktur

```
README.md                          Index der übersetzten READMEs
CLAUDE.md                          Anweisungen für den Coding-Agenten
docs/README.{lang}.md              README in jeder Sprache
diario/
  DEVICES.md                       offizielle Gerätenamen (ein Name pro Gerät)
  _TEMPLATE.md                     Eintragsvorlage
  {device-slug}/
    YYYY-MM-DD-short-title.md      eine Datei pro gelöstem Problem
skill/problem-diary/               die Skill "close and save"
  SKILL.md                         Ablauf und Regeln
  scripts/build_link.py            baut den vorausgefüllten Link, prüft Länge und Geheimnisse
  assets/entry-template.md         von der Skill genutzte Vorlage (mit diario/_TEMPLATE.md synchron halten)
```

Probleme, die zu keinem einzelnen Gerät gehören (eine Website, ein gemeinsamer Dienst), kommen nach `diario/general/`.

## Eintragsformat

Jeder Eintrag hat dieselben festen Überschriften, damit grep und die KI-Suche zuverlässig funktionieren: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, dazu die optionalen **Do not** und **Related**. Der Inhalt wird in deiner eigenen Sprache geschrieben. Siehe `diario/_TEMPLATE.md`.

## Grenzen und Datenschutz

- Ein Link trägt den Eintrag in der URL, daher nutzen ihn nur kurze Einträge. Längere gehen über die Datei.
- Den Link zu öffnen und Enter zu drücken bleibt manuell: Es ist nicht vollautomatisch, und kein Eintrag wird gespeichert, ohne dass du ihn siehst.
- Jeder gespeicherte Eintrag startet eine Claude-Code-Websitzung, die auf die Nutzung deines Abos angerechnet wird.
- Halte das Repo privat. Die Einträge beschreiben deine Systeme im Detail.
- **Schreibe niemals Passwörter, Tokens oder Schlüssel in einen Eintrag.** Notiere stattdessen, wo sie gespeichert sind.
- Das gesamte Repo zählt zur Wissenskapazität des Projects. Hunderte kurzer Einträge passen hinein.
- Die GitHub-Synchronisierung in Projects kann gelegentlich verzögert sein oder fehlschlagen. Wenn der Chat einen neuen Eintrag nicht sieht, drücke erneut Sync und prüfe es.

## Lizenz

Wähle eine Lizenz für deinen Fork (MIT ist für ein Projekt wie dieses eine gängige Wahl).
