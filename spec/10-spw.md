<!-- AI-CONSTRAINTS
Zakres: Integracja BE–CashDirector (aktywacja, SSO, płatności, rachunki, dezaktywacja, statusy płatności, leady, historia operacji)
Format: RQ-ACT-###
Źródła: 
    Wymagania klienta: /src/*, 
    Dokumentacja systemu: /doc_basic/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagań – {{PROJECT_NAME}}

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz główny cel biznesowy rozwiązania dla wskazanego zakresu modyfikacji.
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
Źródła: Wymagania klienta: /src/*
Wyjście: 3–5 zdań.
Kryteria jakości: jednoznaczność, brak domysłów, spójność terminologii.
-->

Celem projektu jest udostępnienie w systemie Bankowości Elektronicznej (BE) integracji z systemem księgowym CashDirector (CD) dla klientów instytucjonalnych (firm), w zakresie aktywacji usługi, logowania jednokrotnego (SSO), inicjowania płatności oraz wymiany informacji niezbędnych do obsługi księgowej. Rozwiązanie ma umożliwiać uruchomienie i utrzymanie usługi w ujęciu firmy (kontekstu firmowego) oraz obsługę dezaktywacji inicjowanej zarówno przez Bank, jak i CashDirector. Zakres obejmuje również przekazywanie do CashDirector danych o rachunkach, statusów płatności, leadów sprzedażowych oraz historii operacji bankowych – w zakresie opisanym w źródłach.

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: /src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->

- Integracja BE–CashDirector obejmuje: aktywację usługi, rejestrację/parowanie firmy i użytkownika, SSO, dezaktywację usługi (inicjowaną przez Bank lub CashDirector), inicjowanie i realizację płatności, przekazywanie statusów płatności, przekazywanie leadów sprzedażowych oraz przekazywanie historii operacji bankowych (`src/wymagania_funkcjonalne_be_integracja_z_cash_director v1.md`).
- Bank udostępnia usługi API wykorzystywane w integracji, m.in.: `customerContext` (SSO), `accounts` (lista rachunków), `unassignCompany` (odpięcie usługi), `domesticPaymentInit`/`domesticSplitPaymentInit`/`foreignPaymentInit`/`taxPaymentInit` (inicjowanie płatności) oraz `POST redirect (płatność)` (`src/banki-api-uslugi-banku.md`).
- `src/wymagania banku.md` nie zawiera treści (brak danych wejściowych).

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: /doc_basic/* (np. /doc_basic/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->

- **BE** – system bankowości elektronicznej.
- **CashDirector (CD)** – system księgowy.
- **Firma** – podmiot gospodarczy klienta banku.
- **Użytkownik** – osoba fizyczna działająca w imieniu firmy.
- **SSO** – Single Sign-On.
- **ssoToken** – jednorazowy, krótkoterminowy token przekazany w ramach redirecta z banku (na potrzeby SSO).
- **accessToken** – token autoryzujący wykorzystywany w usługach integracyjnych.
- **paymentToken** – token do wykonania płatności (wykorzystywany do przekierowania na formatkę przelewową).

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: /doc_basic/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->

System BE (Asseco EBP) umożliwia pracę w różnych kontekstach użytkownika (indywidualny oraz firmowy), z rozróżnieniem obszarów roboczych mikro i korporacyjnego, oraz przełączanie kontekstu w trakcie pracy. Po zalogowaniu użytkownik korzysta z pulpitu z miniaplikacjami/widżetami, których dostępność zależy od kontekstu. Dla klienta firmowego możliwe jest nadawanie uprawnień do poszczególnych opcji systemu. W trakcie korzystania z BE może wystąpić wylogowanie wynikające z wygaśnięcia sesji (np. po okresie bezczynności), co stanowi ograniczenie dla długotrwałych procesów realizowanych w kanale elektronicznym.

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: /src/*, /doc_basic/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->

W modelu docelowym użytkownik BE w kontekście firmowym uruchamia obsługę CashDirector z poziomu opcji „eKsięgowość”. System BE, w zależności od statusu aktywacji usługi dla firmy, prezentuje ekran aktywacji (gdy usługa nie jest aktywna) albo przekierowuje użytkownika do CashDirector w ramach SSO (gdy usługa jest aktywna). Aktywacja obejmuje prezentację wymaganych zgód/regulaminów/umów, rejestrację akceptacji oraz przekazanie do CashDirector danych identyfikacyjnych firmy i użytkownika w celu rejestracji/parowania usługi. Po aktywacji i w trakcie korzystania z usługi CashDirector możliwa jest wymiana danych integracyjnych, w tym pobieranie listy rachunków oraz inicjowanie płatności w BE z wykorzystaniem tokenów (SSO i płatności) oraz przekazywanie do CashDirector informacji o zdarzeniach (np. statusy płatności), leadach sprzedażowych i historii operacji – w zakresie wskazanym w wymaganiach klienta.

## 3. Wymagania szczegółowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiązania na nowe i modyfikowane wymagania/user stories.
Źródła: Wymagania klienta: /src/*
-->
### 3.1 Wymagania funkcjonalne

#### RQ-ACT-001: Punkt wejścia „eKsięgowość” dla usługi CashDirector
**Opis:** System BE musi udostępniać w menu głównym opcję „eKsięgowość” jako punkt wejścia do obsługi aktywacji lub uruchomienia usługi CashDirector.

**Uzasadnienie:** Wymagania klienta wskazują, że uruchomienie procesu aktywacji/usługi ma następować z poziomu bankowości elektronicznej poprzez dedykowaną opcję w menu.

**AC:**
- Given Użytkownik jest zalogowany do systemu BE
- When Użytkownik wybiera opcję „eKsięgowość”
- Then system uruchamia obsługę usługi CashDirector zgodnie z logiką statusu aktywacji usługi dla firmy

---

#### RQ-ACT-002: Status aktywacji usługi w ujęciu firmy i logika wejścia
**Opis:** System BE musi utrzymywać status aktywacji usługi CashDirector w ujęciu firmy (kontekstu firmowego) i wykorzystywać go do decyzji o prezentacji ekranu aktywacji lub przekierowaniu do CashDirector po wejściu przez „eKsięgowość”.

**Uzasadnienie:** Wymagania klienta definiują decyzję biznesową utrzymywania statusu aktywacji na firmie oraz użycie tego statusu w logice wejścia do usługi.

**AC:**
- Given Użytkownik jest w kontekście firmowym i wybiera „eKsięgowość”
- When status aktywacji usługi CashDirector dla bieżącej firmy jest „nieaktywna”
- Then system prezentuje ekran aktywacji usługi
- Given Użytkownik jest w kontekście firmowym i wybiera „eKsięgowość”
- When status aktywacji usługi CashDirector dla bieżącej firmy jest „aktywna”
- Then system przekierowuje Użytkownika do CashDirector w ramach SSO

---

#### RQ-ACT-003: Dostępność aktywacji w kontekstach firmowych mikro i korporacyjnym
**Opis:** Funkcjonalność aktywacji usługi CashDirector musi być dostępna w kontekście firmowym w wariantach: mikro oraz korporacyjnym.

**Uzasadnienie:** Wymagania klienta określają dostępność funkcjonalności w kontekście firmowym, a dokumentacja BE opisuje rozróżnienie kontekstów/obszarów roboczych mikro i korporacyjnego.

**AC:**
- Given Użytkownik jest zalogowany w kontekście firmowym mikro
- When Użytkownik wybiera „eKsięgowość”
- Then system umożliwia realizację procesu aktywacji zgodnie z RQ-ACT-002
- Given Użytkownik jest zalogowany w kontekście firmowym korporacyjnym
- When Użytkownik wybiera „eKsięgowość”
- Then system umożliwia realizację procesu aktywacji zgodnie z RQ-ACT-002

---

#### RQ-ACT-004: Kontrola dostępu uprawnieniem „eKsięgowość – aktywacja”
**Opis:** Dostęp do uruchomienia procesu aktywacji usługi CashDirector musi być kontrolowany uprawnieniem funkcjonalnym „eKsięgowość – aktywacja”.

**Uzasadnienie:** Wymagania klienta wprost wskazują, że uruchomienie aktywacji jest kontrolowane uprawnieniem funkcjonalnym; dokumentacja BE opisuje zarządzanie uprawnieniami dla opcji systemu w kontekście firmowym.

**AC:**
- Given Użytkownik jest w kontekście firmowym i posiada uprawnienie „eKsięgowość – aktywacja”
- When Użytkownik wybiera „eKsięgowość”
- Then system umożliwia rozpoczęcie procesu aktywacji
- Given Użytkownik jest w kontekście firmowym i nie posiada uprawnienia „eKsięgowość – aktywacja”
- When Użytkownik wybiera „eKsięgowość”
- Then system nie umożliwia rozpoczęcia aktywacji i prezentuje komunikat o braku uprawnień

---

#### RQ-ACT-005: Rejestracja zdarzenia uruchomienia aktywacji
**Opis:** System BE musi rejestrować uruchomienie procesu aktywacji usługi CashDirector w Rejestrze zdarzeń jako typ zdarzenia „Aktywacja usługi CashDirector”.

**Uzasadnienie:** Wymagania klienta wskazują konieczność audytu uruchomienia procesu aktywacji poprzez rejestr zdarzeń.

**AC:**
- Given Użytkownik uruchamia proces aktywacji usługi CashDirector
- When system rozpoczyna proces aktywacji
- Then system rejestruje zdarzenie typu „Aktywacja usługi CashDirector” w Rejestrze zdarzeń

---

#### RQ-ACT-006: Ekran aktywacji: zgody/regulaminy/umowy i rejestracja akceptacji
**Opis:** System BE musi umożliwiać pobranie, prezentację oraz rejestrację akceptacji zgód, regulaminów i umów wymaganych do aktywacji usługi CashDirector oraz udostępniać pliki wskazane przez Bank do pobrania.

**Uzasadnienie:** Wymagania klienta wskazują, że aktywacja wymaga obsługi zgód/regulaminów/umów oraz że BE udostępnia do pobrania pliki wskazane przez Bank; nie zakłada się generowania, podpisywania ani wysyłania umów po stronie BE.

**AC:**
- Given Użytkownik jest na ekranie aktywacji usługi CashDirector
- When system prezentuje wymagane zgody/regulaminy/umowy oraz pliki Banku do pobrania
- Then Użytkownik ma możliwość zapoznania się z treściami oraz pobrania plików
- Given Użytkownik nie zaakceptował wszystkich wymaganych pozycji
- When Użytkownik próbuje kontynuować aktywację
- Then system blokuje kontynuację i prezentuje informację o brakujących akceptacjach
- Given Użytkownik zaakceptował wszystkie wymagane pozycje
- When Użytkownik zatwierdza aktywację
- Then system rejestruje akceptację zgód/regulaminów/umów

---

#### RQ-ACT-007: Rejestracja firmy i użytkownika w CashDirector
**Opis:** System BE musi przekazywać dane identyfikacyjne firmy oraz właściciela/użytkownika do systemu CashDirector w celu rejestracji usługi.

**Uzasadnienie:** Wymagania klienta wskazują konieczność rejestracji firmy i użytkownika w CashDirector jako element procesu aktywacji/integracji.

**AC:**
- Given Użytkownik zakończył etap akceptacji zgód/regulaminów/umów
- When system BE uruchamia rejestrację usługi CashDirector
- Then system przekazuje do CashDirector dane identyfikacyjne firmy oraz użytkownika

---

#### RQ-ACT-008: Obsługa błędu aktywacji (niepowodzenie rejestracji)
**Opis:** System BE musi przerwać proces aktywacji i zaprezentować klientowi komunikat o błędzie w przypadku niepowodzenia rejestracji usługi CashDirector.

**Uzasadnienie:** Wymagania klienta wprost wymagają przerwania procesu i komunikatu dla użytkownika w przypadku błędu aktywacji.

**AC:**
- Given Użytkownik jest w trakcie aktywacji usługi CashDirector
- When rejestracja usługi w CashDirector kończy się niepowodzeniem
- Then system przerywa proces aktywacji
- Then system prezentuje Użytkownikowi komunikat o błędzie aktywacji

---

#### RQ-ACT-009: Parowanie firmy i użytkownika z rekordami w CashDirector
**Opis:** System BE musi umożliwiać parowanie firmy i użytkownika z istniejącymi rekordami w CashDirector przy użyciu identyfikatorów zewnętrznych.

**Uzasadnienie:** Wymagania klienta przewidują scenariusz, w którym podmiot istnieje w CashDirector i wymagane jest jego powiązanie (parowanie) w oparciu o identyfikatory zewnętrzne.

**AC:**
- Given firma lub Użytkownik istnieje już w CashDirector
- When system BE wykonuje rejestrację/parowanie w CashDirector z użyciem identyfikatorów zewnętrznych
- Then system realizuje parowanie zamiast tworzenia nowego rekordu

---

#### RQ-ACT-010: Obsługa scenariusza istniejących danych w CashDirector
**Opis:** System BE musi obsługiwać scenariusz, w którym firma lub użytkownik istnieje już w systemie CashDirector.

**Uzasadnienie:** Wymagania klienta wprost wskazują konieczność obsługi istniejących danych w systemie zewnętrznym.

**AC:**
- Given firma lub Użytkownik istnieje w CashDirector
- When Użytkownik uruchamia aktywację usługi CashDirector w BE
- Then system nie kończy procesu błędem wyłącznie z powodu istnienia danych w CashDirector

---

#### RQ-ACT-011: Logowanie jednokrotne (SSO) do CashDirector
**Opis:** System BE musi umożliwiać logowanie użytkownika do CashDirector z wykorzystaniem mechanizmu SSO.

**Uzasadnienie:** Zakres integracji obejmuje SSO jako sposób przejścia użytkownika z BE do CashDirector bez ponownego logowania.

**AC:**
- Given Użytkownik znajduje się w kontekście firmowym oraz usługa CashDirector dla firmy jest aktywna
- When Użytkownik wybiera „eKsięgowość”
- Then system realizuje logowanie SSO do CashDirector i przekierowuje Użytkownika do CashDirector

---

#### RQ-ACT-012: Usługa `customerContext` dla SSO
**Opis:** System BE musi udostępniać usługę `customerContext` umożliwiającą pobranie kontekstu klienta na potrzeby SSO na podstawie parametrów: `ssoToken`, `externalCompanyId`, `externalUserId`, zwracając `accessToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę `customerContext` oraz jej parametry wejścia/wyjścia, co stanowi podstawę do obsługi SSO.

**AC:**
- Given serwis księgowy wywołuje `customerContext` z `ssoToken`, `externalCompanyId`, `externalUserId`
- When system BE przetwarza żądanie
- Then system zwraca `accessToken` jako token autoryzujący

---

#### RQ-ACT-013: Usługa `bankRedirect` dla powrotu SSO
**Opis:** System BE musi udostępniać usługę `bankRedirect` realizującą przekierowanie z serwisu księgowego do banku w ramach powrotu SSO, przyjmując parametr `accessToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę `bankRedirect` jako element przepływu SSO.

**AC:**
- Given serwis księgowy wywołuje `bankRedirect` z `accessToken`
- When system BE przetwarza żądanie
- Then system realizuje przekierowanie w ramach powrotu SSO

---

#### RQ-ACT-014: Zarządzanie tokenami dostępowymi w integracji
**Opis:** System BE musi obsługiwać pobieranie i odświeżanie tokenów dostępowych wykorzystywanych w integracji z CashDirector.

**Uzasadnienie:** Wymagania klienta wskazują potrzebę zarządzania tokenami wykorzystywanymi w procesach integracyjnych.

**AC:**
- Given system BE korzysta z tokenów dostępowych w integracji z CashDirector
- When token dostępu wymaga odświeżenia
- Then system realizuje odświeżenie tokenu zgodnie z interfejsem integracyjnym

---

#### RQ-ACT-015: Udostępnienie listy rachunków firmy (`accounts`)
**Opis:** System BE musi udostępniać usługę `accounts` zwracającą listę aktywnych rachunków bieżących firmy, z wykorzystaniem parametrów: `accessToken`, `externalCompanyId`, `externalUserId`, oraz pola wyjściowe obejmujące co najmniej `accountNumber` i `displayName`.

**Uzasadnienie:** Źródła integracyjne definiują usługę `accounts` i minimalny zakres danych na wyjściu.

**AC:**
- Given serwis księgowy wywołuje `accounts` z poprawnym `accessToken`, `externalCompanyId`, `externalUserId`
- When system BE przetwarza żądanie
- Then system zwraca listę rachunków firmy zawierającą `accountNumber` oraz `displayName`

---

#### RQ-ACT-016: Autoryzacja dostępu do danych rachunkowych
**Opis:** System BE musi zapewnić, że dane rachunkowe udostępniane w ramach integracji są przekazywane wyłącznie po poprawnej autoryzacji użytkownika.

**Uzasadnienie:** Wymagania klienta wskazują konieczność ograniczenia dostępu do danych rachunkowych wyłącznie do uprawnionych, poprawnie autoryzowanych wywołań.

**AC:**
- Given serwis księgowy wywołuje `accounts` bez poprawnej autoryzacji
- When system BE przetwarza żądanie
- Then system nie udostępnia danych rachunkowych

---

#### RQ-ACT-017: Inicjacja dezaktywacji usługi przez klienta
**Opis:** System BE musi umożliwiać klientowi zainicjowanie procesu dezaktywacji usługi CashDirector.

**Uzasadnienie:** Zakres integracji obejmuje dezaktywację usługi inicjowaną przez Bank/klienta.

**AC:**
- Given usługa CashDirector jest aktywna dla firmy
- When Użytkownik inicjuje dezaktywację usługi w BE
- Then system rozpoczyna proces dezaktywacji usługi CashDirector

---

#### RQ-ACT-018: Rejestracja i realizacja dezaktywacji w CashDirector
**Opis:** System BE musi rejestrować dezaktywację usługi CashDirector w systemie CashDirector oraz umożliwiać dezaktywację firmy i użytkowników powiązanych z usługą.

**Uzasadnienie:** Wymagania klienta wskazują obowiązek rejestracji dezaktywacji w systemie zewnętrznym oraz dezaktywacji powiązanych podmiotów.

**AC:**
- Given Użytkownik zainicjował dezaktywację usługi CashDirector
- When system BE realizuje proces dezaktywacji
- Then system rejestruje dezaktywację w CashDirector
- Then system realizuje dezaktywację firmy i powiązanych użytkowników w zakresie integracji

---

#### RQ-ACT-019: Obsługa błędów dezaktywacji i spójność statusu usługi
**Opis:** System BE musi obsługiwać błędy procesu dezaktywacji i zapewnić spójność statusu usługi CashDirector.

**Uzasadnienie:** Wymagania klienta wymagają obsługi błędów dezaktywacji oraz utrzymania spójnego statusu usługi.

**AC:**
- Given proces dezaktywacji usługi CashDirector jest w toku
- When wystąpi błąd w procesie dezaktywacji
- Then system obsługuje błąd i zapewnia spójność statusu usługi

---

#### RQ-ACT-020: Obsługa żądania dezaktywacji inicjowanego przez CashDirector
**Opis:** System BE musi obsługiwać żądanie dezaktywacji usługi CashDirector inicjowane po stronie CashDirector oraz zapisywać status dezaktywacji usługi CashDirector w systemach bankowych.

**Uzasadnienie:** Wymagania klienta obejmują scenariusz dezaktywacji inicjowanej przez CashDirector wraz z rejestracją statusu w systemach bankowych.

**AC:**
- Given CashDirector inicjuje żądanie dezaktywacji usługi
- When system BE przetwarza żądanie dezaktywacji
- Then system zapisuje status dezaktywacji w systemach bankowych

---

#### RQ-ACT-021: Autoryzacja użytkownika przed potwierdzeniem dezaktywacji
**Opis:** System BE musi przeprowadzić autoryzację użytkownika przed potwierdzeniem dezaktywacji usługi CashDirector.

**Uzasadnienie:** Wymagania klienta wprost wymagają autoryzacji użytkownika jako warunku potwierdzenia dezaktywacji.

**AC:**
- Given żądanie dezaktywacji usługi CashDirector jest przetwarzane
- When system ma potwierdzić dezaktywację
- Then system wymaga autoryzacji użytkownika przed potwierdzeniem

---

#### RQ-ACT-022: Usługa `unassignCompany` do usunięcia powiązania usługi
**Opis:** System BE musi udostępniać usługę `unassignCompany` umożliwiającą usunięcie powiązania między bankiem a usługą księgową, z parametrami: `externalCompanyId`, `externalUserId`.

**Uzasadnienie:** Źródła integracyjne opisują usługę `unassignCompany` jako operację odpięcia powiązania.

**AC:**
- Given serwis księgowy wywołuje `unassignCompany` z `externalCompanyId` i `externalUserId`
- When system BE przetwarza żądanie
- Then system usuwa powiązanie między bankiem a usługą księgową

---

#### RQ-ACT-023: Inicjowanie płatności w BE na zlecenie CashDirector
**Opis:** System BE musi umożliwiać inicjowanie płatności zleconych w systemie CashDirector.

**Uzasadnienie:** Wymagania klienta obejmują inicjowanie i realizację płatności jako element integracji BE–CashDirector.

**AC:**
- Given CashDirector zleca inicjowanie płatności w BE
- When system BE otrzymuje żądanie inicjacji płatności
- Then system rozpoczyna proces inicjowania płatności

---

#### RQ-ACT-024: Usługa `domesticPaymentInit` (przelew krajowy bez split payment)
**Opis:** System BE musi udostępniać usługę `domesticPaymentInit` inicjującą płatność w banku (przelew krajowy bez split payment) z parametrami: `accessToken`, `paymentId`, `externalCompanyId`, `externalUserId`, `sourceAccount`, `amount`, `currency`, `title`, `beneficiaryName`, `beneficiaryAddress`, `beneficiaryAccount`, zwracając `paymentToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę inicjowania płatności krajowej bez split payment wraz z parametrami.

**AC:**
- Given serwis księgowy wywołuje `domesticPaymentInit` z wymaganymi parametrami i poprawnym `accessToken`
- When system BE przetwarza żądanie
- Then system zwraca `paymentToken`

---

#### RQ-ACT-025: Usługa `domesticSplitPaymentInit` (przelew krajowy ze split payment)
**Opis:** System BE musi udostępniać usługę `domesticSplitPaymentInit` inicjującą płatność w banku (przelew krajowy ze split payment) z parametrami: `accessToken`, `paymentId`, `externalCompanyId`, `externalUserId`, `sourceAccount`, `amount`, `vatAmount`, `currency`, `title`, `beneficiaryName`, `beneficiaryAddress`, `beneficiaryAccount`, `taxpayerIdType`, `taxpayerId`, `invoiceNumber`, zwracając `paymentToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę inicjowania split payment wraz z parametrami.

**AC:**
- Given serwis księgowy wywołuje `domesticSplitPaymentInit` z wymaganymi parametrami i poprawnym `accessToken`
- When system BE przetwarza żądanie
- Then system zwraca `paymentToken`

---

#### RQ-ACT-026: Usługa `foreignPaymentInit` (przelew zagraniczny / z przewalutowaniem)
**Opis:** System BE musi udostępniać usługę `foreignPaymentInit` inicjującą płatność w banku (przelew zagraniczny / z przewalutowaniem) z parametrami: `accessToken`, `paymentId`, `externalCompanyId`, `externalUserId`, `sourceAccount`, `amount`, `currency`, `title`, `beneficiaryName`, `beneficiaryAddress`, `beneficiaryAccount`, zwracając `paymentToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę inicjowania płatności zagranicznej wraz z parametrami.

**AC:**
- Given serwis księgowy wywołuje `foreignPaymentInit` z wymaganymi parametrami i poprawnym `accessToken`
- When system BE przetwarza żądanie
- Then system zwraca `paymentToken`

---

#### RQ-ACT-027: Usługa `taxPaymentInit` (przelew podatkowy)
**Opis:** System BE musi udostępniać usługę `taxPaymentInit` inicjującą płatność w banku (przelew podatkowy) z parametrami: `accessToken`, `paymentId`, `externalCompanyId`, `externalUserId`, `sourceAccount`, `amount`, `officeAccount`, `formSymbol`, `formPeriod`, `payerIdType`, `payerIdNumber`, zwracając `paymentToken`.

**Uzasadnienie:** Źródła integracyjne definiują usługę inicjowania przelewu podatkowego wraz z parametrami.

**AC:**
- Given serwis księgowy wywołuje `taxPaymentInit` z wymaganymi parametrami i poprawnym `accessToken`
- When system BE przetwarza żądanie
- Then system zwraca `paymentToken`

---

#### RQ-ACT-028: Przekierowanie do banku do formatki przelewowej (POST redirect)
**Opis:** System BE musi umożliwiać przekierowanie do banku do formatki przelewowej na podstawie parametrów: `paymentToken`, `accessToken`, `backUrl`.

**Uzasadnienie:** Źródła integracyjne opisują operację przekierowania do banku do formatki przelewowej, z `backUrl` dla powrotu po wykonaniu płatności.

**AC:**
- Given serwis księgowy realizuje przekierowanie do formatki przelewowej z `paymentToken`, `accessToken` i `backUrl`
- When system BE przetwarza przekierowanie
- Then Użytkownik zostaje skierowany do formatki przelewowej w banku
- Then po wykonaniu płatności Użytkownik może zostać przekierowany na `backUrl`

---

#### RQ-ACT-029: Autoryzacja płatności w BE
**Opis:** System BE musi przekierować użytkownika do bankowości elektronicznej w celu autoryzacji płatności inicjowanej z CashDirector.

**Uzasadnienie:** Wymagania klienta wprost wymagają autoryzacji płatności w BE.

**AC:**
- Given płatność została zainicjowana z CashDirector
- When wymagana jest autoryzacja płatności
- Then system przekierowuje Użytkownika do BE w celu autoryzacji

---

#### RQ-ACT-030: Walidacja płatności
**Opis:** System BE musi weryfikować poprawność danych płatności oraz dostępność środków.

**Uzasadnienie:** Wymagania klienta wskazują obowiązek walidacji danych płatności i dostępności środków.

**AC:**
- Given system BE otrzymuje dane płatności do realizacji
- When system wykonuje walidację
- Then system potwierdza poprawność danych oraz dostępność środków albo przerywa proces i zwraca informację o błędzie

---

#### RQ-ACT-031: Aktualizacja statusu płatności do CashDirector
**Opis:** System BE musi przekazywać do CashDirector informacje o zmianie statusu płatności.

**Uzasadnienie:** Wymagania klienta obejmują przekazywanie statusów płatności w ramach integracji.

**AC:**
- Given status płatności uległ zmianie w BE
- When system przekazuje informację do CashDirector
- Then CashDirector otrzymuje informację o zmianie statusu płatności

---

#### RQ-ACT-032: Idempotentność aktualizacji statusów płatności
**Opis:** System BE musi zapewnić idempotentność aktualizacji statusów płatności przekazywanych do CashDirector.

**Uzasadnienie:** Wymagania klienta wprost wymagają idempotentności przekazywania statusów płatności.

**AC:**
- Given status płatności został już przekazany do CashDirector
- When system BE ponownie przetwarza przekazanie tego samego statusu (np. retry)
- Then wynik po stronie CashDirector pozostaje zgodny (brak duplikacji skutków biznesowych)

---

#### RQ-ACT-033: Identyfikacja leada sprzedażowego
**Opis:** System BE musi umożliwiać identyfikację leada sprzedażowego w trakcie procesów bankowych związanych z obsługą klienta instytucjonalnego.

**Uzasadnienie:** Zakres integracji obejmuje przekazywanie leadów sprzedażowych.

**AC:**
- Given Użytkownik realizuje procesy bankowe w BE związane z obsługą firmy
- When wystąpi sytuacja kwalifikująca do identyfikacji leada
- Then system identyfikuje leada sprzedażowego

---

#### RQ-ACT-034: Przekazanie leada do CashDirector po uzyskaniu zgód
**Opis:** System BE musi umożliwiać przekazanie danych leada sprzedażowego do systemu CashDirector po uzyskaniu wymaganych zgód klienta.

**Uzasadnienie:** Wymagania klienta wskazują, że przekazanie leada wymaga uzyskania zgód.

**AC:**
- Given system zidentyfikował leada sprzedażowego oraz wymagane zgody klienta zostały uzyskane
- When system przekazuje dane leada do CashDirector
- Then CashDirector otrzymuje dane leada sprzedażowego

---

#### RQ-ACT-035: Przekazywanie historii operacji bankowych
**Opis:** System BE musi umożliwiać przekazywanie historii operacji bankowych do systemu CashDirector.

**Uzasadnienie:** Zakres integracji obejmuje przekazywanie historii operacji bankowych do CashDirector.

**AC:**
- Given CashDirector wymaga danych o historii operacji bankowych
- When system BE przekazuje historię operacji
- Then CashDirector otrzymuje historię operacji bankowych

---

#### RQ-ACT-036: Warianty integracji historii operacji (REST lub zdarzeniowy)
**Opis:** System BE musi obsługiwać przekazywanie danych operacji bankowych do CashDirector w modelu REST API lub zdarzeniowym.

**Uzasadnienie:** Wymagania klienta dopuszczają różne warianty integracji dla historii operacji.

**AC:**
- Given model integracji dla historii operacji jest skonfigurowany jako REST API
- When system przekazuje dane operacji do CashDirector
- Then komunikacja odbywa się w modelu REST API
- Given model integracji dla historii operacji jest skonfigurowany jako zdarzeniowy
- When system przekazuje dane operacji do CashDirector
- Then komunikacja odbywa się w modelu zdarzeniowym

---

#### RQ-ACT-037: Minimalny zakres przekazywanych danych transakcyjnych
**Opis:** System BE musi przekazywać minimalny zestaw danych transakcyjnych wymaganych do obsługi księgowej w CashDirector.

**Uzasadnienie:** Wymagania klienta wskazują wymóg przekazywania minimalnego zestawu danych transakcyjnych, bez doprecyzowania listy pól w źródłach.

**AC:**
- Given system przekazuje dane transakcyjne do CashDirector
- When dane są przygotowywane do przekazania
- Then system przekazuje minimalny zestaw danych wymagany do obsługi księgowej

---

#### RQ-ACT-038: Rejestrowanie i monitorowanie błędów integracyjnych
**Opis:** System BE musi rejestrować i monitorować błędy występujące w procesach integracyjnych BE–CashDirector.

**Uzasadnienie:** Wymagania klienta wskazują potrzebę rejestrowania i monitorowania błędów integracyjnych.

**AC:**
- Given wystąpi błąd w procesie integracyjnym BE–CashDirector
- When system obsługuje błąd
- Then system rejestruje błąd i udostępnia go do monitorowania

---

#### RQ-ACT-039: Komunikaty dla użytkownika przy niepowodzeniu procesu
**Opis:** System BE musi prezentować użytkownikowi czytelne komunikaty w przypadku niepowodzenia realizacji procesu integracyjnego.

**Uzasadnienie:** Wymagania klienta wskazują konieczność komunikatów dla użytkownika w przypadku niepowodzenia.

**AC:**
- Given proces integracyjny zakończył się niepowodzeniem
- When system kończy obsługę procesu
- Then system prezentuje Użytkownikowi czytelny komunikat o niepowodzeniu

---

#### RQ-ACT-040: Spójność danych integracyjnych
**Opis:** System BE musi zapewnić spójność danych pomiędzy systemami Banku i CashDirector.

**Uzasadnienie:** Wymagania końcowe klienta definiują spójność danych jako warunek integracji.

**AC:**
- Given dane są przetwarzane w procesach integracyjnych BE–CashDirector
- When proces integracyjny zostaje zakończony
- Then dane w BE i CashDirector są spójne w zakresie objętym integracją

---

#### RQ-ACT-041: Audytowalność kluczowych zdarzeń integracyjnych
**Opis:** System BE musi zapewnić możliwość audytu kluczowych zdarzeń integracyjnych, w szczególności aktywacji, dezaktywacji oraz płatności.

**Uzasadnienie:** Wymagania klienta wskazują konieczność audytu kluczowych zdarzeń integracyjnych.

**AC:**
- Given wystąpiło zdarzenie integracyjne (aktywacja, dezaktywacja lub płatność)
- When wymagany jest audyt zdarzenia
- Then dostępne są informacje umożliwiające audyt tego zdarzenia

---

#### 3.1.1 Obsługa błędów
(Ta sekcja MUSI istnieć)

- Brak uprawnienia „eKsięgowość – aktywacja” przy próbie uruchomienia aktywacji (RQ-ACT-004).
- Niepowodzenie rejestracji usługi CashDirector w procesie aktywacji (RQ-ACT-008).
- Brak wymaganych akceptacji zgód/regulaminów/umów uniemożliwiający kontynuację aktywacji (RQ-ACT-006).
- Brak poprawnej autoryzacji wywołań integracyjnych skutkujący odmową dostępu do danych (np. rachunki) (RQ-ACT-016).
- Błędy procesu dezaktywacji i konieczność zachowania spójności statusu usługi (RQ-ACT-019).
- Błędy walidacji płatności (np. niepoprawne dane lub brak dostępności środków) skutkujące przerwaniem procesu (RQ-ACT-030).
- Błędy integracyjne BE–CashDirector wymagające rejestrowania i monitorowania oraz prezentacji czytelnych komunikatów (RQ-ACT-038, RQ-ACT-039).
- Wygaśnięcie sesji użytkownika w trakcie realizacji procesu w kanale BE (ograniczenie wynikające z mechanizmów sesji opisanych w dokumentacji BE).

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: /src/*, /doc_basic/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->

W dostępnych materiałach źródłowych nie zidentyfikowano mierzalnych wymagań niefunkcjonalnych specyficznych dla integracji BE–CashDirector (np. SLA, limity wydajnościowe, parametry bezpieczeństwa). Braki doprecyzowania zostały ujęte w sekcji „Zagadnienia otwarte”.
---
#### 3.2.1. Wydajność
#### 3.2.2. Bezpieczeństwo
#### 3.2.3. Wdrożenie i proces migracji danych
## 5. Wymagane licencje
<!-- SPW-SECTION
Cel: Wskaż licencje / zależności licencyjne wymagane przez rozwiązanie.
Źródła: /src/*, /doc_basic/*
Wyjście: lista licencji i zakres ich użycia.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 6. Obszary pod wpływem
<!-- SPW-SECTION
Cel: Wymień systemy, moduły, procesy i kanały dotknięte zmianą.
Źródła: /src/*, /doc_basic/*
Wyjście: lista obszarów + krótki opis wpływu.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 7. Założenia i ograniczenia
<!-- SPW-SECTION
Cel: Zapisz założenia, ograniczenia oraz decyzje projektowe wpływające na zakres.
Źródła: /src/*, /doc_basic/*
Wyjście: lista punktów; brakujące dane oznaczaj OPEN-QUESTION.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->

## 8. Zagadnienia otwarte
- OPEN-QUESTION-001: Co oznacza skrót „CB” użyty w opisie WM-01 (przekierowanie użytkownika do „CB” przy aktywnej usłudze) – czy chodzi o CashDirector, inny komponent, czy kanał/ekran BE?

#TODO: 

- OPEN-QUESTION-002: Jaki jest katalog dopuszczalnych wartości statusu aktywacji usługi CashDirector na firmie (poza „aktywna/nieaktywna”) oraz ich znaczenie w procesie?
- OPEN-QUESTION-003: Jakie dokładnie „dane identyfikacyjne firmy oraz właściciela/użytkownika” mają być przekazywane do CashDirector w procesie rejestracji/parowania (lista pól, walidacje, formaty)?
- OPEN-QUESTION-004: Jak BE ma pozyskiwać treści zgód/regulaminów/umów „wskazane przez Bank” (źródło, wersjonowanie, języki, identyfikatory dokumentów)?
- OPEN-QUESTION-005: Jaki jest interfejs integracyjny dla „pobierania i odświeżania tokenów dostępowych” (WM-08) – endpointy, czasy życia, warunki odświeżenia, unieważnianie?
- OPEN-QUESTION-006: Czy usługa `accounts` ma zwracać również „informację o dostępnych saldach” (WM-09); jeśli tak, w jakim zakresie i formacie (brak w `src/banki-api-uslugi-banku.md`)?
- OPEN-QUESTION-007: Jakim kanałem i w jakim formacie BE przekazuje do CashDirector „statusy płatności” (WM-21) oraz w jaki sposób realizowana jest idempotentność (klucz idempotencyjny / deduplikacja)?
- OPEN-QUESTION-008: Jaki jest zakres danych i zdarzeń dla leadów sprzedażowych (WM-23/WM-24) oraz jakie „wymagane zgody” są niezbędne do przekazania leada?
- OPEN-QUESTION-009: Jaki jest minimalny zestaw danych transakcyjnych dla historii operacji (WM-25/WM-27) oraz czy preferowany jest wariant REST czy zdarzeniowy (WM-26)?
- OPEN-QUESTION-010: Jakie są wymagania bezpieczeństwa dla udostępnianych usług (`customerContext`, `accounts`, `paymentInit*`) w zakresie uwierzytelnienia/autoryzacji, a także logowania/audytu wywołań?
## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: /src/*, /doc_basic/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
