Wymagania funkcjonalne Blokowanie możliwości logowania do systemu BE po terminie ważności dowodu osobistego
1. Cel dokumentu
Celem dokumentu jest opisanie wymagań funkcjonalnych dla systemu Bankowości Elektronicznej (BE) w zakresie blokowanie możliwości logowania do systemu BE dla klientów którzy posiadają nieaktualny dokument tożsamości.  Dokument stanowi podstawę dla projektowania, implementacji i testów backendu BE.

2. Zakres funkcjonalny integracji
- Blokowanie możliwości logowania do systemu BE po terminie ważności dowodu osobistego

3. Aktorzy
•	Klient instytucjonalny / Właściciel firmy – użytkownik BE.
•	System BE (Backend Banku) – system Bankowości Elektronicznej.

4. Wymagania funkcjonalne

WM-01 Blokowanie możlwiości zalogowania do ssytemu BE po terminie ważności dowodu osobistego
Wymaganiem Banku jest sprawdzanie ważności dokumentu tożsamości po zalogowaniu użytkownika do systemu. W przypadku gdy data ważności dokumentu tożsamości jest nieaktualna to system BE aktualizuje datę pobierając ją z systemu Asseco CB. Jeżeli po aktualizacji data dokumentu tożsamości pozostaje nieaktualna to weryfikowany jest parametr (idExpiryGracePeriodDays - liczba dni od daty ważności dokumentu tożsamości po których blokowany jest dostęp do systemu, tryb restrykcyjny). W trybie restrykcyjnym użytkownikowi prezentowany jest odpowiedni komunikat oraz może on przejść wyłącznie do opcji Wnioski (wniosek w Ferryt do aktualizacji danych dokumentu tożsamości – obecnie dostępna funkcjonlaność). Tryb restrykcyjny działa zarówno dla desktop oraz mobile. W szczególności w trybie restrykcyjnym mobile nie można przejść do opcji generowania kodu BLIK. W przypadku gdy data ważności dokumentu jest aktualna albo nie został przekroczony parametr idExpiryGracePeriodDays to logowanie do systemu realizowane jest standardowo.

Zmiana dotyczy również logowania dla szybkich płatności PBN.

