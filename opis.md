# Opis projektu
Zbudowałem workspace w Visual Studio Code, którego zadaniem jest generowanie specyfikacji wymagań na podstawie materiałów (wymagań) klienta oraz dokumentacji systemów informatycznych.
Narzędzie będzie wykorzystywało model LLM (GPT) oraz rozszerzenie COdex. Specyfikacja będzie posiadało określoną strukturę - opisaną w /spec/10-spw.md

Obsługa narzędzie będzie realizowna przez wykonywanie odpowiednich promptów w codex i praca na plikach projektu.

Chciałbym w pliku project-parameters.md zawrzeć najważniejsze parametry projektu np. 
-nazwę projektu, 
- nazwę klienta 
- Styl i Język Generowania dokumentóe

Dodatkowo w pliku (project-prompt.md) będzie głowny prompt który określa sposób pracy LLM.

Jak to obsłużyć, jak z tym pracować w VSC i Codex?

# Struktura katalogów
/doc - dokumetnacja systemów których dotyczy analiza w formacie MD
    /cpb - dokumentacja CBP w podzile na obszary /Przelewy, Rachunki itd. w soobnych plikach
    /ebp
/scr - wymagania Banku w formacie 
    /Bank - pliki z Banku np. PDF, DOCX itd (format inny niż MD)
    /MD - wymagania banku w formacie tesktowym MD
/spec - dokument specyfikacji wymagań

Utrzymanie kontroli nad AI
- Jeśli informacja jest ze źródeł → AI dopisuje znacznik Source: (np. plik/sekcja)
- Jeśli AI nie ma podstawy → musi oznaczyć ASSUMPTION albo OPEN-QUESTION
- Zakaz: AI nie może tworzyć endpointów, pól, statusów „z głowy”




# Praca z narzędziem

1. Uzupełniasz tylko parametry w project-parameters.md (nazwa projektu, klient, język, styl, ścieżki).
2. Trzymasz stały „silnik” w project-prompt.md (bez danych klienta).
3. W każdej sesji odpalasz prompt startowy do Codex:

Propmpty:
```markdown
Pracujemy w tym repo. Najpierw wczytaj:
- project-parameters.md
- project-prompt.md
- spec/00-outline.md
- pliki źródłowe z doc/

Następnie potwierdź: projekt, klient, język, styl, zakres.
Nie generuj treści, dopóki nie potwierdzisz konfiguracji.
```

4. Potem prompt zadaniowy, np. dla rozdziału:
```
Na podstawie doc/* uzupełnij spec/10-spw.md.
Wymagania:
- ID: RQ-ACT-###
- każde wymaganie: opis, uzasadnienie, AC (Given/When/Then)
- sekcje: Obsługa błędów i Zagadnienia otwarte muszą pozostać
- bez domysłów: brak danych -> OPEN-QUESTION-###
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

* „Zrób wymagania z materiałów od Kkienta”
„Na podstawie /scr/ zaproponuj wymagania w formacie RQ-###. Dodaj kryteria akceptacji i przypadki negatywne.”

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


TODO

TODO - skrypt który dzieli całą dokumentację na obszary