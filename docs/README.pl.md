# Problem Diary

**Mały system niezależny od używanej AI do prowadzenia przeszukiwalnego dziennika rozwiązanych problemów, żeby Twój asystent AI przestał zapominać.**

Języki: [wszystkie języki](../README.md)

## Pomysł

Jeśli codziennie rozmawiasz z asystentem AI, w kółko rozwiązujesz te same rodzaje problemów, na wielu urządzeniach i w wielu projektach. Asystent nie pamięta szczegółów, a Ty tracisz kilka zapytań na odtworzenie kontekstu.

Ten projekt prowadzi dziennik w zwykłym Markdownie w repozytorium Git. Gdy problem zostanie rozwiązany, asystent zapisuje krótki wpis: **na czym polegał problem, jakie kroki naprawdę zadziałały i wniosek** (nie cały czat i nie nieudane próby). Następnym razem asystent najpierw czyta dziennik i znajduje odpowiedź przy mniejszej liczbie zapytań.

Przydaje się, jeśli masz wiele projektów i urządzeń. Jeśli zadajesz tylko szybkie, jednorazowe pytania, nie jest Ci potrzebny.

## Jak to działa

```
 czat z Claude ──"close and save"──▶ wstępnie wypełniony link ──▶ Claude Code w sieci ──▶ commit + push
        ▲                                                                                    │
        └──────── Project Claude (repo GitHub jako wiedza, naciśnij Sync) ◀──────────────────┘
```

- **Zapis:** Claude Code (terminal lub web) tworzy wpis, wykonuje `git pull`, commit i push.
- **Odczyt:** repo jest dodawane do Project Claude jako wiedza. Po każdym nowym wpisie naciśnij ikonę Sync.
- **Bez serwera i bez tokenów w czacie.** Dziennik to zwykłe pliki w Twoim repo, więc działa z każdym narzędziem czytającym Markdown.

## Wymagania

- Własne repozytorium GitHub (prywatne wystarczy) utworzone z tego szablonu.
- Konto Claude Pro, Max lub Team (potrzebne do Claude Code w sieci).
- GitHub połączony z [claude.ai/code](https://claude.ai/code), z aplikacją Claude autoryzowaną w repo dziennika.
- GitHub połączony z claude.ai (integracja z GitHub), aby Project mógł czytać repo.
- Dla długich wpisów tworzonych z czatu: włączone wykonywanie kodu i tworzenie plików w ustawieniach Claude.

## Konfiguracja

1. Utwórz **prywatne** repo z tego szablonu i sklonuj lub wgraj te pliki.
2. Połącz GitHub na claude.ai/code i autoryzuj repo (daj dostęp tylko do tego repo).
3. Utwórz **Project** Claude. W sekcji wiedzy naciśnij **+**, wybierz **GitHub**, zaznacz swoje repo i pliki do uwzględnienia.
4. Zainstaluj skill z `skill/problem-diary/` i zmień jego linię `REPO:` na swoje `owner/nazwa-repo`.
5. Wypisz swoje urządzenia w `diario/DEVICES.md`, z jedną oficjalną nazwą na urządzenie.

## Codzienne użycie

Gdy problem zostanie rozwiązany, powiedz asystentowi **"close and save"**. W zależności od długości używana jest jedna z trzech ścieżek:

| Sytuacja | Co się dzieje |
|---|---|
| Krótki wpis, z czatu | Skill przygotowuje link `claude.ai/code` z już wypełnionym promptem i repo. Otwórz go i naciśnij Enter. |
| Długi wpis, z czatu | Skill tworzy plik `.md` z właściwą nazwą i podaje dokładny folder. Wgraj go ze strony GitHub (*Add file > Upload files*). |
| Jesteś już w Claude Code | Zapisuje plik bezpośrednio: `git pull`, commit, push. Bez limitu długości. |

Następnie naciśnij **Sync** w Project Claude, aby czaty widziały nowy wpis.

## Struktura repozytorium

```
README.md                          indeks przetłumaczonych README
CLAUDE.md                          instrukcje dla agenta kodującego
docs/README.{lang}.md              README w każdym języku
diario/
  DEVICES.md                       oficjalne nazwy urządzeń (jedna nazwa na urządzenie)
  _TEMPLATE.md                     szablon wpisu
  {device-slug}/
    YYYY-MM-DD-short-title.md      jeden plik na rozwiązany problem
skill/problem-diary/               skill "close and save"
  SKILL.md                         przebieg i zasady
  scripts/build_link.py            buduje wstępnie wypełniony link, sprawdza długość i sekrety
  assets/entry-template.md         szablon używany przez skill (utrzymuj zgodny z diario/_TEMPLATE.md)
```

Problemy, które nie należą do żadnego konkretnego urządzenia (strona internetowa, usługa współdzielona), trafiają do `diario/general/`.

## Format wpisu

Każdy wpis ma te same stałe nagłówki, aby grep i wyszukiwanie AI działały niezawodnie: **Date, Device, Tags, Context, Problem, Solution, Conclusion**, plus opcjonalne **Do not** i **Related**. Treść piszesz we własnym języku. Zobacz `diario/_TEMPLATE.md`.

## Ograniczenia i prywatność

- Link niesie wpis w adresie URL, więc korzystają z niego tylko krótkie wpisy. Dłuższe idą przez plik.
- Otwarcie linku i naciśnięcie Enter pozostaje ręczne: nie jest to w pełni automatyczne i żaden wpis nie zostanie zapisany bez Twojego wglądu.
- Każdy zapisany wpis uruchamia sesję Claude Code w sieci, która wlicza się do zużycia Twojej subskrypcji.
- Trzymaj repo jako prywatne. Wpisy szczegółowo opisują Twoje systemy.
- **Nigdy nie wpisuj haseł, tokenów ani kluczy do wpisu.** Napisz zamiast tego, gdzie są przechowywane.
- Całe repo wlicza się do pojemności wiedzy Project. Mieszczą się setki krótkich wpisów.
- Synchronizacja GitHub w Projects może czasem się opóźniać lub zawieść. Jeśli czat nie widzi nowego wpisu, naciśnij Sync ponownie i sprawdź.

## Licencja

Wybierz licencję dla swojego forka (MIT to częsty wybór dla takiego projektu).
