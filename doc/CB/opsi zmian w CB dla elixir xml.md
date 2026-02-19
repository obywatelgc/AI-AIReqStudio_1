### Ogólne założenia

Ogólne założenia przyjęte dla wymagania **WK\.01**\.

- **Obsługa w modelu danych biznesowych**
Zakłada się implementację komunikacji z Payment Hub w zakresie Elixir XML w postaci danych biznesowych bez formatowania danych do postaci komunikatów\.

Numerowanie i formatowanie komunikatów Elixir zostanie przeniesione do Payment Hub, tzn\. Asseco CB nie będzie posługiwało się pojęciem komunikatu ani jego numerem w KIR\. W komunikacji z Payment HUB, Asseco CB będzie używało pojęć biznesowych, które nie będą numerowane wg dotychczasowej nomenklatury KIR\.

W szczególności w komunikacji z PH zakłada się używanie:

- IBAN zamiast NRB
- numerów BIC banków uczestników\.
- **Separacja Asseco CB od sesji rozliczeniowych KIR**
Asseco CB wyłączy obsługę sesyjności, dane dotyczące płatności będą wymieniane z PH bez określania sesji rozliczeniowych\. Generacja komunikatów i tworzenie plików dla płatności wychodzących w Asseco CB zostanie zastąpione przekazywaniem informacji o płatnościach w postaci informacji o uznaniach wychodzących, wychodzących żądaniach poleceń zapłaty, obciążeniach bezpośrednich, odmowach do poleceń zapłaty\. Wczytywanie plików rozliczeniowych zostanie w Asseco CB zastąpione przez przyjmowanie za pomocą API REST danych biznesowych zawierających informacje o uznaniach przychodzących, przychodzących poleceniach zapłaty, przychodzących odmowach poleceń zapłaty, przychodzących zwrotach, których źródłem będzie PH\.

W przypadku braku możliwości przetworzenia informacji przychodzących, Asseco CB będzie informowało PH o przyczynie braku możliwości realizacji\. Obsługa zwrotów do niezrealizowanych płatności będzie przebiegała po stronie PH\.

W instalacjach korzystających obecnie z PH z komunikacją REST API z Asseco CB zmieniona zostanie informacja biznesowa, która obecnie oparta jest o numerację komunikatów KIR zgodną z numeracją komunikatów w plikach płaskich, w omawianym rozwiązaniu numeracja KIR zostanie zastąpiona informacją biznesową określającą rodzaj przekazywanej informacji\.

- **Dane ustrukturyzowane**
Dla danych biznesowych inicjowanych w Asseco CB zakłada się wprowadzenie wymagalności używania postaci ustrukturyzowanej\. Jednocześnie mając na uwadze uwarunkowania systemów zewnętrznych, dopuszcza się przyjmowanie danych do rejestracji dokumentów w postaci dotychczasowej, w szczególności dla danych pochodzących z interfejsów plikowych\.

- **Monitorowanie procesów w Asseco CB**
Zakłada się, że aktywne funkcjonalności w opcjach Rozliczenia oparte o obsługę komunikatów nie będą dostępne dla przelewów utworzonych po wdrożeniu ELIXIR XML\.

Wymiana danych z PH będzie realizowana procesami automatycznymi działającymi w tle\. Na potrzeby obserwacji przebiegu procesów wymiany danych pomiędzy Asseco CB i PH udostępnione będą widoki monitorujące przebieg przetwarzania\.

- **Wysyłka priorytetowa**
Ze względu na brak generacji plików Elixir przez Asseco CB w planowanym rozwiązaniu, wysyłka priorytetowa zostanie zmodyfikowana\. W Asseco CB pozostanie rejestracja Grup klientów i klientów w grupach objętych wysyłką priorytetową, natomiast zarządzanie generacją komunikatów dla grup klientów priorytetowych zostanie przeniesione do PH\. Bank, który korzysta z rozwiązania z wysyłką priorytetową wykorzystuje COT\_MODE=2 lub inne ustawienia COT\_MODE w połączeniu z wydłużoną godziną odcięcia, umożliwiającą przekazywanie rozliczeń poza główną sesją\.

- **COT**
Asseco CB podtrzyma istniejącą obecnie obsługę godziny odcięcia przyjmowania przelewów wychodzących Elixir w oparciu o Macierz COT oraz parametr systemowy **COT\_MODE**, który określa sposób reakcji systemu na przelewy Elixir zgłaszane po COT\.

- **NOSTRO**
Zmiana modelu księgowań na NOSTRO PLN\. Zakłada się, że w architekturze, w której kontem NOSTRO zlokalizowanym w Asseco GL zarządza system Asseco TR, nastąpi zmiana w zakresie dostarczania informacji o podsumowaniach sesji rozliczeniowych Elixir\. Zakłada się, że informację o podsumowaniach sesji Elixir dla Asseco TR będzie dostarczał Payment Hub, wyłączone zostanie wystawianie przez Asseco CB podsumowań sesji Elixir\.

- **Interfejsy API**
Interfejsy API służące do wprowadzania danych będących źródłem dokumentów przelewów Elixir będą dostosowane do przekazywania danych Nadawcy/Odbiorcy w postaci zawierającej adres ustrukturyzowany\. Zmiana obejmie REST API do wprowadzania dokumentów zewnętrznych, poleceń zapłaty, zleceń stałych, dyspozycji dla odsetek i wypłaty środków do umów\. Zmiana będzie wprowadzona również w funkcji WS API inserttransferdoc\.

Jednocześnie w funkcjach API dopuszcza się przekazywanie danych do rejestracji dokumentów Elixir w postaci dotychczasowej nieustrukturyzowanej\.

- **Interfejsy plikowe**
Interfejsy plikowe pozwalające na wprowadzanie przelewów do systemu Asseco CB stosują pliki przecinkowe o formacie zbliżonym do formatu Elixir\. W okresie pierwszego Release Elixir XML na podstawie danych z takich interfejsów plikowych, system Asseco CB będzie przyjmował do realizacji przelewy Elixir, używając dla danych Nadawcy i Odbiorcy pól Nazwa bez ustrukturyzowanego adresu\. Ten typ obsługi będzie dostępny do czasu Release, który wprowadzi wymagalność ustrukturyzowanego adresu\.

- **Konwersja Elixir na Sorbnet**
Dla przelewów wychodzących uznaniowych Elixir, które będą posiadały dane w postaci wymaganej dla płatności Sorbnet \(tzn\. dane Nadawcy/Obiorcy w postaci z ustrukturyzowanym adresem\) możliwe będzie przywrócenie funkcjonalności automatycznej konwersji na Sorbnet\. Automatyczna konwersja nie będzie dostępna w obsłudze automatycznej dla przelewów mających dane tylko w dotychczasowym formacie bez ustrukturyzowanego adresu\.

- **Komunikaty 71n, 73n i 74n**
Wyłączenie funkcjonalności\.

### Zmiana danych Nadawcy/Odbiorcy w komunikatach Elixir

Dotychczas w do przekazywania Danych Nadawcy/Odbiorcy w komunikatach Elixir używane były pola o formacie 4\*35, służące do przekazywania zbiorczej informacji o Nazwie i adresie Nadawcy/Odbiorcy\.

W Elixir XML dane Nadawcy/Odbiorcy są podzielone na Nazwę i sekcję Adresu w postaci ustrukturyzowanej, adres jest opcjonalny\.

Zestawienie danych Nadawcy/Odbiorcy, które będą obsługiwane przez system Asseco CB dla zgłoszeń Elixir otrzymywanych z PH i wysyłanych do PH\.

| **Dane zleceniodawcy/ beneficjenta** **\(senderData/ beneficiaryData\)** | **Odpowiednik XML** | **Krotność** | **Typ** | **Wymagalne** | **Opis pola wg KIR** |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nm | </Nm\> | \[1\] | text\{1,140\} | Tak | Nazwa \(zleceniodawcy/ beneficjenta\) |  |
| PstlAdr | </PstlAdr\> | \[0\.\.1\] |  |  | Adres \(forma ustrukturyzowana\) |  |
| Dept | </PstlAdr/Dept\> | \[0\.\.1\] | text\{1,70\} |  | Identyfikacja Działu dla organizacji lub jednostki organizacyjnej |  |
| SubDept | </PstlAdr/SubDept\> | \[0\.\.1\] | text\{1,70\} |  | Identyfikacja Poddziału |  |
| StrtNm | </PstlAdr/StrtNm\> | \[0\.\.1\] | text\{1,70\} |  | Ulica |  |
| BldgNb | </PstlAdr/BldgNb\> | \[0\.\.1\] | text\{1,16\} |  | Numer budynku |  |
| BldgNm | </PstlAdr/BldgNm\> | \[0\.\.1\] | text\{1,35\} |  | Nazwa budynku |  |
| Flr | </PstlAdr/Flr\> | \[0\.\.1\] | text\{1,70\} |  | Piętro |  |
| PstBx | </PstlAdr/PstBx\> | \[0\.\.1\] | text\{1,16\} |  | Skrytka pocztowa |  |
| Room | </PstlAdr/Room\> | \[0\.\.1\] | text\{1,70\} |  | Numer lokalu |  |
| PstCd | </PstlAdr/PstCd\> | \[0\.\.1\] | text\{1,16\} |  | Kod pocztowy |  |
| TwnNm | </PstlAdr/TwnNm\> | \[0\.\.1\] | text\{1,35\} |  | Miasto |  |
| TwnLctnNm | </PstlAdr/TwnLctnNm\> | \[0\.\.1\] | text\{1,35\} |  | Dzielnica \(dodatkowa lokalizacja w mieście\) |  |
| DstrctNm | </PstlAdr/DstrctNm\> | \[0\.\.1\] | text\{1,35\} |  | Powiat |  |
| CtrySubDvsn | </PstlAdr/CtrySubDvsn\> | \[0\.\.1\] | text\{1,35\} |  | Województwo/Region \(dodatkowa lokalizacja w kraju\) |  |
| Ctry | </PstlAdr/Ctry\> | \[0\.\.1\] | text \[A\-Z\]\{2,2\} |  | Kod kraju |  |

Na podstawie pól Nm i ustrukturyzowanego adresu, system Asseco CB będzie wypełniał na dokumencie Elixir wychodzącym i przychodzącym dotychczasowe pola Nazwy Nadawcy/Odbiorcy w formacie 4\*35 znaków zgodnie z funkcjonalnością dostępną w Asseco CB dla innych typów płatności w formacie ISO20022\.

Zasady łączenia linii 4\*35 w pole 140 znaków

W przypadku, gdy dane Nadawcy/Odbiorcy zostaną przekazane w dotychczasowym formacie 4\*35, system uzna te dane za Nazwę i dokona złączenia czterech linii o długości 35 znaków w jeden ciąg o długości 140 znaków, stosując poniższe zasady wprowadzania separującej spacji pomiędzy liniami po 35 znaków:

- jeżeli suma znaków w czterech liniach będzie równa 140, wówczas nie będą dodawane separatory;
- jeśli linia 1 lub 2 lub 3 będzie miała mniej niż 35 znaków, to pomiędzy tą linią a następną dodana zostanie spacja;
- jeśli linia 1 lub 2 lub 3 będzie miała 35 znaków, to ta linia zostanie połączona z następną linią bez separatora\.
Analogiczna zasada łączenia 4 linii po 35 znaków w jedną linię o długości 140 znaków zostanie zastosowana dla pola Tytułem\.

### Komunikacja Asseco CB – Payment Hub

Opis ogólny

Poniższy diagram przedstawia planowany model usług Asseco CB i Payment Hub do komunikacji w ramach obsługi płatności ELIXIR XML\.

**Uznania****,**** obciążenia****, zwroty uznań, PZ, przychodzące zwroty PZ, ****przychodzące**** zapytania o zgodę na obciążenie \(z kwotą 0\)**** **będą przyjmowane przez Asseco CB w postaci porcji danych połączonych w paczki\. PH decyduje o zawartości paczki, paczki mogą zawierać jednolite typy zgłoszeń lub mieszane\. Asseco CB przystąpi do przetwarzania paczki danych po odebraniu kompletu zadeklarowanych porcji\. W wyniku przetwarzania zgłoszeń wykonywane będą księgowania na rachunkach/kontach własnych odbiorców płatności w korespondencji z kontami drogi wynikającymi z typu płatności\. Jeżeli w trakcie przetwarzania danych wystąpi konieczność zgłoszenia **zwrotu**, wówczas Asseco CB wykona obsługę zależną od parametryzacji systemu \(zależne od parametryzacji księgowanie zwrotu\) i na bieżąco wyśle informację o zwrocie/odmowie do PH\. Bieżący status paczki będzie dostępny do pobrania za pomocą usługi wystawionej przez Asseco CB\. Po zakończeniu przetwarzania wszystkich zgłoszeń z paczki, Asseco CB poinformuje PH o **zakończeniu obsługi** paczki\.

**Uznania i obciążenia wychodzące** dla dokumentów wystawionych w Asseco CB będą przekazywane do Payment Hub w postaci porcji danych w trybie nadążnym do usługi wystawionej przez PH\. Przyjmowanie 	płatności w Asseco CB podlega parametryzacji i może być uzależnione od godziny odcięcia \(COT\), w takim przypadku dla płatności zatrzymanych do realizacji w kolejnym dniu rozliczeniowym w dniu przyjęcia płatności nie są wystawiane dokumenty, dokumenty będą wystawione po otwarciu kolejnego dnia rozliczeniowego zgodnie z kalendarzem płatności Elixir i wówczas będą przekazywane do Payment Hub\.

**Wychodzące PZ, zapytania o zgodę na obciążenie** będą wysyłane przez Asseco CB do PH porcjami po generacji PZ oraz w trakcie dnia dla nowych dyspozycji zgłoszonych przez klientów\.

W przypadku konieczności **anulowania** dokumentu przelewu wychodzącego, możliwa konfiguracja systemu będzie następująca:

- anulowanie dostępne tylko dla dokumentów, które nie zostały przekazane do PH;
- anulowanie poprzedzone zapytaniem do PH\.
W przypadku opcji pierwszej system nie pozwoli na anulowanie dokumentów przekazanych do PH\. W przypadku opcji drugiej, anulowanie będzie poprzedzone weryfikacją wysłania zgłoszenia Elixir do PH a w przypadku dokumentu z wygenerowanym zgłoszeniem Elixir, wykonana będzie weryfikacja dopuszczalności anulowania w PH\.

W systemie Asseco CB możliwe jest oznaczenie klientów \(połączonych w grupy\), dla których dokumenty wychodzące Elixir miały dostępną opcję generacji komunikatów w ramach tzw\. **wysyłki priorytetowej**\. Ze względu na zmianę modelu generacji komunikatów dla ELIXIR XML, generacja komunikatów w ramach tzw\. **wysyłki priorytetowej** zostanie przeniesiona do Payment Hub\. System Asseco CB przekaże do PH informację o tym, że zgłoszenie dotyczy klienta objętego grupą wysyłki priorytetowej, na podstawie tej informacji w PH będą podejmowane dalsze działania związane z generacją komunikatów w ramach dedykowanych godzin generacji komunikatów po głównej sesji rozliczeniowej\.

Asseco CB udostępnia bez zmian usługi do wykonywania **księgowań** na rachunkach klientów, rachunkach LORO, kontach własnych banku, które będą wykorzystywane przez Payment Hub do wykonywania pozostałych operacji biznesowych, które nie są ujęte w powyżej wskazanych metodach wymiany danych\.

Typy zgłoszeń Elixir w komunikacji Asseco CB – Payment Hub

Propozycja typów zgłoszeń, które będą występowały w komunikacji Asseco CB – Payment Hub\.

| Typ zgłoszenia Elixir | Rodzaj komunikatu Elixir | Kierunek komunikacji |
| --- | --- | --- |
| Wychodzące uznanie | Uznaniowe | Wychodzący |
| Wychodzące polecenie zapłaty | Obciążeniowe | Wychodzący |
| Wychodzące zapytanie o zgodę na obciążenie \(z kwotą 0\) | Obciążeniowe | Wychodzący |
| Wychodzący zwrot PZ | Obciążeniowe | Wychodzący |
| Wychodzące obciążenia bezpośrednie | Obciążeniowe | Wychodzący |
| Przychodzące uznanie | Uznaniowe | Przychodzący |
| Przychodzący zwrot uznania | Uznaniowe | Przychodzący |
| Przychodzące polecenie zapłaty | Obciążeniowe | Przychodzący |
| Przychodzące zapytanie o zgodę na obciążenie \(z kwotą 0\) | Obciążeniowe | Przychodzący |
| Przychodzący zwrot PZ | Obciążeniowe | Przychodzący |
| Przychodzące potwierdzenie PZ | Obciążeniowe | Przychodzący |
| Przychodząca odmowa PZ | Obciążeniowe | Przychodzący |
| Przychodzące obciążenia bezpośrednie | Obciążeniowe | Przychodzący |
| Przychodzący zwrot obciążenia bezpośredniego | Obciążeniowe | Przychodzący |

Typy informacji w komunikacji Asseco CB – Payment Hub

Propozycja typów informacji – sygnałów przekazywanych do PH, wynikających z obsługi zgłoszeń Elixir w systemie Asseco CB\.

| Typ zgłoszenia Elixir | Rodzaj komunikatu Elixir | Kierunek komunikacji |
| --- | --- | --- |
| Zwrot uznania przychodzącego | Uznaniowe | Wychodzący |
| Odmowa realizacji PZ | Obciążeniowe | Wychodzący |
| Odmowa do zapytania o zgodę na obciążenie \(z kwotą 0\) | Obciążeniowe | Wychodzący |
| Zwrot obciążenia bezpośredniego przychodzącego | Obciążeniowe | Wychodzący |

Usługi Asseco CB

Asseco CB wystawi usługi:

- Przyjmowania porcji zgłoszeń w ramach paczki
- Księgowania na rachunkach i kontach własnych\.
Usługi PH

Oczekiwane obowiązkowe usługi Payment Hub:

- Rejestracja zgłoszeń z systemu transakcyjnego
- Przyjmowania informacji o zwrotach i odmowach
- Przyjmowanie Informacji o zakończeniu obsługi paczki\.
Opcjonalne usługi Payment Hub:

- Obsługa anulowania zgłoszenia wychodzącego\.
Dane funkcji wysyłania zgłoszeń do PH

Biznesowy zakres danych występujący w komunikacji Asseco CB – Payment HUB dla paczki zgłoszeń wychodzących Elixir:

- identyfikator paczki płatności w Payment Hub \- packReferenceNo
- grupa zgłoszeń: Międzybankowe, Wewnątrzgrupowe, Międzybankowe PZ, Wewnątrzgrupowe PZ \- paymentType
- liczba porcji, które zostaną wysłane w ramach paczki \- totalPartNo\.
- nr kolejny porcji w ramach paczki \(wykorzystywany do przesyłania paczki porcjami limitowanymi wielkością pojedynczej wysyłki\) – packPartNo
- KNR banku wywołującego usługę – bankKnr – wypełniany na podstawie parametru systemowego **PH\_SETTL\_UNIT\_NO**\.
Atrybuty zgłoszeń:

- numer zgłoszenia w paczce – positionNo – nie będzie ustawiane przez Asseco CB
- identyfikator płatności w Asseco CB \- cbOriginalRefNo
- referencja na identyfikator w Asseco CB – cbPaymentReferenceNo
- data waluty \- valueDate
- numer rachunku Nadawcy \- senderAccountNumber
- kwota transakcji – amount/amount
- waluta transakcji \(tylko PLN\) – amount/currency
- numer rachunku Odbiorcy \- receiverAccountNumber
- czy płatność podzielona \(MPP\) \- isSplitPayment
- kwota Vat \(MPP\) – splitPayment/vatAmount/amount
- waluta kwoty Vat \(MPP\) \(PLN\) – splitPayment/vatAmount/currency
- identyfikator podatkowy \(MPP\) – splitPayment/taxRef
- nr faktury \(MPP\) – splitPayment/invoiceNo
- opis płatności podzielonej \(MPP\) – splitPayment/description
- opis płatności – Tytułem/tekst wolny \- description
- informacje międzybankowe \- interbankInformation
- PZ – IDP – directDebit/idp
- PZ – NIP/NIW – directDebit/taxTef
- PZ \- TYT – szczegóły płatności – directDebit/description
- Identyfikator zwracanej płatności PZ – cbReturnedRefNo
- Czy jest to zwrot PZ nieautoryzowanego \- isDirectDebitReturnNotAuthorized
- numer czeku \- chequeNo
- data nadania przelewu Elixir – postingDate
- szczegóły reklamacji \- reclamationDetails
- UIK \(dla zgłoszeń wynikających z komunikatów utworzonych przed Elixir XML\) \- originalUik
- pierwotna, oryginalna kwota zlecenia \- currencyOrder/amount
- pierwotna, oryginalna waluta zlecenia \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/currency
- pierwotny, oryginalny numer konta Nadawcy \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/senderAccountNo
- pierwotna, oryginalna nazwa Nadawcy \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/senderName
- kod kraju rzeczywistego nadawcy przelewu \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/senderCountry,
- kod dokumentu źródłowego – zgodnie ze słownikiem kodów dokumentów źródłowych \- kirDocumentCode
- kod błędu, przyczyna odmowy, powód zwrotu – wartości ze słownika kodów *External Code Sets*
- Identyfikator zwracanej płatności PZ \- phReturnedRefNo
- Data złożenia zlecenia – submissionDate
- Dane dotyczące płatności podatkowej Tytułem \- TaxSettlement/description
- Dane dotyczące płatności podatkowej Symbol formularza \- TaxSettlement/formSymbol
- Dane dotyczące płatności podatkowej Typ identyfikacji zobowiązania \- TaxSettlement/identifierType
- Dane dotyczące płatności podatkowej Numer identyfikacji zobowiązania \- TaxSettlement/identifierTypeValue
- Dane dotyczące płatności podatkowej Okres \- numer \-TaxSettlement/periodNumber
- Dane dotyczące płatności podatkowej Okres \- typ \- TaxSettlement/periodType
- Dane dotyczące płatności podatkowej a \- aa
- Tekst dowolny \- unlimitedText
- typ zgłoszenia Elixir \(określa kierunek komunikacji – przychodzący/wychodzący oraz rodzaj komunikatu – uznaniowy/obciążeniowy\)
- dane Nadawcy \(szczegóły w dalszej części dokumentu\)
- dane Odbiorcy \(szczegóły w dalszej części dokumentu\)
- BIC banku uczestnika nadawcy
- BIC banku uczestnika odbiorcy
- Symbole grup klientów związane z wysyłką priorytetową\.
Dane, które nie będą wypełniane dla zgłoszeń Elixir:

- Typ płatności KIR \- kirPaymentTypeWithThirdDigit
- dane Odbiorcy \- receiverName
- dane Nadawcy – senderName
- UIK \(oryginalny identyfikator płatności\) \- originalUik
- Numer operacji w paczce \- positionNo
Dane funkcji przyjmowania zgłoszeń z PH

Biznesowy zakres danych występujący w komunikacji Payment HUB – Asseco CB dla paczki zgłoszeń przychodzących Elixir:

- identyfikator paczki płatności w Payment Hub \- packReferenceNo
- grupa zgłoszeń: Międzybankowe, Wewnątrzgrupowe, Międzybankowe PZ, Wewnątrzgrupowe PZ \- paymentType
- liczba porcji, które zostaną wysłane w ramach paczki \- totalPartNo\.
- nr kolejny porcji w ramach paczki \(wykorzystywany do przesyłania paczki porcjami limitowanymi wielkością pojedynczej wysyłki\) \- packPartNo
Atrybuty zgłoszeń:

- numer zgłoszenia w paczce \- positionNo
- referencja na identyfikator w Asseco CB \- cbOriginalRefNo
- referencja na identyfikator w Payment Hub – paymentReferenceNo
- data waluty \- valueDate
- numer rachunku Nadawcy \- senderAccountNumber
- kwota transakcji – amount/amountaamount/currency
- numer rachunku Odbiorcy \- receiverAccountNumber
- kwota Vat \(MPP\) – splitPayment/vatAmount/amount
- waluta kwoty Vat \(MPP\) \(PLN\) – splitPayment/vatAmount/currency
- identyfikator podatkowy \(MPP\) – splitPayment/taxRef
- nr faktury \(MPP\) – splitPayment/invoiceNo
- opis płatności podzielonej \(MPP\) – splitPayment/description
- opis płatności – Tytułem/tekst wolny \- description
- informacje międzybankowe \- interbankInformation
- PZ – IDP – directDebit/idp
- PZ – NIP/NIW – directDebit/taxTef
- PZ \- TYT – szczegóły płatności – directDebit/description
- PZ – odsetki kwota – directDebitDebtorAnswer/interestAmount/amount
- PZ – odsetki waluta – directDebitDebtorAnswer/interestAmount/currency
- PZ – kod odmowy – directDebitDebtorAnswer/directDebitReturnCode
- PZ \- nieautotyzowany– directDebitDebtorAnswer/isUnauthorized
- numer czeku \- chequeNoaapostingDate
- szczegóły reklamacji \- reclamationDetailsaoriginalUik
- pierwotna, oryginalna kwota zlecenia – currencyOrder/amount
- pierwotna, oryginalna waluta zlecenia \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/currencyacurrencyOrder/senderAccountNo
- pierwotna, oryginalna nazwa Nadawcy \(dotyczy przychodzących zleceń walutowych skonwertowanych na Elixir – dawne pole 16\) – currencyOrder/senderNameacurrencyOrder/senderCountry,
- kod dokumentu źródłowego – zgodnie ze słownikiem kodów dokumentów źródłowych \- kirDocumentCode
- Identyfikator weryfikacji płatności w AML  \- amlVerificationIda
- Data złożenia zlecenia – submissionDate
- Tekst dowolny \- unlimitedText
- typ zgłoszenia Elixir \(określa kierunek komunikacji – przychodzący/wychodzący oraz rodzaj komunikatu – uznaniowy/obciążeniowy\)
- dane Nadawcy \(szczegóły w dalszej części dokumentu\)
- dane Odbiorcy \(szczegóły w dalszej części dokumentu\)
- BIC banku uczestnika nadawcy
- BIC banku uczestnika odbiorcy
- kod błędu, przyczyna odmowy, powód zwrotu – wartości ze słownika kodów *External Code Sets*\.
Dane, które nie będą interpretowane dla zgłoszeń Elixir:

- Typ płatności KIR \- kirPaymentTypeWithThirdDigit
- dane Odbiorcy \- receiverName
- dane Nadawcy \- senderName
- Numer operacji w paczce \- positionNo
Dane informacji zwrotnej o zgłoszeniu Elixir

Informacja o zwrotach i odmowach do zgłoszeń Elixir przekazywane z Asseco CB do Payment HUB zawierają dane identyfikujące zgłoszenie oraz informacje dodatkowe uzależnione od typu zgłoszenia:

- Identyfikator paczki w systemie zewnętrznym \- extPackReferenceNo
- Identyfikator operacji w systemie zewnętrznym – extPaymentReferenceNo
- Identyfikator paczki w systemie Payment Hub \- packReferenceNo
- Identyfikator operacji w systemie Payment Hub \- paymentReferenceNo
- Szczegóły reklamacji \- reclamationDetails
- Kod odrzucenia – rejectCode
- Kod odrzucenia ISO \(wartość ze Słownika External Code Sets\)
Dane Nadawcy/Odbiorcy

Zestawienie danych Nadawcy/Odbiorcy, które będą obsługiwane w zgłoszeniach Elixir\.

| **beneficiaryData** **s****enderData** | **Odpowiednik XML** | **Krotność** | **Typ** | **Wymagalne**** ** | **Opis pola wg KIR** |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nm | </Nm\> | \[1\] | text\{1,140\} | Tak | Nazwa \(zleceniodawcy/ beneficjenta\) |  |
| PstlAdr | </PstlAdr\> | \[0\.\.1\] |  |  | Adres \(forma ustrukturyzowana\) |  |
| Dept | </PstlAdr/Dept\> | \[0\.\.1\] | text\{1,70\} |  | Identyfikacja Działu dla organizacji lub jednostki organizacyjnej |  |
| SubDept | </PstlAdr/SubDept\> | \[0\.\.1\] | text\{1,70\} |  | Identyfikacja Poddziału |  |
| StrtNm | </PstlAdr/StrtNm\> | \[0\.\.1\] | text\{1,70\} |  | Ulica |  |
| BldgNb | </PstlAdr/BldgNb\> | \[0\.\.1\] | text\{1,16\} |  | Numer budynku |  |
| BldgNm | </PstlAdr/BldgNm\> | \[0\.\.1\] | text\{1,35\} |  | Nazwa budynku |  |
| Flr | </PstlAdr/Flr\> | \[0\.\.1\] | text\{1,70\} |  | Piętro |  |
| PstBx | </PstlAdr/PstBx\> | \[0\.\.1\] | text\{1,16\} |  | Skrytka pocztowa |  |
| Room | </PstlAdr/Room\> | \[0\.\.1\] | text\{1,70\} |  | Numer lokalu |  |
| PstCd | </PstlAdr/PstCd\> | \[0\.\.1\] | text\{1,16\} |  | Kod pocztowy |  |
| TwnNm | </PstlAdr/TwnNm\> | \[0\.\.1\] | text\{1,35\} |  | Miasto |  |
| TwnLctnNm | </PstlAdr/TwnLctnNm\> | \[0\.\.1\] | text\{1,35\} |  | Dzielnica \(dodatkowa lokalizacja w mieście\) |  |
| DstrctNm | </PstlAdr/DstrctNm\> | \[0\.\.1\] | text\{1,35\} |  | Powiat |  |
| CtrySubDvsn | </PstlAdr/CtrySubDvsn\> | \[0\.\.1\] | text\{1,35\} |  | Województwo/Region \(dodatkowa lokalizacja w kraju\) |  |
| Ctry | </PstlAdr/Ctry\> | \[0\.\.1\] | text \[A\-Z\]\{2,2\} |  | Kod kraju |  |

Słownik kodów dokumentów źródłowych

Słownik KIR \- wartości kodów dokumentów źródłowych

| **Lp** | **Kod** | **Nazwa** | **Uwagi** |
| --- | --- | --- | --- |
| 1 | 01 | Polecenia zapłaty | Obciążenie z możliwością odrzucenia |
| 2 | 51 | Polecenie Przelewu | Uznanie |
| 3 | 53 | Polecenie Przelewu; Polecenie zapłaty \- płatność podzielona \(MPP\) | Uznanie; Obciążenie z możliwością odrzucenia |
| 4 | 54 | Bankowy Dowód Wpłaty/ Wpłata gotówkowa | Uznanie |
| 5 | 55 | Bankowa Nota Memoriałowa | Uznanie |
| 6 | 56 | Polecenie Przelewu–odpowiada komunikatowi MX pacs\.008 | Uznanie |
| 7 | 71 | Polecenie Przelewu \- do urzędu obsługującego organ podatkowy | Uznanie |
| 8 | 74 | Wpłata Gotówkowa do urzędu obsługującego organ podatkowy | Uznaniowe |

Uwaga

Do obsługi obciążeń bezpośrednich, występujących dla rozliczeń wewnątrzgrupowych, stosowany będzie \(tak jak obecnie\) kod dokumentu **05**, który nie występuje w specyfikacji KIR dla Elixir XML\.

Słownik kodów *External Code Sets*

Słownik *External Code Sets*

| **Kod** | **Nazwa** | **Opis** |
| --- | --- | --- |
| AC01 | IncorrectAccountNumber | Nieprawidłowy numer rachunku lub rachunek nie istnieje |
| AC04 | ClosedAccountNumber | Rachunek jest zamknięty przez bank |
| AC06 | BlockedAccount | Zablokowany rachunek |
| AG01 | TransactionForbidden | Nieobsługiwany typ Transakcji na rachunku |
| AG02 | InvalidBankOperationCode | Nieprawidłowy kod operacji bankowej |
| AM01 | ZeroAmount | Zerowa kwota Transakcji |
| AM02 | NotAllowedAmount | Kwota Transakcji powyżej górnego limitu |
| AM03 | NotAllowedCurrency | Nieobsługiwana waluta Transakcji |
| AM04 | InsufficientFunds | Brak wystarczających środków do realizacji Transakcji |
| AM05 | Duplication | Duplikat Transakcji |
| AM06 | TooLowAmount | Kwota Transakcji poniżej dolnego limitu |
| AM07 | BlockedAmount | Dostępna kwota jest niewystarczająca do realizacji Transakcji |
| AM09 | WrongAmount | Błędna kwota Transakcji |
| AM10 | InvalidControlSum | Błąd sumy kontrolnej |
| BE01 | InconsistenWithEndCustomer | Dane klienta niezgodne z numerem rachunku |
| BE04 | MissingCreditorAddress | Brak wymaganego adresu beneficjenta |
| BE05 | UnrecognisedInitiatingParty | Nierozpoznana strona inicjująca Transakcję |
| BE06 | UnknownEndCustomer | Klient jest nieznany lub nieobsługiwany przez Bank |
| BE07 | MissingDebtorAddress | Brak wymaganego adresu płatnika |
| CURR | IncorrectCurrency | Nieprawidłowa waluta Transakcji |
| CUST | RequestedByCustomer | Żądanie anulowania Transakcji przez płatnika |
| DT01 | InvalidDate | Błędna data |
| ED01 | CorrespondentBankNotPossible | Bank korespondent nie jest możliwy |
| ED03 | BalanceInfoRequest | Zażądano uzupełniających danych |
| ED05 | SettlementFailed | Nieudane rozliczenie Transakcji |
| FOCR | FollowingCancellationRequest | Zwrot po żądaniu anulowania |
| MD01 | NoMandate | Brak upoważnienia |
| MD02 | MissingMandatoryInformationIn Mandate | Brak wymaganych powiązanych danych |
| MD06 | RefundRequestByEndCustomer | Zwrot środków wnioskowany przez klienta końcowego |
| MD07 | EndCustomerDeceased | Klient końcowy nie żyje |
| MS02 | NotSpecifiedReasonCustomer Generated | Przyczyna nie została podana przez klienta |
| MS03 | NotSpecifiedReasonAgent Generated | Powód nie został podany przez Jednostkę Uczestnika |
| NARR | Narrative | Powód jest podany w formie opisowej – kod używany, gdy wystąpiła sytuacja nie opisana innymi kodami\. |
| RC01 | BankIdentifierIncorrect | Nieprawidłowy identyfikator banku |
| RF01 | NotUniqueTransactionReference | Referencja do Transakcji nie jest unikalna w Komunikacie |
| RR01 | Missing Debtor Account or Identification | Brak rachunku płatnika lub jego identyfikacji |
| RR02 | Missing Debtor Name or Address | Brak nazwy płatnika lub jego adresu |
| RR03 | Missing Creditor Name or Address | Brak nazwy beneficjenta lub jego adresu |
| RR04 | Regulatory Reason | Powód zgodny z regulacją |
| SL01 | Specific Service offered by Debtor Agent | Z powodu specyfiki usługi agenta płatnika |
| SL02 | Specific Service offered by Creditor Agent | Z powodu specyfiki usługi agenta beneficjenta |
| TM01 | CutOffTime | Odebrano Komunikat po oczekiwanym czasie |

### Obsługa płatności i poleceń zapłaty Elixir w Asseco CB

Płatności i Polecenia zapłaty Elixir z formatek

Formatki Asseco CB są źródłem płatności wychodzących Elixir\.

Płatności wychodzące system będzie tworzył na podstawie dokumentów rejestrowanych w opcjach systemu i z poziomu umów klientów:

- Przelew wychodzący zewnętrzny
- Przelew na rachunek US
- Polecenie zapłaty zewnętrzne
- Zwrot dla polecenia zapłaty
- Obciążenie bezpośrednie wychodzące
- Przelew zewnętrzny z konta własnego
- Obciążenie bezpośrednie wychodzące \(na konto własne\)
- Przelew na rachunek US z konta własnego
- Wpłata na rachunek zewnętrzny \(również żetonowa\)
- Wpłata na rachunek US \(również żetonowa\)
- GL Nota dwustronna z księgowaniem w CB \-\> Przelew na rachunek zewnętrzny
- Przelew wychodzący zewnętrzny transzy kredytu
- Przelew wychodzący z rejestru nadpłat
Obecnie dla przelewów Elixir formatki obsługują dane Nadawcy/Odbiorcy w polu Nazwa o formacie 4\*35\. Formatki zostaną zmodyfikowane, po włączeniu formatu Elixir XML, dla przelewów Elixir wymagane będzie wprowadzanie danych Nadawcy/Odbiorcy w postaci z wydzielonym polem Nazwa i ustrukturyzowanymi danymi adresowymi\. Szczegóły dotyczące danych Nadawcy/Odbiorcy w Elixir XML podane są w rozdziale 2\.3\.2 Zmiana danych Nadawcy/Odbiorcy w komunikatach Elixir\.

Na formatkach Asseco CB dla przelewów Elixir system wypełni automatycznie dane Nadawcy w nowym formacie na podstawie danych z kartoteki klienta\. Dane Odbiorcy na formatkach będą wymagane w formacie ustrukturyzowanym, przy czym dane adresowe będą opcjonalne \(dotyczy parametryzacji Elixir XML\)\.

Powyższe formatki wystawiają w systemie dokumenty\. Dokumenty uznaniowe i obciążeń bezpośrednich są dekretowane\. Na podstawie dokumentów system Asseco CB wykona generację zgłoszeń Elixir\. Zgłoszenia będą przekazywane porcjami do PH zgodnie z parametryzacją systemu Asseco CB\.

Na podstawie powyższych dokumentów system Asseco CB utworzy i prześle do PH zgłoszenia Elixir o typach wskazanych w poniższym zestawieniu\.

| Dokument zarejestrowany w opcji | Typ zgłoszenia Elixir przekazywany do PH |
| --- | --- |
| Przelew wychodzący zewnętrzny Przelew na rachunek US Przelew zewnętrzny z konta własnego Przelew na rachunek US z konta własnego Wpłata na rachunek zewnętrzny Wpłata na rachunek US GL Nota dwustronna z księgowaniem w CB \-\> Przelew na rachunek zewnętrzny Przelew wychodzący zewnętrzny transzy kredytu Przelew wychodzący z rejestru nadpłat | Wychodzące uznanie |
| Polecenie zapłaty zewnętrzne | Wychodzące polecenie zapłaty |
| Zwrot dla polecenia zapłaty | Wychodzący zwrot PZ |
| Obciążenie bezpośrednie wychodzące Obciążenie bezpośrednie wychodzące \(na konto własne\) | Wychodzące obciążenia bezpośrednie |

Płatności i Polecenia zapłaty Elixir przez API

W funkcjach wskazanych poniżej wprowadzona zostanie możliwość przekazania danych nadawcy/odbiorcy w postaci pól zawierających osobno Nazwę i Adres ustrukturyzowany\. W funkcjach uwzględnione zostaną dane z rozdziału 2\.3\.2 Zmiana danych Nadawcy/Odbiorcy w komunikatach Elixir\.

Dostosowanie funkcji API służących do wystawiania dokumentu przelewu Elixir wychodzącego:

- documents / cash / cash\-domestic\-transfers
- documents / cash / cash\-tax\-transfers
- documents / customer\-domestic\-transfers
- documents / customer\-tax\-transfers
- documents / debit\-transfer\-to\-customer
- documents / debits / debit\-transfer\-to\-own\-accounts
- documents / own\-account\-domestic\-transfers
- documents / own\-account\-tax\-transfer
- WS inserttransferdoc
- WS setTransfer
Dostosowanie funkcji API służących do obsługi poleceń zapłaty\.

- documents / customer\-domestic\-direct\-debit\-reverses
- documents / customer\-domestic\-direct\-debits
- documents / directdebit / incoming / domestic\-incoming\-customer\-direct\-debits
Dostosowanie funkcji API służących do obsługi zlecenia stałego\.

- contracts / standing\-orders
- current\-accounts / standing\-orders
Dostosowanie funkcji API służących do obsługi umowy – rachunek do zwrotu środków/odsetek\.

- current\-accounts
- deposits
- loans
- syndicated\-loans
- guarantees
Ze względu na opcjonalność danych adresowych Nadawcy/Odbiorcy w komunikatach Elixir XML, powyższe funkcje będą dopuszczały przekazywanie danych w obecnie stosowanym formacie, czyli z danymi Nadawcy/Odbiorcy polach z Nazwą 4\*35 znaków\. W takim przypadku, system Asseco CB wystawi dokument z danymi Nadawcy/Odbiorcy w formacie 4\*35 znaków a podczas tworzenia zgłoszenia Elixir dla PH zinterpretuje przekazane dane jako wsad do pól Nm XML \(Nazwa Nadawcy/Odbiorcy\), 4 linie zostaną złączane w jedno pole o długości 140 znaków, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2, dane adresu ustrukturyzowanego nie będą wypełnione\. Jeżeli pole Tytułem będzie przekazane w postaci 4 linii, to 4 linie zostaną złączane w jedno pole o długości 140 znaków z użyciem zasad łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2\.

Płatności i Polecenia zapłaty Elixir z Payment Hub

Zgłoszenia przekazywane przez Payment Hub będą obsługiwane zgodnie z zadeklarowanym typem zgłoszenia Elixir\.

Poniżej przedstawiono zestawienie typów zgłoszeń z PH i obsługę powiązaną z danym typem zgłoszenia w systemie Asseco CB\.

| Typ zgłoszenia Elixir przekazywany przez PH | Typ obsługi w Asseco CB |
| --- | --- |
| Przychodzące uznanie | Wystawienie dokumentu przychodzącego uznania\. |
| Przychodzący zwrot uznania | Wystawienie dokumentu zwrotu środków na rachunek nadawcy pierwotnego uznania\. |
| Przychodzące polecenie zapłaty | Obsługa polecenia zapłaty przychodzącego\. W przypadku zgody wystawienie dokumentu obciążającego dłużnika\. W przypadku odmowy wysłanie do PH informacji typu Odmowa realizacji PZ\. |
| Przychodzące zapytanie o zgodę na obciążenie \(z kwotą 0\) | Obsługa polecenia zapłaty przychodzącego \(z kwotą 0\), w przypadku odmowy wysłanie do PH informacji typu Odmowa do zapytania o zgodę na obciążenie \(z kwotą 0\)\. |
| Przychodzący zwrot PZ | Obsługa przychodzącego zwrotu PZ, wystawienie dokumentu zwrotu PZ z rachunku wierzyciela\. |
| Przychodzące potwierdzenie PZ | Obsługa potwierdzenia PZ, dekretacja środków na rachunku wierzyciela\. |
| Przychodząca odmowa PZ | Obsługa odmowy PZ\. |
| Przychodzące obciążenia bezpośrednie | Wystawienie dokumentu obciążenia bezpośredniego\. |
| Przychodzący zwrot obciążenia bezpośredniego | Wystawienie dokumentu księgowania zwrotu obciążenia bezpośredniego \(zdjęcie środków z rachunku nadawcy pierwotnego obciążenia\) |

Jeżeli zgłoszenie nie będzie mogło być zrealizowane z powodu błędu, to zachowanie systemu Asseco CB będzie, tak jak obecnie, uzależnione od parametryzacji, która określa czy informacja o zwrocie ma być przekazywana do PH automatycznie po stwierdzeniu konieczności wykonania zwrotu do zgłoszenia, czy ma oczekiwać w systemie Asseco CB na ręczną obsługę przez Operatora\.

Dokument płatności podzielonej \(MPP\) wystawiany dla przelewu przychodzącego będzie obsługiwany na podstawie danych z pól:

- kwota Vat \(MPP\) – splitPayment/vatAmount/amount
- waluta kwoty Vat \(MPP\) \(PLN\) – splitPayment/vatAmount/currency
- identyfikator podatkowy \(MPP\) – splitPayment/taxRef
- nr faktury \(MPP\) – splitPayment/invoiceNo
- opis płatności podzielonej \(MPP\) – splitPayment/description
- opis płatności – Tytułem/tekst wolny \- description
Obsługa danych dla przychodzących płatności transgranicznych i płatności w imieniu będzie wykonywana przy włączonej licencji **D3K\.CB\.PROD\.GIIF\_UPD\_2024** oraz parametrze systemowym **GIIF\_53\_SERVICE** = 1 na podstawie zawartości pola z Nazwą nadawcy i pola Tytułem\.

Płatności i Polecenia zapłaty Elixir z interfejsów plikowych

Obecnie system Asseco CB przyjmuje do realizacji płatności przekazywane w plikach tekstowych\. Format danych opisujący Nadawcę/Odbiorcę w plikach jest zgodny z dotychczasowym formatem komunikatów Elixir, czyli 4\*35\.

Pierwsza edycja Elixir XML dopuszcza użycie włącznie nazwy Nadawcy/Odbiorcy bez danych adresu ustrukturyzowanego, pole Nazwa Nadawcy/Odbiorcy ma długość 140 znaków, zatem możliwe jest przekazywanie danych przelewu Elixir XML bazując na danych Nadawcy/Odbiorcy w dotychczasowym formacie\.

Obsługa płatności Elixir XML na podstawie danych z dotychczasowych interfejsów plikowych będzie wspierana przez Asseco CB do najbliższej zmiany formatu Elixir XML, wykluczającej możliwość przekazywania danych bez adresu ustrukturyzowanego a dalsze decyzje w sprawie interfejsów plikowych będą podejmowane po opublikowaniu informacji o zmianie formatu Elixir XML\.

Numery rachunków Nadawcy/Odbiorcy podane w plikach w formie NRB, system Asseco CB uzupełni do postaci IBAN podczas przekazywania płatności do PH\. Dane Nadawcy/Odbiorcy podane w formacie 4\*35, system Asseco CB złączy w jeden ciąg o długości 140 znaków, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2

Funkcjonalności dla Dokumentów

**Dokumenty przygotowane do wysłania i zablokowane za okres \.\.\.**

Dla dokumentu przelewu wychodzącego dostępna będzie funkcjonalność blokowania i zwalniania blokady wysyłania przelewu do systemu rozliczeniowego\.

**Dokumenty niewysłane**

Przegląd Dokumenty niewysłane uwzględni dokumenty wychodzące zewnętrzne, dla których nie ma komunikatu Elixir ani zgłoszenia Elixir\.

**Dokumenty/Przeglądanie**

Podgląd dokumentu przelewu zewnętrznego wychodzącego i przychodzącego będzie umożliwiał podgląd danych zgłoszenia Elixir z informacją o identyfikatorze paczki, w której nastąpiło przekazanie do PH lub z PH\.

### Monitorowanie płatności w Asseco CB

Generacja zgłoszeń Elixir dla PH będzie wykonywana przez procesy automatyczne, działające zgodnie z harmonogramem\.

W Asseco CB dostępny będzie widok, pozwalający na weryfikację działania procesu generacji zgłoszeń Elixir i wysyłania zgłoszeń Elixir do PH\. Z poziomu przeglądu dokumentów dostępna będzie informacja czy zostało utworzone zgłoszenie Elixir i czy zgłoszenie przekazano do PH\.

Do monitorowania wysyłania zgłoszeń będzie utworzona nowa formatka o roboczej nazwie „Wysyłanie zgłoszeń Elixir XML”\. Szczegółowy opis znajduje się w rozdziale PB\.CB\.046 Formatka Wysyłanie zgłoszeń Elixir XML\.

Przyjmowanie zgłoszeń Elixir z PH będzie realizowane za pomocą funkcji API, które będą przyjmowały dane połączone w paczki i podzielone na porcje\. Zgłoszenia przyjęte do systemu Asseco CB przez API będą obsługiwane przez procesy automatyczne, uruchamiane po odbiorze ostatniej porcji danych w paczce zgłoszeń\.

Dla zgłoszeń Elixir przyjmowanych przez API dostępny będzie widok, prezentujący zadeklarowane i odebrane paczki zgłoszeń, odebrane porcje danych\. Dla paczek zgłoszeń ELIXIR dostępny będzie podgląd statusu przetwarzania zgłoszeń\.

Dla dokumentów utworzonych na podstawie zgłoszeń Elixir, dostępna będzie informacja o pochodzeniu danych z PH\.

### Zwroty w okresie przejściowym

Za okres przejściowy dla obsługi zwrotów, uznaje się czas, w którym otrzymuje się komunikaty Elixir XML do komunikatów wysłanych do KIR przed wdrożeniem Elixir XML\.

W okresie przejściowym zakłada się używanie referencji na zgłoszenie pierwotne w postaci jednej z dwóch wartości UIK lub OLD\_REF w zależności od tego, która wartość będzie dostępna\.

W przypadku, gdy zgłoszenie pierwotne było obsługiwane w komunikacji z PH z użyciem referencji własnych Asseco CB i PH sprzed wdrożenia Elixir XML, to do wskazania komunikatu oryginalnego można użyć referencji własnych przekazanych w polu OLD\_REF\. W przypadku braku referencji własnych sprzed wdrożenia Elixir XML, systemy powinny przekazywać wartość UIK\.

System Asseco CB wykonując zwrot do komunikatu sprzed wdrożenia Elixir XML, przekaże referencję na komunikat pierwotny w polu UIK lub OLD\_REF\_PH w zależności od posiadanych danych\. Zakłada się, że system PH wykorzysta przekazaną informację do sporządzenia komunikatu Elixir XML\.

Zakłada się, że system Payment Hub wykonując zwrot do komunikatu sprzed wdrożenia Elixir XML, przekaże referencję na komunikat pierwotny w polu UIK lub OLD\_REF\_CB w zależności od posiadanych danych\. System Asseco CB, na podstawie jednej z przekazanych wartości, obsłuży zwrot w powiązaniu z danymi źródłowymi\.

### NOSTRO

Przeniesienie obsługi sesji Elixir do Payment Hub oznacza wyłączenie alternatywnej ścieżki architektury dla obsługi NOSTRO w zakresie rozliczeń ELIXIR\.

Obecnie system Asseco CB dokonuje podsumowania komunikatów uznaniowych i obciążeniowych w ramach sesji Elixir i wystawia tę informację w perspektywie dla Asseco TR\. Asseco TR posiada funkcjonalność wystawiania not księgowych na koncie NOSTRO w Asseco GL na podstawie podsumowań sesji Elixir z Asseco CB\.

Funkcjonalność wystawiania podsumowań sesji Elixir nie będzie dostępna w Asseco CB dla ELIXIR XML\. W nowym modelu informowanie Asseco TR o podsumowaniu sesji Elixir powinno być realizowane przez Payment Hub\.

### Opcje i funkcjonalności o ograniczonym działaniu po wdrożeniu Elixir XML w Asseco CB

Po wdrożeniu Elixir XML dotychczasowe opcje działające w oparciu o komunikaty Elixir w Asseco CB będą działały z ograniczeniami, tzn\. funkcjonalności oparte na komunikatach Elixir zostaną zablokowane dla bieżących płatności, natomiast dostępne będą w zakresie przeglądania danych historycznych \(bez możliwości aktywnej obsługi\)\. Dostęp do danych sprzed wdrożenia Elixir XML oraz do funkcjonalności, które nie są oparte o komunikaty Elixir pozostanie bez zmian\.

Lista opcji systemu Asseco CB, które po wdrożeniu Elixir XML będą działać z ograniczeniami:

- Rozliczenia \-\> Elixir \-\> Wczytanie,
- Rozliczenia \-\> Elixir \-\> Wczytanie \- komunikaty MB,
- Rozliczenia \-\> Elixir \-\> Wczytanie \- komunikaty MO,
- Rozliczenia \-\> Elixir\-\> Wysłanie,
- Rozliczenia \-\> Elixir\-\> Wysłanie \- komunikaty MB,
- Rozliczenia \-\> Elixir\-\> Wysłanie \- komunikaty MO,
- Rozliczenia \-\> Elixir \-\> Wysłanie \- tylko komunikaty ZUS,
- Rozliczenia \-\> Elixir \-\> Wysłanie \- wszystkie komunikaty bez ZUS,
- Rozliczenia \-\> Elixir \-\> Wysyłka priorytetowa \-\> Wybór dokumentów do generowania komunikatów,
- Komunikaty wychodzące 71n,
- Komunikaty wychodzące 73n,
- Komunikaty wychodzące 74n,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> RAPORT ROZL\. WYCHODZĄCYCH,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 1 ‑\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Wczytane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 1 ‑\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Zaksięgowane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 1 ‑\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Do wysyłki,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 1 ‑\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Wysłane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 2 ‑\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Wczytane,
- Rozliczenia \-\> Elixir \-\>Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 2 ‑\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Zaksięgowane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 2 ‑\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Do wysyłki,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje \- grupowanie 2 ‑\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Wysłane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje pełne \-\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Wczytane,
- Rozliczenia\-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje pełne \-\> Podsumowanie rozliczeń ELIXIR \- Otrzymane, Zaksięgowane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje pełne \-\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Do wysyłki,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Wersje pełne \-\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Wysłane,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Podsumowanie rozliczeń \-\> Komunikaty adresowane do ZUS,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Zwroty \-\> Podsumowanie rozliczeń ELIXIR \- Wysyłane, Wysłane ZWROTY,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Zestawienie komunikatów w podziale na banki nadawcy/odbiorcy,
- Rozliczenia \-\> Elixir \-\> Wydruki \-\> Zestawienie komunikatów\.
- Rozliczenia \-\> Import komunikatów z systemu MultiComp
- Rozliczenia \-\> Eksport komunikatów do systemu MultiComp
- Rozliczenia \-\> Konfiguracja automatycznego przekazywania komunikatów do systemu MultiComp
- Rozliczenia \-\> Payment Hub \-\> Wysyłanie rozliczeń – po włączeniu Elixir XML w Asseco CB, opcja generacji komunikatów nie będzie uruchamiała przetwarzań
- Rozliczenia \-\> Księgowanie \-\> Księgowanie rozliczeń z Payment Hub
- Rozliczenia \-\> Raport rozliczeń – ograniczenie nie dotyczy przelewów Sorbnet
- Dokumenty \-\> Polecenie zapłaty zewnętrzne GOBI\.