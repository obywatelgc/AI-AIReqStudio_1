# Konwencje specyfikacji wymagań
## Integracja BE – CashDirector

## 1. Cel dokumentu
Dokument opisuje wymagania dla integracji systemów:
- Bankowość Elektroniczna (BE)
- CashDirector

Specyfikacja ma charakter:
- jednoznaczny
- testowalny
- możliwy do użycia jako podstawa do implementacji i testów

---

## 2. Zasady językowe
- MUST – wymaganie obowiązkowe
- SHOULD – wymaganie zalecane
- MAY – wymaganie opcjonalne

Unikać:
- „system umożliwia”
- „system powinien mieć możliwość”
- ogólników bez kryteriów weryfikacji

---

## 3. Struktura wymagania
Każde wymaganie MUSI zawierać:

**ID wymagania**  
**Opis wymagania** – jedno zdanie, język jednoznaczny  
**Uzasadnienie** – dlaczego to wymaganie istnieje  
**Kryteria akceptacji (AC)** – warunki testowe

### Przykład
RQ-SSO-001  
BE MUST umożliwiać jednokrotne logowanie użytkownika do CashDirector bez ponownego podawania danych uwierzytelniających.

Uzasadnienie:  
Zapewnienie spójnego doświadczenia użytkownika.

AC:
- Given użytkownik jest zalogowany w BE  
- When wybiera usługę CashDirector  
- Then zostaje zalogowany do CashDirector bez dodatkowego logowania

---

## 4. Identyfikatory wymagań
- Aktywacja usługi: `RQ-ACT-###`
- Rejestracja: `RQ-REG-###`
- SSO: `RQ-SSO-###`

Numeracja rosnąca, bez zmiany ID po review.

---

## 5. Braki i założenia
Jeżeli brak informacji:
- oznaczyć jako `OPEN-QUESTION`
- NIE zgadywać
- NIE wymyślać API, pól ani statusów
