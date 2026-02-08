# Usługi banku

## unassignCompany

[REQ_SYS]**Opis:** Usuniecie powiązania między bankiem a usługą ksiegową[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]



## customerContext

[REQ_SYS]**Opis:** Pobranie kontekstu klienta na potrzeby SSO[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| ssoToken | Jednorazowy, krótkoterminowy token przekazany w ramach redirecta z banku |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]



## accounts

[REQ_SYS]**Opis:** Pobranie listy aktywnych rachunków bieżących firmy[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujacy |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accountList: | Lista rachunków bieżących firmy |[REQ_SYS_END]
[REQ_SYS]| accountNumber | Numer rachunku |[REQ_SYS_END]
[REQ_SYS]| displayName | Nazwa rachunku (domyśle lub nadana przez klienta) |[REQ_SYS_END]



## bankRedirect

[REQ_SYS]**Opis:** Przekierowanie z serwisu księgowego do banku w ramach powrotu SSO[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujacy |[REQ_SYS_END]



## domesticPaymentInit

[REQ_SYS]**Opis:** Zainicjowanie płatności w banku - przelew krajowy bez split payment[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]
[REQ_SYS]| paymentId | Identyfikator płatności nadany przez CashDirector |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]
[REQ_SYS]| sourceAccount | Rachunek do obciążenia |[REQ_SYS_END]
[REQ_SYS]| amount | Kwota płatności |[REQ_SYS_END]
[REQ_SYS]| currency | Waluta |[REQ_SYS_END]
[REQ_SYS]| title | Tytuł przelewu |[REQ_SYS_END]
[REQ_SYS]| beneficiaryName | Nazwa odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAddress | Adres odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAccount | Rachunek odbiorcy |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| paymentToken | Token do wykonania płatnosci |[REQ_SYS_END]



## domesticSplitPaymentInit

[REQ_SYS]**Opis:** Zainicjowanie płatności w banku - przelew krajowy ze split paymentem[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]
[REQ_SYS]| paymentId | Identyfikator płatności nadany przez CashDirector |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]
[REQ_SYS]| sourceAccount | Rachunek do obciążenia |[REQ_SYS_END]
[REQ_SYS]| amount | Kwota płatności |[REQ_SYS_END]
[REQ_SYS]| vatAmount | Kwota VAT |[REQ_SYS_END]
[REQ_SYS]| currency | Waluta |[REQ_SYS_END]
[REQ_SYS]| title | Tytuł przelewu |[REQ_SYS_END]
[REQ_SYS]| beneficiaryName | Nazwa odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAddress | Adres odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAccount | Rachunek odbiorcy |[REQ_SYS_END]
[REQ_SYS]| taxpayerIdType | Typ identyfikatora płatnika |[REQ_SYS_END]
[REQ_SYS]| taxpayerId | Nr identyfikacji płatnika |[REQ_SYS_END]
[REQ_SYS]| invoiceNumber | Nr faktury |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| paymentToken | Token do wykonania płatnosci |[REQ_SYS_END]



## foreignPaymentInit

[REQ_SYS]**Opis:** Zainicjowanie płatności w banku - przelew zagraniczny / z przewalutowaniem[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]
[REQ_SYS]| paymentId | Identyfikator płatności nadany przez CashDirector |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]
[REQ_SYS]| sourceAccount | Rachunek do obciążenia |[REQ_SYS_END]
[REQ_SYS]| amount | Kwota płatności |[REQ_SYS_END]
[REQ_SYS]| currency | Waluta |[REQ_SYS_END]
[REQ_SYS]| title | Tytuł przelewu |[REQ_SYS_END]
[REQ_SYS]| beneficiaryName | Nazwa odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAddress | Adres odbiorcy |[REQ_SYS_END]
[REQ_SYS]| beneficiaryAccount | Rachunek odbiorcy |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| paymentToken | Token do wykonania płatnosci |[REQ_SYS_END]



## taxPaymentInit

[REQ_SYS]**Opis:** Zainicjowanie płatności w banku - przelew podatowy[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]
[REQ_SYS]| paymentId | Identyfikator płatności nadany przez CashDirector |[REQ_SYS_END]
[REQ_SYS]| externalCompanyId | Identyfikator firmy w banku |[REQ_SYS_END]
[REQ_SYS]| externalUserId | Identyfikator użytkownika w banku |[REQ_SYS_END]
[REQ_SYS]| sourceAccount | Rachunek do obciążenia |[REQ_SYS_END]
[REQ_SYS]| amount | Kwota płatności |[REQ_SYS_END]
[REQ_SYS]| officeAccount | Nr konta organu podatkowego |[REQ_SYS_END]
[REQ_SYS]| formSymbol | Typ formularza urzędu skarbowego |[REQ_SYS_END]
[REQ_SYS]| formPeriod | Okres rozliczenia |[REQ_SYS_END]
[REQ_SYS]| payerIdType | Typ identyfikatora płatnika |[REQ_SYS_END]
[REQ_SYS]| payerIdNumber | Nr identyfikacji płatnika |[REQ_SYS_END]



### Output params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| paymentToken | Token do wykonania płatnosci |[REQ_SYS_END]



## POST redirect (płatność)

[REQ_SYS]**Opis:** Przekierowanie do banku do formatki przelewowej[REQ_SYS_END]

### Input params

[REQ_SYS]| Parametr | Opis |[REQ_SYS_END]
|---|---|
[REQ_SYS]| paymentToken | Token do wykonania płatności otrzymany z usługi paymentInit |[REQ_SYS_END]
[REQ_SYS]| accessToken | Token autoryzujący |[REQ_SYS_END]
[REQ_SYS]| backUrl | URL na który użytkownik zostanie przekierowany po wykonaniu płatności |[REQ_SYS_END]

