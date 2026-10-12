# Problem Diary

**Malý systém nezávislý od AI, ktorú používate, na vedenie prehľadávateľného denníka vyriešených problémov, aby váš AI asistent prestal zabúdať.**

Jazyky: [všetky jazyky](../README.md)

## Myšlienka

Ak denne hovoríte s AI asistentom, riešite stále dokola rovnaké druhy problémov, na mnohých zariadeniach a v mnohých projektoch. Asistent si podrobnosti nepamätá a vy miniete niekoľko požiadaviek na obnovenie kontextu.

Tento projekt vedie denník v obyčajnom Markdowne v repozitári Git. Keď je problém vyriešený, asistent napíše krátky záznam: **v čom problém spočíval, ktoré kroky naozaj zabrali a záver** (nie celý chat a nie neúspešné pokusy). Nabudúce asistent najprv prečíta denník a odpoveď nájde s menším počtom požiadaviek.

Hodí sa, ak máte veľa projektov a zariadení. Ak kladiete len rýchle, jednorazové otázky, nepotrebujete ho.

## Ako to funguje

```
 chat s Claude ──"close and save"──▶ predvyplnený odkaz ──▶ Claude Code na webe ──▶ commit + push
        ▲                                                                              │
        └──────── Claude Project (repozitár GitHub ako znalosti, stlačte Sync) ◀───────┘
```

- **Zápis:** Claude Code (terminál alebo web) vytvorí záznam, spustí `git pull`, commit a push.
- **Čítanie:** repozitár sa pridá do Claude Project ako znalosti. Po každom novom zázname stlačte ikonu Sync.
- **Žiadny server a žiadne tokeny v chate.** Denník sú len súbory vo vašom vlastnom repozitári, takže funguje s každým nástrojom, ktorý číta Markdown.

## Požiadavky

- Vlastný repozitár GitHub (súkromný stačí) vytvorený z tejto šablóny.
- Účet Claude Pro, Max alebo Team (potrebný pre Claude Code na webe).
- GitHub prepojený s [claude.ai/code](https://claude.ai/code), s aplikáciou Claude autorizovanou pre váš repozitár denníka.
- GitHub prepojený s claude.ai (integrácia GitHub), aby Project mohol čítať repozitár.
- Pre dlhé záznamy vytvárané z chatu: zapnuté spúšťanie kódu a vytváranie súborov v nastaveniach Claude.

## Nastavenie

1. Vytvorte z tejto šablóny **súkromný** repozitár a naklonujte alebo nahrajte tieto súbory.
2. Prepojte GitHub na claude.ai/code a autorizujte repozitár (povoľte prístup len k tomuto repozitáru).
3. Vytvorte Claude **Project**. V sekcii znalostí stlačte **+**, vyberte **GitHub**, zvoľte repozitár a súbory, ktoré zahrnúť.
4. Nainštalujte skill z `skill/problem-diary/` a upravte jeho riadok `REPO:` na vaše `owner/nazov-repozitara`.
5. Vypíšte svoje zariadenia do `diario/DEVICES.md`, s jedným oficiálnym názvom na zariadenie.

## Každodenné použitie

Keď je problém vyriešený, povedzte asistentovi **"close and save"**. Podľa dĺžky sa použije jedna z troch ciest:

| Situácia | Čo sa stane |
|---|---|
| Krátky záznam, z chatu | Skill pripraví odkaz `claude.ai/code` s už vyplneným promptom a repozitárom. Otvorte ho a stlačte Enter. |
| Dlhý záznam, z chatu | Skill vytvorí súbor `.md` so správnym názvom a oznámi presný priečinok. Nahrajte ho na webe GitHub (*Add file > Upload files*). |
| Už ste v Claude Code | Súbor zapíše priamo: `git pull`, commit, push. Bez obmedzenia dĺžky. |

Potom stlačte **Sync** v Claude Project, aby chaty videli nový záznam.

## Štruktúra repozitára

```
README.md                          register preložených README
CLAUDE.md                          pokyny pre kódovacieho agenta
docs/README.{lang}.md              README v každom jazyku
diario/
  DEVICES.md                       oficiálne názvy zariadení (jeden názov na zariadenie)
  _TEMPLATE.md                     šablóna záznamu
  {device-slug}/
    YYYY-MM-DD-short-title.md      jeden súbor na vyriešený problém
skill/problem-diary/               skill "close and save"
  SKILL.md                         postup a pravidlá
  scripts/build_link.py            zostaví predvyplnený odkaz, skontroluje dĺžku a tajné údaje
  assets/entry-template.md         šablóna používaná skillom (udržiavajte zhodnú s diario/_TEMPLATE.md)
```

Problémy, ktoré nepatria k jedinému zariadeniu (web, zdieľaná služba), patria do `diario/general/`.

## Formát záznamu

Každý záznam má rovnaké pevné nadpisy, aby grep a vyhľadávanie pomocou AI fungovali spoľahlivo: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus voliteľné **Do not** a **Related**. Obsah píšete vo svojom jazyku. Pozri `diario/_TEMPLATE.md`.

## Obmedzenia a súkromie

- Odkaz nesie záznam v URL, takže ho používajú len krátke záznamy. Dlhšie idú cez súbor.
- Otvorenie odkazu a stlačenie Enter zostáva manuálne: nie je to plne automatické a žiadny záznam sa neuloží, kým ho neuvidíte.
- Každý uložený záznam spustí webovú reláciu Claude Code, ktorá sa počíta do využitia vášho predplatného.
- Udržiavajte repozitár súkromný. Záznamy podrobne opisujú vaše systémy.
- **Nikdy nevkladajte do záznamu heslá, tokeny ani kľúče.** Napíšte namiesto toho, kde sú uložené.
- Celý repozitár sa počíta do kapacity znalostí Project. Zmestia sa stovky krátkych záznamov.
- Synchronizácia GitHub v Projects môže občas váhať alebo zlyhať. Ak chat nový záznam nevidí, stlačte znova Sync a skontrolujte.

## Licencia

Zvoľte licenciu pre svoj fork (MIT je pre takýto projekt bežná voľba).
