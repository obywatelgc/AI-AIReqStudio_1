<!-- AI-CONSTRAINTS
Zakres: Opis zakresu modyfikacji
Format: RQ-###
ĹąrĂłdĹ‚a: 
    Wymagania klienta: src/*, 
    Dokumentacja systemu: doc/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagaĹ„ â€“ {{PROJECT_NAME}}

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz gĹ‚Ăłwny cel biznesowy rozwiÄ…zania dla wskazanego zakresu modyfikacji.
    PrzykĹ‚ad: 
    Celem biznesowym projektu jest umoĹĽliwienie klientom bankowoĹ›ci elektronicznej (web i mobile) samodzielnego pobrania ostatniego wyciÄ…gu z rachunku w formacie elektronicznym (np. PDF, csv) w celu zwiÄ™kszenia poziomu samoobsĹ‚ugi, redukcji kosztĂłw operacyjnych oraz poprawy doĹ›wiadczenia uĹĽytkownika.
    Nie stosuj zaspiĂłw w stylu: 
    Celem bizesowym jest dodanie opcji "Pobierz ostatni wyciÄ…g".
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
ĹąrĂłdĹ‚a: Wymagania klienta: src/*
WyjĹ›cie: 3â€“5 zdaĹ„.
Kryteria jakoĹ›ci: jednoznacznoĹ›Ä‡, brak domysĹ‚Ăłw, spĂłjnoĹ›Ä‡ terminologii.
-->

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenies i stresc wymagania przekazane przez Klienta.
Zrodla: Wymagania klienta: src/*
Wyjscie: lista wymagan/zalozen z odniesieniami do zrodel.
-->
- WM-01: Zapewnienie w EBP i CBP kompensacji zmian w API Asseco CB dla zlecania przelewow biezacych i odroczonych. Zrodlo: src/wymagania.md.
- WM-02: Przekazywanie przelewu biezacego (ELIXIR) do Asseco CB z danymi adresowymi w postaci ustrukturyzowanej. Zrodlo: src/wymagania.md.
- WM-03: Rejestracja w Asseco CB przelewu odroczonego i zlecenia stalego z danymi adresowymi ustrukturyzowanymi. Zrodlo: src/wymagania.md.
- WM-04: Umozliwienie edycji aktywnego zlecenia stalego w zakresie danych adresowych ustrukturyzowanych i przekazanie tej edycji do Asseco CB. Zrodlo: src/wymagania.md.
- WM-05: Rozbudowa formatow importu przelewow i szablonow o ustrukturyzowane dane adresowe. Zrodlo: src/wymagania.md.
- WM-06: Rozbudowa ERP API, BS API i PSD2 API o obsluge danych ustrukturyzowanych dla przelewow ELIXIR. Zrodlo: src/wymagania.md.
## 2. Perspektywa biznesowa rozwiazania
### 2.1. Slownik pojec
<!-- SPW-SECTION
Cel: Zdefiniuj terminy uzywane w dokumencie (lub wskaz, ze obowiazuje slownik zrodlowy).
Zrodla: Dokumentacja systemu: doc/* (np. doc/glossary.md)
Wyjscie: lista pojec i definicji; bez wprowadzania nowych znaczen.
-->
- **BE**: System bankowosci elektronicznej. Zrodlo: doc/glossary.md.
- **EBP**: Modul BE dla kontekstu mikro i firmowego (korporacyjnego). Zrodlo: doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md.
- **CBP**: Modul BE dla kontekstu indywidualnego. Zrodlo: doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md.
- **CB (Asseco CB)**: System transakcyjny banku (master data) integrowany z BE. Zrodlo: src/wymagania.md.
- **Payment Hub (PH)**: System rozliczeniowy integrowany z Asseco CB dla ELIXIR XML. Zrodlo: src/wymagania.md oraz doc/CB/opsi zmian w CB dla elixir xml.md.
- **ELIXIR XML**: Format wymiany danych ELIXIR zgodny z ISO 20022. Zrodlo: src/wymagania.md.
### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objetym zmiana (as-is).
Zrodla: Dokumentacja systemu: doc/*
Wyjscie: krotki opis + kluczowe ograniczenia i zaleznosci.
-->
System BE dziala w podziale na konteksty klienta: CBP (indywidualny) oraz EBP (mikro i firmowy), w kanalach desktop i mobile. W miniaplikacji Przelewy dostepne sa przelewy biezace ELIXIR, przelewy odroczone i zlecenia stale, wraz z operacjami edycji i anulowania. Formularze przelewow w EBP i CBP zawieraja pola adresowe odbiorcy, a walidacje zalezne sa od typu przelewu i parametryzacji banku. Import przelewow i szablonow jest obslugiwany, w tym formaty XML i formaty historyczne, gdzie wystepuje mapowanie danych odbiorcy oparte m.in. o pola nazwy 4x35. BE wywoluje API Asseco CB (w tym inserttransferdoc) dla realizacji przelewow ELIXIR. Ograniczeniem jest brak kompletnej specyfikacji docelowych kontraktow ERP API, BS API i PSD2 API dla ELIXIR XML.
Kluczowe zrodla as-is:
- doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md
- doc/EBP/Miniaplikacja_Przelewy.adoc
- doc/CBP/Miniaplikacja_Przelewy.adoc
- doc/EBP/Import_Eksport_Danych.adoc
- doc/CB/opis-systemu-CB (BE).md
### 2.3. Model rozwiazania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiazania w zakresie zmian (to-be) na poziomie biznesowym.
Zrodla: src/*, doc/*
Wyjscie: opis przeplywu + kluczowe decyzje biznesowe.
-->
Docelowo BE (EBP i CBP) ma przekazywac do Asseco CB dane przelewow ELIXIR w modelu zgodnym z ELIXIR XML (ISO 20022), tj. z rozdzieleniem danych na nazwe i adres ustrukturyzowany. Zmiana obejmuje przelewy biezace, przelewy odroczone i zlecenia stale, w tym edycje aktywnych zlecen stalych. Zakres obejmuje takze import przelewow i szablonow oraz interfejsy ERP API, BS API i PSD2 API. Po stronie Asseco CB wymagane sa interfejsy obslugujace dane ustrukturyzowane oraz integracja z Payment Hub dla procesowania ELIXIR XML. W okresie przejsciowym dokumentacja CB dopuszcza obsluge danych nieustrukturyzowanych; sposob i termin wygaszenia trybu przejsciowego wymagaja decyzji biznesowo-architektonicznej.
## 3. Wymagania szczegolowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiazania na nowe i modyfikowane wymagania/user stories.
Zrodla: Wymagania klienta: src/*
-->
### 3.1 Wymagania funkcjonalne
#### RQ-001 - Kompensacja zmian w API Asseco CB
**Opis:**
System BE zapewnia kompatybilnosc funkcjonalna EBP i CBP przy zmianach API Asseco CB dla przelewow biezacych i odroczonych.
**Stan obecny (as-is):**
BE realizuje przelewy przez wywolania API Asseco CB, w tym inserttransferdoc; EBP/CBP obsluguja przelewy biezace i odroczone.
**Opis modyfikacji (to-be):**
BE dostosowuje warstwe integracyjna do zmian API CB zwiazanych z ELIXIR XML bez utraty funkcji biznesowych dostepnych obecnie dla Uzytkownika.

- Wymagane dlugosci pol:
  - Nazwa odbiorcy (`Nm`): `text{1,140}`; pole wymagane w modelu ELIXIR XML.
  - Pole `Tytulem`: maksymalnie `140` znakow w formularzach BE; dla danych przekazywanych w formacie historycznym `4*35` stosowane jest laczenie do `140` znakow.

**AC (Given/When/Then):**
- Given Uzytkownik ma uprawnienia do przelewow w EBP/CBP, 
- When zleca przelew biezacy lub odroczony, Then dyspozycja jest przekazana przez BE do Asseco CB przez zaktualizowany interfejs i otrzymuje status zgodny z wynikiem przetwarzania.
- Given API CB zwraca blad kontraktu dla zlecenia, When BE odbiera odpowiedz, Then BE prezentuje blad i nie traci danych wprowadzonych przez Uzytkownika.


**Zrodla:** src/wymagania.md (WM-01), doc/CB/opis-systemu-CB (BE).md, doc/CB/opsi zmian w CB dla elixir xml.md, doc/EBP/Miniaplikacja_Przelewy.adoc, doc/CBP/Miniaplikacja_Przelewy.adoc.
#### RQ-002 - Przelew biezacy ELIXIR z danymi ustrukturyzowanymi
**Opis:**
System BE przekazuje przelew biezacy ELIXIR do Asseco CB z danymi odbiorcy/nadawcy w modelu nazwa + adres ustrukturyzowany.
**Stan obecny (as-is):**
Formularze przelewow w EBP/CBP udostepniaja pola adresowe odbiorcy; walidacje sa zalezne od typu przelewu i parametryzacji.
**Opis modyfikacji (to-be):**
Dla przelewu biezacego ELIXIR system mapuje dane z formularza BE do struktury danych wymaganej przez ELIXIR XML po stronie CB.
**AC (Given/When/Then):**
- Given Uzytkownik wypelnil wymagane pola przelewu ELIXIR, When wybiera autoryzacje i zatwierdza dyspozycje, Then BE przekazuje do CB dane odbiorcy/nadawcy w modelu ustrukturyzowanym.
- Given nie uzupelniono wymaganych danych adresowych dla scenariusza, ktory ich wymaga, When Uzytkownik probuje przejsc dalej, Then system blokuje zapis i pokazuje komunikat walidacyjny.
**Zrodla:** src/wymagania.md (WM-02), doc/EBP/Miniaplikacja_Przelewy.adoc, doc/CBP/Miniaplikacja_Przelewy.adoc, doc/CB/opsi zmian w CB dla elixir xml.md.
#### RQ-003 - Rejestracja przelewu odroczonego i zlecenia stalego
**Opis:**
System BE rejestruje w Asseco CB przelew odroczony i zlecenie stale z danymi adresowymi ustrukturyzowanymi.
**Stan obecny (as-is):**
W EBP i CBP dostepne sa procesy tworzenia, autoryzacji, edycji i anulowania przelewow odroczonych oraz zlecen stalych.
**Opis modyfikacji (to-be):**
BE rozszerza mapowanie danych dla przelewu odroczonego i zlecenia stalego tak, aby w rejestracji w CB przekazywac dane zgodne z ELIXIR XML.
**AC (Given/When/Then):**
- Given Uzytkownik tworzy przelew odroczony lub zlecenie stale, When zatwierdza dyspozycje, Then dyspozycja jest zapisana w CB z danymi ustrukturyzowanymi.
- Given Uzytkownik nie ma wymaganych uprawnien, When probuje zarejestrowac dyspozycje, Then system odrzuca akcje i komunikuje brak uprawnien.
**Zrodla:** src/wymagania.md (WM-03), doc/EBP/Miniaplikacja_Przelewy.adoc, doc/CBP/Miniaplikacja_Przelewy.adoc, doc/EBP/Main.adoc.
#### RQ-004 - Edycja aktywnego zlecenia stalego
**Opis:**
System BE umozliwia edycje aktywnego zlecenia stalego i przekazuje zmienione dane adresowe ustrukturyzowane do Asseco CB.
**Stan obecny (as-is):**
Edycja i anulowanie zlecen stalych sa dostepne w EBP/CBP; zakres zalezy od parametryzacji banku.
**Opis modyfikacji (to-be):**
Dla procesu edycji aktywnego zlecenia stalego BE stosuje ten sam model danych ustrukturyzowanych co dla nowej rejestracji i utrzymuje dotychczasowy proces autoryzacji.
**AC (Given/When/Then):**
- Given aktywne zlecenie stale istnieje i Uzytkownik ma prawo edycji, When zmienia dane odbiorcy i zatwierdza edycje, Then BE przekazuje do CB zaktualizowane dane ustrukturyzowane.
- Given bank ma wylaczona mozliwosc edycji zlecen stalych parametryzacja, When Uzytkownik wybiera akcje edycji, Then system nie udostepnia lub blokuje edycje zgodnie z konfiguracja.
**Zrodla:** src/wymagania.md (WM-04), doc/CBP/Miniaplikacja_Przelewy.adoc, doc/EBP/Main.adoc, doc/CB/opsi zmian w CB dla elixir xml.md.
#### RQ-005 - Rozbudowa importu przelewow i szablonow
**Opis:**
System BE rozszerza import przelewow i szablonow o obsluge ustrukturyzowanych danych adresowych.
**Stan obecny (as-is):**
Import przelewow i szablonow dziala dla wielu formatow (m.in. XML i formaty historyczne), z mapowaniem danych opartym takze o pola nazw 4x35.
**Opis modyfikacji (to-be):**
Dla formatow objetych zakresem zmiany BE przyjmuje i mapuje dane adresowe ustrukturyzowane do modelu ELIXIR XML oraz zachowuje walidacje plikow i obsluge bledow importu.
**AC (Given/When/Then):**
- Given Uzytkownik wybiera plik importu zgodny z nowym zakresem danych, When uruchamia import, Then system waliduje i zapisuje poprawne rekordy z mapowaniem adresu ustrukturyzowanego.
- Given w pliku sa rekordy bledne i poprawne, When import sie konczy, Then system prezentuje liczbe poprawnych i blednych rekordow oraz przyczyny odrzucenia blednych rekordow.
**Zrodla:** src/wymagania.md (WM-05), doc/EBP/Import_Eksport_Danych.adoc, doc/EBP/Miniaplikacja_Przelewy.adoc, doc/CBP/Miniaplikacja_Przelewy.adoc, doc/CB/opsi zmian w CB dla elixir xml.md.
#### RQ-006 - Rozbudowa ERP API, BS API i PSD2 API
**Opis:**
System BE rozszerza uslugi ERP API, BS API i PSD2 API o obsluge danych ustrukturyzowanych dla przelewow ELIXIR.
**Stan obecny (as-is):**
W dokumentacji dostepne sa odniesienia do kanalu API (BS.API) oraz do integracji BE z API CB, ale brak pelnych kontraktow dla wszystkich wskazanych API w zakresie ELIXIR XML.
**Opis modyfikacji (to-be):**
Interfejsy ERP API, BS API i PSD2 API maja przyjmowac/przekazywac model danych zgodny z ELIXIR XML dla danych nadawcy i odbiorcy.
**AC (Given/When/Then):**
- Given klient integracyjny wywoluje endpoint API dla przelewu ELIXIR, When przekazuje dane nazwy i adresu ustrukturyzowanego, Then API waliduje dane i przekazuje dyspozycje do dalszego przetwarzania BE/CB.
- Given klient integracyjny przekazuje dane niezgodne z kontraktem API, When walidacja konczy sie bledem, Then API zwraca blad walidacyjny z kodem i opisem.
**Zrodla:** src/wymagania.md (WM-06), doc/BO/BackofficeUserGuide-pl.adoc, doc/CB/opis-systemu-CB (BE).md, doc/CB/opsi zmian w CB dla elixir xml.md.
**OPEN-QUESTION-001:** Jaki jest docelowy katalog kodow bledow i mapowanie bledow Asseco CB/PH na komunikaty w EBP i CBP?
**OPEN-QUESTION-002:** Czy dla ERP API, BS API i PSD2 API obowiazuje jednolity kontrakt odpowiedzi bledow i jednolita lista kodow dla ELIXIR XML?
### 3.1.1 Obsluga bledow
- System waliduje dane wymagane przed przekazaniem dyspozycji do CB, w tym dane odbiorcy i pola wymagane dla typu przelewu.
- W przypadku bledu walidacji system blokuje przejscie do autoryzacji i wskazuje przyczyne odrzucenia.
- W procesach importu system rozdziela rekordy poprawne i bledne oraz prezentuje przyczyne bledu dla rekordow odrzuconych.
- W przypadku bledu z systemu zewnetrznego (CB/PH/API) system zachowuje informacje diagnostyczna potrzebna do audytu i prezentuje komunikat dla Uzytkownika zgodny z kontraktem bledu.
- Szczegolowe mapowanie kodow bledow do komunikatow uzytkownika pozostaje otwarte: OPEN-QUESTION-001, OPEN-QUESTION-002.
### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Zrodla: src/*, doc/*
Wyjscie: wymagania testowalne + mierzalne kryteria akceptacji, jesli mozliwe.
-->
---
#### 3.2.1. Wydajnosc
- W procesie importu przelewow obowiazuje limit MAX_LICZBA_PRZELEWOW_DO_IMPORTU (domyslnie 100) i system waliduje plik przed zapisem danych.
- Asynchroniczny import przelewow posiada limity liczby rekordow i rozmiaru pliku konfigurowane parametrami technicznymi.
- OPEN-QUESTION-003: Czy wdrozenie ELIXIR XML zmienia limity wolumenu importu i czasy przetwarzania dla importu przelewow i szablonow?
#### 3.2.2. Bezpieczenstwo
- Funkcje przelewow i importu pozostaja objete mechanizmami uprawnien i autoryzacji obecnymi w BE.
- Dostep do funkcji zalezy od kontekstu klienta i uprawnien nadanych uzytkownikowi.
- OPEN-QUESTION-004: Jakie dodatkowe wymagania bezpieczenstwa (np. podpis, audit trail API, ograniczenia dla kanalow API) sa wymagane dla danych ustrukturyzowanych ELIXIR XML?
#### 3.2.3. Wdrozenie i proces migracji danych
- Dokumentacja zmian CB dopuszcza przejsciowo obsluge danych nieustrukturyzowanych w API i interfejsach plikowych, z planowanym przejsciem na wymagalnosc danych ustrukturyzowanych.
- OPEN-QUESTION-005: Jaki jest docelowy harmonogram i sposob migracji po stronie BE dla kanalow EBP, CBP, ERP API, BS API, PSD2 API?
- OPEN-QUESTION-006: Czy wymagane jest wsparcie rownolegle dla starego i nowego formatu danych po stronie BE, a jesli tak to do kiedy?

## 5. Wymagane licencje
<!-- SPW-SECTION
Cel: WskaĹĽ licencje / zaleĹĽnoĹ›ci licencyjne wymagane przez rozwiÄ…zanie.
ĹąrĂłdĹ‚a: src/*, doc/*
WyjĹ›cie: lista licencji i zakres ich uĹĽycia.
Generowanie: POMIĹ (ten rozdziaĹ‚ uzupeĹ‚niany rÄ™cznie)
-->
---
## 6. Obszary pod wpĹ‚ywem
<!-- SPW-SECTION
Cel: WymieĹ„ systemy, moduĹ‚y, procesy i kanaĹ‚y dotkniÄ™te zmianÄ….
ĹąrĂłdĹ‚a: src/*, doc/*
WyjĹ›cie: lista obszarĂłw + krĂłtki opis wpĹ‚ywu.
Generowanie: POMIĹ (ten rozdziaĹ‚ uzupeĹ‚niany rÄ™cznie)
-->
---
## 7. ZaĹ‚oĹĽenia i ograniczenia
<!-- SPW-SECTION
Cel: Zapisz zaĹ‚oĹĽenia, ograniczenia oraz decyzje projektowe wpĹ‚ywajÄ…ce na zakres.
ĹąrĂłdĹ‚a: src/*, doc/*
WyjĹ›cie: lista punktĂłw; brakujÄ…ce dane oznaczaj OPEN-QUESTION.
Generowanie: POMIĹ (ten rozdziaĹ‚ uzupeĹ‚niany rÄ™cznie)
-->

## 8. Zagadnienia otwarte
- OPEN-QUESTION-001: Jaki jest docelowy katalog kodow bledow i mapowanie bledow Asseco CB/PH na komunikaty w EBP i CBP?
- OPEN-QUESTION-002: Czy dla ERP API, BS API, PSD2 API obowiazuje jednolity kontrakt odpowiedzi bledow i jednolita lista kodow dla ELIXIR XML?
- OPEN-QUESTION-003: Czy wdrozenie ELIXIR XML zmienia limity wolumenu importu i czasy przetwarzania dla importu przelewow i szablonow?
- OPEN-QUESTION-004: Jakie dodatkowe wymagania bezpieczenstwa (np. podpis, audit trail API, ograniczenia dla kanalow API) sa wymagane dla danych ustrukturyzowanych ELIXIR XML?
- OPEN-QUESTION-005: Jaki jest docelowy harmonogram i sposob migracji po stronie BE dla kanalow EBP, CBP, ERP API, BS API, PSD2 API?
- OPEN-QUESTION-006: Czy wymagane jest wsparcie rownolegle dla starego i nowego formatu danych po stronie BE, a jesli tak to do kiedy?
## 9. ZaĹ‚Ä…czniki
<!-- SPW-SECTION
Cel: DoĹ‚Ä…cz lub wskaĹĽ materiaĹ‚y referencyjne (np. diagramy, tabele, sĹ‚owniki, zrzuty).
ĹąrĂłdĹ‚a: src/*, doc/*
WyjĹ›cie: lista zaĹ‚Ä…cznikĂłw + identyfikatory/odnoĹ›niki.
Generowanie: POMIĹ (ten rozdziaĹ‚ uzupeĹ‚niany rÄ™cznie)
-->

