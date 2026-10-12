# Problem Diary

**Egy apró, a használt MI-től független rendszer a megoldott problémák kereshető naplójának vezetésére, hogy az MI-asszisztensed végre ne felejtsen.**

Nyelvek: [minden nyelv](../README.md)

## Az ötlet

Ha naponta beszélsz egy MI-asszisztenssel, újra és újra ugyanolyan problémákat oldasz meg, sok eszközön és sok projektben. Az asszisztens nem emlékszik a részletekre, te pedig több kérést elhasználsz a háttér helyreállítására.

Ez a projekt egyszerű Markdownban vezet naplót egy Git-tárolóban. Amikor egy probléma megoldódott, az asszisztens rövid bejegyzést ír: **mi volt a probléma, mely lépések működtek valójában, és mi a végkövetkeztetés** (nem a teljes csevegés, és nem a sikertelen kísérletek). Legközelebb az asszisztens először a naplót olvassa el, és kevesebb kéréssel találja meg a választ.

Akkor hasznos, ha sok projekted és eszközöd van. Ha csak gyors, különálló kérdéseket teszel fel, nincs rá szükséged.

## Hogyan működik

```
 csevegés Claude-dal ──"close and save"──▶ előre kitöltött link ──▶ Claude Code a weben ──▶ commit + push
        ▲                                                                                      │
        └──────── Claude Project (GitHub-tároló tudásként, nyomd meg a Sync-et) ◀──────────────┘
```

- **Írás:** a Claude Code (terminál vagy web) létrehozza a bejegyzést, lefuttatja a `git pull`-t, commitol és pushol.
- **Olvasás:** a tárolót tudásként hozzáadod egy Claude Projecthez. Minden új bejegyzés után nyomd meg a Sync ikont.
- **Nincs szerver, és nincs token a csevegésben.** A napló csak fájlok a saját tárolódban, így bármely Markdownt olvasó eszközzel működik.

## Követelmények

- Saját GitHub-tároló (privát is megfelel), ebből a sablonból létrehozva.
- Claude Pro, Max vagy Team fiók (a weben futó Claude Code-hoz szükséges).
- A GitHub összekötve a [claude.ai/code](https://claude.ai/code) oldalon, a Claude alkalmazás engedélyezve a naplótárolón.
- A GitHub összekötve a claude.ai-jal (GitHub-integráció), hogy egy Project olvashassa a tárolót.
- A csevegésből létrehozott hosszú bejegyzésekhez: a kódfuttatás és a fájlkészítés be van kapcsolva a Claude beállításaiban.

## Beállítás

1. Hozz létre ebből a sablonból egy **privát** tárolót, és klónozd vagy töltsd fel ezeket a fájlokat.
2. Kapcsold össze a GitHubot a claude.ai/code oldalon, és engedélyezd a tárolót (csak ehhez a tárolóhoz adj hozzáférést).
3. Hozz létre egy Claude **Projectet**. A tudás szakaszban nyomd meg a **+** gombot, válaszd a **GitHub** lehetőséget, jelöld ki a tárolót és a bevonandó fájlokat.
4. Telepítsd a `skill/problem-diary/` mappában lévő skillt, és a `REPO:` sorát írd át a saját `owner/tarolo-neve` értékedre.
5. Sorold fel az eszközeidet a `diario/DEVICES.md` fájlban, eszközönként egy hivatalos névvel.

## Napi használat

Amikor egy probléma megoldódott, mondd az asszisztensnek: **"close and save"**. A hossztól függően három út közül az egyiket használja:

| Helyzet | Mi történik |
|---|---|
| Rövid bejegyzés, csevegésből | A skill elkészít egy `claude.ai/code` linket, amelyben a prompt és a tároló már ki van töltve. Nyisd meg, és nyomj Entert. |
| Hosszú bejegyzés, csevegésből | A skill létrehozza a `.md` fájlt a megfelelő névvel, és megmondja a pontos mappát. Töltsd fel a GitHub oldalán (*Add file > Upload files*). |
| Már a Claude Code-ban vagy | Közvetlenül írja a fájlt: `git pull`, commit, push. Nincs hosszkorlát. |

Ezután nyomd meg a **Sync** gombot a Claude Projectben, hogy a csevegések lássák az új bejegyzést.

## A tároló szerkezete

```
README.md                          a lefordított README-k jegyzéke
CLAUDE.md                          utasítások a kódoló ágensnek
docs/README.{lang}.md              README minden nyelven
diario/
  DEVICES.md                       az eszközök hivatalos nevei (eszközönként egy név)
  _TEMPLATE.md                     bejegyzéssablon
  {device-slug}/
    YYYY-MM-DD-short-title.md      egy fájl megoldott problémánként
skill/problem-diary/               a "close and save" skill
  SKILL.md                         munkafolyamat és szabályok
  scripts/build_link.py            összeállítja az előre kitöltött linket, ellenőrzi a hosszt és a titkokat
  assets/entry-template.md         a skill által használt sablon (tartsd szinkronban a diario/_TEMPLATE.md-vel)
```

Azok a problémák, amelyek nem tartoznak egyetlen eszközhöz sem (weboldal, megosztott szolgáltatás), a `diario/general/` mappába kerülnek.

## A bejegyzés formátuma

Minden bejegyzés ugyanazokat a rögzített címsorokat használja, hogy a grep és az MI-keresés megbízhatóan működjön: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, valamint az opcionális **Do not** és **Related**. A tartalmat a saját nyelveden írod. Lásd: `diario/_TEMPLATE.md`.

## Korlátok és adatvédelem

- A link az URL-ben viszi a bejegyzést, ezért csak a rövid bejegyzések használják. A hosszabbak a fájlon át mennek.
- A link megnyitása és az Enter megnyomása továbbra is kézi: nem teljesen automatikus, és egy bejegyzés sem mentődik úgy, hogy ne látnád.
- Minden mentett bejegyzés elindít egy Claude Code webes munkamenetet, amely beleszámít az előfizetésed használatába.
- Tartsd privátként a tárolót. A bejegyzések részletesen leírják a rendszereidet.
- **Soha ne írj jelszót, tokent vagy kulcsot a bejegyzésbe.** Írd le inkább, hol vannak tárolva.
- A teljes tároló beleszámít a Project tudáskapacitásába. Több száz rövid bejegyzés elfér.
- A GitHub-szinkronizáció a Projectekben olykor késhet vagy meghiúsulhat. Ha a csevegés nem látja az új bejegyzést, nyomd meg újra a Sync-et, és ellenőrizd.

## Licenc

Válassz licencet a forkodhoz (az MIT gyakori választás egy ilyen projekthez).
