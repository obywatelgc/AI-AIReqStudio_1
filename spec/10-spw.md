<!-- AI-CONSTRAINTS
Zakres: Opis zakresu modyfikacji
Format: RQ-###
Źródła: 
    Wymagania klienta: src/*, 
    Dokumentacja systemu: doc/*
    Parametry projektu: /project-parameters.md
-->

# Specyfikacja wymagań – {{PROJECT_NAME}}

## 1. Wprowadzenie

### 1.1 Cel biznesowy projektu
<!-- SPW-SECTION
Cel: Opisz główny cel biznesowy rozwiązania dla wskazanego zakresu modyfikacji.
    Przykład: 
    Celem biznesowym projektu jest umożliwienie klientom bankowości elektronicznej (web i mobile) samodzielnego pobrania ostatniego wyciągu z rachunku w formacie elektronicznym (np. PDF, csv) w celu zwiększenia poziomu samoobsługi, redukcji kosztów operacyjnych oraz poprawy doświadczenia użytkownika.
    Nie stosuj zaspiów w stylu: 
    Celem bizesowym jest dodanie opcji "Pobierz ostatni wyciąg".
Zakres: Perspektywa biznesowa (nie opis implementacji IT).
Źródła: Wymagania klienta: src/*
Wyjście: 3–5 zdań.
Kryteria jakości: jednoznaczność, brak domysłów, spójność terminologii.
-->
Celem biznesowym projektu jest ograniczenie ryzyka operacyjnego i regulacyjnego wynikającego z korzystania z bankowości elektronicznej przez użytkownika z nieważnym dokumentem tożsamości. Zmiana ma wymusić aktualizację danych dokumentu po przekroczeniu zdefiniowanego okresu tolerancji, bez wyłączania ścieżki złożenia odpowiedniego wniosku aktualizacyjnego. Zakres obejmuje kanał desktop i mobile oraz logowanie w scenariuszu szybkich płatności PBN. Rozwiązanie ma utrzymać standardowe logowanie dla użytkowników z ważnym dokumentem albo nieprzekroczonym okresem tolerancji.

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->
- WM-01: Po zalogowaniu system BE sprawdza ważność dokumentu tożsamości użytkownika.  
  Źródło: `src/wymagania.md` (sekcja: „4. Wymagania funkcjonalne”, pozycja „WM-01”).
- Jeżeli data ważności dokumentu jest nieaktualna, BE aktualizuje datę dokumentu na podstawie danych z Asseco CB.  
  Źródło: `src/wymagania.md` (WM-01).
- Jeżeli po aktualizacji dokument nadal jest nieważny, BE stosuje parametr `idExpiryGracePeriodDays` i po jego przekroczeniu uruchamia tryb restrykcyjny.  
  Źródło: `src/wymagania.md` (WM-01).
- W trybie restrykcyjnym użytkownik widzi komunikat i może przejść wyłącznie do opcji Wnioski (wniosek Ferryt aktualizacji danych dokumentu).  
  Źródło: `src/wymagania.md` (WM-01).
- Tryb restrykcyjny działa dla desktop i mobile; w mobile w trybie restrykcyjnym nie można przejść do generowania kodu BLIK.  
  Źródło: `src/wymagania.md` (WM-01).
- Gdy dokument jest ważny albo nie przekroczono `idExpiryGracePeriodDays`, logowanie przebiega standardowo. Zmiana obejmuje również logowanie dla szybkich płatności PBN.  
  Źródło: `src/wymagania.md` (WM-01 + zdanie końcowe).

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: doc/* (np. doc/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->
- Obowiązuje słownik źródłowy: `doc/glossary.md`.
- **BE** – system bankowości elektronicznej.  
  Źródło: `doc/glossary.md`.
- **Użytkownik** – osoba fizyczna działająca w imieniu firmy.  
  Źródło: `doc/glossary.md`.
- **Kontekst firmowy/korporacyjny** – kontekst klienta obsługiwany w module Asseco EBP.  
  Źródło: `doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md`.
- **Tryb restrykcyjny** – tryb wymuszający wykonanie wymaganej czynności przez użytkownika po zalogowaniu; w AS-IS opisany dla potwierdzenia danych osobowych.  
  Źródło: `doc/EBP/Main.adoc`, `doc/CBP/Main.adoc`.
- **Kod BLIK / Szybka Płatność BLIK** – kod używany do płatności; szybka płatność wykorzystuje kod wygenerowany bez logowania do aplikacji mobilnej.  
  Źródło: `doc/mobile/blik.adoc`, `doc/mobile/blik_t6_generowanie_kodu.adoc`.
- **Wnioski** – miniaplikacja używana do obsługi procesów wnioskowych.  
  Źródło: `doc/CBP/Miniaplikacja_Kredyty.adoc`, `doc/CBP/Miniaplikacja_Ubezpieczenia.adoc`, `doc/EBP/Miniaplikacja_Karty.adoc`.

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: doc/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->
- System BE działa w kanałach desktop i mobile; dla kontekstu firmowego wykorzystywany jest moduł Asseco EBP.  
  Źródło: `doc/system-state/kluczowe-wytyczne-stan-obecny-systemu.md`.
- W EBP istnieją standardowe procesy logowania i tryby dostępu, w tym logowanie po przekierowaniu z PayByNet.  
  Źródło: `doc/EBP/Main.adoc` (sekcje „Tryby dostępu do systemu”, „Logowanie do systemu”).
- W AS-IS system prezentuje po zalogowaniu informację o upływającej/utraconej ważności dokumentu tożsamości oraz umożliwia przejście do danych osobowych i ich edycji.  
  Źródło: `doc/CBP/Main.adoc` (sekcja „Informacja o upływającym terminie ważności dokumentu tożsamości”), `doc/EBP/Main.adoc` (sekcja „Dane osobowe/Dane firmy”).
- W AS-IS istnieje tryb restrykcyjny dla cyklicznego potwierdzania danych osobowych (z parametrem liczby dni), który blokuje przejście do innych opcji niż dane osobowe do momentu potwierdzenia/edycji.  
  Źródło: `doc/EBP/Main.adoc`, `doc/CBP/Main.adoc`, `doc/BO/BackofficeUserGuide-pl.adoc`.
- W aplikacji mobilnej użytkownik może przejść do generowania kodu BLIK zarówno przed zalogowaniem, jak i po zalogowaniu; szybkie płatności BLIK działają bez logowania do aplikacji.  
  Źródło: `doc/mobile/logowanie.adoc`, `doc/mobile/blik.adoc`, `doc/mobile/blik_t6_generowanie_kodu.adoc`, `doc/mobile/blik_ustawienia_zgody.adoc`.
- Brak potwierdzenia w `doc/*` dla automatycznego odświeżania daty dokumentu tożsamości z Asseco CB podczas logowania oraz dla szczegółowej definicji procesu Ferryt dla aktualizacji dokumentu.  
  Status: `OPEN-QUESTION-005`, `OPEN-QUESTION-006`.

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: src/*, doc/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->
Docelowo system po zalogowaniu użytkownika sprawdza ważność dokumentu tożsamości, a w przypadku wykrycia nieaktualnej daty wykonuje odświeżenie danych z Asseco CB. Jeżeli po odświeżeniu dokument nadal jest nieważny, system porównuje stan z parametrem `idExpiryGracePeriodDays` i po przekroczeniu progu uruchamia tryb restrykcyjny. W trybie restrykcyjnym użytkownik dostaje komunikat i ma dostęp wyłącznie do opcji Wnioski, gdzie realizuje proces aktualizacji danych dokumentu. Dla kanału mobile tryb restrykcyjny dodatkowo blokuje przejście do generowania kodu BLIK, a standardowy dostęp do kodu BLIK pozostaje poza trybem restrykcyjnym. Tę samą logikę system stosuje do logowania w scenariuszu szybkich płatności PBN.

## 3. Wymagania szczegółowe
<!-- SPW-SECTION
Cel: W niniejszym rozdziale jest dokonane mapowanie modelu rozwiązania na nowe i modyfikowane wymagania/user stories.
Przykład:
Opis: 
[Krótki opis wymagania]
Dodanie opcji pobrania ostatniego wyciągu.

Stan obecny:
[Opis stanu obecnego as-is na podstawie /doc/**. UWAGA! Jeżeli nie znaleziono informacji o danej funkcjonalności w systemie to należy dodać opis, że danej funkcjonlaności nie ma w systemie!]
Obecnie w sytemie Asseco EBP użytkonik ma możliwość przejścia z poziomu rachunku do opcji podglądu listy wyciągów danego rachunku. System po wejściu w opcję, prezentuje listę wyciągów z możliwością pobrania w formacie pdf, csv.

Opis modyfikacji:
[Opis modyfikacji to-be na postawie wymagań Klieta /src/wymagania.md]
Zmiana polegała będzie na dodaniu na poziomoie listy rachunków (miniaplikacja Rachunki) nowej opcji "Ostatni wyciąg". Opcja pozwoli użytkownikowi na pobiranie ostatniego (najnowszego) wyciągu bez potrzeby wchodzenia w listę wyciągów.

Źródła: 
Wymagania klienta: src/*
Stan obecny (as-is): doc/**
AC: (pilnuj wcięć dla każej z lini Given/When/Then)
-->
### 3.1 Wymagania funkcjonalne

#### RQ-001: Weryfikacja ważności dokumentu tożsamości po logowaniu
**Opis:** System BE weryfikuje ważność dokumentu tożsamości po zalogowaniu użytkownika.

**Stan obecny:** W AS-IS po zalogowaniu system prezentuje komunikaty o upływającej lub utraconej ważności dokumentu tożsamości oraz umożliwia edycję danych dokumentu w ustawieniach. Dokumentacja nie opisuje blokowania logowania wyłącznie z powodu utraty ważności dokumentu na tym etapie.

**Opis modyfikacji:** Po zalogowaniu BE sprawdza datę ważności dokumentu tożsamości. Jeżeli dokument jest nieaktualny, system uruchamia odświeżenie daty dokumentu z Asseco CB i dopiero na tej podstawie wykonuje dalszą decyzję o dostępie.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#wm-01]`
- Stan obecny (as-is): `[doc/CBP/Main.adoc#informacja-o-uplywajacym-terminie-waznosci-dokumentu-tozsamosci]`
- Stan obecny (as-is): `[doc/EBP/Main.adoc#dane-osobowedane-firmy]`

**AC:** 
- Given użytkownik poprawnie się zalogował do BE
- When system wykryje, że data ważności dokumentu tożsamości jest nieaktualna
- Then system pobierze aktualną datę dokumentu z Asseco CB przed podjęciem decyzji o dostępie

---

#### RQ-002: Uruchomienie trybu restrykcyjnego po przekroczeniu `idExpiryGracePeriodDays`
**Opis:** System uruchamia tryb restrykcyjny, gdy po odświeżeniu danych dokument pozostaje nieważny i przekroczony jest próg `idExpiryGracePeriodDays`.

**Stan obecny:** W AS-IS istnieje tryb restrykcyjny dla procesu potwierdzania danych osobowych sterowany parametrem liczby dni. W tej logice użytkownik nie może przejść do innych opcji niż dane osobowe do momentu wykonania wymaganej czynności.

**Opis modyfikacji:** System wykorzystuje analogiczny mechanizm restrykcyjny dla scenariusza nieważnego dokumentu tożsamości, ale z parametrem biznesowym `idExpiryGracePeriodDays` i warunkiem po odświeżeniu danych z Asseco CB.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#wm-01]`
- Stan obecny (as-is): `[doc/EBP/Main.adoc#tryb-restrykcyjny]`
- Stan obecny (as-is): `[doc/CBP/Main.adoc#tryb-restrykcyjny]`
- Stan obecny (as-is): `[doc/BO/BackofficeUserGuide-pl.adoc#po-ilu-dniach-od-prezentacji-monitu-o-potwierdzenie-danych-jest-ono-wymagane-tryb-restrykcyjny]`

**AC:**
- Given użytkownik zalogował się, a dokument po odświeżeniu z Asseco CB nadal jest nieważny
- When liczba dni od utraty ważności przekroczy wartość `idExpiryGracePeriodDays`
- Then system uruchomi tryb restrykcyjny i ograniczy dostęp zgodnie z wymaganiem WM-01

---

#### RQ-003: Ograniczenie dostępu do opcji Wnioski w trybie restrykcyjnym
**Opis:** W trybie restrykcyjnym użytkownik może przejść wyłącznie do opcji Wnioski służącej aktualizacji danych dokumentu.

**Stan obecny:** W AS-IS miniaplikacja Wnioski jest wykorzystywana przez różne procesy biznesowe (np. kredyty, ubezpieczenia, karty). W dokumentacji brak opisu dedykowanego procesu Ferryt dla aktualizacji dokumentu tożsamości i brak opisu globalnego ograniczenia dostępu wyłącznie do Wniosków po logowaniu.

**Opis modyfikacji:** System po wejściu w tryb restrykcyjny prezentuje komunikat i udostępnia użytkownikowi wyłącznie ścieżkę do opcji Wnioski, w której realizowany jest wniosek Ferryt aktualizacji danych dokumentu tożsamości.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#wm-01]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Kredyty.adoc#miniaplikacja-kredyty]`
- Stan obecny (as-is): `[doc/CBP/Miniaplikacja_Ubezpieczenia.adoc#zlozenie-wniosku-o-zakup-ubezpieczenia]`
- Stan obecny (as-is): `[doc/EBP/Miniaplikacja_Karty.adoc#wniosek-o-karte-debetowa-cardon]`

**AC:**
- Given użytkownik znajduje się w trybie restrykcyjnym po logowaniu
- When użytkownik próbuje przejść do dowolnej opcji innej niż Wnioski
- Then system blokuje przejście i utrzymuje dostęp wyłącznie do opcji Wnioski oraz prezentuje komunikat restrykcyjny

---

#### RQ-004: Blokada generowania kodu BLIK w mobile w trybie restrykcyjnym
**Opis:** W trybie restrykcyjnym mobile system nie pozwala na przejście do generowania kodu BLIK.

**Stan obecny:** W AS-IS użytkownik w mobile może przejść do opcji [Kod BLIK] z ekranu powitalnego przed logowaniem albo po zalogowaniu. Dokumentacja BLIK opisuje obsługę szybkich płatności opartych o kod BLIK wygenerowany bez logowania do aplikacji.

**Opis modyfikacji:** Po aktywacji trybu restrykcyjnego dla nieważnego dokumentu tożsamości system mobile blokuje przejście do ekranu generowania kodu BLIK, niezależnie od ścieżki wejścia.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#wm-01]`
- Stan obecny (as-is): `[doc/mobile/logowanie.adoc#logowanie---ekran-powitalny]`
- Stan obecny (as-is): `[doc/mobile/blik.adoc#usluga-blik]`
- Stan obecny (as-is): `[doc/mobile/blik_t6_generowanie_kodu.adoc#generowanie-kodu-blik]`
- Stan obecny (as-is): `[doc/mobile/blik_ustawienia_zgody.adoc#zgoda-na-realizacje-szybkich-platnosci]`

**AC:**
- Given użytkownik znajduje się w trybie restrykcyjnym w kanale mobile
- When użytkownik wybiera opcję [Kod BLIK] (z ekranu powitalnego lub po zalogowaniu)
- Then system nie prezentuje ekranu kodu BLIK i pozostawia użytkownika w ograniczonym dostępie zgodnym z trybem restrykcyjnym

---

#### RQ-005: Zachowanie logowania standardowego i objęcie scenariusza PBN
**Opis:** System zachowuje standardowe logowanie poza trybem restrykcyjnym i stosuje nową logikę również do logowania dla szybkich płatności PBN.

**Stan obecny:** W AS-IS EBP obsługuje logowanie pełne oraz logowanie po przekierowaniu z systemu zewnętrznego PayByNet. W dokumentacji `doc/*` nie ma jawnej definicji skrótu „PBN” ani mapowania „PBN = PayByNet”.

**Opis modyfikacji:** Jeżeli dokument jest ważny albo nie przekroczono `idExpiryGracePeriodDays`, logowanie odbywa się standardowo. Jednocześnie mechanizm kontroli dokumentu i restrykcji obejmuje także logowanie dla szybkich płatności PBN.

**Źródła:**
- Wymaganie klienta: `[src/wymagania.md#wm-01]`
- Stan obecny (as-is): `[doc/EBP/Main.adoc#tryby-dostepu-do-systemu]`
- Stan obecny (as-is): `[doc/EBP/Main.adoc#logowanie-do-systemu]`

**AC:**
- Given użytkownik loguje się w trybie standardowym lub przez ścieżkę szybkich płatności PBN
- When dokument tożsamości jest ważny albo nie upłynął `idExpiryGracePeriodDays`
- Then system realizuje logowanie standardowo dla danego trybu dostępu

---

#### 3.1.1 Obsługa błędów
(Ta sekcja MUSI istnieć)

- System w trybie restrykcyjnym prezentuje użytkownikowi komunikat o ograniczonym dostępie.  
  Status szczegółowej treści komunikatu: `OPEN-QUESTION-003`.
- Dla kanału mobile próba wejścia do generowania kodu BLIK w trybie restrykcyjnym kończy się komunikatem i brakiem przejścia do ekranu kodu.  
  Status szczegółowej treści i kodu błędu: `OPEN-QUESTION-003`.
- Gdy odświeżenie daty dokumentu z Asseco CB nie powiedzie się, źródła nie definiują oczekiwanego fallbacku (np. blokada vs tryb standardowy vs retry).  
  Status: `OPEN-QUESTION-006`.

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: src/*, doc/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->
---
#### 3.2.1. Wydajność
- W źródłach brak mierzalnych wymagań wydajnościowych (np. maksymalny czas walidacji dokumentu podczas logowania).  
  Status: `OPEN-QUESTION-007`.

#### 3.2.2. Bezpieczeństwo
- System musi egzekwować kontrolę ważności dokumentu tożsamości przy każdym logowaniu objętym zakresem zmiany i ograniczać dostęp po przekroczeniu progu `idExpiryGracePeriodDays`.
- Ograniczenie dostępu w trybie restrykcyjnym musi obowiązywać w obu kanałach (desktop, mobile), z dodatkową blokadą wejścia do kodu BLIK w mobile.
- Mechanizm ma działać także w ścieżce szybkich płatności PBN.  
  Status szczegółów mapowania PBN: `OPEN-QUESTION-004`.

#### 3.2.3. Wdrożenie i proces migracji danych
- W źródłach brak wymagań migracji danych historycznych dla tej zmiany.
- Zmiana wymaga parametryzacji wartości `idExpiryGracePeriodDays` przed uruchomieniem produkcyjnym.  
  Status miejsca konfiguracji i wartości początkowej: `OPEN-QUESTION-001`.
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
- OPEN-QUESTION-001: W jakim miejscu i przez jaki moduł administracyjny konfigurowany jest parametr `idExpiryGracePeriodDays` (ścieżka konfiguracji, wartość domyślna)?
- OPEN-QUESTION-002: Jak dokładnie liczyć `idExpiryGracePeriodDays` (dni kalendarzowe czy robocze, strefa czasowa, warunek graniczny `>` czy `>=`)?
- OPEN-QUESTION-003: Jaka jest docelowa treść komunikatów restrykcyjnych i kodów błędów dla desktop, mobile oraz ścieżki PBN?
- OPEN-QUESTION-004: Czy „PBN” w wymaganiu klienta jest równoważne trybowi logowania „PayByNet” z dokumentacji EBP i które dokładnie warianty tej ścieżki obejmuje zmiana?
- OPEN-QUESTION-005: Jaki jest dokładny proces i identyfikator wniosku Ferryt służącego aktualizacji danych dokumentu tożsamości (desktop/mobile)?
- OPEN-QUESTION-006: Jakie ma być zachowanie systemu przy niedostępności Asseco CB podczas odświeżenia daty dokumentu tożsamości?
- OPEN-QUESTION-007: Jakie są akceptowalne czasy odpowiedzi dla procesu logowania po dodaniu walidacji dokumentu i odświeżenia z Asseco CB?
- OPEN-QUESTION-008: Czy zakres zmiany dotyczy wyłącznie aktora „Klient instytucjonalny / Właściciel firmy”, czy także innych kontekstów użytkownika BE?
## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: src/*, doc/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
