# Problem Diary

**Córas beag, neamhspleách ar an AI a úsáideann tú, chun dialann inchuardaithe de na fadhbanna a réitigh tú a choinneáil, ionas go stopfaidh do chúntóir AI de dhearmad a dhéanamh.**

Teangacha: [gach teanga](../README.md)

## An smaoineamh

Má labhraíonn tú le cúntóir AI gach lá, réitíonn tú na cineálacha céanna fadhbanna arís agus arís eile, ar go leor feistí agus tionscadal. Ní chuimhníonn an cúntóir ar na mionsonraí, agus caitheann tú roinnt iarrataí ag atógáil an chomhthéacs.

Coinníonn an tionscadal seo dialann i Markdown simplí i stór Git. Nuair a réitítear fadhb, scríobhann an cúntóir iontráil ghearr: **cad a bhí san fhadhb, na céimeanna a d'oibrigh i ndáiríre agus an chonclúid** (ní an comhrá ar fad, agus ní na hiarrachtaí a theip). An chéad uair eile, léann an cúntóir an dialann ar dtús agus faigheann sé an freagra le níos lú iarrataí.

Tá sé úsáideach má tá go leor tionscadal agus feistí agat. Mura gcuireann tú ach ceisteanna tapa, aonair, níl sé de dhíth ort.

## Conas a oibríonn sé

```
 comhrá le Claude ──"close and save"──▶ nasc réamhlíonta ──▶ Claude Code ar an ngréasán ──▶ commit + push
        ▲                                                                                      │
        └──────── Claude Project (stór GitHub mar eolas, brúigh Sync) ◀────────────────────────┘
```

- **Scríobh:** cruthaíonn Claude Code (teirminéal nó gréasán) an iontráil, rithníonn sé `git pull`, commit agus push.
- **Léamh:** cuirtear an stór le Claude Project mar eolas. Tar éis gach iontráil nua, brúigh an deilbhín Sync.
- **Gan freastalaí agus gan chomharthaí sa chomhrá.** Níl sa dialann ach comhaid i do stór féin, mar sin oibríonn sí le haon uirlis a léann Markdown.

## Riachtanais

- Do stór GitHub féin (is fiú príobháideach) a cruthaíodh ón teimpléad seo.
- Cuntas Claude Pro, Max nó Team (de dhíth le haghaidh Claude Code ar an ngréasán).
- GitHub ceangailte ag [claude.ai/code](https://claude.ai/code), agus an aip Claude údaraithe ar do stór dialainne.
- GitHub ceangailte le claude.ai (comhtháthú GitHub) ionas gur féidir le Project an stór a léamh.
- Le haghaidh iontrálacha fada a chruthaítear ón gcomhrá: forghníomhú cód agus cruthú comhad cumasaithe i socruithe Claude.

## Socrú

1. Cruthaigh stór **príobháideach** ón teimpléad seo agus clónáil nó uaslódáil na comhaid seo.
2. Ceangail GitHub ag claude.ai/code agus údaraigh an stór (tabhair rochtain don stór seo amháin).
3. Cruthaigh **Project** Claude. Sa chuid eolais brúigh **+**, roghnaigh **GitHub**, roghnaigh do stór agus na comhaid le cur san áireamh.
4. Suiteáil an skill ó `skill/problem-diary/` agus cuir do `owner/ainm-an-stóir` féin ina líne `REPO:`.
5. Liostaigh do chuid feistí in `diario/DEVICES.md`, le hainm oifigiúil amháin do gach feiste.

## Úsáid laethúil

Nuair a réitítear fadhb, abair leis an gcúntóir **"close and save"**. Ag brath ar an fhad, úsáidtear ceann de thrí bhealach:

| Cás | Cad a tharlaíonn |
|---|---|
| Iontráil ghearr, ón gcomhrá | Ullmhaíonn an skill nasc `claude.ai/code` agus an prompt agus an stór líonta cheana. Oscail é agus brúigh Enter. |
| Iontráil fhada, ón gcomhrá | Cruthaíonn an skill an comhad `.md` leis an ainm ceart agus insíonn sé duit an fillteán beacht. Uaslódáil ón suíomh GitHub é (*Add file > Upload files*). |
| Tá tú i Claude Code cheana | Scríobhann sé an comhad go díreach: `git pull`, commit, push. Gan teorainn fhaid. |

Ansin brúigh **Sync** sa Claude Project, ionas go bhfeicfidh na comhráite an iontráil nua.

## Struchtúr an stóir

```
README.md                          innéacs na README aistrithe
CLAUDE.md                          treoracha don ghníomhaire códaithe
docs/README.{lang}.md              README i ngach teanga
diario/
  DEVICES.md                       ainmneacha oifigiúla na bhfeistí (ainm amháin do gach feiste)
  _TEMPLATE.md                     teimpléad na hiontrála
  {device-slug}/
    YYYY-MM-DD-short-title.md      comhad amháin do gach fadhb a réitíodh
skill/problem-diary/               an skill "close and save"
  SKILL.md                         sreabhadh oibre agus rialacha
  scripts/build_link.py            tógann an nasc réamhlíonta, seiceálann fad agus rúin
  assets/entry-template.md         teimpléad a úsáideann an skill (coinnigh ar aon dul le diario/_TEMPLATE.md é)
```

Téann fadhbanna nach mbaineann le feiste ar leith (suíomh gréasáin, seirbhís roinnte) isteach in `diario/general/`.

## Formáid na hiontrála

Tá na ceannteidil sheasta chéanna ag gach iontráil, ionas go n-oibreoidh grep agus cuardach AI go muiníneach: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, móide na cinn roghnacha **Do not** agus **Related**. Scríobhann tú an t-ábhar i do theanga féin. Féach `diario/_TEMPLATE.md`.

## Teorainneacha agus príobháideacht

- Iompraíonn nasc an iontráil san URL, mar sin ní úsáideann ach iontrálacha gearra é. Téann na cinn is faide tríd an gcomhad.
- Tá oscailt an naisc agus brú Enter fós láimhe: níl sé go hiomlán uathoibríoch, agus ní shábháiltear aon iontráil gan tú í a fheiceáil.
- Tosaíonn gach iontráil shábháilte seisiún gréasáin Claude Code, a chuirtear le húsáid do shuibscríbhinne.
- Coinnigh an stór príobháideach. Déanann na hiontrálacha cur síos mionsonraithe ar do chórais.
- **Ná cuir pasfhocail, comharthaí ná eochracha in iontráil choíche.** Scríobh in ionad sin cá bhfuil siad stóráilte.
- Áirítear an stór ar fad i gcumas eolais an Project. Tagann na céadta iontráil ghearr isteach.
- D'fhéadfadh sioncrónú GitHub i Projects moill a bheith air nó teip uaireanta. Mura bhfeiceann an comhrá iontráil nua, brúigh Sync arís agus seiceáil.

## Ceadúnas

Roghnaigh ceadúnas do d'fhorc (is rogha choitianta é MIT do thionscadal mar seo).
