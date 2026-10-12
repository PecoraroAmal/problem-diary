# Problem Diary

**Mažytė sistema, nepriklausoma nuo naudojamo DI, skirta vesti ieškomą išspręstų problemų dienoraštį, kad jūsų DI asistentas nustotų pamiršti.**

Kalbos: [visos kalbos](../README.md)

## Idėja

Jei kasdien kalbatės su DI asistentu, vėl ir vėl sprendžiate tokias pačias problemas, daugelyje įrenginių ir projektų. Asistentas neprisimena smulkmenų, o jūs išleidžiate kelias užklausas kontekstui atkurti.

Šis projektas veda dienoraštį paprastu Markdown formatu Git saugykloje. Kai problema išspręsta, asistentas parašo trumpą įrašą: **kokia buvo problema, kurie žingsniai tikrai padėjo ir išvada** (ne visą pokalbį ir ne nesėkmingus bandymus). Kitą kartą asistentas pirmiausia perskaito dienoraštį ir atsakymą randa su mažiau užklausų.

Jis naudingas, jei turite daug projektų ir įrenginių. Jei užduodate tik greitus, pavienius klausimus, jo nereikia.

## Kaip tai veikia

```
 pokalbis su Claude ──"close and save"──▶ užpildyta nuoroda ──▶ Claude Code naršyklėje ──▶ commit + push
        ▲                                                                                      │
        └──────── Claude Project (GitHub saugykla kaip žinios, paspauskite Sync) ◀─────────────┘
```

- **Rašymas:** Claude Code (terminalas arba naršyklė) sukuria įrašą, paleidžia `git pull`, commit ir push.
- **Skaitymas:** saugykla pridedama prie Claude Project kaip žinios. Po kiekvieno naujo įrašo paspauskite Sync piktogramą.
- **Jokio serverio ir jokių tokenų pokalbyje.** Dienoraštis yra tik failai jūsų saugykloje, todėl veikia su bet kuria priemone, skaitančia Markdown.

## Reikalavimai

- Sava GitHub saugykla (tinka ir privati), sukurta iš šio šablono.
- Claude Pro, Max arba Team paskyra (reikalinga Claude Code naršyklėje).
- GitHub prijungtas prie [claude.ai/code](https://claude.ai/code), Claude programėlei suteiktas leidimas dienoraščio saugyklai.
- GitHub prijungtas prie claude.ai (GitHub integracija), kad Project galėtų skaityti saugyklą.
- Ilgiems įrašams, kuriami iš pokalbio: Claude nustatymuose įjungtas kodo vykdymas ir failų kūrimas.

## Nustatymas

1. Iš šio šablono sukurkite **privačią** saugyklą ir nukopijuokite arba įkelkite šiuos failus.
2. Prijunkite GitHub svetainėje claude.ai/code ir suteikite leidimą saugyklai (suteikite prieigą tik šiai saugyklai).
3. Sukurkite Claude **Project**. Žinių skiltyje paspauskite **+**, pasirinkite **GitHub**, pažymėkite savo saugyklą ir įtrauktinus failus.
4. Įdiekite skill iš `skill/problem-diary/` ir jo eilutėje `REPO:` nurodykite savo `owner/saugyklos-pavadinimas`.
5. Išvardykite savo įrenginius faile `diario/DEVICES.md`, kiekvienam įrenginiui po vieną oficialų pavadinimą.

## Kasdienis naudojimas

Kai problema išspręsta, pasakykite asistentui **"close and save"**. Pagal ilgį naudojamas vienas iš trijų kelių:

| Situacija | Kas vyksta |
|---|---|
| Trumpas įrašas, iš pokalbio | Skill paruošia `claude.ai/code` nuorodą su jau užpildytu promptu ir saugykla. Atidarykite ją ir paspauskite Enter. |
| Ilgas įrašas, iš pokalbio | Skill sukuria `.md` failą su tinkamu pavadinimu ir pasako tikslų aplanką. Įkelkite jį GitHub svetainėje (*Add file > Upload files*). |
| Jau esate Claude Code | Jis įrašo failą tiesiogiai: `git pull`, commit, push. Be ilgio apribojimo. |

Tada paspauskite **Sync** Claude Project, kad pokalbiai matytų naują įrašą.

## Saugyklos struktūra

```
README.md                          išverstų README rodyklė
CLAUDE.md                          nurodymai kodavimo agentui
docs/README.{lang}.md              README kiekviena kalba
diario/
  DEVICES.md                       oficialūs įrenginių pavadinimai (vienas pavadinimas įrenginiui)
  _TEMPLATE.md                     įrašo šablonas
  {device-slug}/
    YYYY-MM-DD-short-title.md      vienas failas kiekvienai išspręstai problemai
skill/problem-diary/               skill "close and save"
  SKILL.md                         darbo eiga ir taisyklės
  scripts/build_link.py            sudaro užpildytą nuorodą, tikrina ilgį ir paslaptis
  assets/entry-template.md         skill naudojamas šablonas (laikykite suderintą su diario/_TEMPLATE.md)
```

Problemos, nepriklausančios jokiam konkrečiam įrenginiui (svetainė, bendra paslauga), keliauja į `diario/general/`.

## Įrašo formatas

Kiekvienas įrašas turi tas pačias pastovias antraštes, kad grep ir DI paieška veiktų patikimai: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, taip pat neprivalomi **Do not** ir **Related**. Turinį rašote sava kalba. Žr. `diario/_TEMPLATE.md`.

## Apribojimai ir privatumas

- Nuoroda neša įrašą URL, todėl ją naudoja tik trumpi įrašai. Ilgesni eina per failą.
- Nuorodos atidarymas ir Enter paspaudimas lieka rankiniai: tai nėra visiškai automatiška ir joks įrašas neišsaugomas jums jo nematant.
- Kiekvienas išsaugotas įrašas paleidžia Claude Code naršyklės sesiją, kuri įskaičiuojama į jūsų prenumeratos naudojimą.
- Laikykite saugyklą privačią. Įrašai išsamiai aprašo jūsų sistemas.
- **Niekada nerašykite į įrašą slaptažodžių, tokenų ar raktų.** Parašykite, kur jie saugomi.
- Visa saugykla įskaičiuojama į Project žinių talpą. Telpa šimtai trumpų įrašų.
- GitHub sinchronizavimas Projects kartais vėluoja arba nepavyksta. Jei pokalbis nemato naujo įrašo, dar kartą paspauskite Sync ir patikrinkite.

## Licencija

Pasirinkite licenciją savo fork (MIT yra įprastas pasirinkimas tokiam projektui).
