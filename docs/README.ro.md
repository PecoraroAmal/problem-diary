# Problem Diary

**Un sistem mic, independent de AI-ul pe care îl folosești, pentru a ține un jurnal care poate fi căutat al problemelor rezolvate, ca asistentul tău AI să nu mai uite.**

Limbi: [toate limbile](../README.md)

## Ideea

Dacă vorbești zilnic cu un asistent AI, rezolvi iar și iar aceleași tipuri de probleme, pe multe dispozitive și în multe proiecte. Asistentul nu ține minte detaliile, iar tu cheltuiești mai multe cereri ca să refaci contextul.

Acest proiect ține un jurnal în Markdown simplu într-un depozit Git. Când o problemă este rezolvată, asistentul scrie o intrare scurtă: **care a fost problema, pașii care au funcționat cu adevărat și concluzia** (nu toată conversația și nici încercările eșuate). Data viitoare, asistentul citește mai întâi jurnalul și găsește răspunsul cu mai puține cereri.

Este util dacă ai multe proiecte și dispozitive. Dacă pui doar întrebări rapide și izolate, nu ai nevoie de el.

## Cum funcționează

```
 chat cu Claude ──"close and save"──▶ link precompletat ──▶ Claude Code pe web ──▶ commit + push
        ▲                                                                              │
        └──────── Claude Project (depozit GitHub ca informații, apasă Sync) ◀──────────┘
```

- **Scriere:** Claude Code (terminal sau web) creează intrarea, rulează `git pull`, commit și push.
- **Citire:** depozitul este adăugat într-un Claude Project ca informații. După fiecare intrare nouă, apasă pictograma Sync.
- **Fără server și fără token-uri în chat.** Jurnalul este doar un set de fișiere în propriul depozit, deci funcționează cu orice instrument care citește Markdown.

## Cerințe

- Propriul depozit GitHub (privat este în regulă) creat din acest șablon.
- Un cont Claude Pro, Max sau Team (necesar pentru Claude Code pe web).
- GitHub conectat la [claude.ai/code](https://claude.ai/code), cu aplicația Claude autorizată pe depozitul jurnalului.
- GitHub conectat la claude.ai (integrarea GitHub) pentru ca un Project să poată citi depozitul.
- Pentru intrările lungi create din chat: execuția codului și crearea de fișiere activate în setările Claude.

## Configurare

1. Creează un depozit **privat** din acest șablon și clonează sau încarcă aceste fișiere.
2. Conectează GitHub la claude.ai/code și autorizează depozitul (acordă acces doar la acest depozit).
3. Creează un **Project** Claude. În secțiunea de informații apasă **+**, alege **GitHub**, selectează depozitul și fișierele de inclus.
4. Instalează skill-ul din `skill/problem-diary/` și editează linia `REPO:` cu `owner/numele-depozitului` tău.
5. Listează dispozitivele în `diario/DEVICES.md`, cu un singur nume oficial pe dispozitiv.

## Utilizare zilnică

Când o problemă este rezolvată, spune-i asistentului **"close and save"**. În funcție de lungime, se folosește una dintre trei căi:

| Situație | Ce se întâmplă |
|---|---|
| Intrare scurtă, din chat | Skill-ul pregătește un link `claude.ai/code` cu promptul și depozitul deja completate. Deschide-l și apasă Enter. |
| Intrare lungă, din chat | Skill-ul creează fișierul `.md` cu numele corect și îți spune folderul exact. Încarcă-l de pe site-ul GitHub (*Add file > Upload files*). |
| Ești deja în Claude Code | Scrie fișierul direct: `git pull`, commit, push. Fără limită de lungime. |

Apoi apasă **Sync** în Claude Project, ca chat-urile să vadă intrarea nouă.

## Structura depozitului

```
README.md                          indexul README-urilor traduse
CLAUDE.md                          instrucțiuni pentru agentul de cod
docs/README.{lang}.md              README în fiecare limbă
diario/
  DEVICES.md                       numele oficiale ale dispozitivelor (un nume pe dispozitiv)
  _TEMPLATE.md                     șablonul intrării
  {device-slug}/
    YYYY-MM-DD-short-title.md      un fișier pentru fiecare problemă rezolvată
skill/problem-diary/               skill-ul "close and save"
  SKILL.md                         flux de lucru și reguli
  scripts/build_link.py            construiește linkul precompletat, verifică lungimea și secretele
  assets/entry-template.md         șablon folosit de skill (păstrează-l sincronizat cu diario/_TEMPLATE.md)
```

Problemele care nu aparțin unui singur dispozitiv (un site web, un serviciu partajat) merg în `diario/general/`.

## Formatul intrării

Fiecare intrare are aceleași titluri fixe, pentru ca grep și căutarea cu AI să funcționeze fiabil: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus opționalele **Do not** și **Related**. Conținutul îl scrii în limba ta. Vezi `diario/_TEMPLATE.md`.

## Limite și confidențialitate

- Un link poartă intrarea în URL, deci doar intrările scurte îl folosesc. Cele mai lungi trec prin fișier.
- Deschiderea linkului și apăsarea Enter rămân manuale: nu este complet automat și nicio intrare nu este salvată fără să o vezi.
- Fiecare intrare salvată pornește o sesiune Claude Code pe web, care se numără în utilizarea abonamentului tău.
- Păstrează depozitul privat. Intrările îți descriu sistemele în detaliu.
- **Nu pune niciodată parole, token-uri sau chei într-o intrare.** Scrie în loc unde sunt păstrate.
- Întregul depozit contează în capacitatea de informații a Project. Încap sute de intrări scurte.
- Sincronizarea GitHub din Projects poate întârzia sau eșua uneori. Dacă chat-ul nu vede o intrare nouă, apasă din nou Sync și verifică.

## Licență

Alege o licență pentru fork-ul tău (MIT este o alegere obișnuită pentru un proiect ca acesta).
