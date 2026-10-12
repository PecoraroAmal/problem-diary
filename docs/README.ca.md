# Problem Diary

**Un petit sistema, independent de la IA que facis servir, per portar un diari consultable dels problemes que has resolt, de manera que el teu assistent deixi d'oblidar.**

Llengües: [totes les llengües](../README.md)

## La idea

Si parles amb un assistent d'IA cada dia, resols una vegada i una altra els mateixos tipus de problemes, en molts dispositius i projectes. L'assistent no recorda els detalls i gastes diverses peticions a reconstruir el context.

Aquest projecte guarda un diari en Markdown senzill dins d'un repositori Git. Quan es resol un problema, l'assistent escriu una entrada breu: **quin era el problema, els passos que realment han funcionat i la conclusió** (no tota la conversa ni els intents fallits). La propera vegada, l'assistent llegeix primer el diari i troba la resposta amb menys peticions.

És útil si tens molts projectes i dispositius. Si només fas preguntes ràpides i puntuals, no ho necessites.

## Com funciona

```
 xat amb Claude ──"close and save"──▶ enllaç emplenat ──▶ Claude Code al web ──▶ commit + push
        ▲                                                                              │
        └──────── Project de Claude (repo de GitHub com a coneixement, prem Sync) ◀────┘
```

- **Escriptura:** Claude Code (terminal o web) crea l'entrada, executa `git pull`, fa commit i push.
- **Lectura:** el repo s'afegeix a un Project de Claude com a coneixement. Després de cada entrada nova, prem la icona Sync.
- **Sense servidor i sense tokens al xat.** El diari són només fitxers al teu propi repo, així que funciona amb qualsevol eina que llegeixi Markdown.

## Requisits

- El teu propi repositori de GitHub (pot ser privat) creat a partir d'aquesta plantilla.
- Un compte Claude Pro, Max o Team (necessari per a Claude Code al web).
- GitHub connectat a [claude.ai/code](https://claude.ai/code), amb l'aplicació de Claude autoritzada al repo del diari.
- GitHub connectat a claude.ai (la integració amb GitHub) perquè un Project pugui llegir el repo.
- Per a les entrades llargues creades des del xat: execució de codi i creació de fitxers activades a la configuració de Claude.

## Configuració

1. Crea un repo **privat** a partir d'aquesta plantilla i clona o puja aquests fitxers.
2. Connecta GitHub a claude.ai/code i autoritza el repo (dona accés només a aquest repo).
3. Crea un **Project** de Claude. A la secció de coneixement prem **+**, tria **GitHub**, selecciona el teu repo i els fitxers a incloure.
4. Instal·la la skill de `skill/problem-diary/` i edita-ne la línia `REPO:` amb el teu `owner/nom-del-repo`.
5. Escriu els teus dispositius a `diario/DEVICES.md`, amb un sol nom oficial per dispositiu.

## Ús diari

Quan es resolgui un problema, digues a l'assistent **"close and save"**. Segons la llargada, s'utilitza un de tres camins:

| Situació | Què passa |
|---|---|
| Entrada curta, des del xat | La skill prepara un enllaç `claude.ai/code` amb el prompt i el repo ja emplenats. Obre'l i prem Intro. |
| Entrada llarga, des del xat | La skill crea el fitxer `.md` amb el nom correcte i t'indica la carpeta exacta. Puja'l des del web de GitHub (*Add file > Upload files*). |
| Ja ets a Claude Code | Escriu el fitxer directament: `git pull`, commit, push. Sense límit de llargada. |

Després prem **Sync** al Project de Claude perquè els xats vegin l'entrada nova.

## Estructura del repositori

```
README.md                          índex dels README traduïts
CLAUDE.md                          instruccions per a l'agent de codi
docs/README.{lang}.md              README en cada llengua
diario/
  DEVICES.md                       noms oficials dels dispositius (un nom per dispositiu)
  _TEMPLATE.md                     plantilla d'entrada
  {device-slug}/
    YYYY-MM-DD-short-title.md      un fitxer per problema resolt
skill/problem-diary/               la skill "close and save"
  SKILL.md                         flux de treball i regles
  scripts/build_link.py            construeix l'enllaç emplenat, comprova llargada i secrets
  assets/entry-template.md         plantilla que fa servir la skill (mantén-la sincronitzada amb diario/_TEMPLATE.md)
```

Els problemes que no pertanyen a cap dispositiu concret (un web, un servei compartit) van a `diario/general/`.

## Format de l'entrada

Cada entrada té els mateixos encapçalaments fixos, perquè grep i la cerca amb IA funcionin de manera fiable: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, més els opcionals **Do not** i **Related**. El contingut s'escriu en la teva llengua. Consulta `diario/_TEMPLATE.md`.

## Límits i privadesa

- Un enllaç porta l'entrada dins de l'URL, així que només el fan servir les entrades curtes. Les més llargues passen pel fitxer.
- Obrir l'enllaç i prémer Intro continua sent manual: no és del tot automàtic i cap entrada es desa sense que la vegis.
- Cada entrada desada inicia una sessió de Claude Code al web, que compta per a l'ús de la teva subscripció.
- Mantén el repo privat. Les entrades descriuen els teus sistemes amb detall.
- **No posis mai contrasenyes, tokens ni claus en una entrada.** Escriu en lloc seu on estan guardats.
- Tot el repo compta per a la capacitat de coneixement del Project. Hi caben centenars d'entrades curtes.
- La sincronització de GitHub als Projects de vegades pot anar lenta o fallar. Si el xat no veu una entrada nova, prem Sync un altre cop i comprova-ho.

## Llicència

Tria una llicència per al teu fork (MIT és una opció habitual per a un projecte com aquest).
