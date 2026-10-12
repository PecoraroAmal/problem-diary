# Problem Diary

**Väike, kasutatavast tehisintellektist sõltumatu süsteem lahendatud probleemide otsitava päeviku pidamiseks, et sinu tehisintellekti assistent lõpetaks unustamise.**

Keeled: [kõik keeled](../README.md)

## Idee

Kui räägid tehisintellekti assistendiga iga päev, lahendad ikka ja jälle samu probleeme, paljudes seadmetes ja projektides. Assistent ei mäleta üksikasju ning sa kulutad mitu päringut konteksti taastamisele.

See projekt peab päevikut lihtsas Markdownis Giti hoidlas. Kui probleem on lahendatud, kirjutab assistent lühikese kirje: **mis probleem oli, millised sammud tõesti töötasid ja järeldus** (mitte kogu vestlust ega ebaõnnestunud katseid). Järgmisel korral loeb assistent esmalt päevikut ja leiab vastuse väiksema arvu päringutega.

See on kasulik, kui sul on palju projekte ja seadmeid. Kui esitad ainult kiireid üksikküsimusi, pole sul seda vaja.

## Kuidas see töötab

```
 vestlus Claude'iga ──"close and save"──▶ eeltäidetud link ──▶ Claude Code veebis ──▶ commit + push
        ▲                                                                                │
        └──────── Claude Project (GitHubi hoidla teadmistena, vajuta Sync) ◀─────────────┘
```

- **Kirjutamine:** Claude Code (terminal või veeb) loob kirje, käivitab `git pull`, teeb commiti ja pushi.
- **Lugemine:** hoidla lisatakse Claude Projectile teadmistena. Pärast iga uut kirjet vajuta Sync-ikooni.
- **Serverit ega tokeneid vestluses pole.** Päevik on vaid failid sinu enda hoidlas, seega töötab see iga tööriistaga, mis oskab Markdowni lugeda.

## Nõuded

- Oma GitHubi hoidla (privaatne sobib), loodud sellest mallist.
- Claude Pro, Max või Team konto (vajalik Claude Code'i jaoks veebis).
- GitHub ühendatud aadressil [claude.ai/code](https://claude.ai/code), Claude'i rakendus volitatud sinu päevikuhoidlale.
- GitHub ühendatud claude.ai-ga (GitHubi integratsioon), et Project saaks hoidlat lugeda.
- Vestlusest loodavate pikkade kirjete jaoks: koodi käivitamine ja failide loomine lubatud Claude'i seadetes.

## Seadistamine

1. Loo sellest mallist **privaatne** hoidla ning klooni või lae need failid üles.
2. Ühenda GitHub aadressil claude.ai/code ja volita hoidla (anna juurdepääs ainult sellele hoidlale).
3. Loo Claude'i **Project**. Teadmiste jaotises vajuta **+**, vali **GitHub**, vali oma hoidla ja kaasatavad failid.
4. Paigalda skill kaustast `skill/problem-diary/` ja muuda selle rida `REPO:` oma `owner/hoidla-nimi` vastu.
5. Loetle oma seadmed failis `diario/DEVICES.md`, iga seadme kohta üks ametlik nimi.

## Igapäevane kasutus

Kui probleem on lahendatud, ütle assistendile **"close and save"**. Sõltuvalt pikkusest kasutatakse ühte kolmest teest:

| Olukord | Mis juhtub |
|---|---|
| Lühike kirje, vestlusest | Skill valmistab ette lingi `claude.ai/code`, kus prompt ja hoidla on juba täidetud. Ava see ja vajuta Enter. |
| Pikk kirje, vestlusest | Skill loob `.md` faili õige nimega ja ütleb täpse kausta. Lae see üles GitHubi saidil (*Add file > Upload files*). |
| Oled juba Claude Code'is | See kirjutab faili otse: `git pull`, commit, push. Pikkuspiirangut pole. |

Seejärel vajuta Claude Projectis **Sync**, et vestlused näeksid uut kannet.

## Hoidla struktuur

```
README.md                          tõlgitud README-de register
CLAUDE.md                          juhised kodeerimisagendile
docs/README.{lang}.md              README igas keeles
diario/
  DEVICES.md                       seadmete ametlikud nimed (üks nimi seadme kohta)
  _TEMPLATE.md                     kirje mall
  {device-slug}/
    YYYY-MM-DD-short-title.md      üks fail lahendatud probleemi kohta
skill/problem-diary/               skill "close and save"
  SKILL.md                         töövoog ja reeglid
  scripts/build_link.py            koostab eeltäidetud lingi, kontrollib pikkust ja saladusi
  assets/entry-template.md         skilli kasutatav mall (hoia sünkroonis failiga diario/_TEMPLATE.md)
```

Probleemid, mis ei kuulu ühegi konkreetse seadme alla (veebisait, jagatud teenus), lähevad kausta `diario/general/`.

## Kirje vorming

Igal kirjel on samad püsipealkirjad, et grep ja tehisintellekti otsing töötaksid usaldusväärselt: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, pluss valikulised **Do not** ja **Related**. Sisu kirjutad oma keeles. Vaata `diario/_TEMPLATE.md`.

## Piirangud ja privaatsus

- Link kannab kirje URL-is, seega kasutavad seda ainult lühikesed kirjed. Pikemad lähevad faili kaudu.
- Lingi avamine ja Enteri vajutamine jääb käsitsi tegevuseks: see pole täielikult automaatne ning ühtegi kirjet ei salvestata nii, et sa seda ei näeks.
- Iga salvestatud kirje käivitab Claude Code'i veebisessiooni, mis läheb arvesse sinu tellimuse kasutuses.
- Hoia hoidla privaatsena. Kirjed kirjeldavad sinu süsteeme üksikasjalikult.
- **Ära kunagi kirjuta kirjesse paroole, tokeneid ega võtmeid.** Kirjuta selle asemel, kus need on hoiul.
- Kogu hoidla läheb arvesse Projecti teadmiste mahus. Sadu lühikesi kirjeid mahub.
- GitHubi sünkroonimine Projectides võib vahel venida või ebaõnnestuda. Kui vestlus ei näe uut kannet, vajuta uuesti Sync ja kontrolli.

## Litsents

Vali oma forgile litsents (MIT on sellise projekti jaoks tavaline valik).
