# Problem Diary

**Mali sustav, neovisan o AI-ju koji koristite, za vođenje pretraživog dnevnika riješenih problema, kako bi vaš AI asistent prestao zaboravljati.**

Jezici: [svi jezici](../README.md)

## Ideja

Ako svaki dan razgovarate s AI asistentom, iznova rješavate iste vrste problema, na mnogo uređaja i u mnogo projekata. Asistent ne pamti pojedinosti, a vi trošite nekoliko upita na ponovno uspostavljanje konteksta.

Ovaj projekt vodi dnevnik u običnom Markdownu u Git repozitoriju. Kad je problem riješen, asistent napiše kratak zapis: **što je bio problem, koji su koraci doista upalili i zaključak** (ne cijeli chat i ne neuspjeli pokušaji). Sljedeći put asistent najprije pročita dnevnik i odgovor pronađe s manje upita.

Koristan je ako imate mnogo projekata i uređaja. Ako postavljate samo brza, jednokratna pitanja, ne treba vam.

## Kako radi

```
 chat s Claudeom ──"close and save"──▶ unaprijed ispunjena poveznica ──▶ Claude Code na webu ──▶ commit + push
        ▲                                                                                          │
        └──────── Claude Project (GitHub repozitorij kao znanje, pritisnite Sync) ◀────────────────┘
```

- **Pisanje:** Claude Code (terminal ili web) stvara zapis, pokreće `git pull`, commit i push.
- **Čitanje:** repozitorij se dodaje u Claude Project kao znanje. Nakon svakog novog zapisa pritisnite ikonu Sync.
- **Nema poslužitelja ni tokena u chatu.** Dnevnik su samo datoteke u vašem repozitoriju, pa radi s bilo kojim alatom koji čita Markdown.

## Zahtjevi

- Vlastiti GitHub repozitorij (privatni je u redu) stvoren iz ovog predloška.
- Račun Claude Pro, Max ili Team (potreban za Claude Code na webu).
- GitHub povezan na [claude.ai/code](https://claude.ai/code), s aplikacijom Claude ovlaštenom za repozitorij dnevnika.
- GitHub povezan s claude.ai (GitHub integracija) kako bi Project mogao čitati repozitorij.
- Za duge zapise stvorene iz chata: uključeno izvršavanje koda i stvaranje datoteka u postavkama Claudea.

## Postavljanje

1. Iz ovog predloška stvorite **privatni** repozitorij i klonirajte ili učitajte ove datoteke.
2. Povežite GitHub na claude.ai/code i ovlastite repozitorij (dajte pristup samo ovom repozitoriju).
3. Stvorite Claude **Project**. U odjeljku znanja pritisnite **+**, odaberite **GitHub**, odaberite repozitorij i datoteke koje želite uključiti.
4. Instalirajte skill iz `skill/problem-diary/` i u njegovu retku `REPO:` upišite svoj `owner/naziv-repozitorija`.
5. Navedite svoje uređaje u `diario/DEVICES.md`, s jednim službenim nazivom po uređaju.

## Svakodnevna uporaba

Kad je problem riješen, recite asistentu **"close and save"**. Ovisno o duljini koristi se jedan od tri puta:

| Situacija | Što se događa |
|---|---|
| Kratak zapis, iz chata | Skill priprema poveznicu `claude.ai/code` s već ispunjenim promptom i repozitorijem. Otvorite je i pritisnite Enter. |
| Dug zapis, iz chata | Skill stvara datoteku `.md` s točnim nazivom i kaže vam točnu mapu. Učitajte je na web-mjestu GitHub (*Add file > Upload files*). |
| Već ste u Claude Codeu | Datoteku piše izravno: `git pull`, commit, push. Bez ograničenja duljine. |

Zatim pritisnite **Sync** u Claude Projectu kako bi chatovi vidjeli novi zapis.

## Struktura repozitorija

```
README.md                          kazalo prevedenih README datoteka
CLAUDE.md                          upute za agenta za kodiranje
docs/README.{lang}.md              README na svakom jeziku
diario/
  DEVICES.md                       službeni nazivi uređaja (jedan naziv po uređaju)
  _TEMPLATE.md                     predložak zapisa
  {device-slug}/
    YYYY-MM-DD-short-title.md      jedna datoteka po riješenom problemu
skill/problem-diary/               skill "close and save"
  SKILL.md                         tijek rada i pravila
  scripts/build_link.py            gradi unaprijed ispunjenu poveznicu, provjerava duljinu i tajne podatke
  assets/entry-template.md         predložak koji koristi skill (držite usklađenim s diario/_TEMPLATE.md)
```

Problemi koji ne pripadaju nijednom uređaju (web-mjesto, zajednička usluga) idu u `diario/general/`.

## Format zapisa

Svaki zapis ima iste stalne naslove kako bi grep i AI pretraživanje radili pouzdano: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, uz neobavezne **Do not** i **Related**. Sadržaj pišete na svojem jeziku. Pogledajte `diario/_TEMPLATE.md`.

## Ograničenja i privatnost

- Poveznica nosi zapis u URL-u, pa je koriste samo kratki zapisi. Dulji idu preko datoteke.
- Otvaranje poveznice i pritisak na Enter ostaju ručni: nije potpuno automatski i nijedan zapis nije spremljen a da ga ne vidite.
- Svaki spremljeni zapis pokreće web-sesiju Claude Codea, koja se računa u potrošnju vaše pretplate.
- Držite repozitorij privatnim. Zapisi detaljno opisuju vaše sustave.
- **Nikad ne upisujte lozinke, tokene ni ključeve u zapis.** Umjesto toga napišite gdje su pohranjeni.
- Cijeli repozitorij ulazi u kapacitet znanja Projecta. Stotine kratkih zapisa stane.
- GitHub sinkronizacija u Projectsima povremeno kasni ili ne uspije. Ako chat ne vidi novi zapis, ponovno pritisnite Sync i provjerite.

## Licenca

Odaberite licencu za svoj fork (MIT je uobičajen izbor za ovakav projekt).
