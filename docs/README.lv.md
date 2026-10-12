# Problem Diary

**Neliela, no izmantotā MI neatkarīga sistēma, lai vestu meklējamu atrisināto problēmu dienasgrāmatu, lai tavs MI asistents beidzot pārstātu aizmirst.**

Valodas: [visas valodas](../README.md)

## Ideja

Ja ar MI asistentu runā katru dienu, tu atkal un atkal risini tāda paša veida problēmas, daudzās ierīcēs un projektos. Asistents neatceras detaļas, un tu iztērē vairākus pieprasījumus konteksta atjaunošanai.

Šis projekts vada dienasgrāmatu parastā Markdown formātā Git repozitorijā. Kad problēma ir atrisināta, asistents uzraksta īsu ierakstu: **kāda bija problēma, kuri soļi patiešām palīdzēja un secinājums** (nevis visu sarunu un ne neveiksmīgos mēģinājumus). Nākamreiz asistents vispirms izlasa dienasgrāmatu un atbildi atrod ar mazāk pieprasījumu.

Tā noder, ja tev ir daudz projektu un ierīču. Ja uzdod tikai ātrus, atsevišķus jautājumus, tā tev nav vajadzīga.

## Kā tas darbojas

```
 saruna ar Claude ──"close and save"──▶ aizpildīta saite ──▶ Claude Code tīmeklī ──▶ commit + push
        ▲                                                                                │
        └──────── Claude Project (GitHub repozitorijs kā zināšanas, nospied Sync) ◀──────┘
```

- **Rakstīšana:** Claude Code (terminālis vai tīmeklis) izveido ierakstu, izpilda `git pull`, commit un push.
- **Lasīšana:** repozitorijs tiek pievienots Claude Project kā zināšanas. Pēc katra jaunā ieraksta nospied Sync ikonu.
- **Nav servera un nav token sarunā.** Dienasgrāmata ir tikai faili tavā repozitorijā, tāpēc tā darbojas ar jebkuru rīku, kas lasa Markdown.

## Prasības

- Savs GitHub repozitorijs (der arī privāts), izveidots no šī sagataves.
- Claude Pro, Max vai Team konts (nepieciešams Claude Code tīmeklī).
- GitHub savienots vietnē [claude.ai/code](https://claude.ai/code), Claude lietotnei piešķirta piekļuve dienasgrāmatas repozitorijam.
- GitHub savienots ar claude.ai (GitHub integrācija), lai Project varētu lasīt repozitoriju.
- Gariem ierakstiem, kas veidoti no sarunas: Claude iestatījumos ieslēgta koda izpilde un failu izveide.

## Iestatīšana

1. No šīs sagataves izveido **privātu** repozitoriju un nokopē vai augšupielādē šos failus.
2. Savieno GitHub vietnē claude.ai/code un autorizē repozitoriju (dod piekļuvi tikai šim repozitorijam).
3. Izveido Claude **Project**. Zināšanu sadaļā nospied **+**, izvēlies **GitHub**, atlasi savu repozitoriju un iekļaujamos failus.
4. Instalē skill no `skill/problem-diary/` un tā rindā `REPO:` ieraksti savu `owner/repozitorija-nosaukums`.
5. Uzskaiti savas ierīces failā `diario/DEVICES.md`, katrai ierīcei vienu oficiālo nosaukumu.

## Ikdienas lietošana

Kad problēma ir atrisināta, saki asistentam **"close and save"**. Atkarībā no garuma tiek izmantots viens no trim ceļiem:

| Situācija | Kas notiek |
|---|---|
| Īss ieraksts, no sarunas | Skill sagatavo `claude.ai/code` saiti ar jau aizpildītu promptu un repozitoriju. Atver to un nospied Enter. |
| Garš ieraksts, no sarunas | Skill izveido `.md` failu ar pareizo nosaukumu un pasaka precīzu mapi. Augšupielādē to GitHub vietnē (*Add file > Upload files*). |
| Tu jau esi Claude Code | Tas ieraksta failu tieši: `git pull`, commit, push. Bez garuma ierobežojuma. |

Pēc tam nospied **Sync** Claude Project, lai sarunas redzētu jauno ierakstu.

## Repozitorija struktūra

```
README.md                          tulkoto README rādītājs
CLAUDE.md                          norādījumi kodēšanas aģentam
docs/README.{lang}.md              README katrā valodā
diario/
  DEVICES.md                       ierīču oficiālie nosaukumi (viens nosaukums katrai ierīcei)
  _TEMPLATE.md                     ieraksta sagatave
  {device-slug}/
    YYYY-MM-DD-short-title.md      viens fails katrai atrisinātajai problēmai
skill/problem-diary/               skill "close and save"
  SKILL.md                         darba plūsma un noteikumi
  scripts/build_link.py            izveido aizpildīto saiti, pārbauda garumu un noslēpumus
  assets/entry-template.md         skill izmantotā sagatave (uzturi sinhronu ar diario/_TEMPLATE.md)
```

Problēmas, kas nepieder nevienai konkrētai ierīcei (vietne, kopīgs pakalpojums), nonāk mapē `diario/general/`.

## Ieraksta formāts

Katram ierakstam ir vienādi fiksēti virsraksti, lai grep un MI meklēšana darbotos uzticami: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, kā arī neobligātie **Do not** un **Related**. Saturu raksti savā valodā. Skat. `diario/_TEMPLATE.md`.

## Ierobežojumi un privātums

- Saite nes ierakstu URL, tāpēc to izmanto tikai īsi ieraksti. Garāki iet caur failu.
- Saites atvēršana un Enter nospiešana joprojām ir manuāla: tas nav pilnībā automātiski, un neviens ieraksts netiek saglabāts, tev to neredzot.
- Katrs saglabātais ieraksts sāk Claude Code tīmekļa sesiju, kas tiek ieskaitīta tavā abonementa lietojumā.
- Uztur repozitoriju privātu. Ieraksti detalizēti apraksta tavas sistēmas.
- **Nekad neieraksti ierakstā paroles, token vai atslēgas.** Raksti tā vietā, kur tās tiek glabātas.
- Viss repozitorijs tiek ieskaitīts Project zināšanu ietilpībā. Ietilpst simtiem īsu ierakstu.
- GitHub sinhronizācija Projects dažkārt var kavēties vai neizdoties. Ja saruna neredz jaunu ierakstu, nospied Sync vēlreiz un pārbaudi.

## Licence

Izvēlies licenci savam forkam (MIT ir izplatīta izvēle šādam projektam).
