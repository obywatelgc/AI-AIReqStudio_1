<!-- AI-CONSTRAINTS
Zakres: Opis zakresu modyfikacji
Format: RQ-###
Źródła:
    Wymagania klienta: src/*,
    Dokumentacja systemu: doc/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagań - {{PROJECT_NAME}}

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz główny cel biznesowy rozwiązania dla wskazanego zakresu modyfikacji.
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
Źródła: Wymagania klienta: src/*
Wyjście: 3-5 zdań.
Kryteria jakości: jednoznaczność, brak domysłów, spójność terminologii.
-->
Celem biznesowym projektu jest dostosowanie BE (EBP i CBP) do modelu ELIXIR XML (ISO 20022) oraz do zmian po stronie Asseco CB i Payment Hub. Zakres obejmuje utrzymanie ciągłości procesów przelewów dla klientów indywidualnych i instytucjonalnych przy zmianie interfejsów integracyjnych. Projekt ma zapewnić obsługę danych adresowych ustrukturyzowanych w procesach zlecania, edycji i importu przelewów. Efektem biznesowym ma być ograniczenie ryzyka operacyjnego po wdrożeniu nowego formatu wymiany danych KIR.

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->
- WM-BE-01: Kompensacja zmian API Asseco CB dla zlecania przelewów bieżących i odroczonych (`src/wymagania.md#4.1 ELIXIR XML w BE`).
- WM-BE-02: Przekazywanie przelewu bieżącego ELIXIR do Asseco CB z danymi adresowymi ustrukturyzowanymi (`src/wymagania.md#4.1 ELIXIR XML w BE`).
- WM-BE-03: Rejestracja przelewu odroczonego i zlecenia stałego z danymi adresowymi ustrukturyzowanymi (`src/wymagania.md#4.1 ELIXIR XML w BE`).
- WM-BE-04: Edycja aktywnego zlecenia stałego w zakresie danych adresowych ustrukturyzowanych i przekazanie zmian do Asseco CB (`src/wymagania.md#4.1 ELIXIR XML w BE`).
- WM-BE-05: Rozbudowa importu przelewów i szablonów w EBP o dane adresowe ustrukturyzowane (`src/wymagania.md#4.1 ELIXIR XML w BE`).
- WM-BE-06: Rozbudowa usług BS API i PSD2 API wystawianych przez BE o obsługę danych ustrukturyzowanych dla przelewów ELIXIR (`src/wymagania.md#4.1 ELIXIR XML w BE`).

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: doc/* (np. doc/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->
Obowiązuje słownik bazowy: `doc/glossary.md`.

Dodatkowe terminy ze źródeł:
- **CBP** - moduł BE dla kontekstu indywidualnego.
- **EBP** - moduł BE dla kontekstu mikro i firmowego.
- **CB** - system transakcyjny banku (Asseco Core Banking).
- **Payment HUB (PH)** - system rozliczeniowy.
- **ELIXIR XML** - format wymiany danych dla rozliczeń ELIXIR oparty o ISO 20022.
- **BS API / PSD2 API** - API wystawiane przez BE (zakres zmian wskazany w `src/wymagania.md`).

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: doc/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->
BE działa w kontekstach CBP (indywidualny) oraz EBP (mikro/firmowy), z obsługą kanałów desktop i mobile. Dla kontekstu firmowego dostęp do funkcji jest kontrolowany uprawnieniami. BE integruje się z CB przez API, w tym do realizacji przelewów ELIXIR (`inserttransferdoc`).

W miniaplikacjach Przelewy (EBP i CBP) istnieje obsługa przelewów ELIXIR, odroczonych i cyklicznych, a formularze zawierają pola adresowe odbiorcy rozbite na pola składowe (np. kod pocztowy, miasto, ulica, nr domu). W CBP potwierdzono jawnie edycję zlecenia stałego, w EBP dostępna jest edycja aktywnej płatności zaplanowanej.

W EBP istnieją: konfiguracja formatów importu i eksportu, import przelewów, import szablonów oraz dokumentacja struktur plików (m.in. ISO20022). Część funkcji jest zależna od parametryzacji banku.

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: src/*, doc/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->
Model docelowy zakłada utrzymanie dotychczasowych procesów użytkownika w EBP i CBP przy jednoczesnym dostosowaniu wymiany danych do ELIXIR XML. Dla przelewów bieżących, odroczonych i zleceń stałych BE przekazuje do CB dane adresowe ustrukturyzowane. W obszarze EBP model obejmuje rozbudowę importu przelewów i szablonów o dane adresowe ustrukturyzowane. Zakres obejmuje też rozszerzenie API wystawianych przez BE (BS API i PSD2 API) o ten sam model danych.

## 3. Wymagania szczegółowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiązania na nowe i modyfikowane wymagania/user stories.
Źródła:
Wymagania klienta: src/*
Stan obecny (as-is): doc/**
AC: (pilnuj wcięć dla każdej z linii Given/When/Then)
-->
### 3.1 Wymagania funkcjonalne

#### RQ-001: Kompensacja zmian API Asseco CB dla przelewów ELIXIR
**Opis:** System BE zapewnia ciągłość obsługi zlecania przelewów bieżących i odroczonych mimo zmian interfejsów API po stronie Asseco CB.

**Stan obecny:** BE realizuje przelewy przez API systemu CB (w tym `inserttransferdoc`). Dokumentacja zmian CB wskazuje modyfikacje interfejsów API dla danych ustrukturyzowanych i dopuszczenie formatu dotychczasowego.

**Opis modyfikacji:** BE kompensuje zmiany interfejsów API Asseco CB tak, aby procesy przelewów bieżących i odroczonych działały w nowym modelu ELIXIR XML.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-01)]`
- Stan obecny (as-is): `[doc/CB/opis-systemu-CB (BE).md#Opis funkcjonalny w odniesieniu do BE]`
- Stan obecny (as-is): `[doc/CB/opsi zmian w CB dla elixir xml.md#Ogólne założenia]`

**AC:**
- Given system BE obsługuje zlecenie przelewu bieżącego lub odroczonego,
- When BE wywołuje API CB po wdrożeniu ELIXIR XML,
- Then dyspozycja jest rejestrowana zgodnie z obowiązującym kontraktem API CB.

---

#### RQ-002: Przelew bieżący ELIXIR z danymi adresowymi ustrukturyzowanymi
**Opis:** System BE przekazuje do Asseco CB przelew bieżący ELIXIR z danymi adresowymi odbiorcy w postaci ustrukturyzowanej.

**Stan obecny:** W EBP i CBP formularze przelewów zawierają pola adresowe odbiorcy rozbite na pola składowe. Istnieje obsługa przelewu zwykłego ELIXIR.

**Opis modyfikacji:** Dla przelewu bieżącego ELIXIR BE przekazuje do CB dane odbiorcy z adresem ustrukturyzowanym.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-02)]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Przelewy.adoc#Zlecenie przelewu zwykłego krajowego]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Przelewy.adoc#Zlecenie przelewu zwykłego krajowego]`

**AC:**
- Given użytkownik tworzy przelew bieżący ELIXIR w EBP lub CBP,
- When uzupełni dane odbiorcy i zaakceptuje dyspozycję,
- Then BE przekazuje do CB dane adresowe odbiorcy w postaci ustrukturyzowanej.

---

#### RQ-003: Rejestracja przelewu odroczonego i zlecenia stałego z adresem ustrukturyzowanym
**Opis:** System BE rejestruje w CB przelewy odroczone i zlecenia stałe z danymi adresowymi ustrukturyzowanymi.

**Stan obecny:** W EBP i CBP istnieje obsługa przelewów odroczonych i zleceń stałych. Dane adresowe odbiorcy są obsługiwane na formularzach przelewów.

**Opis modyfikacji:** Dla rejestracji przelewu odroczonego i zlecenia stałego BE przekazuje do CB dane adresowe odbiorcy w modelu ustrukturyzowanym. Rejestracja w CB przebiega następująco:
- Użytkownik w EBP/CBP definiuje dyspozycję z datą realizacji (przelew odroczony) albo zaznacza opcję zlecenia stałego i uzupełnia parametry cyklu (`Powtarzaj co`, `Data zakończenia` albo `Bezterminowo`).
- Użytkownik zatwierdza dyspozycję aktualnie posiadaną metodą autoryzacji; BE prezentuje potwierdzenie przekazania dyspozycji do realizacji.
- BE rejestruje przelew odroczony przez REST API CB: `POST /application/api/payment-order/sepa-payment-orders/outgoing` albo `POST /application/api/payment-order/swift-payment-orders/outgoing/{incarnation}`.
- BE rejestruje zlecenie stałe przez REST API CB: `POST /application/api/current-account/current-accounts/{contractId}/standing-orders`.
- W obu ścieżkach BE przekazuje dane Nadawcy/Odbiorcy zgodnie z modelem adresu ustrukturyzowanego wymaganym w API CB dla ELIXIR XML.
- Po rejestracji dyspozycja jest dostępna na listach przelewów zaplanowanych (`Aktywne`/`Oczekujące`) oraz na liście `Zlecenia stałe`.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-03)]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Przelewy.adoc#Przeglądanie listy przelewów]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Przelewy.adoc#Oczekujące]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Przelewy.adoc#Zlecenia stałe]`
- Stan obecny (as-is): `[doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md#8. Wybrane zagadnienia funkcjonalne i architektoniczne]`
- Stan obecny (as-is): `[doc/CB/opsi zmian w CB dla elixir xml.md#Interfejsy API]`

**AC:**
- Given użytkownik tworzy przelew odroczony albo zlecenie stałe,
- When zapisze i autoryzuje dyspozycję,
- Then BE rejestruje dyspozycję w CB z danymi adresowymi ustrukturyzowanymi.

---

#### RQ-004: Edycja aktywnego zlecenia stałego z przekazaniem danych ustrukturyzowanych
**Opis:** System BE umożliwia edycję aktywnego zlecenia stałego w zakresie danych adresowych ustrukturyzowanych i przekazuje zmiany do CB.

**Stan obecny:** W CBP istnieje dedykowana funkcja edycji zlecenia stałego (zależna od parametryzacji banku). W EBP dostępna jest edycja aktywnej płatności zaplanowanej.

**Opis modyfikacji:** Dla aktywnego zlecenia stałego BE przekazuje do CB zaktualizowane dane adresowe ustrukturyzowane.



**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-04)]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Przelewy.adoc#Edycja zlecenia stałego]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Przelewy.adoc#Przeglądanie listy przelewów]`

**AC:**
- Given użytkownik ma aktywne zlecenie stałe i uprawnienie do edycji,
- When edytuje dane i zatwierdzi dyspozycję,
- Then BE przekazuje do CB zmodyfikowane dane adresowe ustrukturyzowane.

---

#### RQ-005: Rozbudowa importu przelewów i szablonów w EBP o dane ustrukturyzowane
**Opis:** System EBP rozszerza import przelewów i import szablonów o obsługę danych adresowych ustrukturyzowanych.

**Stan obecny:** EBP obsługuje import przelewów oraz import szablonów, a konfiguracja formatów jest realizowana w opcji Ustawienia importu i eksportu. Dokumentacja zawiera struktury plików, w tym ISO20022.

**Opis modyfikacji:** W EBP formaty importu przelewów i szablonów są rozszerzane o dane adresowe ustrukturyzowane. W zakresie importu przelewów zwykłych:
- `Elixir`, `VideoTel`: system importuje dane odbiorcy (nazwa i adres) łącznie do pola `Odbiorca`.
- `XML`, `Liniowy`: system udostępnia dedykowane pola adresowe ustrukturyzowane, a pole nazwy odbiorcy rozszerza z 35 do 140 znaków.
- `Telekonto`: brak zmian; system odczytuje dane odbiorcy na podstawie numeru NRB z listy odbiorców zdefiniowanych.
W ramach projektu system dodaje także nowy format importu przelewu zwykłego: `ISO 20022`.


**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-05)]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Przelewy.adoc#Import szablonów przelewów]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Przelewy.adoc#Import przelewów]`
- Stan obecny (as-is): `[doc/EBP/Main.adoc#Ustawienia importu i eksportu]`
- Stan obecny (as-is): `[doc/EBP/Import_Eksport_Danych.adoc#Struktury plików]`

**AC:**
- Given użytkownik EBP importuje przelewy lub szablony,
- When plik zawiera dane adresowe ustrukturyzowane,
- Then system waliduje plik i rejestruje poprawne rekordy wraz z danymi adresowymi.

---

#### RQ-006: Rozbudowa BS API i PSD2 API o dane ustrukturyzowane ELIXIR
**Opis:** System BE rozszerza usługi BS API i PSD2 API o obsługę danych ustrukturyzowanych dla przelewów ELIXIR.

**Stan obecny:** W dostarczonej dokumentacji `doc/*` nie znaleziono jednoznacznego opisu aktualnego kontraktu BS API i PSD2 API dla przelewów ELIXIR.

**Opis modyfikacji:** Zakres WM-BE-06 wymaga rozszerzenia API wystawianych przez BE o pola danych adresowych ustrukturyzowanych dla przelewów ELIXIR.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#4.1 ELIXIR XML w BE (WM-BE-06)]`
- Stan obecny (as-is): `[doc/* - brak jednoznacznego opisu BS API i PSD2 API dla tego zakresu]`

**AC:**
- Given konsument korzysta z BS API lub PSD2 API dla przelewu ELIXIR,
- When przesyła lub odczytuje dane przelewu,
- Then API obsługuje dane adresowe ustrukturyzowane zgodnie z docelowym kontraktem API.

---

#### 3.1.1 Obsługa błędów
(Ta sekcja MUSI istnieć)

- Dla przelewu ELIXIR system odrzuca zapis typu ELIXIR, gdy bank odbiorcy nie jest uczestnikiem ELIXIR, i prezentuje komunikat o braku banku w ewidencji.
- Dla szablonu z niekompletnymi danymi odbiorcy system prezentuje komunikat o brakujących informacjach i wymusza uzupełnienie danych.
- Dla importu system sprawdza zgodność pliku ze strukturą i raportuje rekordy poprawne i błędne.
- Dla importu przekraczającego limit `MAX_LICZBA_PRZELEWOW_DO_IMPORTU` system prezentuje komunikat o zbyt dużej liczbie przelewów.
- Dla formatu liniowego bez załadowanej struktury system prezentuje ostrzeżenie `Puste struktury liniowe`.

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: src/*, doc/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->
---
#### 3.2.1. Wydajność
- NFR-001: Dla asynchronicznego importu przelewów system obsługuje plik do 25000 rekordów i rozmiaru do 10 MB.
- NFR-002: Maksymalna liczba jednocześnie trwających importów asynchronicznych wynosi 3.
- NFR-003: Dla importu synchronicznego limit liczby przelewów jest kontrolowany parametrem `MAX_LICZBA_PRZELEWOW_DO_IMPORTU` (wartość domyślna: 100).

#### 3.2.2. Bezpieczeństwo
- NFR-004: Dostęp do funkcji przelewów i akcji z nimi związanych pozostaje kontrolowany uprawnieniami.
- NFR-005: Anulowanie i edycja przelewów odroczonych/zleceń stałych wymaga akceptacji aktualną metodą autoryzacji.
- NFR-006: Dla importu szablonów autoryzacji podlega proces importu.

#### 3.2.3. Wdrożenie i proces migracji danych
- OPEN-QUESTION-001: Brak w źródłach planu wdrożenia zmian WM-BE-01..WM-BE-06 (kolejność, okno wdrożeniowe, rollback).
- OPEN-QUESTION-002: Brak potwierdzonego zakresu migracji danych historycznych szablonów/odbiorców do modelu adresu ustrukturyzowanego.
- OPEN-QUESTION-003: Brak kryteriów kompatybilności wstecznej dla danych nieustrukturyzowanych po stronie API wystawianych przez BE.

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
- OPEN-QUESTION-001: Jaki jest docelowy harmonogram wdrożenia zmian WM-BE-01..WM-BE-06 (środowiska, kolejność, rollback)?
- OPEN-QUESTION-002: Czy i w jakim zakresie należy migrować istniejące szablony/odbiorców do modelu danych adresowych ustrukturyzowanych?
- OPEN-QUESTION-003: Jaki jest docelowy kontrakt BS API dla przelewów ELIXIR XML (endpointy, pola, walidacje, wersjonowanie)?
- OPEN-QUESTION-004: Jaki jest docelowy kontrakt PSD2 API dla przelewów ELIXIR XML (zakres danych, zgodność regulacyjna, wersjonowanie)?

## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: src/*, doc/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
