<!-- AI-CONSTRAINTS
Zakres: Logowanie jednokrotne (SSO)
Format: RQ-SSO-###
Źródła: /kb/banki-api-uslugi-banku.md, /kb/glossary.md, /kb/wymagania_funkcjonalne_be_integracja_z_cash_director v1.md, /spec/99-conventions.md
-->

# Logowanie jednokrotne (SSO)

## 1. Cel
Zapewnienie bezpiecznego i bezobsługowego logowania użytkownika
z BE do CashDirector.

---

## 2. Wymagania funkcjonalne

### RQ-SSO-001
BE MUST przekazać do CashDirector `ssoToken` (jednorazowy, krótkoterminowy) w ramach przekierowania Użytkownika z BE do CashDirector.

Uzasadnienie:  
CashDirector wymaga `ssoToken` do pobrania kontekstu klienta na potrzeby SSO.

AC:
- Given Użytkownik jest zalogowany w BE
- When Użytkownik wybiera usługę CashDirector w BE
- Then BE przekazuje do CashDirector `ssoToken` w ramach przekierowania

---

### RQ-SSO-002
BE MUST udostępnić usługę `customerContext`, która umożliwia CashDirector wymianę `ssoToken` na `accessToken` dla wskazanych `externalCompanyId` i `externalUserId`.

Uzasadnienie:  
CashDirector potrzebuje `accessToken` do autoryzowanych wywołań usług banku po stronie BE.

AC:
- Given CashDirector posiada `ssoToken` otrzymany w ramach SSO
- When CashDirector wywołuje `customerContext` przekazując `ssoToken`, `externalCompanyId` i `externalUserId`
- Then BE zwraca `accessToken`

---

### RQ-SSO-003
BE MUST wymagać użycia `accessToken` jako parametru autoryzującego dla usług banku wywoływanych przez CashDirector: `accounts`, `domesticPaymentInit`, `domesticSplitPaymentInit`, `foreignPaymentInit`, `taxPaymentInit` oraz `bankRedirect`.

Uzasadnienie:  
Ograniczenie dostępu do usług banku do kontekstu uzyskanego w ramach SSO.

AC:
- Given CashDirector nie przekazuje `accessToken`
- When CashDirector wywołuje dowolną z usług: `accounts`, `domesticPaymentInit`, `domesticSplitPaymentInit`, `foreignPaymentInit`, `taxPaymentInit`, `bankRedirect`
- Then BE odrzuca żądanie

---

## 3. Bezpieczeństwo

### RQ-SSO-004
BE MUST odrzucać ponowne użycie `ssoToken` w usłudze `customerContext`.

Uzasadnienie:  
`ssoToken` jest tokenem jednorazowym i nie może zostać użyty do ponownego pozyskania `accessToken`.

AC:
- Given CashDirector użył poprawnego `ssoToken` w `customerContext` i uzyskał `accessToken`
- When CashDirector ponownie wywołuje `customerContext` z tym samym `ssoToken`
- Then BE odrzuca żądanie

---

### RQ-SSO-005
BE MUST odrzucać `ssoToken` nieznany lub wygasły w usłudze `customerContext`.

Uzasadnienie:  
`ssoToken` jest tokenem krótkoterminowym i jego użycie musi być ograniczone czasowo.

AC:
- Given `ssoToken` jest nieznany albo wygasły
- When CashDirector wywołuje `customerContext` z tym `ssoToken`
- Then BE odrzuca żądanie

---

### RQ-SSO-006
BE MUST powiązać `ssoToken` z `externalCompanyId` i `externalUserId` oraz odrzucać wywołanie `customerContext`, gdy przekazane identyfikatory nie odpowiadają powiązaniu.

Uzasadnienie:  
Ochrona przed wykorzystaniem tokenu dla innej firmy lub innego użytkownika.

AC:
- Given `ssoToken` został wygenerowany dla pary (`externalCompanyId`, `externalUserId`)
- When CashDirector wywołuje `customerContext` z tym `ssoToken`, ale z innym `externalCompanyId` lub `externalUserId`
- Then BE odrzuca żądanie

---

## 4. Scenariusze negatywne

### RQ-SSO-007
BE MUST odrzucić wywołanie `customerContext` w przypadku braku parametru `ssoToken`.

Uzasadnienie:  
`ssoToken` jest wymagany do pobrania kontekstu klienta na potrzeby SSO.

AC:
- Given CashDirector wywołuje `customerContext`
- When nie przekazuje `ssoToken`
- Then BE odrzuca żądanie

---

### RQ-SSO-008
BE MUST obsłużyć scenariusz powrotu z CashDirector do banku poprzez usługę `bankRedirect` autoryzowaną `accessToken`.

Uzasadnienie:  
Powrót do BE po zakończeniu działań w CashDirector wymaga autoryzowanego przekierowania.

AC:
- Given CashDirector posiada poprawny `accessToken`
- When CashDirector inicjuje powrót do banku wykorzystując `bankRedirect`
- Then Użytkownik zostaje przekierowany do BE

---

## 5. Zagadnienia otwarte
- OPEN-QUESTION-001: Jaki jest wymagany czas życia (`TTL`) dla `ssoToken` (konkretna wartość i jednostka)?
- OPEN-QUESTION-002: W jaki sposób BE przekazuje `ssoToken` w przekierowaniu do CashDirector (np. query params vs POST) i jaka jest nazwa pola/parametru po stronie CashDirector?
- OPEN-QUESTION-003: Skąd CashDirector pozyskuje `externalCompanyId` i `externalUserId` do wywołania `customerContext` (redirect vs dane z rejestracji/parowania)?
- OPEN-QUESTION-004: Jakie są oczekiwane odpowiedzi błędów (statusy/kody i komunikaty) dla `customerContext` przy: token nieznany/wygasły/użyty ponownie/brak parametrów?
- OPEN-QUESTION-005: Jaki jest format i czas życia `accessToken` oraz zasady jego unieważniania?
- OPEN-QUESTION-006: Czy `bankRedirect` jest wywołaniem API (z odpowiedzią/redirectem), czy wyłącznie adresem URL do przekierowania w przeglądarce?
- OPEN-QUESTION-007: Czy BE ma weryfikować stan Użytkownika (np. nieaktywny) i uprawnienia do CashDirector na etapie `customerContext`, a jeśli tak — według jakich reguł?
