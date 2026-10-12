# Problem Diary

**Et lille, AI-uafhængigt system til at føre en søgbar dagbog over problemer, du har løst, så din AI-assistent holder op med at glemme.**

Sprog: [alle sprog](../README.md)

## Idéen

Hvis du taler med en AI-assistent hver dag, løser du de samme slags problemer igen og igen, på mange enheder og i mange projekter. Assistenten husker ikke detaljerne, og du bruger flere forespørgsler på at genskabe konteksten.

Dette projekt fører en dagbog i almindelig Markdown i et Git-repository. Når et problem er løst, skriver assistenten en kort post: **hvad problemet var, de trin der faktisk virkede, og konklusionen** (ikke hele chatten og ikke de mislykkede forsøg). Næste gang læser assistenten først dagbogen og finder svaret med færre forespørgsler.

Det er nyttigt, hvis du har mange projekter og enheder. Stiller du kun hurtige, enkeltstående spørgsmål, har du ikke brug for det.

## Sådan fungerer det

```
 chat med Claude ──"close and save"──▶ udfyldt link ──▶ Claude Code på nettet ──▶ commit + push
        ▲                                                                              │
        └──────── Claude Project (GitHub-repo som viden, tryk Sync) ◀──────────────────┘
```

- **Skrivning:** Claude Code (terminal eller web) opretter posten, kører `git pull`, committer og pusher.
- **Læsning:** repoet tilføjes til et Claude Project som viden. Efter hver ny post trykker du på Sync-ikonet.
- **Ingen server og ingen tokens i chatten.** Dagbogen er blot filer i dit eget repo, så den virker med ethvert værktøj, der kan læse Markdown.

## Krav

- Dit eget GitHub-repository (privat er fint) oprettet fra denne skabelon.
- En Claude Pro-, Max- eller Team-konto (kræves til Claude Code på nettet).
- GitHub forbundet på [claude.ai/code](https://claude.ai/code), med Claude-appen godkendt til dit dagbogsrepo.
- GitHub forbundet til claude.ai (GitHub-integrationen), så et Project kan læse repoet.
- Til lange poster oprettet fra chatten: kodeudførelse og filoprettelse slået til i Claudes indstillinger.

## Opsætning

1. Opret et **privat** repo fra denne skabelon og klon eller upload filerne.
2. Forbind GitHub på claude.ai/code og godkend repoet (giv kun adgang til dette repo).
3. Opret et Claude **Project**. I vidensektionen trykker du på **+**, vælger **GitHub** og markerer dit repo og de filer, der skal med.
4. Installer skillen i `skill/problem-diary/` og ret linjen `REPO:` til dit `owner/repo-navn`.
5. Skriv dine enheder i `diario/DEVICES.md`, med ét officielt navn pr. enhed.

## Daglig brug

Når et problem er løst, så sig til assistenten **"close and save"**. Afhængigt af længden bruges en af tre veje:

| Situation | Hvad der sker |
|---|---|
| Kort post, fra chatten | Skillen laver et `claude.ai/code`-link med prompt og repo allerede udfyldt. Åbn det og tryk Enter. |
| Lang post, fra chatten | Skillen opretter `.md`-filen med det rigtige navn og fortæller dig præcis, hvilken mappe den skal i. Upload den fra GitHubs hjemmeside (*Add file > Upload files*). |
| Du er allerede i Claude Code | Den skriver filen direkte: `git pull`, commit, push. Ingen længdegrænse. |

Tryk derefter på **Sync** i Claude Project, så chattene kan se den nye post.

## Repostruktur

```
README.md                          indeks over de oversatte README-filer
CLAUDE.md                          instruktioner til kodeagenten
docs/README.{lang}.md              README på hvert sprog
diario/
  DEVICES.md                       officielle enhedsnavne (ét navn pr. enhed)
  _TEMPLATE.md                     postskabelon
  {device-slug}/
    YYYY-MM-DD-short-title.md      én fil pr. løst problem
skill/problem-diary/               skillen "close and save"
  SKILL.md                         arbejdsgang og regler
  scripts/build_link.py            bygger det udfyldte link, kontrollerer længde og hemmeligheder
  assets/entry-template.md         skabelon brugt af skillen (hold den synkroniseret med diario/_TEMPLATE.md)
```

Problemer, der ikke hører til en bestemt enhed (en hjemmeside, en delt tjeneste), kommer i `diario/general/`.

## Postformat

Hver post har de samme faste overskrifter, så grep og AI-søgning virker pålideligt: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus de valgfrie **Do not** og **Related**. Indholdet skrives på dit eget sprog. Se `diario/_TEMPLATE.md`.

## Begrænsninger og privatliv

- Et link bærer posten i URL'en, så kun korte poster bruger det. Længere poster går via filen.
- At åbne linket og trykke Enter er stadig manuelt: det er ikke fuldt automatisk, og ingen post gemmes, uden at du ser den.
- Hver gemt post starter en Claude Code-websession, som tæller med i dit abonnements forbrug.
- Hold repoet privat. Posterne beskriver dine systemer i detaljer.
- **Skriv aldrig adgangskoder, tokens eller nøgler i en post.** Skriv i stedet, hvor de opbevares.
- Hele repoet tæller med i Projectets videnskapacitet. Hundredvis af korte poster kan være der.
- GitHub-synkroniseringen i Projects kan til tider halte eller fejle. Hvis chatten ikke kan se en ny post, så tryk Sync igen og kontroller.

## Licens

Vælg en licens til din fork (MIT er et almindeligt valg til et projekt som dette).
