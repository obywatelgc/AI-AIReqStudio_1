# POdstawowe informacje o systemie Asseco CB

Asseco Core Banking (CB) zapewnia efektywną i niezawodną obsługę transakcji klientów banku oraz szeroką i elastyczną definicję produktów i usług bankowych.

Kliento-centryczna architektura systemu, jak również możliwość szybkiej integracji z innymi systemami banku, w oparciu o zestaw usług biznesowych (SOA), w pełni spełniają wymagania architektury wielokanałowej (omnichannel architecture). System Asseco Core Banking jest rozwiązaniem kompleksowym, zdolnym do obsługi banków o różnych profilach działalności: uniwersalnych, detalicznych, korporacyjnych, hipotecznych, samochodowych oraz bankowości spółdzielczej. Asseco Core Banking jest systemem wydajnym i w pełni skalowalnym, pracującym w trybie 24x7. System transakcyjny umożliwia obsługę nawet dużych organizacji bankowych. Asseco Core Banking jest zaprojektowany do wdrożenia zarówno w siedzibie Banku, jak również może być dostarczony w modelu SaaS.

## Produkty bankowe
 
### Bankowość detaliczna
Konto osobiste 
Konto oszczędnościowe
Karta płatnicza
Depozyt terminowy: standardowy, rentierski, progresywny
Kredyt odnawialny: limit w koncie
Kredyt nieodnawialny: gotówkowy, ratalny, hipoteczny, samochodowy, z dopłatami 
Płatności: wewnętrzne, krajowe, transgraniczne
Zlecenia stałe
Polecenie zapłaty

 	 
### Bankowość korporacyjna
Rachunek bieżący z depozytem overnight, konsolidacja
Depozyt terminowy
Karta biznesowa
Kredyt odnawialny: operacyjny, kredyt w rachunku bieżącym
Kredyt nieodnawialny: inwestycyjny, dyskontowy, konsorcjalny
Linia wielozadaniowa
Płatności: wewnętrzne, krajowe, transgraniczne, lista płac
Zlecenia stałe
Gwarancja bankowa

 
 # Opis funkcjonalny w odniesieniu do BE (Bankwości Elektronicznej)
 1. BE pobiera wszystkie dane klienta (osoba fizyczna, firma) z systemu CB. Dane pochodzą z kartoteki klienta w CB za pomocą usług API (replikuje dane).
 2. BE pobiera dane umów (rachunki, lokaty, kredyty) z CB za pomocą usług API (replikuje dane).
 3. BE pobiera historię operacji na umowach z CB za pomocą usług API  (replikuje dane)
 4. BE pobiera wyciągi dla rachunków z CB za pomocą usług API.
 6. BE w celu realizacji przelewu ELIXIR, własnego, wewnątrzgrupowego wywiołuje usługi API systemu CB (inserttransferdoc).