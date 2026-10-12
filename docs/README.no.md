# Problem Diary

**Et lite, KI-uavhengig system for å føre en søkbar dagbok over problemer du har løst, slik at KI-assistenten din slutter å glemme.**

Språk: [alle språk](../README.md)

## Ideen

Hvis du snakker med en KI-assistent hver dag, løser du de samme typene problemer om og om igjen, på mange enheter og i mange prosjekter. Assistenten husker ikke detaljene, og du bruker flere forespørsler på å gjenskape konteksten.

Dette prosjektet fører en dagbok i enkel Markdown i et Git-repository. Når et problem er løst, skriver assistenten en kort oppføring: **hva problemet var, trinnene som faktisk fungerte og konklusjonen** (ikke hele chatten og ikke de mislykkede forsøkene). Neste gang leser assistenten dagboken først og finner svaret med færre forespørsler.

Det er nyttig hvis du har mange prosjekter og enheter. Stiller du bare raske, enkeltstående spørsmål, trenger du det ikke.

## Slik fungerer det

```
 chat med Claude ──"close and save"──▶ forhåndsutfylt lenke ──▶ Claude Code på nett ──▶ commit + push
        ▲                                                                                  │
        └──────── Claude Project (GitHub-repo som kunnskap, trykk Sync) ◀──────────────────┘
```

- **Skriving:** Claude Code (terminal eller nett) lager oppføringen, kjører `git pull`, committer og pusher.
- **Lesing:** repoet legges til i et Claude Project som kunnskap. Etter hver nye oppføring trykker du på Sync-ikonet.
- **Ingen server og ingen tokens i chatten.** Dagboken er bare filer i ditt eget repo, så den fungerer med alle verktøy som kan lese Markdown.

## Krav

- Et eget GitHub-repository (privat går fint) opprettet fra denne malen.
- En Claude Pro-, Max- eller Team-konto (kreves for Claude Code på nett).
- GitHub koblet til [claude.ai/code](https://claude.ai/code), med Claude-appen autorisert for dagbokrepoet ditt.
- GitHub koblet til claude.ai (GitHub-integrasjonen) slik at et Project kan lese repoet.
- For lange oppføringer laget fra chatten: kodekjøring og filoppretting aktivert i Claudes innstillinger.

## Oppsett

1. Opprett et **privat** repo fra denne malen og klon eller last opp filene.
2. Koble GitHub til claude.ai/code og autoriser repoet (gi tilgang kun til dette repoet).
3. Opprett et Claude **Project**. I kunnskapsdelen trykker du **+**, velger **GitHub** og markerer repoet og filene som skal være med.
4. Installer skillen i `skill/problem-diary/` og endre linjen `REPO:` til ditt `owner/repo-navn`.
5. List enhetene dine i `diario/DEVICES.md`, med ett offisielt navn per enhet.

## Daglig bruk

Når et problem er løst, si til assistenten **"close and save"**. Avhengig av lengde brukes en av tre veier:

| Situasjon | Hva som skjer |
|---|---|
| Kort oppføring, fra chatten | Skillen lager en `claude.ai/code`-lenke med prompt og repo allerede utfylt. Åpne den og trykk Enter. |
| Lang oppføring, fra chatten | Skillen lager `.md`-filen med riktig navn og forteller deg nøyaktig hvilken mappe den skal i. Last den opp fra GitHub-nettstedet (*Add file > Upload files*). |
| Du er allerede i Claude Code | Den skriver filen direkte: `git pull`, commit, push. Ingen lengdebegrensning. |

Trykk deretter **Sync** i Claude Project, slik at chattene ser den nye oppføringen.

## Repostruktur

```
README.md                          indeks over de oversatte README-filene
CLAUDE.md                          instruksjoner til kodeagenten
docs/README.{lang}.md              README på hvert språk
diario/
  DEVICES.md                       offisielle enhetsnavn (ett navn per enhet)
  _TEMPLATE.md                     oppføringsmal
  {device-slug}/
    YYYY-MM-DD-short-title.md      én fil per løst problem
skill/problem-diary/               skillen "close and save"
  SKILL.md                         arbeidsflyt og regler
  scripts/build_link.py            bygger den forhåndsutfylte lenken, sjekker lengde og hemmeligheter
  assets/entry-template.md         malen skillen bruker (hold synkronisert med diario/_TEMPLATE.md)
```

Problemer som ikke hører til én bestemt enhet (et nettsted, en delt tjeneste) havner i `diario/general/`.

## Oppføringsformat

Hver oppføring har de samme faste overskriftene, slik at grep og KI-søk fungerer pålitelig: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, pluss de valgfrie **Do not** og **Related**. Innholdet skrives på ditt eget språk. Se `diario/_TEMPLATE.md`.

## Begrensninger og personvern

- En lenke bærer oppføringen i URL-en, så bare korte oppføringer bruker den. Lengre går via filen.
- Å åpne lenken og trykke Enter er fortsatt manuelt: det er ikke fullt automatisk, og ingen oppføring lagres uten at du ser den.
- Hver lagrede oppføring starter en Claude Code-nettøkt, som teller mot bruken av abonnementet ditt.
- Hold repoet privat. Oppføringene beskriver systemene dine i detalj.
- **Skriv aldri passord, tokens eller nøkler i en oppføring.** Skriv i stedet hvor de oppbevares.
- Hele repoet teller mot Projectets kunnskapskapasitet. Hundrevis av korte oppføringer får plass.
- GitHub-synkroniseringen i Projects kan av og til henge eller feile. Hvis chatten ikke ser en ny oppføring, trykk Sync igjen og sjekk.

## Lisens

Velg en lisens for forken din (MIT er et vanlig valg for et prosjekt som dette).
