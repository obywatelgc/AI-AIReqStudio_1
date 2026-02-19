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