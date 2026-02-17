<!-- AI-CONSTRAINTS
Zakres: Opis zakresu modyfikacji
Format: RQ-ACT-###
Źródła:
    Wymagania klienta: /src/*,
    Dokumentacja systemu: /doc/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagań – Integracja BE z CashDirector

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz główny cel biznesowy rozwiązania dla wskazanego zakresu modyfikacji.
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
Źródła: Wymagania klienta: /src/*
Wyjście: 3–5 zdań.
Kryteria jakości: jednoznaczność, brak domysłów, spójność terminologii.
-->
Celem projektu jest uruchomienie i utrzymanie integracji Bankowości Elektronicznej (BE) z systemem księgowym CashDirector dla klientów instytucjonalnych.
Zakres biznesowy obejmuje pełny cykl usługi: aktywację, dostęp SSO, inicjowanie płatności, przekazywanie statusów, dezaktywację oraz wymianę danych operacyjnych.
Rozwiązanie ma umożliwić klientowi realizację procesów księgowo-płatniczych z zachowaniem autoryzacji bankowej i spójności danych między BE i CashDirector.
Istotnym celem jest także audytowalność zdarzeń integracyjnych oraz obsługa błędów bez utraty kontroli nad statusem usługi.

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: /src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->
- Integracja obejmuje: aktywację usługi, rejestrację/parowanie firmy i użytkownika, SSO, dezaktywację (inicjowaną przez Bank i CashDirector), inicjowanie płatności, statusy płatności, leady sprzedażowe, historię operacji (`src/wymagania.md`).
- Aktywacja usługi ma być dostępna z BE przez opcję `eKsięgowość`, zależną od statusu aktywacji usługi w kontekście firmy (`src/wymagania.md`).
- Proces aktywacji ma obejmować prezentację i akceptację zgód/regulaminów/umów oraz plików wskazanych przez Bank, bez generowania i podpisywania umów po stronie BE (`src/wymagania.md`).
- Integracja płatności ma wykorzystywać dedykowane usługi inicjacji płatności i token `paymentToken`, a wykonanie płatności ma następować przez redirect do banku (`src/banki-api-uslugi-banku.md`).
- Wymagana jest obsługa tokenów dostępowych i przekazywanie kontekstu klienta dla SSO (`src/wymagania.md`, `src/banki-api-uslugi-banku.md`).
- Wymagana jest rejestracja i monitorowanie błędów integracyjnych oraz audyt kluczowych zdarzeń (`src/wymagania.md`).

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: doc/* (np. /doc/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->
- **BE** – system bankowości elektronicznej.
- **CashDirector** – system księgowy.
- **Firma** – podmiot gospodarczy klienta banku.
- **Użytkownik** – osoba fizyczna działająca w imieniu firmy.
- **SSO** – Single Sign-On.

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: doc/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->
System BE obsługuje kontekst indywidualny, mikro (MŚP) oraz instytucjonalny (firmowy/korporacyjny), a dla klientów firmowych umożliwia zarządzanie uprawnieniami funkcjonalnymi (`doc/opis systemu BE.md`).
Dokumentacja stanu obecnego wskazuje szeroki zakres istniejących funkcji bankowości (m.in. rachunki, przelewy, lista zleceń, wiadomości, karty, lokaty, kredyty oraz konfiguracja BO), co potwierdza istnienie bazowych procesów płatności i autoryzacji po stronie BE (`doc/EBP/*.adoc`, `doc/BO/BackofficeUserGuide-pl_basic.adoc`).
W materiałach źródłowych brak opisu już działającej integracji BE z CashDirector, dlatego zakres tej specyfikacji traktuje tę integrację jako zmianę do wdrożenia.

W sekcji Rachunki dostęp użytkownika jest ograniczony do rachunków, do których użytkownik ma nadane uprawnienia.
Funkcjonalność wymaga jednocześnie uprawnień do miniaplikacji oraz uprawnień do rachunków, konfigurowanych przez Administratora Użytkowników w opcji `Ustawienia -> Uprawnienia Użytkowników`.
Dodatkowo funkcja otwarcia nowego rachunku wymaga spełnienia warunków konfiguracyjnych (m.in. przełącznik `accountOpening`) oraz dla klienta firmowego nadania uprawnienia funkcjonalnego `Otwarcie rachunku`.

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: /src/*, /doc/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->
Model docelowy zakłada, że klient firmowy aktywuje usługę `eKsięgowość` w BE, akceptuje wymagane zgody, a BE rejestruje/paruje firmę i użytkownika z CashDirector.
Po aktywacji użytkownik korzysta z logowania SSO i otrzymuje dostęp do kontekstu firmy oraz usług integracyjnych opartych o tokeny.
CashDirector może pobierać kontekst klienta i listę rachunków, inicjować płatności przez usługi bankowe oraz przekierowywać użytkownika do BE w celu autoryzacji i realizacji zlecenia.
BE przekazuje do CashDirector statusy płatności (z zachowaniem idempotentności), leady sprzedażowe i historię operacji, a także obsługuje dezaktywację usługi po stronie Banku lub CashDirector.
W całym przepływie wymagane jest logowanie zdarzeń i obsługa błędów integracyjnych.

## 3. Wymagania szczegółowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiązania na nowe i modyfikowane wymagania/user stories.
Źródła: Wymagania klienta: src/*
-->
### 3.1 Wymagania funkcjonalne

#### RQ-ACT-001: Aktywacja usługi eKsięgowość w BE
**Opis:** System BE musi udostępniać opcję `eKsięgowość` i uruchamiać proces aktywacji usługi CashDirector dla klienta firmowego.

**Uzasadnienie:** Wymagane jest zapewnienie punktu wejścia do integracji z poziomu bankowości elektronicznej.

**AC:**
- Given klient działa w kontekście firmowym i ma dostęp do BE
- When wybiera opcję `eKsięgowość`
- Then BE uruchamia przepływ aktywacji usługi CashDirector

````mermaid`
sequenceDiagram
    actor U as Użytkownik
    participant BE as System BE
    participant CD as CashDirector

    U->>BE: Wybór opcji eKsięgowość
    BE->>BE: Weryfikacja kontekstu firmowego i uprawnień
    alt Brak kontekstu/uprawnień
        BE-->>U: Komunikat o braku dostępu
    else Dostęp przyznany
        BE->>BE: Odczyt statusu aktywacji usługi
        alt Status = nieaktywna
            BE-->>U: Ekran aktywacji + zgody/regulaminy
            U->>BE: Akceptacja i potwierdzenie aktywacji
            BE->>CD: Rejestracja firmy i użytkownika
            alt Rejestracja zakończona powodzeniem
                CD-->>BE: Potwierdzenie
                BE-->>U: Przekierowanie do CashDirector (SSO)
            else Błąd rejestracji
                CD-->>BE: Błąd
                BE-->>U: Komunikat o błędzie aktywacji
            end
        else Status = aktywna
            BE-->>U: Przekierowanie do CashDirector (SSO)
        end
    end
```

---

#### RQ-ACT-002: Sterowanie dostępem na podstawie statusu i uprawnień
**Opis:** System BE musi utrzymywać status aktywacji usługi na poziomie firmy i na tej podstawie prezentować ekran aktywacji albo przekierowanie do CashDirector; uruchomienie aktywacji musi być kontrolowane uprawnieniem funkcjonalnym.

**Uzasadnienie:** Wymagane jest spójne sterowanie dostępem i zgodność z modelem uprawnień dla klienta firmowego.

**AC:**
- Given firma ma zapisany status aktywacji usługi i użytkownik posiada lub nie posiada odpowiednie uprawnienie
- When użytkownik wybiera `eKsięgowość`
- Then BE prezentuje właściwy ekran (aktywacja lub przejście do CashDirector) zgodnie ze statusem i uprawnieniami

---

#### RQ-ACT-003: Obsługa zgód i dokumentów aktywacyjnych
**Opis:** System BE musi prezentować i rejestrować akceptację zgód/regulaminów/umów wskazanych przez Bank oraz udostępniać pliki do pobrania na formularzu aktywacji.

**Uzasadnienie:** Aktywacja usługi wymaga formalnej akceptacji treści udostępnionych przez Bank.

**AC:**
- Given Bank udostępnił zestaw treści i plików wymaganych do aktywacji
- When użytkownik przechodzi formularz aktywacyjny i akceptuje wymagane pozycje
- Then BE zapisuje fakt akceptacji i umożliwia kontynuację procesu

---

#### RQ-ACT-004: Rejestracja i parowanie firmy oraz użytkownika
**Opis:** System BE musi przekazywać dane identyfikacyjne firmy i użytkownika do CashDirector oraz obsługiwać parowanie z rekordami już istniejącymi po stronie CashDirector.

**Uzasadnienie:** Integracja wymaga jednoznacznego powiązania podmiotów między systemami.

**AC:**
- Given rozpoczęto aktywację usługi dla firmy i użytkownika
- When BE wywołuje proces rejestracji/parowania w CashDirector
- Then powiązanie firma-użytkownik-usługa zostaje utworzone albo zaktualizowane zgodnie z odpowiedzią CashDirector

---

#### RQ-ACT-005: Logowanie SSO i obsługa kontekstu klienta
**Opis:** System BE musi obsługiwać logowanie SSO do CashDirector oraz przekazywanie/pobieranie kontekstu klienta z użyciem tokenów zgodnie z usługą `customerContext`.

**Uzasadnienie:** Użytkownik musi uzyskać dostęp do CashDirector bez ponownego logowania i z poprawnym kontekstem firmy.

**AC:**
- Given użytkownik ma aktywną usługę i inicjuje przejście do CashDirector
- When BE i CashDirector realizują przepływ SSO z użyciem tokenów
- Then użytkownik uzyskuje dostęp w kontekście właściwej firmy i użytkownika

---

#### RQ-ACT-006: Udostępnianie rachunków klienta
**Opis:** System BE musi udostępniać CashDirector listę aktywnych rachunków firmy przez usługę `accounts` po poprawnej autoryzacji.

**Uzasadnienie:** Dane rachunków są niezbędne do przygotowania i inicjowania płatności.

**AC:**
- Given CashDirector posiada poprawny token dostępu i identyfikatory firmy/użytkownika
- When wywołuje usługę `accounts`
- Then BE zwraca listę aktywnych rachunków firmy

---

#### RQ-ACT-007: Inicjowanie płatności z CashDirector
**Opis:** System BE musi obsługiwać inicjowanie płatności przekazanych przez CashDirector dla wskazanych typów usług inicjacji (`domesticPaymentInit`, `domesticSplitPaymentInit`, `foreignPaymentInit`, `taxPaymentInit`) i zwracać `paymentToken`.

**Uzasadnienie:** Integracja wymaga przekazania zlecenia płatności z systemu księgowego do kanału bankowego.

**AC:**
- Given CashDirector przekazuje komplet parametrów dla obsługiwanego typu płatności
- When wywołuje właściwą usługę `*PaymentInit`
- Then BE tworzy płatność i zwraca `paymentToken`

---

#### RQ-ACT-008: Autoryzacja płatności przez redirect do BE
**Opis:** System BE musi umożliwiać przekierowanie użytkownika do banku w celu autoryzacji i wykonania płatności oraz obsłużyć powrót do CashDirector.

**Uzasadnienie:** Autoryzacja operacji finansowej musi odbywać się w bankowości elektronicznej.

**AC:**
- Given CashDirector posiada `paymentToken` i `accessToken`
- When wykonuje redirect płatności do BE z `backUrl`
- Then użytkownik realizuje autoryzację w BE i wraca do CashDirector zgodnie z przepływem

---

#### RQ-ACT-009: Aktualizacja statusów płatności i idempotentność
**Opis:** System BE musi przekazywać do CashDirector informacje o zmianie statusu płatności oraz zapewniać idempotentność tych aktualizacji.

**Uzasadnienie:** Proces księgowy wymaga spójnych i niepowielonych statusów operacji.

**AC:**
- Given status płatności uległ zmianie po stronie BE
- When BE publikuje lub udostępnia status do CashDirector
- Then ta sama aktualizacja przetworzona wielokrotnie nie powoduje niespójności statusu

---

#### RQ-ACT-010: Dezaktywacja usługi inicjowana przez Bank lub CashDirector
**Opis:** System BE musi obsługiwać dezaktywację usługi CashDirector zarówno inicjowaną przez klienta/Bank, jak i żądaniem z CashDirector, z rejestracją statusu w systemach bankowych.

**Uzasadnienie:** Cykl życia usługi musi obejmować kontrolowane zakończenie współpracy i spójność statusów.

**AC:**
- Given istnieje aktywna usługa CashDirector dla firmy
- When wystąpi żądanie dezaktywacji z BE albo z CashDirector
- Then BE wykonuje dezaktywację i zapisuje końcowy status usługi

---

#### RQ-ACT-011: Przekazywanie leadów sprzedażowych
**Opis:** System BE musi umożliwiać identyfikację i przekazanie leada sprzedażowego do CashDirector po uzyskaniu wymaganych zgód klienta.

**Uzasadnienie:** Wymagany jest obsługiwany przez integrację przepływ danych sprzedażowych.

**AC:**
- Given w procesie bankowym zidentyfikowano leada i dostępne są wymagane zgody
- When BE uruchamia przekazanie leada do CashDirector
- Then dane leada są przekazane do CashDirector

---

#### RQ-ACT-012: Przekazywanie historii operacji bankowych
**Opis:** System BE musi udostępniać CashDirector historię operacji bankowych w modelu REST API lub zdarzeniowym oraz przekazywać minimalny zestaw danych transakcyjnych wymaganych do obsługi księgowej.

**Uzasadnienie:** Dane transakcyjne są niezbędne do obsługi procesów księgowych w CashDirector.

**AC:**
- Given CashDirector żąda danych historii operacji w obsługiwanym modelu integracji
- When BE realizuje przekazanie danych
- Then CashDirector otrzymuje historię operacji zawierającą wymagany minimalny zakres danych

---

#### 3.1.1 Obsługa błędów

#### RQ-ACT-013: Obsługa błędów aktywacji i dezaktywacji
**Opis:** System BE musi przerywać proces aktywacji/dezaktywacji w przypadku błędu integracyjnego, prezentować komunikat użytkownikowi oraz utrzymywać spójny status usługi.

**Uzasadnienie:** Błędy procesów krytycznych nie mogą prowadzić do niejednoznacznego stanu usługi.

**AC:**
- Given w trakcie aktywacji albo dezaktywacji wystąpi błąd wywołania integracyjnego
- When BE obsługuje błąd
- Then proces jest zatrzymany, użytkownik otrzymuje komunikat, a status usługi pozostaje spójny

---

#### RQ-ACT-014: Rejestrowanie i monitorowanie błędów integracyjnych
**Opis:** System BE musi rejestrować i monitorować błędy występujące w procesach integracyjnych z CashDirector.

**Uzasadnienie:** Wymagana jest audytowalność i możliwość operacyjnej analizy incydentów.

**AC:**
- Given wystąpił błąd w dowolnym procesie integracji BE-CashDirector
- When BE zapisuje zdarzenie błędu
- Then błąd jest dostępny do monitorowania i analizy operacyjnej

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: /src/*, /doc/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->
---
#### 3.2.1. Wydajność
- OPEN-QUESTION-001: Jakie są docelowe czasy odpowiedzi (SLA) dla usług `customerContext`, `accounts` oraz `*PaymentInit`?
- OPEN-QUESTION-002: Jaki jest wymagany wolumen (TPS/liczba żądań) dla integracji BE-CashDirector w godzinach szczytu?

#### 3.2.2. Bezpieczeństwo

#### RQ-ACT-015: Ochrona dostępu i danych integracyjnych
**Opis:** System BE musi wymagać poprawnej autoryzacji tokenowej dla usług integracyjnych oraz ograniczać dostęp do danych firmowych do właściwego kontekstu firmy i użytkownika.

**Uzasadnienie:** Integracja przetwarza dane finansowe i identyfikacyjne, które wymagają kontrolowanego dostępu.

**AC:**
- Given żądanie integracyjne dotyczy danych firmy lub operacji płatniczej
- When żądanie jest przetwarzane przez BE
- Then BE dopuszcza operację wyłącznie po poprawnej autoryzacji i zgodności kontekstu firmy/użytkownika

#### 3.2.3. Wdrożenie i proces migracji danych
- OPEN-QUESTION-003: Czy wdrożenie wymaga migracji istniejących powiązań firma-użytkownik między BE i CashDirector?
- OPEN-QUESTION-004: Jaki jest wymagany plan cut-over/rollback dla uruchomienia integracji produkcyjnej?
## 5. Wymagane licencje
<!-- SPW-SECTION
Cel: Wskaż licencje / zależności licencyjne wymagane przez rozwiązanie.
Źródła: /src/*, /doc/*
Wyjście: lista licencji i zakres ich użycia.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 6. Obszary pod wpływem
<!-- SPW-SECTION
Cel: Wymień systemy, moduły, procesy i kanały dotknięte zmianą.
Źródła: /src/*, /doc/*
Wyjście: lista obszarów + krótki opis wpływu.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
---
## 7. Założenia i ograniczenia
<!-- SPW-SECTION
Cel: Zapisz założenia, ograniczenia oraz decyzje projektowe wpływające na zakres.
Źródła: /src/*, /doc/*
Wyjście: lista punktów; brakujące dane oznaczaj OPEN-QUESTION.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->

## 8. Zagadnienia otwarte
- OPEN-QUESTION-005: `src/wymagania banku.md` jest pusty (0 linii). Czy istnieje brakujący dokument wymagań banku, który powinien zostać uwzględniony?
- OPEN-QUESTION-006: Czy lista rachunków przekazywana przez usługę `accounts` ma zawierać również informacje o saldach dostępnych (wymóg w `src/wymagania.md`) czy wyłącznie pola opisane w `src/banki-api-uslugi-banku.md`?
- OPEN-QUESTION-007: Jaki jest minimalny zakres danych dla historii operacji wymagany przez CashDirector (nazwy pól, zakres dat, statusy)?
## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: /src/*, /doc/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
