# Wymagania funkcjonalne – system BE (Bankowość Elektroniczna dla klientów instytucjonalnych)

## 1. Cel projektu
Celem projektu jest dostosowanie systemów Asseco CB i Asseco EBP do zmian wynikających z wprowadzenia przez Krajową Izbę Rozliczeniową nowego formatu wymiany danych w ramach rozliczeń w systemie płatności krajowych w PLN ELIXIR implementującego standard ISO 20022 pod nazwą ELIXIR XML oraz integracja systemu Asseco CB z systemami typu Payment Hub w obszarze płatności ELIXIR XML

## 2. Zakres funkcjonalny integracji
dostosowanie systemów Asseco CB i Asseco EBP do zmian wynikających z wprowadzenia przez Krajową Izbę Rozliczeniową nowego formatu wymiany danych w ramach rozliczeń w systemie płatności krajowych w PLN ELIXIR implementującego standard ISO 20022 pod nazwą ELIXIR XML

## 3. Aktorzy
- **Klient indywidualny** – użytkownik BE.
- **Klient instytucjonalny / Właściciel firmy** – użytkownik BE.
- **System BE (CBP i EBP)** – system bankowości internetowej detal i korpo
- **System CB (CB)** – system transakcyjny w Banku master data
- **Payment HUB (PH)** – system rozliczeniowy


## 4. Wymagania funkcjonalne

### 4.1 ELIXIR XML w BE
**Opis wymagań**

**WM-01 ELIXIR XML - Integracja Asseco CB z Payment Hub**  
Wymaganiem jest integracja systemu Asseco CB z systemem typu Payment Hub w ramach płatności realizowanych jako ELIXIR XML\.

**WM-02 ELIXIR XML - Integracja Asseco CB z Payment Hub**  
Wymaganiem jest integracja systemu Asseco CB z system

**WM-01 ELIXIR XML - Kompensacja zmian w API Asseco CB**
Wymaganiem jest zapewnienie kompensacji zmian w interfejsach API Asseco CB w zakresie zlecania przelewów bieżących i odroczonych.

**WM-02 ELIXIR XML - Przekazywanie przelewu bieżącego z danymi ustrukturyzowanymi**
Wymaganiem jest przekazywanie przelewu bieżącego (ELIXIR) do Asseco CB z danymi adresowymi w postaci ustrukturyzowanej.

**WM-03 ELIXIR XML - Rejestracja przelewu odroczonego i zlecenia stałego**
Wymaganiem jest rejestracja w Asseco CB zlecenia przelewu odroczonego oraz zlecenia stałego z danymi adresowymi w postaci ustrukturyzowanej.

**WM-04 ELIXIR XML - Edycja aktywnego zlecenia stałego**
Wymaganiem jest umożliwienie edycji aktywnego zlecenia stałego w zakresie danych adresowych ustrukturyzowanych oraz przekazywanie tej edycji do Asseco CB z danymi ustrukturyzowanymi.

**WM-05 ELIXIR XML - Rozbudowa importu przelewów i szablonów**
Wymaganiem jest rozbudowa formatów importu przelewów i szablonów w zakresie ustrukturyzowanych danych adresowych.

**WM-06 ELIXIR XML - Rozbudowa ERP API, BS API i PSD2 API**
Wymaganiem jest rozbudowa usług ERP API, BS API i PSD2 API w zakresie obsługi danych ustrukturyzowanych w przelewach ELIXIR.

