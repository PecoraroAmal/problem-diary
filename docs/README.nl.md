# Problem Diary

**Een klein, AI-onafhankelijk systeem om een doorzoekbaar dagboek bij te houden van de problemen die je hebt opgelost, zodat je AI-assistent niet meer vergeet.**

Talen: [alle talen](../README.md)

## Het idee

Als je dagelijks met een AI-assistent praat, los je steeds dezelfde soorten problemen op, op veel apparaten en in veel projecten. De assistent onthoudt de details niet en jij besteedt meerdere verzoeken aan het herstellen van de context.

Dit project houdt een dagboek bij in gewone Markdown in een Git-repository. Zodra een probleem is opgelost, schrijft de assistent een korte notitie: **wat het probleem was, de stappen die echt werkten en de conclusie** (niet de hele chat en niet de mislukte pogingen). De volgende keer leest de assistent eerst het dagboek en vindt het antwoord met minder verzoeken.

Het is nuttig als je veel projecten en apparaten hebt. Stel je alleen snelle, losse vragen, dan heb je het niet nodig.

## Hoe het werkt

```
 chat met Claude ──"close and save"──▶ voorgevulde link ──▶ Claude Code op het web ──▶ commit + push
        ▲                                                                                  │
        └──────── Claude Project (GitHub-repo als kennis, druk op Sync) ◀──────────────────┘
```

- **Schrijven:** Claude Code (terminal of web) maakt de notitie, voert `git pull` uit, commit en pusht.
- **Lezen:** de repo wordt als kennis aan een Claude Project toegevoegd. Druk na elke nieuwe notitie op het Sync-icoon.
- **Geen server en geen tokens in de chat.** Het dagboek bestaat alleen uit bestanden in je eigen repo en werkt dus met elk hulpmiddel dat Markdown kan lezen.

## Vereisten

- Een eigen GitHub-repository (privé is prima), gemaakt van dit sjabloon.
- Een Claude Pro-, Max- of Team-account (nodig voor Claude Code op het web).
- GitHub gekoppeld aan [claude.ai/code](https://claude.ai/code), met de Claude-app geautoriseerd voor je dagboekrepo.
- GitHub gekoppeld aan claude.ai (de GitHub-integratie) zodat een Project de repo kan lezen.
- Voor lange notities vanuit de chat: code-uitvoering en bestandscreatie ingeschakeld in de Claude-instellingen.

## Installatie

1. Maak van dit sjabloon een **privé**-repo en kloon of upload deze bestanden.
2. Koppel GitHub op claude.ai/code en autoriseer de repo (geef alleen toegang tot deze repo).
3. Maak een Claude **Project**. Druk in het kennisgedeelte op **+**, kies **GitHub** en selecteer je repo en de bestanden die je wilt opnemen.
4. Installeer de skill uit `skill/problem-diary/` en pas de regel `REPO:` aan met je `owner/repo-naam`.
5. Zet je apparaten in `diario/DEVICES.md`, met één officiële naam per apparaat.

## Dagelijks gebruik

Zodra een probleem is opgelost, zeg je tegen de assistent **"close and save"**. Afhankelijk van de lengte wordt een van drie routes gebruikt:

| Situatie | Wat er gebeurt |
|---|---|
| Korte notitie, vanuit de chat | De skill maakt een `claude.ai/code`-link met prompt en repo al ingevuld. Open hem en druk op Enter. |
| Lange notitie, vanuit de chat | De skill maakt het `.md`-bestand met de juiste naam en vertelt je de exacte map. Upload het via de GitHub-website (*Add file > Upload files*). |
| Je zit al in Claude Code | Het schrijft het bestand direct: `git pull`, commit, push. Geen lengtelimiet. |

Druk daarna op **Sync** in het Claude Project, zodat chats de nieuwe notitie zien.

## Repositorystructuur

```
README.md                          index van de vertaalde README's
CLAUDE.md                          instructies voor de codeeragent
docs/README.{lang}.md              README in elke taal
diario/
  DEVICES.md                       officiële apparaatnamen (één naam per apparaat)
  _TEMPLATE.md                     notitiesjabloon
  {device-slug}/
    YYYY-MM-DD-short-title.md      één bestand per opgelost probleem
skill/problem-diary/               de skill "close and save"
  SKILL.md                         werkwijze en regels
  scripts/build_link.py            bouwt de voorgevulde link, controleert lengte en geheimen
  assets/entry-template.md         sjabloon van de skill (houd gelijk aan diario/_TEMPLATE.md)
```

Problemen die bij geen enkel apparaat horen (een website, een gedeelde dienst) komen in `diario/general/`.

## Notitieformaat

Elke notitie heeft dezelfde vaste koppen, zodat grep en AI-zoeken betrouwbaar werken: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus de optionele **Do not** en **Related**. De inhoud schrijf je in je eigen taal. Zie `diario/_TEMPLATE.md`.

## Beperkingen en privacy

- Een link bevat de notitie in de URL, dus alleen korte notities gebruiken hem. Langere gaan via het bestand.
- De link openen en op Enter drukken blijft handmatig: het is niet volledig automatisch en er wordt geen notitie opgeslagen zonder dat je hem ziet.
- Elke opgeslagen notitie start een Claude Code-websessie, die meetelt voor het gebruik van je abonnement.
- Houd de repo privé. Notities beschrijven je systemen in detail.
- **Zet nooit wachtwoorden, tokens of sleutels in een notitie.** Schrijf in plaats daarvan waar ze zijn opgeslagen.
- De hele repo telt mee voor de kenniscapaciteit van het Project. Honderden korte notities passen erin.
- De GitHub-synchronisatie in Projects kan soms vertraagd zijn of mislukken. Ziet de chat een nieuwe notitie niet, druk dan opnieuw op Sync en controleer het.

## Licentie

Kies een licentie voor je fork (MIT is een gangbare keuze voor een project als dit).
