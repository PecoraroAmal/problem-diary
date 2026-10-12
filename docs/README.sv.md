# Problem Diary

**Ett litet, AI-oberoende system för att föra en sökbar dagbok över problem du har löst, så att din AI-assistent slutar glömma.**

Språk: [alla språk](../README.md)

## Idén

Om du pratar med en AI-assistent varje dag löser du samma typer av problem om och om igen, på många enheter och i många projekt. Assistenten minns inte detaljerna, och du lägger flera förfrågningar på att återskapa sammanhanget.

Det här projektet för en dagbok i enkel Markdown i ett Git-repository. När ett problem är löst skriver assistenten en kort post: **vad problemet var, stegen som faktiskt fungerade och slutsatsen** (inte hela chatten och inte de misslyckade försöken). Nästa gång läser assistenten dagboken först och hittar svaret med färre förfrågningar.

Det är användbart om du har många projekt och enheter. Ställer du bara snabba, enstaka frågor behöver du det inte.

## Så fungerar det

```
 chatt med Claude ──"close and save"──▶ förifylld länk ──▶ Claude Code på webben ──▶ commit + push
        ▲                                                                                │
        └──────── Claude Project (GitHub-repo som kunskap, tryck Sync) ◀─────────────────┘
```

- **Skriva:** Claude Code (terminal eller webb) skapar posten, kör `git pull`, committar och pushar.
- **Läsa:** repot läggs till i ett Claude Project som kunskap. Efter varje ny post trycker du på Sync-ikonen.
- **Ingen server och inga tokens i chatten.** Dagboken är bara filer i ditt eget repo, så den fungerar med alla verktyg som kan läsa Markdown.

## Krav

- Ett eget GitHub-repository (privat går bra) skapat från den här mallen.
- Ett Claude Pro-, Max- eller Team-konto (krävs för Claude Code på webben).
- GitHub anslutet till [claude.ai/code](https://claude.ai/code), med Claude-appen auktoriserad för ditt dagboksrepo.
- GitHub anslutet till claude.ai (GitHub-integrationen) så att ett Project kan läsa repot.
- För långa poster skapade från chatten: kodexekvering och filskapande aktiverade i Claudes inställningar.

## Installation

1. Skapa ett **privat** repo från den här mallen och klona eller ladda upp filerna.
2. Anslut GitHub på claude.ai/code och auktorisera repot (ge åtkomst endast till det här repot).
3. Skapa ett Claude **Project**. I kunskapsdelen trycker du på **+**, väljer **GitHub** och markerar ditt repo och filerna som ska ingå.
4. Installera skillen i `skill/problem-diary/` och ändra raden `REPO:` till ditt `owner/repo-namn`.
5. Lista dina enheter i `diario/DEVICES.md`, med ett officiellt namn per enhet.

## Daglig användning

När ett problem är löst, säg till assistenten **"close and save"**. Beroende på längd används en av tre vägar:

| Situation | Vad som händer |
|---|---|
| Kort post, från chatten | Skillen förbereder en `claude.ai/code`-länk med prompt och repo redan ifyllda. Öppna den och tryck Enter. |
| Lång post, från chatten | Skillen skapar `.md`-filen med rätt namn och talar om exakt vilken mapp den ska i. Ladda upp den via GitHubs webbplats (*Add file > Upload files*). |
| Du är redan i Claude Code | Den skriver filen direkt: `git pull`, commit, push. Ingen längdgräns. |

Tryck sedan på **Sync** i Claude Project så att chattarna ser den nya posten.

## Repostruktur

```
README.md                          index över de översatta README-filerna
CLAUDE.md                          instruktioner för kodagenten
docs/README.{lang}.md              README på varje språk
diario/
  DEVICES.md                       officiella enhetsnamn (ett namn per enhet)
  _TEMPLATE.md                     postmall
  {device-slug}/
    YYYY-MM-DD-short-title.md      en fil per löst problem
skill/problem-diary/               skillen "close and save"
  SKILL.md                         arbetsflöde och regler
  scripts/build_link.py            bygger den förifyllda länken, kontrollerar längd och hemligheter
  assets/entry-template.md         mall som skillen använder (håll synkad med diario/_TEMPLATE.md)
```

Problem som inte hör till någon enskild enhet (en webbplats, en delad tjänst) hamnar i `diario/general/`.

## Postformat

Varje post har samma fasta rubriker, så att grep och AI-sökning fungerar tillförlitligt: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus de valfria **Do not** och **Related**. Innehållet skrivs på ditt eget språk. Se `diario/_TEMPLATE.md`.

## Begränsningar och integritet

- En länk bär posten i URL:en, så bara korta poster använder den. Längre poster går via filen.
- Att öppna länken och trycka Enter är fortfarande manuellt: det är inte helt automatiskt, och ingen post sparas utan att du ser den.
- Varje sparad post startar en Claude Code-webbsession, som räknas mot din prenumerations användning.
- Håll repot privat. Posterna beskriver dina system i detalj.
- **Skriv aldrig lösenord, tokens eller nycklar i en post.** Skriv i stället var de förvaras.
- Hela repot räknas mot Projectets kunskapskapacitet. Hundratals korta poster ryms.
- GitHub-synkningen i Projects kan ibland vara fördröjd eller misslyckas. Om chatten inte ser en ny post, tryck Sync igen och kontrollera.

## Licens

Välj en licens för din fork (MIT är ett vanligt val för ett projekt som det här).
