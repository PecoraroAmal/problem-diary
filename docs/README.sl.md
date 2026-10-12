# Problem Diary

**Majhen sistem, neodvisen od umetne inteligence, ki jo uporabljate, za vodenje iskalnega dnevnika rešenih težav, da vaš pomočnik z umetno inteligenco preneha pozabljati.**

Jeziki: [vsi jeziki](../README.md)

## Zamisel

Če se vsak dan pogovarjate s pomočnikom z umetno inteligenco, vedno znova rešujete iste vrste težav, na številnih napravah in v številnih projektih. Pomočnik si podrobnosti ne zapomni, vi pa porabite več zahtevkov za obnovitev konteksta.

Ta projekt vodi dnevnik v preprostem Markdownu v repozitoriju Git. Ko je težava rešena, pomočnik napiše kratek zapis: **kaj je bila težava, kateri koraki so res delovali in zaključek** (ne celotnega klepeta in ne spodletelih poskusov). Naslednjič pomočnik najprej prebere dnevnik in odgovor najde z manj zahtevki.

Koristno je, če imate veliko projektov in naprav. Če postavljate le hitra, enkratna vprašanja, ga ne potrebujete.

## Kako deluje

```
 klepet s Claude ──"close and save"──▶ predizpolnjena povezava ──▶ Claude Code v spletu ──▶ commit + push
        ▲                                                                                     │
        └──────── Claude Project (repozitorij GitHub kot znanje, pritisnite Sync) ◀───────────┘
```

- **Pisanje:** Claude Code (terminal ali splet) ustvari zapis, požene `git pull`, commit in push.
- **Branje:** repozitorij se doda v Claude Project kot znanje. Po vsakem novem zapisu pritisnite ikono Sync.
- **Brez strežnika in brez žetonov v klepetu.** Dnevnik so samo datoteke v vašem lastnem repozitoriju, zato deluje s katerim koli orodjem, ki zna brati Markdown.

## Zahteve

- Lasten repozitorij GitHub (zasebni zadošča), ustvarjen iz te predloge.
- Račun Claude Pro, Max ali Team (potreben za Claude Code v spletu).
- GitHub, povezan z [claude.ai/code](https://claude.ai/code), z aplikacijo Claude, pooblaščeno za repozitorij dnevnika.
- GitHub, povezan s claude.ai (integracija GitHub), da lahko Project bere repozitorij.
- Za dolge zapise, ustvarjene iz klepeta: vključeni izvajanje kode in ustvarjanje datotek v nastavitvah Claude.

## Namestitev

1. Iz te predloge ustvarite **zaseben** repozitorij in klonirajte ali naložite te datoteke.
2. Povežite GitHub na claude.ai/code in pooblastite repozitorij (omogočite dostop samo do tega repozitorija).
3. Ustvarite Claude **Project**. V razdelku znanja pritisnite **+**, izberite **GitHub**, izberite repozitorij in datoteke, ki jih želite vključiti.
4. Namestite skill iz `skill/problem-diary/` in v njegovi vrstici `REPO:` nastavite svoj `owner/ime-repozitorija`.
5. Naštejte svoje naprave v `diario/DEVICES.md`, z enim uradnim imenom na napravo.

## Vsakdanja uporaba

Ko je težava rešena, pomočniku recite **"close and save"**. Glede na dolžino se uporabi ena od treh poti:

| Situacija | Kaj se zgodi |
|---|---|
| Kratek zapis, iz klepeta | Skill pripravi povezavo `claude.ai/code` z že izpolnjenim promptom in repozitorijem. Odprite jo in pritisnite Enter. |
| Dolg zapis, iz klepeta | Skill ustvari datoteko `.md` s pravilnim imenom in vam pove natančno mapo. Naložite jo na spletnem mestu GitHub (*Add file > Upload files*). |
| Ste že v Claude Code | Datoteko zapiše neposredno: `git pull`, commit, push. Brez omejitve dolžine. |

Nato pritisnite **Sync** v Claude Project, da klepeti vidijo nov zapis.

## Struktura repozitorija

```
README.md                          kazalo prevedenih README
CLAUDE.md                          navodila za kodirnega agenta
docs/README.{lang}.md              README v vsakem jeziku
diario/
  DEVICES.md                       uradna imena naprav (eno ime na napravo)
  _TEMPLATE.md                     predloga zapisa
  {device-slug}/
    YYYY-MM-DD-short-title.md      ena datoteka na rešeno težavo
skill/problem-diary/               skill "close and save"
  SKILL.md                         potek dela in pravila
  scripts/build_link.py            sestavi predizpolnjeno povezavo, preveri dolžino in skrivnosti
  assets/entry-template.md         predloga, ki jo uporablja skill (ohranite usklajeno z diario/_TEMPLATE.md)
```

Težave, ki ne spadajo k eni sami napravi (spletno mesto, skupna storitev), gredo v `diario/general/`.

## Oblika zapisa

Vsak zapis ima enake stalne naslove, da grep in iskanje z umetno inteligenco delujeta zanesljivo: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, poleg izbirnih **Do not** in **Related**. Vsebino pišete v svojem jeziku. Glejte `diario/_TEMPLATE.md`.

## Omejitve in zasebnost

- Povezava nosi zapis v naslovu URL, zato jo uporabljajo samo kratki zapisi. Daljši gredo prek datoteke.
- Odpiranje povezave in pritisk na Enter ostaneta ročna: ni povsem samodejno in noben zapis ni shranjen, ne da bi ga videli.
- Vsak shranjen zapis zažene spletno sejo Claude Code, ki se všteva v porabo vaše naročnine.
- Repozitorij naj ostane zaseben. Zapisi podrobno opisujejo vaše sisteme.
- **V zapis nikoli ne vpisujte gesel, žetonov ali ključev.** Namesto tega zapišite, kje so shranjeni.
- Celoten repozitorij se všteva v zmogljivost znanja Project. Stotine kratkih zapisov se prilega.
- Sinhronizacija GitHub v Projects lahko občasno zaostaja ali ne uspe. Če klepet ne vidi novega zapisa, znova pritisnite Sync in preverite.

## Licenca

Izberite licenco za svoj fork (MIT je za tak projekt pogosta izbira).
