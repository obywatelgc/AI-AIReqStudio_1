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