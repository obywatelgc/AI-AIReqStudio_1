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

### 1.2 Wymagania klienta
<!-- SPW-SECTION
Cel: Przenieś i streść wymagania przekazane przez Klienta.
Źródła: Wymagania klienta: src/*
Wyjście: lista wymagań/założeń z odnośnikami do źródeł.
-->

## 2. Perspektywa biznesowa rozwiązania

### 2.1. Słownik pojęć
<!-- SPW-SECTION
Cel: Zdefiniuj terminy używane w dokumencie (lub wskaż, że obowiązuje słownik źródłowy).
Źródła: Dokumentacja systemu: doc/* (np. doc/glossary.md)
Wyjście: lista pojęć i definicji; bez wprowadzania nowych znaczeń.
-->

### 2.2. Stan obecny
<!-- SPW-SECTION
Cel: Opisz stan obecny w zakresie objętym zmianą (as-is).
Źródła: Dokumentacja systemu: doc/*
Wyjście: krótki opis + kluczowe ograniczenia i zależności.
-->

### 2.3. Model rozwiązania #zakres bazowy
<!-- SPW-SECTION
Cel: Opisz docelowy model rozwiązania w zakresie zmian (to-be) na poziomie biznesowym.
Źródła: src/*, doc/*
Wyjście: opis przepływu + kluczowe decyzje biznesowe.
-->

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
Źródła: Wymagania klienta: src/*
-->
### 3.1 Wymagania funkcjonalne

#### RQ-001: [NAZWA WYMAGANIA]
**Opis:** [OPIS WYMAGANIA]

**Stan obecny:** [OPIS STANU OBECNEGO SYSTEMU]

**Opis modyfikacji:** [OPIS ZMIANY STANU OBECNEGO W SYSTEMIE NA PODSTAWIE WYMGAŃ KLINTA]

**Źródła:**
- Wymaganie klienta: `[src/<plik>.md#sekcja]`
- Stan obecny (as-is): `[doc/<plik>.md|.adoc#sekcja]`

**AC:** 
- Given …
- When …
- Then …

---

#### RQ-002: [NAZWA WYMAGANIA]
**Opis:** [OPIS WYMAGANIA]

**Stan obecny:** [OPIS STANU OBECNEGO SYSTEMU]

**Opis modyfikacji:** [OPIS ZMIANY STANU OBECNEGO W SYSTEMIE NA PODSTAWIE WYMGAŃ KLINTA]

**Źródła:**
- Wymaganie klienta: `[src/<plik>.md#sekcja]`
- Stan obecny (as-is): `[doc/<plik>.md|.adoc#sekcja]`

**AC:**
- Given …
- When …
- Then …

---

#### RQ-003: [NAZWA WYMAGANIA]
**Opis:** [OPIS WYMAGANIA]

**Stan obecny:** [OPIS STANU OBECNEGO SYSTEMU]

**Opis modyfikacji:** [OPIS ZMIANY STANU OBECNEGO W SYSTEMIE NA PODSTAWIE WYMGAŃ KLINTA]

**Źródła:**
- Wymaganie klienta: `[src/<plik>.md#sekcja]`
- Stan obecny (as-is): `[doc/<plik>.md|.adoc#sekcja]`

**AC:**
- Given …
- When …
- Then …

---

#### RQ-004: [NAZWA WYMAGANIA]
**Opis:** [OPIS WYMAGANIA]

**Stan obecny:** [OPIS STANU OBECNEGO SYSTEMU]

**Opis modyfikacji:** [OPIS ZMIANY STANU OBECNEGO W SYSTEMIE NA PODSTAWIE WYMGAŃ KLINTA]

**Źródła:**
- Wymaganie klienta: `[src/<plik>.md#sekcja]`
- Stan obecny (as-is): `[doc/<plik>.md|.adoc#sekcja]`

**AC:**
- Given …
- When …
- Then …

---

#### RQ-005: [NAZWA WYMAGANIA]
**Opis:** [OPIS WYMAGANIA]

**Stan obecny:** [OPIS STANU OBECNEGO SYSTEMU]

**Opis modyfikacji:** [OPIS ZMIANY STANU OBECNEGO W SYSTEMIE NA PODSTAWIE WYMGAŃ KLINTA]

**Źródła:**
- Wymaganie klienta: `[src/<plik>.md#sekcja]`
- Stan obecny (as-is): `[doc/<plik>.md|.adoc#sekcja]`

**AC:**
- Given …
- When …
- Then …

---

#### 3.1.1 Obsługa błędów
(Ta sekcja MUSI istnieć)

---

### 3.2 Wymagania niefunkcjonalne
<!-- SPW-SECTION
Cel: Zdefiniuj wymagania niefunkcjonalne dla zakresu zmian.
Źródła: src/*, doc/*
Wyjście: wymagania testowalne + mierzalne kryteria akceptacji, jeśli możliwe.
-->
---
#### 3.2.1. Wydajność
#### 3.2.2. Bezpieczeństwo
#### 3.2.3. Wdrożenie i proces migracji danych
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
- OPEN-QUESTION-001: …
## 9. Załączniki
<!-- SPW-SECTION
Cel: Dołącz lub wskaż materiały referencyjne (np. diagramy, tabele, słowniki, zrzuty).
Źródła: src/*, doc/*
Wyjście: lista załączników + identyfikatory/odnośniki.
Generowanie: POMIŃ (ten rozdział uzupełniany ręcznie)
-->
