# Problem Diary

**Pieni, tekoälystä riippumaton järjestelmä, jolla pidät haettavaa päiväkirjaa ratkaisemistasi ongelmista, jotta tekoälyavustajasi lakkaa unohtamasta.**

Kielet: [kaikki kielet](../README.md)

## Idea

Jos puhut tekoälyavustajalle päivittäin, ratkaiset samantyyppisiä ongelmia yhä uudelleen, monilla laitteilla ja monissa projekteissa. Avustaja ei muista yksityiskohtia, ja käytät useita pyyntöjä asiayhteyden palauttamiseen.

Tämä projekti pitää päiväkirjaa pelkässä Markdownissa Git-repositoriossa. Kun ongelma on ratkaistu, avustaja kirjoittaa lyhyen merkinnän: **mikä ongelma oli, mitkä vaiheet todella toimivat ja johtopäätös** (ei koko keskustelua eikä epäonnistuneita yrityksiä). Seuraavalla kerralla avustaja lukee ensin päiväkirjan ja löytää vastauksen pienemmällä määrällä pyyntöjä.

Siitä on hyötyä, jos sinulla on paljon projekteja ja laitteita. Jos esität vain nopeita, yksittäisiä kysymyksiä, et tarvitse sitä.

## Miten se toimii

```
 keskustelu Clauden kanssa ──"close and save"──▶ esitäytetty linkki ──▶ Claude Code verkossa ──▶ commit + push
        ▲                                                                                          │
        └──────── Clauden Project (GitHub-repo tietona, paina Sync) ◀──────────────────────────────┘
```

- **Kirjoittaminen:** Claude Code (pääte tai verkko) luo merkinnän, ajaa `git pull`, commitoi ja pushaa.
- **Lukeminen:** repo lisätään Clauden Projectiin tietopohjaksi. Jokaisen uuden merkinnän jälkeen paina Sync-kuvaketta.
- **Ei palvelinta eikä tokeneita keskustelussa.** Päiväkirja on vain tiedostoja omassa repossasi, joten se toimii kaikilla työkaluilla, jotka osaavat lukea Markdownia.

## Vaatimukset

- Oma GitHub-repositorio (yksityinen käy), luotu tästä pohjasta.
- Claude Pro-, Max- tai Team-tili (tarvitaan Claude Codea varten verkossa).
- GitHub yhdistetty osoitteessa [claude.ai/code](https://claude.ai/code), ja Claude-sovellukselle annettu lupa päiväkirjarepoon.
- GitHub yhdistetty claude.ai:hin (GitHub-integraatio), jotta Project voi lukea repon.
- Keskustelusta luotavia pitkiä merkintöjä varten: koodin suoritus ja tiedostojen luonti käytössä Clauden asetuksissa.

## Käyttöönotto

1. Luo tästä pohjasta **yksityinen** repo ja kloonaa tai lataa nämä tiedostot.
2. Yhdistä GitHub osoitteessa claude.ai/code ja anna lupa repolle (anna pääsy vain tähän repoon).
3. Luo Clauden **Project**. Paina tietoalueella **+**, valitse **GitHub** ja valitse repo sekä mukaan otettavat tiedostot.
4. Asenna skill kansiosta `skill/problem-diary/` ja muokkaa sen `REPO:`-riville oma `owner/repon-nimi`.
5. Luettele laitteesi tiedostossa `diario/DEVICES.md`, yksi virallinen nimi laitetta kohden.

## Päivittäinen käyttö

Kun ongelma on ratkaistu, sano avustajalle **"close and save"**. Pituudesta riippuen käytetään yhtä kolmesta reitistä:

| Tilanne | Mitä tapahtuu |
|---|---|
| Lyhyt merkintä, keskustelusta | Skill valmistelee `claude.ai/code`-linkin, jossa prompt ja repo on jo täytetty. Avaa se ja paina Enter. |
| Pitkä merkintä, keskustelusta | Skill luo `.md`-tiedoston oikealla nimellä ja kertoo tarkan kansion. Lataa se GitHubin sivustolla (*Add file > Upload files*). |
| Olet jo Claude Codessa | Se kirjoittaa tiedoston suoraan: `git pull`, commit, push. Ei pituusrajaa. |

Paina sitten **Sync** Clauden Projectissa, jotta keskustelut näkevät uuden merkinnän.

## Repositorion rakenne

```
README.md                          käännettyjen README-tiedostojen hakemisto
CLAUDE.md                          ohjeet koodausagentille
docs/README.{lang}.md              README kullakin kielellä
diario/
  DEVICES.md                       laitteiden viralliset nimet (yksi nimi laitetta kohden)
  _TEMPLATE.md                     merkintäpohja
  {device-slug}/
    YYYY-MM-DD-short-title.md      yksi tiedosto ratkaistua ongelmaa kohden
skill/problem-diary/               "close and save" -skill
  SKILL.md                         työnkulku ja säännöt
  scripts/build_link.py            rakentaa esitäytetyn linkin, tarkistaa pituuden ja salaisuudet
  assets/entry-template.md         skillin käyttämä pohja (pidä synkassa tiedoston diario/_TEMPLATE.md kanssa)
```

Ongelmat, jotka eivät kuulu mihinkään yksittäiseen laitteeseen (verkkosivusto, jaettu palvelu), menevät kansioon `diario/general/`.

## Merkinnän muoto

Jokaisella merkinnällä on samat kiinteät otsikot, jotta grep ja tekoälyhaku toimivat luotettavasti: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, sekä valinnaiset **Do not** ja **Related**. Sisältö kirjoitetaan omalla kielelläsi. Katso `diario/_TEMPLATE.md`.

## Rajoitukset ja yksityisyys

- Linkki kuljettaa merkinnän URL-osoitteessa, joten vain lyhyet merkinnät käyttävät sitä. Pidemmät kulkevat tiedoston kautta.
- Linkin avaaminen ja Enterin painaminen on edelleen manuaalista: se ei ole täysin automaattista, eikä mitään merkintää tallenneta ilman että näet sen.
- Jokainen tallennettu merkintä käynnistää Claude Code -verkkoistunnon, joka kuluttaa tilauksesi käyttöä.
- Pidä repo yksityisenä. Merkinnät kuvaavat järjestelmäsi yksityiskohtaisesti.
- **Älä koskaan kirjoita salasanoja, tokeneita tai avaimia merkintään.** Kirjoita sen sijaan, missä ne säilytetään.
- Koko repo lasketaan Projectin tietokapasiteettiin. Satoja lyhyitä merkintöjä mahtuu.
- Projectien GitHub-synkronointi voi toisinaan viivästyä tai epäonnistua. Jos keskustelu ei näe uutta merkintää, paina Sync uudelleen ja tarkista.

## Lisenssi

Valitse lisenssi forkillesi (MIT on yleinen valinta tämänkaltaiselle projektille).
