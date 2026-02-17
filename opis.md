# Opis projektu
To jest framework dokumentacyjny/MVP procesu analitycznego. Służy do systematycznego generowania i utrzymywania specyfikacji wymagań na podstawie dokumentów wejściowych, z kontrolą jakości i śladowaniem źródeł.
Aktualnie repo zawiera głównie szablony, reguły i przykładowe dane wejściowe.



AI-AIReqStudio_1/
├── doc/
│   ├── glossary.md
│   ├── opis systemu BE.md
│   ├── BO/
│   │   └── BackofficeUserGuide-pl_basic.adoc
│   └── EBP/
│       ├── Main.adoc
│       └── Miniaplikacja_*.adoc
├── kb/
│   ├── chunks/
│   │   └── EBP/
│   │       └── DOC-*.json
│   └── _manifest.json
├── spec/
│   ├── 00-outline.md
│   ├── 10-spw.md
│   ├── 10-spw temp v3.md
│   ├── 10-spw temp v4.md
│   ├── 10-spw_out.md
│   └── spw_szablon v2.md
├── src/
│   ├── banki-api-uslugi-banku.md
│   └── wymagania.md
├── tools/
│   ├── ingest_adoc.py
│   ├── parse_requirements.py
│   ├── render-placeholders.ps1
│   └── search_kb.py
├── opis.md
├── project-parameters.md
├── project-prompt.md
├── README.md
├── requirements.txt
└── zagadnienia otwarte.md

Zagadnienia 
1) Dokumentacja wymagań (SPW) powinna powstać w odniesieniu do dokumetnacji systemu Bankowość Internetowej (desktop, mobile). DOdatkowo powinna uezględniać architektórę systemu (mikroserwisy) oraz możliwości API. Dokumentacja systemu to około 800 stron. Jak można rozbudować ten framework aby LLM wiedział jak działa obecnie system i gdzie trzeba zrealizować zmiany będące wymaganiami klienta?


Zbudowałem framework w Visual Studio Code, którego zadaniem jest generowanie specyfikacji wymagań na podstawie materiałów (wymagań) klienta oraz dokumentacji systemów informatycznych (w szczególności Bankowości Elektronicznej detal, mikro, korpo w wersji desktop oraz mobile). Narzędzie wykorzystuje model LLM (GPT) oraz rozszerzenie Codex. Specyfikacja będzie posiadała określoną strukturę - opisaną w /spec/10-spw.md

Obsługa narzędzia będzie realizowana przez wykonywanie odpowiednich promptów w Codex i pracę na plikach projektu.


# Struktura katalogów
/doc_basic - dokumentacja systemu (źródła) w formatach tekstowych (np. .md, .adoc)
/src - wymagania/oczekiwania klienta (źródła) w formacie .md (docelowo: także PDF/DOCX po konwersji)
/spec - dokument specyfikacji wymagań (generowany/utrzymywany)
/tools - skrypty pomocnicze (np. render placeholderów)

Utrzymanie kontroli nad AI
- Jeśli informacja jest ze źródeł → AI dopisuje znacznik Source: (np. plik/sekcja)
- Jeśli AI nie ma podstawy → musi oznaczyć ASSUMPTION albo OPEN-QUESTION
- Zakaz: AI nie może tworzyć endpointów, pól, statusów „z głowy”



# Wymagania klienta 
1. Wymagania powinny mieć format WM-<num>
Wymgania powinny mieć odpowiednią strkturę
Przykład:
## 4. Wymagania funkcjonalne
### 4.1 Aktywacja usługi CashDirector
**WM-01 Aktywacja usługi CashDirector**  
System BE musi umożliwiać klientowi ...
**WM-02 Obsługa zgód i regulaminów**  
System BE musi umożliwiać pobranie, prezentację oraz rejestrację akceptacji zgód ...

### 4.2 Rejestracja i parowanie firmy
**WM-05 Parowanie firmy i użytkownika**  
System BE musi umożliwiać parowanie firmy i ...
**WM-06 Obsługa istniejących danych w CashDirector**  
System BE musi obsługiwać scenariusz, w którym firma lub użytkownik istnieje już w systemie CashDirector.

Założenia wejścia (kontrakt)
Sekcje są w nagłówkach:
## 4. Wymagania funkcjonalne
### 4.1 ...
Wymaganie zawsze zaczyna się od linii:
**WM-XX Tytuł** (np. **WM-01 Aktywacja usługi CashDirector** )
Treść wymagania to kolejne linie aż do następnego **WM-... albo do kolejnego ### .../## .../końca pliku.



# Praca z narzędziem

1. Uzupełniasz tylko parametry w project-parameters.md (nazwa projektu, klient, język, styl, ścieżki).
2. Trzymasz stały „silnik” w project-prompt.md (bez danych klienta).
3. W każdej sesji odpalasz prompt startowy do Codex:

Prompty:
```markdown
Pracujemy w tym repo. Najpierw wczytaj:
- project-parameters.md
- project-prompt.md
- spec/00-outline.md
- pliki źródłowe z src/ (wymagania klienta, zmiany któryc oczekuje klienta)
- wszystkie pliki dokumentacji systemu z doc_basic/ oraz pliki z katalogów podrzędnych(dokumentacja systemu, stan obecny systemu, przed zmianami o które wnioskuje klient)

Następnie potwierdź: projekt, klient, język, styl, zakres.
Nie generuj treści, dopóki nie potwierdzisz konfiguracji.
```

4. Potem prompt zadaniowy, np. dla rozdziału:
```
Na podstawie src/* oraz doc_basic/* uzupełnij spec/10-spw.md.
Wymagania:
- ID: RQ-ACT-###
- każde wymaganie: opis, uzasadnienie, AC (Given/When/Then)
- sekcje: Obsługa błędów i Zagadnienia otwarte muszą pozostać
- bez domysłów: brak danych -> OPEN-QUESTION-###
- nie modyfikuj sekcji z "Generowanie: POMIŃ"
```

5. Na końcu prompt walidacyjny:
```
Zrób review spójności:
- zgodność z spec/00-outline.md
- unikalność ID wymagań
- spójność terminologii
- lista braków i pytań otwartych
```


##################################### POPRZEDNI OPIS


# Minimalny „standard promptów” do pracy w czacie w VSC
Żeby praca była powtarzalna, przygotuj sobie 6–8 gotowych komend (snippetów). Przykłady (do używania na zaznaczeniu albo pliku):

* „Zrób wymagania z materiałów od Klienta”
„Na podstawie /src/ zaproponuj wymagania w formacie RQ-###. Dodaj kryteria akceptacji i przypadki negatywne.”

* „Utestowalnij”
„Przerób wymagania na testowalne. Każde wymaganie ma mieć: warunek, działanie, wynik. Usuń ogólniki.”

* „Wykryj luki”
„Wskaż brakujące wymagania: bezpieczeństwo, audyt, błędy, retry, idempotency, zgodność danych.”

* „Zrób macierz śledzenia”
„Zrób tabelę: ID wymagania → źródło → test/AC → zależności.”

* „Wersja na review”
„Przeredaguj pod czytelnika biznesowego, bez utraty jednoznaczności.”

* „Lista pytań otwartych”
„Wypisz decyzje wymagane od biznesu/architekta + konsekwencje wyborów.”



Lista tematów do rozważenia:
- skrypt który dzieli całą dokumentację na obszary


# TOOLS

## Renderowanie placeholderów

Markdown sam z siebie nie „podstawi” {{PROJECT_NAME}} — musisz mieć etap renderowania (zamiany placeholderów na wartości).
LLM robi to automatycznie na podstawie założeń z project-prompt.md pkt. 3.6

Ustaw wartość w project-parameters.md w formacie:
- **Nazwa projektu (`PROJECT_NAME`):** `Integracja BE z CashDirector`
W dowolnym pliku używaj placeholdera:
{{PROJECT_NAME}}
Wygeneruj wersje „z podstawionymi wartościami” skryptem:
do osobnego katalogu (bez nadpisywania źródeł):
.\tools\render-placeholders.ps1 -OutDir rendered
albo nadpisując pliki (in-place):
.\tools\render-placeholders.ps1 -InPlace
Skrypt jest w tools/render-placeholders.ps1 i domyślnie renderuje pliki z spec/, src/, doc_basic/ oraz opis.md i project-prompt.md, biorąc wartości z project-parameters.md.
