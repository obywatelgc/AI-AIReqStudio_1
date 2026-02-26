# Wybrane zagadnienia funkcjonalne i architektoniczne
## 1. Rachunki

## 1. Przelewy
### 1. W ramach projektu ELIXIR XML obsługa:
  - rejestracji przelewu odroczonego / zlecenia stałego
  - edycji przelewu odroczonego / zlecenia stałego
  - pobierania przelewów odroczonych / zleceń stałych
  - pobierania realizacji zleceń stałych
będzie realizowana przez API REST Asseco CB 

Rejestracja przelewu odroczonego / zlecenia stałego
Zlecenie stałe: POST /application/api/current-account/current-accounts/{contractId}/standing-orders
Przelew odroczony: POST /application/api/payment-order/sepa-payment-orders/outgoing lub POST /application/api/payment-order/swift-payment-orders/outgoing/{incarnation} 

### 1. Obsługa przelewów zagranicznych w BPS (CUSTOMER_NAME=BPS)

Weryfikacji danych rejestrowanego przelewu walutowego (SEPA, SWIFT, TARGET2) realizowana jest w oparciu o API modułu Asseco CL – Proxy. Koszty realizacji zlecenia oraz kurs przewalutowania pobrany zostanie z MC (MultiCentaur). Realizacja zlecenia zostanie przekazana do systemu MC (MultiCentaur).

Klient na formularzu przelewu walutowego nie określa czy przelew zostanie zrealizowany jako SEPA/TARGET2. Wyznacza to system MC.

Koszty realizacji zlecenia oraz kurs przewalutowania pobrany zostanie z MC (valueMoneyTransfer). Realizacja zlecenia zostanie przekazana do systemu MC (setMoneyTransfer). BE odpytuje o status transakcji MC, aż do momentu osiągnięcia statusu końcowego (statusMoneyTransfer).

Przelewy walutowe wewnętrzne przekazywane są do Asseco CB (nie MC!).Do Multicentaur przekazywane są przelewy walutowe zewnętrzne oraz wewnątrzgrupowe.