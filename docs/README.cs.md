# Problem Diary

**Malý systém nezávislý na tom, kterou AI používáte, pro vedení prohledávatelného deníku vyřešených problémů, aby váš AI asistent přestal zapomínat.**

Jazyky: [všechny jazyky](../README.md)

## Myšlenka

Pokud denně mluvíte s AI asistentem, řešíte stále dokola stejné druhy problémů, na mnoha zařízeních a v mnoha projektech. Asistent si podrobnosti nepamatuje a vy utratíte několik dotazů za obnovení kontextu.

Tento projekt vede deník v prostém Markdownu v repozitáři Git. Když je problém vyřešen, asistent napíše krátký záznam: **v čem problém spočíval, které kroky skutečně zabraly a závěr** (ne celý chat a ne neúspěšné pokusy). Příště asistent nejdřív přečte deník a odpověď najde s menším počtem dotazů.

Hodí se, pokud máte mnoho projektů a zařízení. Pokud klademe jen rychlé, jednorázové otázky, nepotřebujete ho.

## Jak to funguje

```
 chat s Claude ──"close and save"──▶ předvyplněný odkaz ──▶ Claude Code na webu ──▶ commit + push
        ▲                                                                              │
        └──────── Claude Project (repozitář GitHub jako znalosti, stiskněte Sync) ◀────┘
```

- **Zápis:** Claude Code (terminál nebo web) vytvoří záznam, spustí `git pull`, commit a push.
- **Čtení:** repozitář se přidá do Claude Project jako znalosti. Po každém novém záznamu stiskněte ikonu Sync.
- **Žádný server a žádné tokeny v chatu.** Deník jsou jen soubory ve vašem vlastním repozitáři, takže funguje s jakýmkoli nástrojem, který čte Markdown.

## Požadavky

- Vlastní repozitář GitHub (soukromý stačí) vytvořený z této šablony.
- Účet Claude Pro, Max nebo Team (nutný pro Claude Code na webu).
- GitHub propojený s [claude.ai/code](https://claude.ai/code), s aplikací Claude autorizovanou pro váš repozitář deníku.
- GitHub propojený s claude.ai (integrace GitHub), aby Project mohl číst repozitář.
- Pro dlouhé záznamy vytvářené z chatu: zapnuté spouštění kódu a vytváření souborů v nastavení Claude.

## Nastavení

1. Vytvořte z této šablony **soukromý** repozitář a naklonujte nebo nahrajte tyto soubory.
2. Propojte GitHub na claude.ai/code a autorizujte repozitář (povolte přístup jen k tomuto repozitáři).
3. Vytvořte Claude **Project**. V sekci znalostí stiskněte **+**, vyberte **GitHub**, zvolte repozitář a soubory, které zahrnout.
4. Nainstalujte skill z `skill/problem-diary/` a upravte jeho řádek `REPO:` na vaše `owner/nazev-repozitare`.
5. Vypište svá zařízení do `diario/DEVICES.md`, s jedním oficiálním názvem na zařízení.

## Každodenní použití

Když je problém vyřešen, řekněte asistentovi **"close and save"**. Podle délky se použije jedna ze tří cest:

| Situace | Co se stane |
|---|---|
| Krátký záznam, z chatu | Skill připraví odkaz `claude.ai/code` s již vyplněným promptem a repozitářem. Otevřete ho a stiskněte Enter. |
| Dlouhý záznam, z chatu | Skill vytvoří soubor `.md` se správným názvem a sdělí přesnou složku. Nahrajte ho na webu GitHub (*Add file > Upload files*). |
| Už jste v Claude Code | Soubor zapíše přímo: `git pull`, commit, push. Bez omezení délky. |

Poté stiskněte **Sync** v Claude Project, aby chaty viděly nový záznam.

## Struktura repozitáře

```
README.md                          rejstřík přeložených README
CLAUDE.md                          pokyny pro kódovacího agenta
docs/README.{lang}.md              README v každém jazyce
diario/
  DEVICES.md                       oficiální názvy zařízení (jeden název na zařízení)
  _TEMPLATE.md                     šablona záznamu
  {device-slug}/
    YYYY-MM-DD-short-title.md      jeden soubor na vyřešený problém
skill/problem-diary/               skill "close and save"
  SKILL.md                         postup a pravidla
  scripts/build_link.py            sestaví předvyplněný odkaz, zkontroluje délku a tajné údaje
  assets/entry-template.md         šablona používaná skillem (udržujte shodnou s diario/_TEMPLATE.md)
```

Problémy, které nepatří k jedinému zařízení (web, sdílená služba), patří do `diario/general/`.

## Formát záznamu

Každý záznam má stejné pevné nadpisy, aby grep a vyhledávání pomocí AI fungovaly spolehlivě: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus volitelné **Do not** a **Related**. Obsah píšete ve svém jazyce. Viz `diario/_TEMPLATE.md`.

## Omezení a soukromí

- Odkaz nese záznam v URL, takže ho používají jen krátké záznamy. Delší jdou přes soubor.
- Otevření odkazu a stisknutí Enter zůstává ruční: není to plně automatické a žádný záznam se neuloží, aniž byste ho viděli.
- Každý uložený záznam spustí webovou relaci Claude Code, která se počítá do využití vašeho předplatného.
- Udržujte repozitář soukromý. Záznamy podrobně popisují vaše systémy.
- **Nikdy nevkládejte do záznamu hesla, tokeny ani klíče.** Napište místo toho, kde jsou uloženy.
- Celý repozitář se počítá do kapacity znalostí Project. Vejdou se stovky krátkých záznamů.
- Synchronizace GitHub v Projects může občas váznout nebo selhat. Pokud chat nový záznam nevidí, stiskněte znovu Sync a zkontrolujte.

## Licence

Zvolte licenci pro svůj fork (MIT je pro takový projekt běžná volba).
