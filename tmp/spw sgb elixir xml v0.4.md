| Specyfikacja Wymagań ELIXIR XML Rozwiązanie licencyjne w Asseco CB i dodatkowe funkcjonalności dla Banku SGB |
| --- |
|  |

Spis treści

1\.	Wprowadzenie	4

1\.1\.	Cel biznesowy projektu	4

1\.2\.	Wymagania projektu	4

2\.	Perspektywa biznesowa rozwiązania	4

2\.1\.	Słownik pojęć	4

2\.2\.	Stan obecny	5

2\.3\.	Model rozwiązania \#zakres bazowy	6

2\.4\.	Model rozwiązania \#rozszerzenie 1	22

2\.5\.	Model rozwiązania \#rozszerzenie 2	24

2\.6\.	Model rozwiązania \#rozszerzenie 3 \- opcja	25

3\.	Wymagania szczegółowe	25

3\.1\.	ELIXIR w Asseco CB	25

3\.2\.	Pralnia	37

3\.3\.	Raporty i wydruki	37

3\.4\.	Wyciągi	39

3\.5\.	Inne	40

3\.6\.	Obsługa danych ustrukturyzowanych ELIXIR w bankowości internetowej	42

3\.7\.	\#Rozszerzenie 3 \(Opcja\) \- Narzędzie do konwersji danych adresowych	44

3\.8\.	Zasilanie batch Asseco AML	45

4\.	Wymagane licencje	45

5\.	Obszary pod wpływem	45

5\.1\.	Wpływ na procesy operacyjne/ biznesowe	45

5\.2\.	Wymagania szczególne wynikające z RODO	45

6\.	Uwarunkowania	45

7\.	Dodatki	46

7\.1\.	Analizowane systemy	46

Wprowadzenie

Cel biznesowy projektu

Celem projektu jest dostosowanie systemów Asseco CB i Asseco EBP do zmian wynikających z wprowadzenia przez Krajową Izbę Rozliczeniową nowego formatu wymiany danych w ramach rozliczeń w systemie płatności krajowych w PLN ELIXIR implementującego standard ISO 20022 pod nazwą ELIXIR XML oraz integracja systemu Asseco CB z systemami typu Payment Hub w obszarze płatności ELIXIR XML\.

Wymagania projektu

WK\.01 ELIXIR XML \- Integracja Asseco CB z Payment Hub

Wymaganiem jest integracja systemu Asseco CB z systemem typu Payment Hub w ramach płatności realizowanych jako ELIXIR XML\.

WK\.02 Konwersje Elixir – Express Elixir

Wymaganiem jest wykonywanie przez Asseco CB konwersji przelewów Elixir XML wewnątrzgrupowych na przelewy Express Elixir oraz w przypadku braku możliwości realizacji takiego przelewu, rekonwersja z Express Elixir na Elixir XML w Asseco CL\.

WK\.03 Moduł administracyjny – zbiory bazowe

Wymaganiem jest dystrybucja przez Moduł Administracyjny nowych zbiorów bazowych:

- **OB***rrrrmm\.***0***dd*
- **BC***rrrrmm\.***0***dd*
do baz podrzędnych\.

WK\.04 Konwersja danych adresowych odbiorcy – rozszerzenie \- opcja

Wymaganiem opcjonalnym jest przygotowanie narzędzia, którego zadaniem będzie konwersja danych adresowych \(przekazanych w pliku\) z postaci zagregowanej do ustrukturyzowanej\.

Perspektywa biznesowa rozwiązania

Słownik pojęć

| Pojęcie | Opis |
| --- | --- |
| ELIXIR ISO20022 ELIXIR XML | System rozliczeń sesyjnych w PLN Elixir – nowy standard komunikatów ISO 20022 \(XML\)\. Struktury i zasad tworzenia komunikatów XML wymienianych z Uczestnikami w elektronicznych systemach rozliczeń sesyjnych KIR |
| Płaskie pliki Elixir, pliki Elixir csv, pliki przecinkowe | Pliki tekstowe stosowane w systemie rozliczeń sesyjnych w PLN Elixir |
| Dane ustrukturyzowane | Format danych adresowych w standardzie ISO 20022 |
| Dane zagregowane, dane w postaci zbiorczej | Dane Nadawcy lub Odbiorcy w postaci 4 linii po 35 znaków, w których znajduje się nazwa i adres bez podanego formatu |
| Typ zgłoszenia, Typ zgłoszenia Elixir | Pojęcie używane w ramach niniejszej specyfikacji do opisu typu wiadomości występującej w Elixir XML\. Tabela z wartościami opisującymi Typ zgłoszeń Elixir znajduje się w rozdziale 2\.3\.3**\.** |
| Kod dokumentu KIR | Kod dokumentu wg nomenklatury KIR, wartość ze Słownika kodów dokumentów źródłowych z dokumentacji KIR, tabela z wartościami tego słownika znajduje się w rozdziale 2\.3\.3\. |

Stan obecny

System Asseco CB jest dostosowany do obsługi wychodzących i przychodzących komunikatów Elixir w postaci plików tekstowych przecinkowych a także umożliwia integrację z systemem typu Payment Hub w zakresie wymiany danych biznesowych niosących informację o komunikatach Elixir\. Identyfikacja komunikatów w integracji z systemem Payment Hub realizowana jest w przy użyciu trzycyfrowego symbolu typu komunikatu z plików przecinkowych Elixir\.

System Asseco CB jako system transakcyjny przyjmuje do realizacji płatności w PLN do banków krajowych rozliczane w systemie Elixir\. Obsługa płatności Elixir realizowana jest przez system Asseco CB w trybie sesji Elixir\. Generacja komunikatów wychodzących wykonywana jest w ramach sesji Elixir w postaci plików przecinkowych lub poprzez przekazanie danych biznesowych do systemu Payment Hub za pośrednictwem API\. System Asseco CB przyjmuje dane wejściowe z systemu rozliczeniowego Elixir w postaci plików przecinkowych lub w postaci danych biznesowych przez API dedykowane dla Payment Hub\.

W procesie obsługi płatności Elixir system Asseco CB korzysta z danych dystrybuowanych przy użyciu wybranych zbiorów bazowych KIR\.

### Bankowość internetowa

Obecny zakres obsługi danych adresowych w aktywnych funkcjonalnościach bankowości internetowej przedstawia poniższa tabela\.

| Funkcjonalność | Komentarz |
| --- | --- |
| Przelew zwykły \(ELIXIR\) Przelew odroczony Zlecenie stałe | Pozwala na wprowadzenie danych adresowych w postaci ustrukturyzowanej, które są agregowane do zbiorczego pola danych odbiorcy przy wysyłce przelewu do systemu transakcyjnego\. Dane adresowe są opcjonalne\. Pole nazwy odbiorcy pozwala na wprowadzenie 35 znaków\. |
| Przelew zwykły \(SORBNET\) | Obsługuje dane adresowe \(odbiorcy\) w postaci ustrukturyzowanej\. Pole nazwy odbiorcy pozwala na wprowadzenie 35 znaków\. |
| Przelew zwykły \(Express Elixir\) | Pozwala na wprowadzenie danych adresowych w postaci ustrukturyzowanej, które są agregowane do zbiorczego pola danych odbiorcy przy wysyłce przelewu do systemu transakcyjnego\. |
| Przelew walutowy \(SWIFT/SEPA\) | Obsługuje dane adresowe \(odbiorcy\) w postaci ustrukturyzowanej\. |
| Przelew własny | Nie zawiera pól adresowych do uzupełnienia przez klienta, funkcjonalność zbudowana na bazie usługi do realizacji przelewu zwykłego, gdzie dane nadawcy i odbiorcy uzupełniane są danymi z kartoteki klienta\. |
| Przelew podatkowy | Nie zawiera pól adresowych\. Formatka zawiera pole „Miasto” jednakże służy ono wyłącznie jako filtr\. |
| Przelew PayByNet | Obsługuje dane adresowe \(odbiorcy\) w postaci zagregowanej\. |
| Import przelewu zwykłego \(ELIXIR\) | Obsługuje dane adresowe \(odbiorcy\) w postaci zagregowanej\. |
| Import przelewu walutowego \(SWIFT\) | Obsługuje dane adresowe \(odbiorcy\) w postaci ustrukturyzowanej\. |
| Import przelewu podatkowego | Nie zawiera pól adresowych |
| Szablon przelewu zwykłego | Obsługuje dane adresowe \(odbiorcy\) w postaci ustrukturyzowanej\. |
| Szablon przelewu walutowego | Obsługuje dane adresowe \(odbiorcy\) w postaci ustrukturyzowanej\. |
| Szablon przelewu własnego | Nie zawiera pól adresowych do uzupełnienia przez klienta\. |
| Szablon przelewu podatkowego | Nie zawiera pól adresowych\. Formatka zawiera pole „Miasto” jednakże służy ono wyłącznie jako filtr\. |
| Import szablonu przelewu zwykłego | Nie zawiera dedykowanych pól adresowych \(ustrukturyzowanych\), przekazanie danych ustrukturyzowanych realizowane poprzez dedykowaną strukturę pola NAZWA\. |
| e\-Faktura \(KSeF\) / Przelew z faktury | Dane adresowe w fakturze KSeF zapisywane są w postaci zagregowanej\. |
| Usługi ERP API | W zakresie zlecania przelewu SORBNET/SWIFT/SEPA: Posiada pola do przekazania danych odbiorcy w postaci ustrukturyzowanej\. |
| Usługi BS API | W zakresie zlecania przelewu SORBNET/SWIFT/SEPA: Nie zawiera dedykowanych pól adresowych \(ustrukturyzowanych\), przekazanie danych ustrukturyzowanych realizowane poprzez dedykowaną strukturę pola NAZWA\. |
| Usługi PSD2 API | W zakresie zlecania przelewu SORBNET/SWIFT/SEPA: Posiada pola do przekazania danych odbiorcy w postaci ustrukturyzowanej\. |

Model rozwiązania \#zakres bazowy

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
### Asseco EBP

W ramach zakresu bazowego w Asseco EBP wprowadzona zostanie:

- kompensacja zmian w interfejsach API Asseco CB w zakresie zlecania przelewów bieżących i odroczonych
- przekazywanie przelewu bieżącego \(ELIXIR\) do Asseco CB z danymi ustrukturyzowanymi
- rejestracja zlecenia przelewu odroczonego i zlecenia stałego w Asseco CB z danymi ustrukturyzowanymi
- możliwość edycji aktywnego zlecenia stałego w zakresie danych adresowych w postaci ustrukturyzowanej oraz przekazywanie edycji zlecenia do Asseco CB z danymi ustrukturyzowanymi
- rozbudowa formatów importu przelewów i szablonów w zakresie ustrukturyzowanych danych adresowych
- rozbudowa usług ERP API, BS API i PSD2 API w zakresie obsługi danych ustrukturyzowanych w przelewach ELIXIR
Model rozwiązania \#rozszerzenie 1

W ramach **WK\.02** obecnie:

- Asseco CB przyjmuje przelew Elixir i dokonuje oceny, czy dany przelew spełnia kryteria konwersji na zlecenie Express Elixir\.
- Jeśli przelew spełnia warunki konwersji, Asseco** **CB dokonuje transformacji danych i przekazuje zlecenie Express Elixir do Asseco** **CL\.
- Asseco EBP przyjmuje przelew Elixir i dokonuje oceny, czy dany przelew spełnia kryteria konwersji na zlecenie Express Elixir\.
- Jeśli przelew spełnia warunki konwersji, Asseco** **EBP przekazuje zlecenie Express Elixir do Asseco** **CL\.
- Asseco** **CL odpowiada za obsługę zleceń Express Elixir, ich dalsze przekierowanie do systemu płatności natychmiastowych oraz ewentualną rekonwersję do przelewu Elixir, gdy płatność nie zostanie zrealizowana w trybie Express\.
Rozwiązanie w ramach zadania **WK\.02** zostanie zmodyfikowane w taki sposób, aby system Asseco CL dysponował ustrukturyzowanymi danymi niezbędnymi na wypadek konieczności przeprowadzenia rekonwersji z Express Elixir do Elixir\. W związku z tym, podczas przekazywania skonwertowanych danych EE do funkcji API systemu Asseco CL, oprócz danych EE zostaną również przekazane ustrukturyzowane dane adresowe Nadawcy i Odbiorcy pochodzące z pierwotnego przelewu Elixir, które nie są wymagane do obsługi komunikatu Express Elixir\.

### Asseco CB

W ramach wymagania **WK\.02** po wdrożeniu obsługi formatu Elixir XML \(ISO 20022\) zmodyfikowany zostanie proces konwersji przelewów wewnątrzgrupowych Elixir na zlecenia Express Elixir\.

Uwarunkowania wynikające z różnicy formatów danych po wdrożeniu Elixir XML:

**Format danych w przelewach Elixir XML**

Po wdrożeniu Elixir XML dane Nadawcy i Odbiorcy mogą występować w jednym z dwóch formatów:

- Format ISO 20022:
  - Nazwa: do **140 znaków**
  - Dane adresowe: pola ustrukturyzowane
  - Tytułem: pole o długości **140 znaków**
- Format zbiorczy \(obsługiwany w Asseco CB dla pierwszego wydaniu Elixir XML\):
  - Dane Nadawcy/Odbiorcy: **4 linie × 35 znaków**
  - Tytułem: **4 linie × 35 znaków**
**F****ormat ****danych w ****zlecenia****ch**** Express Elixir**

Zlecenia Express Elixir obsługują wyłącznie format:

- dane Nadawcy/Odbiorcy: **140**** znaków**
- pole *Tytułem*: **140**** znaków**
**Obsługa**** dla**** przelewów Elixir XML z danymi w formacie ISO 20022**

Jeżeli przelew Elixir XML obsługiwany będzie w Asseco CB w formacie ISO 20022, to:

- dane ustrukturyzowane Nadawcy/Odbiorcy zostaną przekształcone do formatu **14****0** znaków z wykorzystaniem funkcjonalności tworzenia nazwy zbiorczej dostępnej obecnie w systemie Asseco CB dla płatności w formacie ISO 20022,
- pole *Tytułem* \(do 140 znaków\) zostanie przekazane bez zmiany
- pozostałe elementy procesu konwersji pozostaną bez modyfikacji
- dodatkowo przekazane zostaną dane Nadawcy/Odbiorcy z oryginalnych pól przelewu Elixir \(nazwa i ustrukturyzowany adres\)\.
**Obsługa dla p****rzelew****ów Elixir**** z danymi w formacie 4 × 35 znaków**

Jeżeli przelew Elixir XML obsługiwany będzie w Asseco CB na podstawie danych przekazanych w dotychczasowym formacie 4\*35, wówczas:

- dane Nadawcy/Odbiorcy zostaną połączone do 140 znaków przez złączenie pól 4\*35 znaków
- pole Tytułem zostanie połączone do 140 znaków przez złączenie pól 4\*35 znaków
- Asseco CB nie przekaże dodatkowych danych ustrukturyzowanych do Asseco CL\.
### Asseco EBP

W ramach wymagania **WK\.02** po wdrożeniu obsługi formatu Elixir XML \(ISO 20022\) Asseco EBP przekaże do Asseco CL:

- dane Nadawcy/Odbiorcy **140**** znaków**
- pole *Tytułem* \(do 140 znaków\) **140**** znaków**
- pozostałe elementy procesu konwersji pozostaną bez modyfikacji
- dodatkowo przekazane zostaną dane Nadawcy/Odbiorcy z oryginalnych pól przelewu Elixir \(nazwa i ustrukturyzowany adres\) oraz Tytułem
### Asseco CL

Opis sporządzono przy założeniu, że w ramach wymagania **WK\.02** zlecenia Express Elixir do Asseco CL będą przekazywane z dodatkowymi danymi Nadawcy/Odbiorcy w postaci ustrukturyzowanej\.

**1\. Odbiór zlecenia Express Elixir**

Asseco CL odbiera zlecenie Express Elixir zawierające:

- dane Express Elixir \(Nadawca, Odbiorca, Tytułem w formacie 140znaków\),
- dodatkowe dane Nadawcy/Odbiorcy z wyodrębnioną Nazwą i ustrukturyzowanymi danymi adresowymi
Asseco CL zapisuje oba zestawy danych, przy czym dodatkowe dane nie biorą udziału w obsłudze przelewu Express Elixir\.

**2\. Obsługa procesu Express Elixir**

Asseco CL przetwarza zlecenie zgodnie z logiką systemu płatności natychmiastowych\.

**3\. ****W przypadku zaistnienia warunków**** rekonwersji****, p****rzygotowanie zgłoszenia Elixir XML**

Asseco CL wykonuje rekonwersję na podstawie dodatkowych danych Nadawcy/Odbiorcy:

- Nadawca\.Nazwa – Nm z oryginału,
- Nadawca\.Adres – PstlAdr z oryginału,
- Odbiorca\.Nazwa – Nm z oryginału,
- Odbiorca\.Adres – PstlAdr z oryginału,
- Tytułem – złączone do 140 znaków\.
W przypadku, gdy zlecenie Express Elixir było przekazane bez dodatkowych danych ustrukturyzowanych, wówczas Asseco CL przygotuje dane w postaci zbiorczej:

- Nadawca\.Nazwa – Nm \- 140 znaków dane z Nazwy Nadawcy,
- Nadawca\.Adres – PstlAdr \- brak,
- Odbiorca\.Nazwa – Nm \- 140 znaków dane z Nazwy Odbiorcy,
- Odbiorca\.Adres – PstlAdr \- brak,
- Tytułem – 140 znaków\.
**4****\. Przekazanie**** przelewu Elixir**** do ****Asseco ****CB**

Asseco CL przesyła do Asseco CB przelew Elixir XML z danymi wypełnionymi na podstawie dodatkowych danych przekazanych wcześniej przez Asseco CB lub Asseco EBP w ramach zlecenia Express Elixir lub w postaci zbiorczej w przypadku braku dodatkowych danych ustrukturyzowanych\.

Model rozwiązania \#rozszerzenie 2

### Asseco CB

W ramach wymagania **WK\.0****3**** **w Module administracyjnym uwzględnione zostaną nowe tabele z danymi ze zbiorów bazowych KIR:

- **OB***rrrrmm\.***0***dd*
- **BC***rrrrmm\.***0***dd*
W definicjach eksportu danych w module administracyjnym w grupie tablic „Konfiguracja KIR” dodana zostanie nowa pozycja odpowiadająca danym ze zbioru bazowego KIR OB*rrrrmm\.*E*dd*\. Nową tabelę będzie można dodać do zestawu eksportowanych tabel\.

Zawartość nowych tabel zostanie uwzględniona przy prezentacji danych na formatce Banki reprezentujące Bank \(Administracja\-\>Jednostki banku\-\>Banki uruchomienie przez przycisk \[Reprezentowany przez\]\)\. Na formatce „Banki reprezentujące Bank” dodane zostaną dwa nowe pola w dolnej części ekranu z informacjami:

- BIC
- BIC przejęty przez\.
W polu „BIC” prezentowana będzie wartość **Nr BIC** wczytana ze zbioru bazowego OB\. Jeżeli w danych wczytanych ze zbioru bazowego BC, będzie dostępny wiersz dla **BIC jednostki przejmowanej** zgodny z BIC prezentowanego banku, to w polu „BIC przejęty przez” prezentowana będzie wartość **BIC jednostki przejmującej** z tego wiersza\.

Model rozwiązania \#rozszerzenie 3 \- opcja

### Asseco EBP

W ramach wymagania **WK\.0****4**** **przygotowane zostanie narzędzie służące do konwersji danych adresowych zagregowanych \(przekazanych w pliku wejściowym\) do postaci ustrukturyzowanej\. Szczegóły w rozdziale 3\.7 \#Rozszerzenie 3 \(Opcja\) \- Narzędzie do konwersji danych adresowych\.

Wymagania szczegółowe

ELIXIR w Asseco CB

### ELIXIR wychodzący

PB\.CB\.011 Dokumenty \- formatki

Formatki systemu Asseco CB zostaną rozbudowane o możliwość wprowadzania danych Nadawcy i Odbiorcy w postaci zawierającej wyodrębnione pole Nazwa i ustrukturyzowane dane adresu\. Pole Nazwa będzie polem obowiązkowym, dane adresowe będą opcjonalne\.

Modyfikowane formatki:

- Przelew wychodzący zewnętrzny
- Przelew na rachunek US
- Polecenie zapłaty zewnętrzne
- Zwrot dla polecenia zapłaty
- Obciążenie bezpośrednie wychodzące
- Przelew zewnętrzny z konta własnego
- Obciążenie bezpośrednie wychodzące \(na konto własne\)
- Przelew na rachunek US z konta własnego
- Wpłata na rachunek zewnętrzny
- Wpłata na rachunek US
- GL Nota dwustronna z księgowaniem w CB \-\> Przelew na rachunek zewnętrzny
- Przelew wychodzący zewnętrzny transzy kredytu
- Przelew wychodzący z rejestru nadpłat\.
Dane zarejestrowane w systemie Asseco CB za pomocą powyższych formatek, będą podstawą do przygotowania zgłoszeń Elixir wychodzących dla PH\.

Uwaga

W przelewach podatkowych dane Odbiorcy wypełniane są przez system na podstawie wskazania Urzędu Skarbowego ze zbioru bazowego **US***rrrrmm*\.**N***dd*\. Zbiór bazowy nie zawiera pełnych danych adresowych Urzędów Skarbowych, w zbiorze wskazana jest jedynie Miejscowość\. Przy obecnej opcjonalności adresu w ELIXIR XML taka informacja jest wystarczającą, ale nie spełnia założeń Banku, aby wypełniać dane adresowe w przelewach inicjowanych w Asseco CB\.

Dodatkowe walidacje

Pola tekstowe przekazywane do PH nie mogą zawierać znaków zastrzeżonych w formacie XML, wymagane rozszerzenie puli znaków niedozwolonych\. W szczególności dotyczy pól Nazwa i poszczególnych pól danych adresowych Nadawcy/Odbiorcy, Tytułem, Informacji dodatkowych\.

Dla dokumentów wychodzących poleceń zapłaty, system Asseco CB będzie tworzył zgłoszenia Elixir tylko do godziny granicznej przekazywania Poleceń Zapłaty\. Godzina graniczna przekazywania Poleceń Zapłaty zastąpi obecną funkcjonalność przekazywania PZ tylko w pierwszej sesji Elixir\.

PB\.CB\.012 Deklaracja wypłaty środków na umowach

Formatki umów systemu Asseco CB umożliwiają rejestrację dyspozycji wypłaty odsetek oraz wypłaty środków przy zamykaniu umowy na rachunek zewnętrzny\. Formatki te zostaną rozbudowane o możliwość wprowadzania w dyspozycji danych Odbiorcy w postaci zawierającej wyodrębnione pole Nazwa i ustrukturyzowane dane adresu\. Pole Nazwa będzie polem obowiązkowym, dane adresowe będą opcjonalne\.

Tak zarejestrowane dane będą wykorzystywane w procesach automatycznych tworzenia dokumentu przelewu wychodzącego ELIXIR, który będzie podstawą do przygotowania zgłoszenia ELIXIR dla PH\.

Dane, które są obecnie zarejestrowane w formie deklaracji zawierających Nazwę Odbiorcy w postaci 4 linii 35 znaków, będą tymczasowo dopuszczone do tworzenia dokumentów przelewów Elixir bez podania adresu Odbiorcy do czasu obowiązywania schematu danych Odbiorcy z opcjonalnymi danymi adresowymi\. W przypadku danych Odbiorcy w formacie 4\*35 znaków, podczas tworzenie dokumentu przelewu wychodzącego Elixir system wypełni dotychczasowy format danych Nadawcy/ Odbiorcy \(4\*35 znaków\) a podczas tworzenia zgłoszenia Elixir dla PH złączy 4 linie w jedno pole, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane w rozdziale 2\.3\.2 i taka wartość będzie wprowadzana do zgłoszenia Elixir w polu Nazwa Odbiorcy a pola adresu ustrukturyzowanego nie będą wypełniane\.

Jeżeli deklaracja wypłaty środków będzie dotyczyła kwoty przekraczającej próg konwersji na Sorbnet i jednocześnie dane Odbiorcy będą wypełnione z adresem ustrukturyzowanym, to dokument zostanie skonwertowany na przelew Sorbnet, w przypadku, gdy dane Odbiorcy będą w formacie 4\*35 znaków, wówczas dokument zostanie wystawiony jako Elixir bez konwersji na przelew Sorbnet\.

PB\.CB\.013 Zlecenia stałe ELIXIR

System Asseco CB przyjmuje zlecenia stałe w postaci przelewu uznaniowego ELIXIR oraz w postaci polecenia zapłaty wychodzącego ELIXIR\. Formatki do rejestracji zleceń stałych typu ELIXIR i PZ zewnętrzny zostaną rozbudowane o możliwość wprowadzania w zleceniu danych Odbiorcy w postaci zawierającej wyodrębnione pole Nazwa i ustrukturyzowane dane adresu\. Pole Nazwa będzie polem obowiązkowym, dane adresowe będą opcjonalne\.

Tak zarejestrowane dane zlecenia stałego będą wykorzystywane w procesach automatycznych tworzenia dokumentu przelewu wychodzącego ELIXIR lub dokumentu PZ zewnętrznego, które będą podstawą do przygotowania zgłoszenia ELIXIR dla PH\. W przypadku realizacji zleceń stałych typu Polecenie zapłaty zewnętrzne, system Asseco CB będzie uwzględniał podczas generacji zgłoszeń Elixir tylko dokumenty PZ wystawione przed godziną graniczną przekazywania Poleceń Zapłaty, która zastąpi obecną funkcjonalność przekazywania PZ tylko w pierwszej sesji Elixir\.

Zlecenia stałe Elixir, które mają obecnie Nazwę Odbiorcy zarejestrowaną w postaci 4 linii 35 znaków, będą tymczasowo do tworzenia dokumentów przelewów Elixir bez podania adresu Odbiorcy do czasu obowiązywania schematu danych Odbiorcy z opcjonalnymi danymi adresowymi\. W przypadku zleceń stałych z danymi Odbiorcy w formacie 4\*35 znaków, system wystawi dokument przelewu w obecnym formacie z danymi Nadawcy/Odbiorcy w polach 4\*35 znaków a tworząc zgłoszenie Elixir dla PH złączy 4 linie w jedno pole, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane w rozdziale 2\.3\.2 i taka wartość będzie wprowadzana do zgłoszenia Elixir w polu Nazwa Odbiorcy a pola adresu ustrukturyzowanego nie będą wypełniane\.

Jeżeli zlecenie stałe Elixir będzie na kwotę przekraczającą próg konwersji na Sorbnet i jednocześnie dane Odbiorcy będą wypełnione z adresem ustrukturyzowanym, to dokument zostanie skonwertowany na przelew Sorbnet, w przypadku, gdy dane Odbiorcy będą w formacie 4\*35 znaków, wówczas dokument zostanie wystawiony jako Elixir bez konwersji na przelew Sorbnet\.

PB\.CB\.014 Dokumenty \- API

Funkcje API systemu Asseco CB podane w rozdziale 2\.3\.4 Obsługa płatności i poleceń zapłaty Elixir w Asseco CB zostaną rozbudowane o możliwość wprowadzania w zleceniu danych Nadawcy/Odbiorcy w postaci zawierającej wyodrębnione pole Nazwa i ustrukturyzowane dane adresu\. Pole Nazwa będzie polem obowiązkowym, dane adresowe będą opcjonalne\.

W przypadku, gdy system dziedzinowy przekaże dane Nadawcy/Odbiorcy w obecnym formacie 4\*35 znaków, to system Asseco CB utworzy dokument bez danych ustrukturyzowanych a podczas wystawiania zgłoszenia Elixir dla Payment Hub zinterpretuje przekazane dane jako wsad do pola „Nm” Nazwa Nadawcy/Odbiorcy, 4 linie zostaną złączane w jedno pole o długości 140 znaków, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale2\.3\.2\. Jeżeli pole Tytułem będzie przekazane w postaci 4 linii, to 4 linie zostaną złączane w jedno pole o długości 140 znaków z użyciem zasad łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2\.

Dokument wystawiony na bazie danych z API, będzie podstawą do przygotowania zgłoszenia Elixir wychodzącego dla PH\.

Dodatkowe walidacje

Pola tekstowe z danymi przekazywanymi dalej do PH nie mogą zawierać znaków zastrzeżonych w formacie XML, wymagane rozszerzenie puli znaków niedozwolonych i zamiana na znaki zastępcze\. W szczególności dotyczy pól Nazwa i poszczególnych pól danych adresowych Nadawcy/Odbiorcy, Tytułem, Informacji dodatkowych\.

PB\.CB\.015 Dokumenty – Obecne interfejsy plikowe

Obecne interfejsy plikowe systemu Asseco CB umożliwiające wprowadzenie przelewu wychodzącego ELIXIR będą wykorzystywane do wprowadzania danych dokumentu wychodzącego zewnętrznego ELIXIR z zastrzeżeniem, że dokument w Asseco CB zostanie zarejestrowany w dotychczasowym formacie bez podziału na Nazwę i dane adresowe, natomiast w zgłoszeniu Elixir przekazywanym do PH, dane Nadawcy/Odbiorcy podane w formacie 4\*35 znaków, będą złączane w jedno pole o długości 140 znaków, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2 i takie pole będzie wprowadzane do pola Nazwa Nadawcy/Odbiorcy, pola adresu ustrukturyzowanego nie będą wypełniane\. Jeżeli pole Tytułem będzie przekazane w postaci 4 linii, to 4 linie zostaną złączane w jedno pole o długości 140 znaków z użyciem zasad łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2

Dokumenty utworzone na podstawie danych z obecnych interfejsów plikowych, będą tymczasowo dopuszczone do przygotowania zgłoszenia Elixir wychodzącego dla PH\.

Dodatkowe walidacje

Podczas tworzenia dokumentów ELIXIR, pola tekstowe z danymi przekazywanymi dalej do PH nie mogą zawierać znaków zastrzeżonych w formacie XML, wymagane rozszerzenie puli znaków niedozwolonych i zamiana na znaki zastępcze\. W szczególności dotyczy pól Nazwa i poszczególnych pól danych adresowych Nadawcy/Odbiorcy, Tytułem, Informacji dodatkowych\.

PB\.CB\.016 Anulowanie dokumentu

W przypadku konieczności anulowania dokumentu przelewu wychodzącego, dopuszczalne będzie anulowanie dokumentu, dla którego nie wysłano zgłoszenia Elixir do PH\. Jeżeli dokument będzie miał zgłoszenie Elixir wysłane do PH, wówczas wykonana będzie weryfikacja dopuszczalności anulowania w PH\. W tym celu Asseco CB wykona zgłoszenie do PH anulowania płatności wychodzącej za pomocą usługi wystawionej przez PH\. Oczekiwana jest odpowiedź potwierdzająca \(o ile będzie to możliwe\) lub odmowna ze strony PH\. W przypadku zgody na anulowanie, PH obsłuży po swojej stronie wycofanie płatności\. W przypadku, gdy płatność nie będzie możliwa do wycofania, PH odpowie negatywnie na zgłoszenie anulowania bez wykonywania dodatkowych działań\. Asseco CB wykona anulowanie dokumentu w przypadku otrzymania zgody na anulowanie z PH\. W przypadku braku zgody na anulowanie z PH, Asseco CB nie zrealizuje anulowania dokumentu\.

PB\.CB\.017 Zwrot zrealizowanego polecenia zapłaty

Odwołanie zrealizowanego polecenia zapłaty będzie przekazywane do PH zgłoszeniem Elixir wychodzącym typu „Wychodzący zwrot PZ”\.

### ELIXIR przychodzący

PB\.CB\.021 Przyjmowanie zgłoszeń ELIXIR z PH

Dane przekazywane do Asseco CB będą przekazywane pogrupowane w paczki z możliwością przesyłania porcjami\. System Asseco CB przystępuje do obsługi zgłoszeń z danej paczki, po odebraniu wszystkich zadeklarowanych porcji\.

Krok 1

Przekazywanie porcji zgłoszeń z paczki zgłoszeńElixir\.

Krok 2

Weryfikacja odbioru wszystkich porcji zgłoszeń dla paczki\. Uruchomienie przetwarzania zgłoszeń\.

W przypadku wystąpienia błędu przetwarzania zgłoszenia lub odmowy realizacji – dla każdego zgłoszenia osobno wykonanie kroku 3\.

Po zakończeniu obsługi wszystkich zgłoszeń, przejście do kroku 4\.

Krok 3

W przypadku wystąpienia odmowy, postępowanie zgodne z obsługą odmowy\. W przypadku błędu, uruchomienie obsługi zwrotu, działanie zależne od parametryzacji systemu\. Jeżeli parametr systemowy **BOOK\_RECLAIMS** = 0, to zwrot nie jest księgowany w systemie Asseco CB\. Jeżeli parametr systemowy **BOOK\_RECLAIMS** = 1, to wykonywane jest księgowanie przyjęcia środków z drogi przychodzącej na tzw\. konto reklamacji, wskazane w parametrze systemowym **NRB\_ACC\_OWN\_FOR\_RECLAIMS\_ELIX**\.

Następnie Asseco CB przekazuje do PH informację o odmowie lub potrzebie zwrotu, podając numer błędu obsługi zgłoszenia \- uruchomienie funkcji API wystawionej przez PH\.

W przypadku, gdy błąd będzie dotyczył przychodzącego Obciążenia bezpośredniego, do PH zostanie przekazana informacja typu „Zwrot obciążenia bezpośredniego przychodzącego”\. Zgłoszenie to zostanie przekazane do PH w celu wycofania obciążenia bezpośredniego, zgodnie z obecną obsługą zwrotów\.

Numeracja błędów zgodnie ze Słownikiem External Code Sets\.

Krok 4

Przekazanie do PH informacji o zakończeniu obsługi paczki zgłoszeń\.

Asseco CB będzie przyjmowało dane Nadawcy/Odbiorcy w nowym formacie z wydzielonymi opcjonalnymi danymi adresowymi\. Jeżeli Payment Hub będzie dysponował tylko danymi Nadawcy/Odbiorcy w formacie 4\*35 znaków, to PH wykona złączenie 4 linii do jednego pola o długości 140 znaków i przekaże złączone dane w polu Nazwa, stosując zasady łączenia linii 4\*35 w pole 140 znaków opisane wyżej w rozdziale 2\.3\.2\.

Uruchamianie skanera AML będzie wykonywane zgodnie z konfiguracją przewidzianą dla przelewów Elixir przychodzących\.

W obsłudze Poleceń zapłaty będą zaimplementowane kody odmowy ze słownika *External Code Sets*\. System Asseco CB będzie reagował na nowe kody odmowy, które zastąpią dotychczas występujące kody odmów\.

PB\.CB\.022 Zwroty przychodzące ELIXIR z PH

Wśród zgłoszeń przychodzących Elixir będą zwroty do komunikatów wysłanych\. Zwrotów przychodzących system transakcyjny nie powinien odrzucać\.

W obsłudze zwrotów przychodzących mogą wystąpić przypadki:

- zwrot na rachunek, na którym nie można wykonać księgowania np\. z powodu czasowej blokady rachunku, z powody zamknięcia rachunku, itp\.
- zwrot przelewu gotówkowego rozpoznawany dla kont własnych podanych w opcji Rozliczenia \-\> Elixir\-\> Konfiguracja blokady zwrotu na konta własne\.
Takie zwroty będzie można przekierować na wskazane konto własne do wyjaśnienia w Asseco CB lub odesłać do obsługi po stronie PH – dopuszczalność funkcjonalności będzie uzależniona od konfiguracji\.

Zwrot przelewu gotówkowego wymaga udziału Operatora, który podejmie czynności mające na celu poinformowanie zleceniodawcę o zaistniałym zwrocie i zdecyduje o sposobie zaksięgowania zwróconych środków\.

### Procesy

PB\.CB\.031 Automatyczna konwersja przelewów wychodzących Elixir na Sorbnet

Funkcjonalność automatycznej konwersji przelewów Elixir na Sorbnet w obecnym schemacie danych nie może być przywrócona w 100% przypadków spełniających warunki konwersji, ze względu na opcjonalność danych adresowych Odbiorcy\. Jeżeli przelew Elixir spełniający warunki kwotowe konwersji na Sorbnet nie będzie miał wypełnionych danych adresowych, to płatność Elixir nie będzie konwertowana na Sorbnet\.

Przywrócenie pełnej konwersji Elixir na Sorbnet nastąpi po wprowadzeniu wymagalności danych adresowych w przelewach Elixir\.

PB\.CB\.032 Obsługa COT dla przelewów Elixir wychodzących

Likwidacja obsługi sesji rozliczeniowych Elixir w Asseco CB nie wpływa na weryfikację godziny granicznej\. Obecna weryfikacja godziny granicznej dla dokumentów Elixir będzie kontynuowana dla ELIXIR XML\. Działanie systemu będzie uzależnione od wartości parametru systemowego **COT\_MODE** oraz godzin granicznych z macierzy COT\.

PB\.CB\.037 Godziny obsługi PZ

Alternatywą do obecnej obsługi uwzględniania wychodzących Poleceń zapłaty tylko w pierwszej sesji Elixir, będzie wprowadzenie parametru określającego godzinę graniczną dla wychodzących Poleceń Zapłaty i uzależnienie wysyłania zgłoszeń Elixir PZ od tego parametru\. Wysyłanie zgłoszeń Elixir typu „Wychodzące polecenie zapłaty” do PH będzie wykonywane do podanej godziny\. Po wskazanej godzinie dla dokumentów PZ do Payment Hub nie będą wysyłane zgłoszenia Elixir typu „Wychodzące polecenie zapłaty”, takie zgłoszenia zostaną przekazane do PH w kolejnej dobie\.

Ograniczenie czasu odpowiedzi do przychodzących zgłoszeń typu „Przychodzące polecenie zapłaty” przez parametr systemowy **PH\_DD\_SERVICE\_TIME**** **będzie funkcjonowało w obsłudze odpowiedzi dla tych zgłoszeń Elixir\.

PB\.CB\.033 Zbiory bazowe

Zestaw zbiorów bazowych wczytywanych do Asseco CB zostanie rozbudowany o możliwość wskazania do wczytywania zbioru:

- **OB***rrrrmm\.***0***dd* –zbiór jednostek bezpośrednio uczestniczących w systemie Elixir \(BIC\-KNR\)
- BCrrrrmm\.0dd	\- Zbiór zamienników BIC jednostek Bezpośrednich Uczestników Elixir\.
Dane wczytane ze zbioru **OB***rrrrmm\.***0***dd* będą służyły do określenia BIC banku uczestnika rozliczeń ELIXIR XML\.

Dane wczytane ze zbioru **B****C***rrrrmm\.***0***dd** *będą wczytywane wyłącznie w celu prezentacji\.

Nowe zbiory bazowe należy dodać do listy wczytywanych zbiorów w parametrze systemowym **DEF\_KIR\_IMPORT\_FILE\_NAMES\_EXT**\.

Usunięcie zbioru **ZR***rrrrmm\.***E***dd* z puli wczytywanych zbiorów bazowych w systemie Asseco CB realizuje się przez zmianę wartości parametru systemowego **DEF\_KIR\_IMPORT\_FILE\_NAMES\_EXT**\.

PB\.CB\.034 Zadania pracujące w tle

W systemie przygotowane będą zadania pracujące w tle nad obsługą zgłoszeń ElIXIR\. Będą to zadania odpowiadające za:

- Tworzenie wychodzących zgłoszeń ELIXIR w tym zwrotów na wniosek Dłużnika
- Przekazywanie wychodzących zgłoszeń ELIXIR do PH
- Obsługa przychodzących zgłoszeń ELIXIR w tym przekazywanie informacji o zwrotach, odmowach
- Informowanie o zakończeniu obsługi paczki zgłoszeń ELIXIR\.
Zgłoszenia Elixir dotyczące Poleceń Zapłaty będą mogły wysyłane w osobnych zestawach danych przekazywania danych do PH niż pozostałe przelewy Elixir\.

System będzie umożliwiał przekazywanie danych w odrębnych paczkach osobno Polecenia zapłaty i bez Poleceń zapłaty\.

Przekazywanie zgłoszeń Elixir w paczce bez wskazanego typu rozliczeń będzie możliwe przez użycie odpowiedniej pozycji w tzw\. Module planisty\.

Przelewy Elixir mające NRB Odbiorcy z KNR wskazującym na rozliczenia wewnątrzgrupowe \(w przypadku banków zrzeszających i zrzeszonych\), będą klasyfikowane jako wewnątrzgrupowe, pozostałe jako międzybankowe\. System będzie umożliwiał przekazywanie danych w odrębnych paczkach w podziale na: wewnątrzgrupowe i międzybankowe oraz w ramach tego podziału osobno Polecenia zapłaty i bez Poleceń zapłaty\.

PB\.CB\.035 Monitorowanie procesów obsługi zgłoszeń ELIXIR

System umożliwi podgląd wysłania zgłoszenia Elixir dla dokumentów, które są podstawą komunikacji w ramach rozliczeń ELIXIR XML\.

System umożliwi podgląd stanu paczki zgłoszeń ELIXIR – system liczbę odebranych i liczbę obsłużonych zgłoszeń a także aktualny status paczki zgłoszeń\.

Przegląd Dokumenty niewysłane uwzględni prezentację dokumentów, dla których system nie wygenerował zgłoszenia Elixir\.

PB\.CB\.036 Blokada wysyłania dokumentu

Istniejąca w systemie funkcjonalność nakładania blokady wysyłania przelewu Elixir będzie podtrzymana dla przelewów ELIXIR XML\. Dokument z nałożoną blokadą wysyłki komunikatu Elixir nie będą uwzględniane podczas tworzenia zgłoszeń Elixir dla Payment Hub\. Po zdjęciu blokady wysyłania, dokument będzie brany pod uwagę podczas najbliższego tworzenia zgłoszeń Elixir dla PH\.

PB\.CB\.038 Wysyłka priorytetowa

Przygotowanie wysyłki priorytetowej nie będzie realizowane po stronie Asseco CB\. System przekaże do PH zgłoszenia ELIXIR z oznaczeniem „wysyłki priorytetowej”, w przypadku, gdy przelew Elixir będzie dotyczył klienta występującego w grupie klientów\.

W systemie Asseco CB możliwe jest oznaczenie klientów \(połączonych w grupy\), dla których dokumenty wychodzące Elixir miały dostępną opcję generacji komunikatów w ramach tzw\. **wysyłki priorytetowej**\.

Jeżeli przelew wychodzący Elixir będzie dotyczył klienta z grupy, to zgłoszenie będzie zawierało informację o tym, że klient jest z grupy oraz Symbole grup, do których jest przypisany\.

Na podstawie tej informacji w PH mogą być podejmowane dalsze działania związane z generacją komunikatów w ramach dedykowanych godzin generacji komunikatów po głównej sesji rozliczeniowej\.

### Rozliczenia

PB\.CB\.042 Zadania pracujące w tle

W systemie przygotowane będą zadania pracujące w tle nad obsługą zgłoszeń Elixir\. Będą to zadania odpowiadające za:

- Tworzenie wychodzących zgłoszeń ELIXIR w tym zwrotów na wniosek Dłużnika
- Przekazywanie wychodzących zgłoszeń ELIXIR do PH
- Obsługa przychodzących zgłoszeń ELIXIR \(zawiera weryfikację kompletności paczki zgłoszeń\) w tym przekazywanie informacji o zwrotach, odmowach
- Informowanie o zakończeniu obsługi paczki zgłoszeń ELIXIR\.
Tworzenie i przekazywanie wychodzących zgłoszeń ELIXIR uruchamiane będzie zgodnie z harmonogramem zadań w tzw\. Module planisty\. Uruchomienie zadania możliwe będzie również z poziomu formatki opisanej w rozdziale PB\.CB\.046\.

Obsługa przychodzących zgłoszeń Elixir będzie uruchamiana po odebraniu danych przez API\. Księgowanie będą mogły startować automatycznie bądź będą uruchamiane z formatki opisanej w rozdziale PB\.CB\.045\.

Informowanie o zakończeniu obsługi paczki będzie wykonywane automatycznie po obsłużeniu wszystkich zgłoszeń z paczki\.

PB\.CB\.044 Księgowania zgłoszeń Elixir

Paczki zgłoszeń Elixir przekazane przez Payment Hub będą gotowe do księgowania po odebraniu przez Asseco CB kompletu porcji podanej dla danej paczki\.

**Sposoby księgowania paczki zgłoszeń**

Księgowanie automatyczne – uruchamiane automatycznie po wczytaniu danych z ostatniej porcji dla paczki\. Uruchomienie automatyczne będzie uzależnione od parametryzacji systemu\.

System Asseco CB umożliwi ręczne księgowanie zgłoszeń Elixir z Payment Hub \- powstanie nowa opcja systemu obsługująca ręczne uruchamianie księgowania odebranych zgłoszeń Elixir\.

Automatyczne księgowania zgłoszeń Elixir po otrzymaniu paczki zgłoszeń z Payment Hub będzie uzależnione od parametryzacji systemu\.

**Konta drogi**

Konta drogi będą dobierane dla zgłoszeń Elixir przez analogię do obecnych księgowań komunikatów Elixir z podziałem na typy kont drogi istniejące obecnie w systemie Asseco CB\.

**NRB wirtualne**

Dla dokumentu przychodzącego system Asseco CB wykonuje weryfikację, czy NRB rachunku odbiorcy jest rzeczywiste czy wirtualne\. Dla NRB wirtualnego system wykona obsługę zgodną z konfiguracją systemu dla płatności na rachunki wirtualne\.

**Blokady księgowania zgłoszeń**

Podczas obsługi zgłoszenia Elixir, które jest przychodzącym zwrotem wykonywane będzie sprawdzenie NRB Odbiorcy czy nie występuje na liście kont własnych podanych w opcji Rozliczenia \-\> Elixir\-\> Konfiguracja blokady zwrotu na konta własne\. Zgłoszenia Elixir na NRB podane w powyższej opcji będzie zatrzymywane, nie będzie wykonywane księgowanie na NRB ze zgłoszenia\.

**Brak możliwości księgowania na NRB Odbiorcy/Informacja o zwrocie**

Jeżeli nie jest możliwa realizacja płatności na NRB Odbiorcy \(np\. brak rachunku, blokada rachunku lub inne\), to system Asseco CB poinformuje Payment Hub o odmowie realizacji, podając powód odmowy\. Powód odmowy będzie wyznaczony ze słownika kodów *External Code Sets\.*

W przypadku odmowy Polecenia Zapłaty lub zwrotu uznania, odpowiedź do Payment Hub jest wysyłana dla pojedynczej płatności bez oczekiwania na zakończenie obsługi całej paczki\.

Jeśli decyzję o zwrocie podejmuje Operator, to powiadomienie do Payment Hub wysyłane jest po decyzji Operatora\.

**Zakończenie księgowania**

Po zakończeniu księgowania wszystkich zgłoszeń z paczki, system poinformuje Payment Hub o zakończeniu obsługi paczki zgłoszeń Elixir\.

PB\.CB\.045 Formatka Księgowanie zgłoszeń Elixir XML

Nowa formatka – opcja Księgowanie zgłoszeń Elixir XML\.

Formatka zaprezentuje listę paczek zgłoszeń Elixir przekazanych do Asseco CB\. Podstawowe uruchomienie domyślnie odczyta dane dla bieżącej Daty operacji\. Możliwa będzie zmiana Daty operacji lub podanie dodatkowych filtrów:

- Data operacji
- Typy rozliczeń:
  - – \(bez określenia typu\) – opcja konfigurowalna
  - Międzybankowe \(bez PZ\)
  - Międzybankowe \(tylko PZ\)
  - Wewnątrzgrupowe \(bez PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
  - Wewnątrzgrupowe \(tylko PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
- Kwota
Dopuszczalność uruchomienia bez podania typu rozliczeń będzie uzależniona od konfiguracji systemu\.

Na liście paczek zgłoszeń przychodzących prezentowane będą:

- Identyfikator CB \(czyli identyfikator paczki zgłoszeń Elixir\)
- Identyfikator PH \(czyli identyfikator paczki zgłoszeń Elixir\)
- Czas rozpoczęcia
- Wczytanych \(Liczba zgłoszeń Elixir otrzymanych w ramach paczki\)
- Kwota \(suma kwot ze zgłoszeń Elixir\)
- Przetworzonych \(Liczba obsłużonych zgłoszeń Elixir w ramach paczki\)
- Błędnych \(Liczba zgłoszeń Elixir w ramach paczki, dla których wystąpił błąd obsługi\)
- Zwróconych \(Liczba zgłoszeń Elixir w ramach paczki, które zostały zwrócone do PH\)
- Typ rozliczeń
- Status paczki
Dla wskazanej paczki zgłoszeń będzie można obejrzeć Dziennik przetwarzania\.

Dla wskazanej paczki zgłoszeń będzie można uruchomić formatkę przeglądania zgłoszeń Elixir otrzymanych w ramach danej paczki\.

Formatka umożliwi ręczne uruchomienie Księgowania zgłoszeń Elixir\.

Formatka umożliwi Anulowanie księgowania paczki zgłoszeń Elixir w trakcie trwania obsługi paczki przez uprawionego Operatora\.

PB\.CB\.046 Formatka Wysyłanie zgłoszeń Elixir XML

Nowa formatka – opcja Rozliczenia\-\>Payment Hub\-\>Wysyłanie zgłoszeń Elixir XML

Formatka zaprezentuje listę paczek zgłoszeń Elixir wychodzących utworzonych w Asseco CB\. Podstawowe uruchomienie domyślnie odczyta dane dla bieżącej Daty operacji\. Możliwa będzie zmiana Daty operacji lub podanie dodatkowych filtrów:

- Data operacji
- Typy rozliczeń:
  - \- \(bez określania typu\) – opcja konfigurowalna
  - Międzybankowe \(bez PZ\)
  - Międzybankowe \(tylko PZ\)
  - Wewnątrzgrupowe \(bez PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
  - Wewnątrzgrupowe \(tylko PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
- Kwota
Dopuszczalność uruchomienia bez podania typu rozliczeń będzie uzależniona od konfiguracji systemu\.

Na liście paczek zgłoszeń wychodzących prezentowane będą:

- Identyfikator CB \(czyli identyfikator paczki zgłoszeń Elixir\)
- Identyfikator PH \(czyli identyfikator paczki zgłoszeń Elixir\)
- Czas rozpoczęcia
- Liczba zgłoszeń Elixir w ramach paczki
- Kwota \(suma kwot ze zgłoszeń Elixir\)
- Typ rozliczeń
- Status paczki
Dla wskazanej paczki zgłoszeń będzie można obejrzeć Dziennik przetwarzania\.

Dla wskazanej paczki zgłoszeń będzie można uruchomić formatkę przeglądania zgłoszeń Elixir utworzonych w ramach danej paczki\.

Formatka umożliwi ręczne uruchomienie generacji zgłoszeń Elixir\. Uruchomienie generacji będzie umożliwiało wskazanie typu rozliczeń, który ma być uwzględniony w paczce zgłoszeń, wówczas dana paczka będzie zawierała tylko jeden typ rozliczeń\. Uruchomienie generacji będzie zakładało mową paczkę zgłoszeń Elixir\.

Paczka utworzona w systemie Asseco CB zostanie przekazana do Payment Hub zgodnie z harmonogramem zdefiniowanym w opcji Lista zadań uruchamianych zgodnie z terminarzem lub na żądanie Operatora\.

PB\.CB\.047 Formatka przeglądu zgłoszeń Elixir XML

Nowa formatka uruchamiana z poziomu obsługi paczki zgłoszeń Elixir wychodzących, z poziomu obsługi paczki zgłoszeń przychodzących oraz z dwóch nowych opcji menu głównego \- opcja Przegląd zgłoszeń wychodzących Elixir XML, Przegląd zgłoszeń przychodzących Elixir XML\.

Formatka zaprezentuje listę zgłoszeń Elixir z użyciem filtrów\. Część filtrów będzie niedostępna w przypadku uruchomienia przeglądu z poziomu paczki zgłoszeń Elixir\. Filtry:

- Rodzaj rozliczeń Wewnętrzne, Wewnątrzgrupowe \(w przypadku banków zrzeszających i zrzeszonych\), Międzybankowe
- Zakres dat
- Status zgłoszenia
- Kwota
Dodatkowe filtry dla wartości na liście:

- Typ zgłoszenia
- Rachunek nadawcy
- Rachunek odbiorcy
Dane prezentowane ma liści zgłoszeń Elixir:

- Typ zgłoszenia
- Kwota
- Zwrócone \(typu znacznik\)
- Wstrzymany \(typu znacznik\)
- Zablokowany \(typu znacznik\)
- Kierunek
- Rachunek nadawcy
- Rachunek odbiorcy
- NRB Odbiorcy w CB
- Tytułem
Dla zgłoszeń Elixir dostępne będą funkcjonalności – dostępność funkcjonalności będzie uzależniona od kontekstu uruchomienia \(wysyłanie, księgowanie, przegląd\):

- Podgląd zgłoszenia
- Wstrzymaj wybrane
- Zablokuj/Odblokuj
- Zwróć wybrane rozliczenie
- Księguj wybrane
- Dodaj do uzgodnionych
- Weryfikacje skanerów
- Procesowanie \(podgląd historii działań na zgłoszeniu\)
- Zwrot
- Podgląd dokumentu
- Odbiorca – przypisanie rozliczenia – wybór umowy/konta własnego
Podgląd zgłoszenia będzie prezentował wybrane dane w postaci formularza oraz pozostałe dane w formie json\. Pola na formularzu:

- NRB Nadawcy
- NRB Odbiorcy
- Kwota
- Typ zgłoszenia \(opisowy\)
- Json z zawartością danych z/do PH
Pralnia

PB\.CB\.051 Rejestracja danych do pralni \(Elixir 56\)

Podczas rejestracji danych do pralni dla przelewów elixir zostaną uwzględnione dane przekazywane w polach ustrukturyzowanego adresu Odbiorcy/Nadawcy\.

Raporty i wydruki

### Raportowanie komunikatów Elixir

PB\.CB\.R01 Raporty rozliczeń dla komunikatów Elixir

Istniejące obecnie raporty tworzące zestawienia dla komunikatów Elixir będą dostępne dla danych historycznych z okresu sprzed wdrożenia Elixir XML\. Zastrzeżenie dotyczy raportów podanych w rozdziale 2\.3\.8 w zakresie komunikatów Elixir\.

### Raportowanie dla zgłoszeń Elixir

PB\.CB\.R02 Raport rozliczeń Elixir XML

W systemie Asseco CB powstanie raport, który będzie prezentował dane z rozliczeń Elixir XML, czyli tworzony na podstawie zgłoszeń Elixir wygenerowanych w Asseco CB i wysyłanych do PH oraz dla zgłoszeń odebranych w Asseco CB z PH w okresie od włączenia obsługi Elixir XML w Asseco CB\.

Raport będzie dostępny w postaci tzw\. analitycznej, czyli prezentujący dane detaliczne zgłoszeń lub w postaci syntetycznej, czyli prezentującej dane podsumowane per paczka i typ zgłoszenia\.

Zakres danych prezentowanych na raporcie będzie wybierany na podstawie parametrów:

- Kierunek:
  - Wychodzący
  - Przychodzący
- Data od
- Data do
- Typy rozliczeń:
  - – \(bez podania typu rozliczeń\)
  - Międzybankowe \(bez PZ\)
  - Międzybankowe \(tylko PZ\)
  - Wewnątrzgrupowe \(bez PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
  - Wewnątrzgrupowe \(tylko PZ\) \(w przypadku banków zrzeszających i zrzeszonych\)
- Identyfikator paczki
- Dokładność:
  - Syntetyka
  - Analityka\.
W przypadku raportu z dokładnością „Analityka” możliwy będzie wybór sposobu sortowania:

- Sortowanie według:
  - Kwota
  - NRB nadawcy
  - NRB odbiorcy
  - Typ zgłoszenia
  - BIC banku uczestnika Nadawcy
  - BIC banku uczestnika Odbiorcy
  - Kod dokumentu KIR
- a
  - Rosnąco
  - Malejąco
Przez Typ zgłoszenia rozumie się wartość przekazywaną pomiędzy Asseco CB i PH w polu „Typ zgłoszenia Elixir”\.

Przez Kod dokumentu KIR rozumie się wartość przekazywaną pomiędzy Asseco CB i PH w polu kirDocumentCode\.

Zakres danych prezentowanych dla zestawienia analitycznego:

- Kwota
- Tytuł przelewu
- NRB Nadawcy
- NRB Odbiorcy
- BIC banku uczestnika Nadawcy
- BIC banku uczestnika Odbiorcy
- Typ zgłoszenia
- Kod dokumentu KIR
W podsumowaniu prezentowana jest:

- Liczba pozycji
- Suma wartości „Kwota”\.
Zakres danych prezentowanych dla zestawienia syntetycznego:

- Identyfikator paczki
- Typ zgłoszeń
- Suma kwot
- Liczba zgłoszeń
W podsumowaniu prezentowana jest:

- Liczba pozycji
- Suma wartości „Suma kwot”\.
PB\.CB\.R03 Pozostałe raporty i wydruki

Istniejące raporty:

- Lista otrzymanych odmów realizacji PZ
- Raport „podzielonych” PZ
- Polecenia zapłaty\-\>Lista autoryzacji
Uwzględnią dane ze zgłoszeń Elixir\.

Wyciągi

PB\.CB\.001 Parametry konfiguratora opisów dokumentów

Dokumenty tworzone na podstawie zgłoszeń Elixir będą miały wypełniane dotychczasowe pola z nazwą Nadawcy/ Odbiorcy w formacie 4\*35 znaków wartością zbiorczą utworzoną na podstawie Nazwy i adresu ustrukturyzowanego\. Dla tych danych będą wypełnione dotychczasowe parametry konfiguratora z informacjami z dokumentu\.

Parametry konfiguratora opisów z dokumentu dla zgłoszeń Elixir z wypełnionymi danymi adresu ustrukturyzowanego będą miały dodatkowo dostępne dane w parametrach:

- Nazwa/Imię i nazwisko nadawcy \(\#$ISO20022\_RE\_NM\)
- Oddział nadawcy \(\#$ISO20022\_RE\_A\_DEPT\)
- Pododdział nadawcy \(\#$ISO20022\_RE\_A\_SUBDEPT\)
- Ulica nadawcy \(\#$ISO20022\_RE\_A\_STRTNM\)
- Numer budynku nadawcy \(\#$ISO20022\_RE\_A\_BLDGNB\)
- Nazwa budynku nadawcy \(\#$ISO20022\_RE\_A\_BLDGNM\)
- Piętro nadawcy \(\#$ISO20022\_RE\_A\_FLR\)
- Skrytka pocztowa nadawcy \(\#$ISO20022\_RE\_A\_PSTBX\)
- Numer lokalu nadawcy \(\#$ISO20022\_RE\_A\_ROOM\)
- Kod pocztowy nadawcy \(\#$ISO20022\_RE\_A\_PSTCD\)
- Miejscowość nadawcy \(\#$ISO20022\_RE\_A\_TWNNM\)
- Dzielnica miasta nadawcy \(\#$ISO20022\_RE\_A\_TWNLCTNNM\)
- Obszar w regionie kraju nadawcy \(\#$ISO20022\_RE\_A\_DSTRCTNM\)
- Region kraju/województwo nadawcy \(\#$ISO20022\_RE\_A\_CTRYSUBDVSN\)
- Kraj nadawcy \(\#$ISO20022\_RE\_A\_CTRY\)
- Nazwa/Imię i nazwisko odbiorcy \(\#$ISO20022\_BE\_NM\)
- Oddział odbiorcy \(\#$ISO20022\_BE\_A\_DEPT\)
- Pododdział odbiorcy \(\#$ISO20022\_BE\_A\_SUBDEPT\)
- Ulica odbiorcy \(\#$ISO20022\_BE\_A\_STRTNM\)
- Numer budynku odbiorcy \(\#$ISO20022\_BE\_A\_BLDGNB\)
- Nazwa budynku odbiorcy \(\#$ISO20022\_BE\_A\_BLDGNM\)
- Piętro odbiorcy \(\#$ISO20022\_BE\_A\_FLR\)
- Skrytka pocztowa odbiorcy \(\#$ISO20022\_BE\_A\_PSTBX\)
- Numer lokalu odbiorcy \(\#$ISO20022\_BE\_A\_ROOM\)
- Kod pocztowy odbiorcy \(\#$ISO20022\_BE\_A\_PSTCD\)
- Miejscowość odbiorcy \(\#$ISO20022\_BE\_A\_TWNNM\)
- Dzielnica miasta odbiorcy \(\#$ISO20022\_BE\_A\_TWNLCTNNM\)
- Obszar w regionie kraju odbiorcy \(\#$ISO20022\_BE\_A\_DSTRCTNM\)
- Region kraju/województwo odbiorcy \(\#$ISO20022\_BE\_A\_CTRYSUBDVSN\)
- Kraj odbiorcy \(\#$ISO20022\_BE\_A\_CTRY\)
Inne

PB\.CB\.I01 Eksporty dla Hurtowni danych

Po wdrożeniu Elixir XML, Asseco CB zmieni zakres danych wystawianych do hurtowni\.

**Zmiany w tabel****i**** ****DOCUMENTS**

Po wdrożeniu Elixir XML, Asseco CB zmieni zakres danych udostępnianych do hurtowni danych\. W tabeli DOCUMENTS znajdą się nowe kolumny;

- BIC banku uczestnika Nadawcy
- BIC banku uczestnika Odbiorcy
**Zmiany w tabelach SETTLEMENT i COMM\_SETTL**

Po wdrożeniu Elixir XML, Asseco CB zmieni zakres danych udostępnianych do hurtowni danych\. W tabelach SETTLEMENT \(STT\) oraz COMM\_SETTL \(CSETTL\) nie będą już pojawiały się wiersze odpowiadające rozliczeniom Elixir\. Czyli:

- W tabeli STT nie będą pojawiały się nowe wiersze z wartością 0 w kolumnie IS\_LOAD\_SPECIAL\.
- W tabeli CSETTL nie będzie nowych wierszy dla komunikatów Elixir\.
**Nowe dane w tabelach ISO\_REFS i ISO\_DATA**

Po zmianach dane Nadawcy i Odbiorcy dla dokumentów Elixir będą dostępne w tabelach:

- ISO\_REFS – wiersze powiązania danych z tabeli DOCUMENTS z danymi w tabeli ISO\_DATA
- ISO\_DATA – dane uczestników płatności w formacie ustrukturyzowanym\.
**Nowa tabela zgłoszeń Elixir**

Zostanie wyeksportowana nowa tabela, która będzie zawierać informacje o wychodzących i przychodzących zgłoszeniach Elixir\. Dane biznesowe będą przekazywane w formacie JSON, zgodnym z zawartością elementu typu zgłoszenie Elixir, używanym w funkcjach API do:

- wysyłania zgłoszeń do PH,
- przyjmowania zgłoszeń w CB\.
Przykładowa zawartość json zgłoszenia przyjmowanego w CB:

\{

"amlVerificationId": null,

"amount": \{

"amount": 77\.0,

"currency": "PLN"

\},

"cbOriginalRefNo": null,

"currencyOrder": \{

"amount": 77\.0,

"currency": "PLN",

"senderAccountNo": "string",

"senderCountry": "PL",

"senderName": " sender name z currency order"

\},

"description": "Przelew xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ewidencyjny",

"interbankInformation": "przel zew przych",

"kirDocumentCode": "51",

"paymentReferenceNo": "KB\_ELIX\_MB\_Z002",

"postingDate": "2030\-08\-15",

"receiverAccountNumber": "78161000067002003034350169",

"receiverParty": \{

"Nm": "XXXXXXXX",

"PstlAdr": \{

"BldgNb": "400",

"BldgNm": null,

"Ctry": null,

"CtrySubDvsn": null,

"Dept": null,

"DstrctNm": null,

"Flr": null,

"PstBx": null,

"PstCd": null,

"Room": "15",

"StrtNm": "WWWWWW",

"SubDept": null,

"TwnLctnNm": null,

"TwnNm": "WAW"

\}

\},

"senderAccountNumber": "11124017926634346446586665",

"senderParty": \{

"Nm": "YYYYYYYYY",u

"PstlAdr": \{

"BldgNb": "43",

"BldgNm": null,

"Ctry": null,

"CtrySubDvsn": null,

"Dept": null,

"DstrctNm": null,

"Flr": null,

"PstBx": null,

"PstCd": null,

"Room": "55",

"StrtNm": "WYsoka",

"SubDept": null,

"TwnLctnNm": null,

"TwnNm": "Warszawa"

\}

\},

"settlementType": "CREDIT",

"unlimitedText": "string unlimitedText",

"valueDate": "2030\-08\-15"

\}

PB\.CB\.I02 Skanowanie AML

Asseco CB udostępnia rozszerzony zakresu danych przelewów Elixir w ekstraktach do hurtowni, do wykorzystania w zasilaniu batchowym\. Opis zmiany w Asseco AML znajduje się w rozdziale 3\.8\.

PB\.CB\.I03 Skrypty techniczne – eksport/import zleceń stałych

Asseco przygotuje skrypt eksportujący dane Zleceniodawcy/Odbiorcy zleceń stałych Elixir i PZ do pliku tekstowego\. Bank może wykorzystać plik do przygotowania wsadu dla pliku importującego dane zleceń stałych w postaci z adresem ustrukturyzowanym\. Asseco przygotuje skrypt importujący modyfikacje zleceń stałych z pliku przygotowanego przez Bank – import będzie realizowany jako modyfikacja istniejących zleceń stałych\.

Obsługa danych ustrukturyzowanych ELIXIR w bankowości internetowej

### Asseco EBP

Założenia ogólne

- Dane nadawcy w transakcjach w ramach przelewów ELIXIR uzupełniane będą po stronie Asseco CB \(na podstawie przekazanego identyfikatora klienta\)\. W bankowości internetowej na formatkach będą prezentowane dane nadawcy w ramach istniejących pól, ale informacje te nie będą przekazywane do Asseco CB\.
- W związku z opcjonalnością danych adresowych odbiorcy walidacja adresu dla przelewów ELIXIR nie ulegnie zmianie\.
- Przyjmuje się, że dane operacji wynikających z realizacji przelewów ELIXIR z danymi ustrukturyzowanymi, pobrane z Asseco CB, zawierać będą zarówno pola adresowe zagregowane jak ustrukturyzowane\.
- Nie przewiduje się automatycznej konwersji danych adresowych w istniejących dyspozycjach przelewów zwykłych i zleceń stałych do postaci ustrukturyzowanej\.
- Przyjmuje się, że w przypadkach:
- istniejących dyspozycji w koszyku zawierających dane nieustrukturyzowane
- przelewów inicjowanych z systemów niezawierających danych ustrukturyzowanych \(np\. PayByNet\)
podczas przekazania przelewu do Asseco CB, dane adresowe nieustrukturyzowane będą przekazywane w ramach pola nazwa\.

### Zlecanie przelewu zwykłego

W zakresie obsługi przelewu zwykłego bieżącego w bankowości internetowej wprowadzone zostaną:

- kompensacja zmian w usłudze API WS Asseco CB
- zmiana maksymalnej liczby znaków w polu „Odbiorca” \(ELIXIR/SORBNET\) z 35 znaków do 140 znaków
- przekazywanie danych adresowych \(ustrukturyzowanych\) przy rejestracji zlecenia w Asseco CB w dedykowanych polach API
### Obsługa zleceń odroczonych / cyklicznych

W zakresie obsługi przelewów odroczonych i zleceń stałych w bankowości internetowej wprowadzone zostaną:

- integracja z nowymi usługami API REST Asseco CB w zakresie:
- rejestracji przelewu odroczonego / zlecenia stałego
- edycji przelewu odroczonego / zlecenia stałego
- pobierania przelewów odroczonych / zleceń stałych
- pobierania realizacji zleceń stałych
- zmiana maksymalnej liczby znaków w polu „Odbiorca” \(ELIXIR/SORBNET\) z 35 znaków do 140 znaków
- rozbudowa edycji zlecenia stałego o możliwość zmiany danych odbiorcy \(nazwy i adresu w postaci ustrukturyzowanej\)
- oznaczenie przelewu odroczonego / zlecenia stałego z poziomu listy, zawierającego dane nieustrukturyzowane jako wymagającego interakcji użytkownika
### Dane adresowe w pozostałych przelewach

Przelew własny

W zakresie przelewu własnego w bankowości internetowej wprowadzone zostanie \(na poziomie logiki biznesowej systemu\) uzupełnianie danych adresowych ustrukturyzowanych w przelewie danymi z kartoteki klienta\.

Przelew PayByNet

W zakresie przelewu PayByNet w bankowości internetowej wprowadzone zostanie \(na poziomie logiki biznesowej systemu\):

- zapisywanie, otrzymanych od usługodawcy, danych odbiorcy przelewu \(nazwy i adresu\) w polu „Odbiorca”
- przekazywanie danych odbiorcy \(nazwy i adresu\) w ramach pola nazwa odbiorcy w API WS Asseco CB przy rejestracji przelewu
Powyższe podejście wynika braku ustrukturyzowanych danych adresowych w danych odbiorcy przekazywanych przez usługodawcę\.

Przelew z faktury KSeF

W zakresie przelewów generowanych automatycznie z faktur KSeF w bankowości internetowej wprowadzone zostanie \(na poziomie logiki biznesowej systemu\):

- zapisywanie, odczytanych z faktury KSeF, danych odbiorcy przelewu \(nazwy i adresu\) w polu „Odbiorca”
- przekazywanie danych odbiorcy \(nazwy i adresu\) w ramach pola nazwa odbiorcy w API WS Asseco CB przy rejestracji przelewu
Powyższe podejście wynika braku ustrukturyzowanych danych adresowych w strukturze faktury KSeF\.

### Import przelewu zwykłego

W zakresie importu przelewów zwykłych dla formatu:

- Elixir, VideoTel – dane odbiorcy przelewu \(nazwa i adres\) zostaną zaimportowane do systemu w całości w polu „Odbiorca”
- XML, Liniowy – wprowadzone zostaną dedykowane pola adresowe \(ustrukturyzowane\), pole nazwa zostanie rozszerzone z 35 znaków do 140 znaków
- Telekonto – nie są wymagane zmiany, dane odbiorcy odczytywane są na podstawie numeru NRB odbiorcy z listy odbiorców zdefiniowanych
Dodatkowo w ramach projektu wprowadzony zostanie nowy format importu przelewu zwykłego – ISO 20022\.

### Import szablonu przelewu zwykłego

W zakresie importu szablonów przelewów zwykłych dla formatu:

- XML, Liniowy – wprowadzone zostaną dedykowane pola adresowe \(ustrukturyzowane\), pole nazwa zostanie rozszerzone z 35 znaków do 140 znaków\.
- Telekonto – nie są planowane zmiany, po wczytaniu szablonu konieczna będzie jego edycja w systemie
### Dane adresowe w usługach API

ERP API

W ramach usługi:

- zwracającej listę oraz szczegóły operacji – zakres danych nie ulegnie zmianie, dane adresowe nadal będą przekazywane w postaci zagregowanej
- rejestrującej przelew zwykły \(ELIXIR\) – wprowadzona zostanie obsługa ustrukturyzowanego adresu odbiorcy, pole nazwa zostanie rozszerzone z 35 znaków do 140 znaków
BS API

Ze względu na to, iż Bank odpowiada za kształt i strukturę BS API opisane niżej zmiany powinny być odzwierciedlone w  BS API i przesłane w formie dokumentacji YAML do implementacji po stronie dostawcy\.

W ramach usługi:

- zwracającej listę oraz szczegóły operacji – dane adresowe nadal będą przekazywane w postaci zagregowanej oraz w polach ustrukturyzowanych \(jeżeli operacja będzie je zawierała\)
- rejestrującej przelew zwykły – zostanie rozbudowana w zakresie danych ustrukturyzowanych odbiorcy
Zakłada się, że opisane wyżej zmiany w BS API zostaną uszczegółowione z Bankiem na etapie implementacji\.

### Asseco OBA

PSD2 API

W ramach usługi rejestrującej przelew zwykły \(ELIXIR\) – pole nazwa zostanie rozszerzone z 35 znaków do 140 znaków\.

\#Rozszerzenie 3 \(Opcja\) \- Narzędzie do konwersji danych adresowych

W ramach wymagania opcjonalnego przygotowane zostanie narzędzie służące do automatycznej konwersji danych adresowych zagregowanych do postaci ustrukturyzowanej\.

### Założenia ogólne

- Narzędzie na wejściu będzie odczytywać plik zawierający dane adresowe zagregowane\.
- W wyniku działania narzędzia powstanie nowy plik zawierający dane adresowe podzielone na pola:
- Ulica
- Numer domu
- Numer mieszkania
- Kod pocztowy
- Miejscowość
- Narzędzie wykona automatyczną propozycję podziału adresu na pola, a nie rozstrzygnięcie jednoznaczne; wynik może wymagać weryfikacji\.
- Zakłada się, że konwersji będą podlegać polskie adresy\.
- Adres zagregowany powinien być jedną linią tekstu na rekord; dane wielowierszowe, zlepione z innymi danymi \(np\. nazwą firmy\) obniżają skuteczność i mogą być odrzucone\.
- Dostawca nie ponosi odpowiedzialności za błędy wynikające z: literówek, braku kodu/miejscowości, nietypowych skrótów, kilku adresów w jednym polu, błędnych kodów pocztowych\.
Przygotowane narzędzie będzie mogło być wykorzystane do masowej konwersji danych adresowych m\.in\. odbiorców zleceń stałych\.

Zasilanie batch Asseco AML

PB\.AML\.01 Zmiany w zasilaniu batchowym systemu AML ze zmienionych ekstraktów CB w zakresie danych ustrukturyzowanych

System Asseco AML zostanie dostosowany do zmienionego zakresu wystawianych ekstraktów z systemu CB dla transakcji elixir w zakresie danych ustrukturyzowanych, w obszarze integracji źródeł:

- ISO\_REFS – wiersze powiązania danych z tabeli DOCUMENTS z danymi w tabeli ISO\_DATA
- ISO\_DATA – dane uczestników płatności w formacie ustrukturyzowanym\.
PB\.AML\.02 Zmiany w zasilaniu batchowym systemu AML w zakresie rozszerzenia informacji o BIC banku nadawcy i BIC banku odbiorcy na dokumencie

System Asseco AML zostanie rozszerzony o możliwość importu danych wystawianych w ekstrakcie dokumentów \(DOCUMENTS\) systemu CB, związanych z przekazaniem informacji o BIC banku nadawcy i BIC banku odbiorcy\.

Wymagane licencje

W celu realizacji wymagań opisanych w niniejszym dokumencie  wymagany zakup dodatkowych licencji\.

| Kod licencji | Nazwa |
| --- | --- |
| D3K\.CB\.PROD\.ELIXIR\_XML | Licencja na obsługę płatności Elixir XML w systemie Asseco CB |

Obszary pod wpływem

Wpływ na procesy operacyjne/ biznesowe

- Komunikacja z Payment HUB – zmiana formatu wymiany danych w istniejących funkcjach API
- Potencjalna zmiana źródła danych dla modelu księgowań na NOSTRO dla podsumowań rozliczeń Elixir w Asseco TR
- Komunikacja Asseco CB \- AML – dostosowanie w zakresie zasilania typu batch z danych wystawionych przez Asseco CB o adresie ustrukturyzowanym Nadawcy/odbiorcy i BIC banków uczestników w przelewie Elixir\.
- Bankowość elektroniczna – wpływ na dane płatności\.
- Hurtowania danych – dostępność nowych danych do wykorzystania przez Hurtownię danych\.
Wymagania szczególne wynikające z RODO

Rozwiązanie nie zmienia podejścia do przetwarzania danych osobowych\.

Uwarunkowania

- Zawarte w dokumencie nazwy nowych pól, operacji, parametrów, statusów, postaci raportów itp\. są przykładowe i mają na celu odzwierciedlenie ich biznesowego znaczenia\. Nazwy w dostarczonym rozwiązaniu mogą zostać zmodyfikowane z uwagi na ograniczenia projektowe lub narzędziowe\.
- Jeżeli w wymaganiu nie zostało zapisane inaczej, to na etapie projektowania zaproponowany sposób realizacji może zostać zmieniony, o ile zmiana ta nie zmieni sensu biznesowego tego wymagania\.
- Obszary dotyczące adresu, które nie zostały opisane w wizji rozwiązania nie ulegają zmianie\. Zmiany w zakresie, który nie został wyspecyfikowany w wizji rozwiązania, należy zgłaszać jako dodatkowe wymagania\.
- Istniejące zlecenia stałe ELIXIR oraz deklaracje wypłat na umowach będą wymagały od Banku uzupełnienia danych adresowych ustrukturyzowanych\. Opcjonalność pól adresowych dotyczy pierwszego wydania ELIXIR XML\.
- Zmiana formatu danych na ELIXIR XML nie obejmuje zmiany sposobu identyfikacji przelewów transgranicznych \(w zakresie danych rzeczywistego zleceniodawcy, gdy w transferze środków pieniężnych bierze udział krajowy pośredniczący dostawca usług płatniczych, zgodnie z wymogami Rozporządzenia Parlamentu Europejskiego i Rady \(UE\) 2015/847 w sprawie informacji towarzyszących transferom środków pieniężnych\)\.
- Dokument przedstawia opis możliwości oferowanego rozwiązania\. Funkcjonalności, które nie zostały opisane w dokumencie a mogą być domniemywane na bazie nazw pól, operacji, parametrów czy makiet nie będą realizowane\.
- Opcje i funkcjonalności wskazane w rozdziale 2\.3\.8 będą działały w ograniczonym zakresie, zgodnie z opisem w tym rozdziale\.
Dodatki

Analizowane systemy

| System | Opis |
| --- | --- |
| Asseco CB | System transakcyjny, w którym obsługiwane są umowy klientów Banku typu Rachunek Bieżący, Depozyt terminowy, Kredyt i Gwarancja, Linia kredytowa\. |
| Asseco EBP | Asseco Enterprise Banking Platform System bankowości elektronicznej dla mikro, małych i średnich oraz dużych przedsiębiorstw\. |

Historia zmian

| Data | Wersja | Autor | Opis |
| --- | --- | --- | --- |
| 01 | Agnieszka Żmudzińska/Asseco | Utworzenie dokumentu |  |
| 01 | Agnieszka Żmudzińska/Asseco | Piotr Długosz/Asseco | Opis w zakresie Bankowości elektronicznej |
| 02 | Bank | Uwagi do dokumentu |  |
| 03 | Agnieszka Żmudzińska/Asseco | Uzupełnienie dokumentu, odpowiedzi do komentarzy |  |
| 04 | Agnieszka Żmudzińska/Asseco | Odpowiedzi do uwag, usunięcie GOBI, opis zwrotów obciążeń bezpośrednich, obsługa zbioru bazowego BCrrrrmm\.0dd, opis eksportów do hurtowni danych\. |  |
| 04 | Agnieszka Żmudzińska/Asseco | Piotr Długosz/Asseco | Uzupełnienie dokumentu w zakresie Bankowości elektronicznej |
| 04 | Agnieszka Żmudzińska/Asseco | Jacek Bobrowski/Asseco | Uzupełnienie dokumentu w zakresie AML |

Autorskie prawa majątkowe do całości dokumentacji projektowej należą do Asseco Poland S\.A\. i podlegają ochronie na podstawie ustawy z dnia 4 lutego 1994 r\. o prawie autorskim i prawach pokrewnych \(tekst jednolity; Dz\.U\. z 2006 r\. Nr 90 poz\. 631 z późn\. zm\.\)\.
