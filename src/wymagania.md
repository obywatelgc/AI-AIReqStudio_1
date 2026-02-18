# Wymagania funkcjonalne – system BE (Bankowość Elektroniczna dla klientów instytucjonalnych)

## 1. Cel dokumentu
Celem dokumentu jest opisanie wymagań funkcjonalnych dla systemu Bankowości Elektronicznej (BE) obsługującego klientów instytucjonalnych, w zakresie integracji z systemem księgowym CashDirector (CD) poprzez API. Dokument stanowi podstawę dla projektowania, implementacji i testów backendu BE.

## 2. Zakres funkcjonalny integracji
Integracja BE–CashDirector obejmuje następujące obszary funkcjonalne:
- aktywacja usługi księgowej CashDirector,
- rejestracja firmy i użytkownika w CashDirector,
- logowanie jednokrotne (SSO),
- dezaktywacja usługi (inicjowana przez Bank lub CashDirector),
- inicjowanie i realizacja płatności,
- przekazywanie statusów płatności,
- przekazywanie leadów sprzedażowych,
- przekazywanie historii operacji bankowych.

## 3. Aktorzy
- **Klient instytucjonalny / Właściciel firmy** – użytkownik BE.
- **System BE (Backend Banku)** – system nadrzędny orkiestrujący procesy.
- **CashDirector** – zewnętrzny system księgowy.

## 4. Wymagania funkcjonalne

### 4.1 Aktywacja usługi CashDirector
**Opis wymagań**

**WM-01 Aktywacja usługi CashDirector**  
System BE musi umożliwiać klientowi uruchomienie procesu aktywacji usługi CashDirector z poziomu bankowości elektronicznej.
W Systemie BE w menu głowym dodana zostanie opcja "eKsiegowość" która w zależności czy Klient aktywował usługę:
- zaprezentuje ekran aktywacji (usługa nie aktywna)
- przekieruje użyktkownika do CB (ułsuga aktywna)

**DEC-ACT-001 Status aktywacji usługi (dla firmy)**  
System BE utrzymuje status aktywacji usługi CashDirector w ujęciu firmy (kontekstu firmowego) i wykorzystuje go do decyzji o prezentacji ekranu aktywacji lub przekierowaniu do CashDirector po wybraniu opcji „eKsięgowość”.

**DEC-ACT-002 Dostępność w kontekstach**  
Funkcjonalność aktywacji usługi CashDirector jest dostępna w kontekście firmowym (mikro oraz korporacyjnym).

**DEC-ACT-004 Audyt/Rejestr zdarzeń**  
System BE rejestruje uruchomienie procesu aktywacji usługi CashDirector w Rejestrze zdarzeń jako typ zdarzenia „Aktywacja usługi CashDirector”.

**WM-02 Obsługa zgód i regulaminów**  
System BE musi umożliwiać pobranie, prezentację oraz rejestrację akceptacji zgód, regulaminów i umów wymaganych do aktywacji usługi CashDirector.
Zakładamy, że BE zaprezentuje zgody, które wskaże Bank. Wykorzystane zostaną usł

Dodatkowo na formularzu udostępnione zostaną (w formie plików do pobrania) pliki wskazane przez Bank (regualminy, formularze umów). Nie zakładamy generowania umów po stronie BE, podpisywania dokumentów oraz ich wysłania do KLienta. Na formularzu zaprezentowane zostaną wyłącznie treści oraz pliki wskazane przez Bank.

**WM-02a Ekran aktywacji: zgody i regulaminy**  
System BE musi udostępnić ekran aktywacji usługi CashDirector umożliwiający prezentację treści zgód/regulaminów/umów oraz pobranie plików wskazanych przez Bank, wraz z mechanizmem rejestracji akceptacji przez użytkownika.

**WM-03 Rejestracja firmy w CashDirector**  
System BE musi przekazywać dane identyfikacyjne firmy oraz właściciela do systemu CashDirector w celu rejestracji usługi.

**WM-04 Obsługa błędu aktywacji**  
System BE musi przerwać proces aktywacji i zaprezentować klientowi komunikat o błędzie w przypadku niepowodzenia rejestracji usługi.

### 4.2 Rejestracja i parowanie firmy
**Opis wymagań**

**WM-05 Parowanie firmy i użytkownika**  
System BE musi umożliwiać parowanie firmy i użytkownika z istniejącymi rekordami w CashDirector przy użyciu identyfikatorów zewnętrznych.

**WM-06 Obsługa istniejących danych w CashDirector**  
System BE musi obsługiwać scenariusz, w którym firma lub użytkownik istnieje już w systemie CashDirector.

### 4.3 Logowanie jednokrotne (SSO)
**Opis wymagań**

**WM-07 Logowanie jednokrotne do CashDirector**  
System BE musi umożliwiać logowanie użytkownika do CashDirector z wykorzystaniem mechanizmu SSO.

**WM-08 Zarządzanie tokenami dostępowymi**  
System BE musi obsługiwać pobieranie i odświeżanie tokenów dostępowych wykorzystywanych w integracji z CashDirector.

### 4.4 Pobieranie danych rachunków
**Opis wymagań**

**WM-09 Udostępnianie rachunków klienta**  
System BE musi umożliwiać przekazywanie do CashDirector listy rachunków klienta wraz z informacją o dostępnych saldach.

**WM-10 Autoryzacja dostępu do danych rachunkowych**  
System BE musi zapewnić, że dane rachunkowe są udostępniane wyłącznie po poprawnej autoryzacji użytkownika.

### 4.5 Dezaktywacja usługi – inicjowana przez Bank
**Opis wymagań**

**WM-11 Inicjacja dezaktywacji przez klienta**  
System BE musi umożliwiać klientowi zainicjowanie procesu dezaktywacji usługi CashDirector.

**WM-12 Rejestracja dezaktywacji usługi**  
System BE musi rejestrować dezaktywację usługi CashDirector w systemie CashDirector.

**WM-13 Dezaktywacja firmy i użytkowników**  
System BE musi umożliwiać dezaktywację firmy oraz użytkowników powiązanych z usługą CashDirector.

**WM-14 Obsługa błędów dezaktywacji**  
System BE musi obsługiwać błędy procesu dezaktywacji i zapewnić spójność statusu usługi.

### 4.6 Dezaktywacja usługi – inicjowana przez CashDirector
**Opis wymagań**

**WM-15 Obsługa żądania dezaktywacji z CashDirector**  
System BE musi obsługiwać żądanie dezaktywacji usługi CashDirector inicjowane po stronie CashDirector.

**WM-16 Autoryzacja dezaktywacji**  
System BE musi przeprowadzić autoryzację użytkownika przed potwierdzeniem dezaktywacji usługi.

**WM-17 Rejestracja statusu dezaktywacji**  
System BE musi zapisać status dezaktywacji usługi CashDirector w systemach bankowych.

### 4.7 Inicjowanie płatności
**Opis wymagań**

**WM-18 Inicjowanie płatności z CashDirector**  
System BE musi umożliwiać inicjowanie płatności zleconych w systemie CashDirector.

**WM-19 Autoryzacja płatności w BE**  
System BE musi przekierować użytkownika do bankowości elektronicznej w celu autoryzacji płatności.

**WM-20 Walidacja płatności**  
System BE musi weryfikować poprawność danych płatności oraz dostępność środków.

### 4.8 Aktualizacja statusu płatności
**Opis wymagań**

**WM-21 Aktualizacja statusu płatności**  
System BE musi przekazywać do CashDirector informacje o zmianie statusu płatności.

**WM-22 Idempotentność statusów płatności**  
System BE musi zapewnić idempotentność aktualizacji statusów płatności przekazywanych do CashDirector.

### 4.9 Przekazywanie leadów
**Opis wymagań**

**WM-23 Identyfikacja leada sprzedażowego**  
System BE musi umożliwiać identyfikację leada sprzedażowego w trakcie procesów bankowych związanych z obsługą klienta instytucjonalnego.

**WM-24 Przekazanie leada do CashDirector**  
System BE musi umożliwiać przekazanie danych leada sprzedażowego do systemu CashDirector po uzyskaniu wymaganych zgód klienta.

### 4.10 Przekazywanie historii operacji bankowych
**Opis wymagań**

**WM-25 Przekazywanie historii operacji**  
System BE musi umożliwiać przekazywanie historii operacji bankowych do systemu CashDirector.

**WM-26 Obsługa różnych wariantów integracji**  
System BE musi obsługiwać przekazywanie danych operacji bankowych w modelu REST API lub zdarzeniowym.

**WM-27 Zakres przekazywanych danych transakcyjnych**  
System BE musi przekazywać minimalny zestaw danych transakcyjnych wymaganych do obsługi księgowej.

## 5. Obsługa błędów i scenariusze alternatywne
**Opis wymagań**

**WM-28 Rejestrowanie błędów integracyjnych**  
System BE musi rejestrować i monitorować błędy występujące w procesach integracyjnych.

**WM-29 Komunikaty dla użytkownika**  
System BE musi prezentować użytkownikowi czytelne komunikaty w przypadku niepowodzenia realizacji procesu.

## 6. Wymagania końcowe
**Opis wymagań**

**WM-30 Spójność danych integracyjnych**  
System BE musi zapewnić spójność danych pomiędzy systemami Banku i CashDirector.

**WM-31 Audytowalność zdarzeń**  
System BE musi zapewnić możliwość audytu kluczowych zdarzeń integracyjnych, w szczególności aktywacji, dezaktywacji oraz płatności.
