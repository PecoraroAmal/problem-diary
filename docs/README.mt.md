# Problem Diary

**Sistema żgħira, indipendenti mill-AI li tuża, biex iżżomm djarju li jista' jiġi ffruntat tal-problemi li solvejt, biex l-assistent AI tiegħek jieqaf jinsa.**

Lingwi: [il-lingwi kollha](../README.md)

## Il-ħsieb

Jekk titkellem ma' assistent AI kuljum, issolvi l-istess tipi ta' problemi għal darba wara l-oħra, fuq ħafna apparati u proġetti. L-assistent ma jiftakarx id-dettalji u inti tonfoq diversi talbiet biex terġa' tibni l-kuntest.

Dan il-proġett iżomm djarju f'Markdown sempliċi f'repożitorju Git. Meta problema tissolva, l-assistent jikteb daħla qasira: **x'kienet il-problema, il-passi li verament ħadmu u l-konklużjoni** (mhux iċ-chat kollu, u lanqas it-tentattivi li fallew). Il-ġurnata ta' wara, l-assistent l-ewwel jaqra d-djarju u jsib it-tweġiba b'inqas talbiet.

Huwa utli jekk għandek ħafna proġetti u apparati. Jekk tistaqsi biss mistoqsijiet veloċi u iżolati, ma għandekx bżonnu.

## Kif jaħdem

```
 chat ma' Claude ──"close and save"──▶ link mimli minn qabel ──▶ Claude Code fuq il-web ──▶ commit + push
        ▲                                                                                      │
        └──────── Claude Project (repożitorju GitHub bħala għarfien, agħfas Sync) ◀────────────┘
```

- **Kitba:** Claude Code (terminal jew web) joħloq id-daħla, imexxi `git pull`, commit u push.
- **Qari:** ir-repożitorju jiżdied ma' Claude Project bħala għarfien. Wara kull daħla ġdida, agħfas l-ikona Sync.
- **L-ebda server u l-ebda token fiċ-chat.** Id-djarju huwa biss fajls fir-repożitorju tiegħek, allura jaħdem ma' kull għodda li taqra Markdown.

## Rekwiżiti

- Repożitorju GitHub tiegħek (privat huwa tajjeb) maħluq minn dan it-template.
- Kont Claude Pro, Max jew Team (meħtieġ għal Claude Code fuq il-web).
- GitHub konness ma' [claude.ai/code](https://claude.ai/code), bl-app Claude awtorizzata fuq ir-repożitorju tad-djarju.
- GitHub konness ma' claude.ai (l-integrazzjoni ta' GitHub) biex Project ikun jista' jaqra r-repożitorju.
- Għal daħliet twal maħluqa miċ-chat: eżekuzzjoni tal-kodiċi u ħolqien tal-fajls attivati fis-settings ta' Claude.

## Konfigurazzjoni

1. Oħloq repożitorju **privat** minn dan it-template u kkloppja jew ikkarga dawn il-fajls.
2. Qabbad GitHub ma' claude.ai/code u awtorizza r-repożitorju (agħti aċċess biss lil dan ir-repożitorju).
3. Oħloq **Project** ta' Claude. Fit-taqsima tal-għarfien agħfas **+**, agħżel **GitHub**, agħżel ir-repożitorju tiegħek u l-fajls li se jiddaħħlu.
4. Installa l-skill minn `skill/problem-diary/` u biddel is-sensja `REPO:` bil-`owner/isem-tar-repożitorju` tiegħek.
5. Elenka l-apparati tiegħek f'`diario/DEVICES.md`, b'isem uffiċjali wieħed għal kull apparat.

## Użu ta' kuljum

Meta problema tissolva, għid lill-assistent **"close and save"**. Skont it-tul, jintuża wieħed minn tliet toroq:

| Sitwazzjoni | X'jiġri |
|---|---|
| Daħla qasira, miċ-chat | L-skill iħejji link `claude.ai/code` bil-prompt u r-repożitorju diġà mimlija. Iftaħha u agħfas Enter. |
| Daħla twila, miċ-chat | L-skill joħloq il-fajl `.md` bl-isem korrett u jgħidlek il-folder eżatt. Ikkarga mis-sit ta' GitHub (*Add file > Upload files*). |
| Diġà int f'Claude Code | Jikteb il-fajl direttament: `git pull`, commit, push. Ebda limitu ta' tul. |

Imbagħad agħfas **Sync** fil-Claude Project, biex iċ-chats jaraw id-daħla l-ġdida.

## Struttura tar-repożitorju

```
README.md                          indiċi tar-README tradotti
CLAUDE.md                          struzzjonijiet għall-aġent tal-kodiċi
docs/README.{lang}.md              README f'kull lingwa
diario/
  DEVICES.md                       ismijiet uffiċjali tal-apparati (isem wieħed għal kull apparat)
  _TEMPLATE.md                     template tad-daħla
  {device-slug}/
    YYYY-MM-DD-short-title.md      fajl wieħed għal kull problema solvuta
skill/problem-diary/               l-skill "close and save"
  SKILL.md                         fluss tax-xogħol u regoli
  scripts/build_link.py            jibni l-link mimli minn qabel, jiċċekkja t-tul u s-sigrieti
  assets/entry-template.md         template użat mill-skill (żommu sinkronizzat ma' diario/_TEMPLATE.md)
```

Il-problemi li ma jappartjenu lil ebda apparat speċifiku (sit web, servizz maqsum) imorru f'`diario/general/`.

## Format tad-daħla

Kull daħla għandha l-istess titli fissi, biex grep u t-tiftix bl-AI jaħdmu b'mod affidabbli: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, flimkien ma' **Do not** u **Related** li huma fakultattivi. Il-kontenut tikteb bil-lingwa tiegħek. Ara `diario/_TEMPLATE.md`.

## Limiti u privatezza

- Link iġorr id-daħla fl-URL, allura jużawh biss id-daħliet qosra. It-twal jgħaddu mill-fajl.
- Il-ftuħ tal-link u l-għafsa ta' Enter jibqgħu manwali: mhux għal kollox awtomatiku u l-ebda daħla ma tinħażen mingħajr ma tarha.
- Kull daħla maħżuna tibda sessjoni ta' Claude Code fuq il-web, li tgħodd mal-użu tal-abbonament tiegħek.
- Żomm ir-repożitorju privat. Id-daħliet jiddeskrivu s-sistemi tiegħek fid-dettall.
- **Qatt tpoġġi passwords, tokens jew keys f'daħla.** Ikteb minflok fejn huma maħżuna.
- Ir-repożitorju kollu jgħodd fil-kapaċità tal-għarfien tal-Project. Jidħlu mijiet ta' daħliet qosra.
- Is-sinkronizzazzjoni ta' GitHub fil-Projects xi drabi tista' tittardja jew tfalli. Jekk iċ-chat ma jarax daħla ġdida, agħfas Sync mill-ġdid u ċċekkja.

## Liċenzja

Agħżel liċenzja għall-fork tiegħek (MIT hija għażla komuni għal proġett bħal dan).
