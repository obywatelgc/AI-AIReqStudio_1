<!-- AI-CONSTRAINTS
Zakres: Opis zakresu modyfikacji
Format: RQ-ACT-###
Źródła: 
    Wymagania klienta: src/*, 
    Dokumentacja systemu: doc/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagań – Elixir XML

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz główny cel biznesowy rozwiązania dla wskazanego zakresu modyfikacji.
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
Źródła: Wymagania klienta: src/*
Wyjście: 3–5 zdań.
Kryteria jakości: jednoznaczność, brak domysłów, spójność terminologii.
-->
Celem biznesowym projektu jest dostosowanie bankowości elektronicznej BE (CBP i EBP) oraz integracji BE z systemem transakcyjnym Asseco CB do standardu ELIXIR XML (ISO 20022). Zmiana ma zapewnić obsługę danych adresowych w postaci ustrukturyzowanej dla procesów płatniczych objętych zakresem klienta. Zakres obejmuje utrzymanie ciągłości realizacji przelewów w BE przy zmianach interfejsów API po stronie CB. Projekt ma też ograniczyć ryzyko operacyjne wynikające z niespójności formatów danych między BE i CB.

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->
- `WM-01`: Integracja Asseco CB z Payment Hub w ramach płatności ELIXIR XML (`src/wymagania.md`).
- `WM-01`: Kompensacja zmian w API Asseco CB dla zlecania przelewów bieżących i odroczonych z BE (`src/wymagania.md`).
- `WM-02`: Przekazywanie przelewu bieżącego (ELIXIR) do Asseco CB z danymi adresowymi ustrukturyzowanymi (`src/wymagania.md`).
- `WM-03`: Rejestracja przelewu odroczonego i zlecenia stałego w Asseco CB z danymi adresowymi ustrukturyzowanymi (`src/wymagania.md`).
- `WM-04`: Edycja aktywnego zlecenia stałego i przekazanie zmian do Asseco CB w postaci danych ustrukturyzowanych (`src/wymagania.md`).
- `WM-05`: Rozbudowa importu przelewów i szablonów o obsługę ustrukturyzowanych danych adresowych (`src/wymagania.md`).
- `WM-06`: Rozbudowa ERP API, BS API i PSD2 API o obsługę danych ustrukturyzowanych dla przelewów ELIXIR (`src/wymagania.md`).

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: doc/* (np. doc/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->
- `BE` - system bankowości elektronicznej (`doc/glossary.md`).
- `CBP` - moduł BE dla kontekstu indywidualnego (detal/osobisty) (`doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md`).
- `EBP` - moduł BE dla kontekstu mikro i instytucjonalnego/korporacyjnego (`doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md`).
- `CB` - system transakcyjny banku (master data) współpracujący z BE przez API (`doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md`, `doc/CB/opis-systemu-CB (BE).md`).
- `Payment Hub (PH)` - system rozliczeniowy wskazany w wymaganiach klienta (`src/wymagania.md`).
- `ELIXIR XML` - nowy format wymiany danych dla rozliczeń ELIXIR w PLN, implementujący ISO 20022 (`src/wymagania.md`).

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: doc/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->
System BE działa w modułach CBP (detal) i EBP (mikro/korpo) oraz obejmuje kanały desktop i mobile. BE pobiera z CB dane klienta, umów i historii oraz zleca przelewy do CB przez API (`inserttransferdoc`). W aktywnych funkcjonalnościach bankowości internetowej część procesów obsługuje dane adresowe ustrukturyzowane, część wyłącznie zagregowane, a część nie obsługuje pól adresowych. Dla przelewów ELIXIR, odroczonych i zleceń stałych dane adresowe mogą być wprowadzane jako ustrukturyzowane, ale przy wysyłce do systemu transakcyjnego są agregowane do pola zbiorczego. W usługach API istnieją różnice: ERP API i PSD2 API posiadają pola dla danych ustrukturyzowanych (dla SORBNET/SWIFT/SEPA), natomiast BS API nie ma dedykowanych pól ustrukturyzowanych.

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: src/*, doc/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->
Docelowo BE (CBP i EBP) przekazuje do CB dane płatności ELIXIR z obsługą danych adresowych w postaci ustrukturyzowanej dla przypadków wskazanych w wymaganiach klienta: przelew bieżący, przelew odroczony, zlecenie stałe, edycja zlecenia stałego, import przelewów i szablonów oraz API (ERP/BS/PSD2). Integracja BE-CB musi zostać dostosowana do zmian interfejsów CB, aby utrzymać ciągłość procesów płatniczych po wdrożeniu ELIXIR XML. W modelu docelowym obowiązuje współistnienie danych ustrukturyzowanych i dotychczasowych danych w formacie 4*35 w okresie przejściowym po stronie API CB. Zakres niniejszej specyfikacji obejmuje BE i integrację z CB; wewnętrzna komunikacja CB-Payment Hub jest uwzględniona wyłącznie w stopniu wpływu na interfejsy BE-CB.

## 3. Wymagania szczegółowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiązania na nowe i modyfikowane wymagania/user stories.
Źródła: Wymagania klienta: src/*
-->
### 3.1 Wymagania funkcjonalne

#### RQ-ACT-001: Kompensacja zmian API CB dla przelewów BE
**Opis:** System BE (CBP + EBP) musi zostać dostosowany do zmian interfejsów API Asseco CB dla zlecania przelewów bieżących i odroczonych, tak aby zachować obsługę procesów płatniczych po wdrożeniu ELIXIR XML.

Po stronie CB przewidziano dostosowanie interfejsów REST/WS (w tym `inserttransferdoc`) do przekazywania danych Nadawcy/Odbiorcy w modelu `Nm` + `PstlAdr/*` dla dokumentów przelewów, poleceń zapłaty, zleceń stałych oraz wybranych umów. Równolegle utrzymano zgodność przejściową z formatem 4*35 (konwersja do `Nm` 140 znaków bez wypełnienia adresu ustrukturyzowanego). Dodatkowo komunikacja rozliczeniowa CB przechodzi z modelu komunikatów/sesji KIR na model danych biznesowych integrowanych z Payment Hub.

**Uzasadnienie:** Wymaganie wynika bezpośrednio z `WM-01` oraz z faktu, że BE realizuje zlecanie przelewów przez API CB.

**AC:**
- Given BE korzysta z API CB do zlecania przelewów bieżących i odroczonych,
- When po stronie CB zostaną wdrożone zmiany API związane z ELIXIR XML,
- Then BE realizuje rejestrację przelewu bieżącego i odroczonego bez utraty funkcjonalnej integracji z CB.

---

#### RQ-ACT-002: Przekazanie przelewu bieżącego ELIXIR z danymi ustrukturyzowanymi
**Opis:** BE musi przekazywać do CB przelew bieżący (ELIXIR) z danymi adresowymi odbiorcy w postaci ustrukturyzowanej.

W stanie obecnym dla przelewu zwykłego ELIXIR w CBP i EBP użytkownik może wprowadzić odbiorcę oraz adres odbiorcy w polach rozbitych (co najmniej: ulica, nr domu, nr mieszkania, kod pocztowy, miejscowość; szczegóły zależne od parametryzacji banku). Dane adresowe są opcjonalne. Przy wysyłce do systemu transakcyjnego dane są agregowane do zbiorczego pola danych odbiorcy.

**Uzasadnienie:** Wymaganie wynika z `WM-02` i z kierunku zmian do ELIXIR XML (ISO 20022), gdzie dane adresowe są obsługiwane jako ustrukturyzowane.

**AC:**
- Given użytkownik BE wprowadza przelew bieżący ELIXIR z danymi odbiorcy,
- When zlecenie jest przekazywane z BE do CB,
- Then dane odbiorcy są przekazane w postaci ustrukturyzowanej zgodnie z zakresem danych obsługiwanym przez API CB.

---

#### RQ-ACT-003: Rejestracja przelewu odroczonego i zlecenia stałego z danymi ustrukturyzowanymi
**Opis:** BE musi rejestrować w CB zlecenie przelewu odroczonego i zlecenie stałe z danymi adresowymi w postaci ustrukturyzowanej.

**Uzasadnienie:** Wymaganie wynika z `WM-03` oraz z zakresu zmian interfejsów API CB dla dokumentów płatniczych i zleceń stałych.

**AC:**
- Given użytkownik BE rejestruje przelew odroczony albo zlecenie stałe ELIXIR,
- When dane są zapisywane w CB,
- Then CB otrzymuje dane adresowe odbiorcy w postaci ustrukturyzowanej.

---

#### RQ-ACT-004: Edycja aktywnego zlecenia stałego z przekazaniem danych ustrukturyzowanych
**Opis:** BE musi umożliwiać edycję aktywnego zlecenia stałego w zakresie danych adresowych ustrukturyzowanych i przekazywać te zmiany do CB.

**Uzasadnienie:** Wymaganie wynika z `WM-04` i utrzymuje spójność danych płatności ELIXIR między BE i CB po modyfikacji zlecenia.

**AC:**
- Given w BE istnieje aktywne zlecenie stałe ELIXIR,
- When użytkownik edytuje dane adresowe odbiorcy w zakresie obsługiwanym przez BE,
- Then BE przekazuje zmienione dane ustrukturyzowane do CB i zapis zmian jest możliwy bez zmiany trybu obsługi zlecenia.

---

#### RQ-ACT-005: Rozbudowa importu przelewów i szablonów o dane adresowe ustrukturyzowane
**Opis:** BE musi rozszerzyć import przelewów i szablonów o obsługę ustrukturyzowanych danych adresowych dla przelewów ELIXIR.

**Uzasadnienie:** Wymaganie wynika z `WM-05`; w stanie obecnym część importów wykorzystuje dane zagregowane lub brak dedykowanych pól ustrukturyzowanych.

**AC:**
- Given użytkownik importuje przelew ELIXIR lub szablon przelewu z danymi adresowymi,
- When plik importu zostanie poprawnie przetworzony przez BE,
- Then BE zapisuje i przekazuje do CB dane adresowe w postaci ustrukturyzowanej dla obsługiwanych formatów importu.

---

#### RQ-ACT-006: Rozbudowa ERP API, BS API i PSD2 API dla ELIXIR XML
**Opis:** BE musi rozszerzyć usługi ERP API, BS API i PSD2 API tak, aby obsługiwały dane adresowe ustrukturyzowane w przelewach ELIXIR.

**Uzasadnienie:** Wymaganie wynika z `WM-06`; dodatkowo stan obecny wskazuje niespójność między API (w szczególności BS API bez dedykowanych pól ustrukturyzowanych).

**AC:**
- Given system zewnętrzny wywołuje ERP API, BS API albo PSD2 API dla przelewu ELIXIR,
- When żądanie zawiera dane adresowe odbiorcy w postaci ustrukturyzowanej,
- Then BE przyjmuje i przekazuje te dane do CB zgodnie z zakresem integracji dla ELIXIR XML.

---

#### 3.1.1 Obsługa błędów
(Ta sekcja MUSI istnieć)
- W źródłach CB zdefiniowano kody błędów i odrzuceń (m.in. `rejectCode`, `directDebitReturnCode` oraz słownik `External Code Sets`), ale brak mapowania tych kodów na komunikaty użytkownika w BE.
- Wymagane jest doprecyzowanie zasad walidacji danych adresowych ustrukturyzowanych na wejściu BE (kanały UI oraz API), w tym reakcji na brak/niepoprawny format pól.
- Wymagane jest doprecyzowanie obsługi błędów częściowych dla importu (rekord poprawny/rekord błędny) oraz sposobu raportowania wyników.
- Wymagane jest uzgodnienie translacji błędów CB na poziomy błędów BE (techniczny/biznesowy) wraz z zasadami prezentacji komunikatów.

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: src/*, doc/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->
---
#### 3.2.1. Wydajność
- Brak mierzalnych parametrów wydajnościowych (SLA/SLO, czasy odpowiedzi API, wolumeny) w `src/*` i `doc/*` dla zakresu ELIXIR XML w BE.
- `OPEN-QUESTION-001`: Jakie są docelowe czasy odpowiedzi i wolumeny dla operacji BE-CB objętych wymaganiami `RQ-ACT-001` do `RQ-ACT-006`?
#### 3.2.2. Bezpieczeństwo
- Dla klienta firmowego (EBP) dostęp do funkcji pozostaje kontrolowany uprawnieniami per obszar funkcjonalny; zmiana nie może naruszyć modelu uprawnień.
- Integracje z systemami zewnętrznymi muszą respektować kontekst klienta (detal/mikro/korpo) oraz model uprawnień.
- `OPEN-QUESTION-002`: Jakie dodatkowe wymagania bezpieczeństwa (audyt, maskowanie danych, retencja logów) obowiązują dla nowych pól adresowych ELIXIR XML?
#### 3.2.3. Wdrożenie i proces migracji danych
- W zakresie API CB dopuszczalne jest przekazywanie danych w dotychczasowym formacie (4*35) równolegle z danymi ustrukturyzowanymi w okresie przejściowym.
- Warunek końca okresu przejściowego został określony źródłowo jako najbliższa zmiana formatu ELIXIR XML, która wykluczy przekazywanie danych bez adresu ustrukturyzowanego.
- `OPEN-QUESTION-003`: Jaki jest harmonogram komunikacji i wdrożenia daty granicznej wyłączenia formatu 4*35 po stronie BE-CB?
## 5. Wymagane licencje
<!-- SPW-SECTION
Cel: Wskaż licencje / zależności licencyjne wymagane przez rozwiązanie.
Źródła: src/*, doc/*
Wyjście: lista licencji i zakres ich użycia.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 6. Obszary pod wpływem
<!-- SPW-SECTION
Cel: Wymień systemy, moduły, procesy i kanały dotknięte zmianą.
Źródła: src/*, doc/*
Wyjście: lista obszarów + krótki opis wpływu.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 7. Założenia i ograniczenia
<!-- SPW-SECTION
Cel: Zapisz założenia, ograniczenia oraz decyzje projektowe wpływające na zakres.
Źródła: src/*, doc/*
Wyjście: lista punktów; brakujące dane oznaczaj OPEN-QUESTION.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->

## 8. Zagadnienia otwarte
- OPEN-QUESTION-004: Jak wygląda szczegółowa mapa pól UI BE (CBP/EBP) do pól API CB (`Nm`, `PstlAdr/*`) dla każdej operacji ELIXIR w zakresie `RQ-ACT-002` do `RQ-ACT-006`?
- OPEN-QUESTION-005: Jakie komunikaty użytkownika i akcje systemu BE mają odpowiadać kodom błędów CB (`External Code Sets`, `rejectCode`, `directDebitReturnCode`)?
- OPEN-QUESTION-006: Czy wszystkie wymagania `RQ-ACT-001` do `RQ-ACT-006` mają obowiązywać w obu kanałach (desktop i mobile) bez wyjątków?
## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: src/*, doc/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
