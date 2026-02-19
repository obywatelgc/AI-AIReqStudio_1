# Kluczowe wytyczne - stan obecny systemu BE (AS-IS)

## 1. Cel dokumentu
Dokument stanowi kanoniczny skrót stanu obecnego systemu BE na potrzeby generowania specyfikacji wymagań.
Nie zastępuje pełnej dokumentacji w `doc/*`, a jedynie porządkuje kluczowe fakty i odwołania źródłowe.

## 2. Konteksty klienta i moduły
- Kontekst indywidualny (detal/osobisty): moduł `Asseco CBP`.
- Kontekst mikro (MŚP): moduł `Asseco EBP`.
- Kontekst instytucjonalny (firmowy/korporacyjny): moduł `Asseco EBP`.
- BackOffice: moduł administracyjny i konfiguracyjny dla obsługi systemu.

| Kontekst | Segment | Moduł | Kanały |
|---|---|---|---|
| Indywidualny | detal | CBP | desktop, mobile |
| Mikro (MŚP) | mikro | EBP | desktop, mobile |
| Firmowy/Korporacyjny | korpo | EBP | desktop, mobile |

Mimo jasnego podziału odpowiedzialności i podziału kontekstów Banki często piszą wymagania w odniesieniu do jednego systemu Asseco EBP mając na myśli zarówno kontekst indywidualny (CBP), mikro (EBP) oraz firmowy (EBP).

## 3. Kanały dostępu
- Zakres dokumentacji obejmuje bankowość internetową i mobilną.
- Wymagania zmian muszą wskazywać, czy dotyczą kanału desktop, mobile, czy obu kanałów.

## 4. Uprawnienia i sterowanie dostępem
- Dla klienta firmowego (EBP) dostęp do funkcji jest kontrolowany uprawnieniami.
- Uprawnienia są nadawane per obszar funkcjonalny i wpływają na widoczność/opcje w BE.

## 5. Integracje i granice odpowiedzialności
- Integracje z systemami zewnętrznymi muszą respektować kontekst klienta (detal/mikro/korpo) oraz model uprawnień.
- W przypadku konfliktu między skrótem AS-IS a dokumentacją szczegółową, należy odwołać się do sekcji źródeł i zgłosić konflikt.
- Asseco CB - system transakcyjny, master data. Opis systemu Asseco CB oraz zakres współpracy z BE został zawarty w /doc/CB/**

## 6. Ograniczenia
- Nie dopuszcza się dopowiadania zachowań systemu bez potwierdzenia w źródłach.
- Braki informacyjne należy oznaczać jako `OPEN-QUESTION-###`.

## 7. Źródła referencyjne (do weryfikacji)
- `doc/EBP/**`
- `doc/CBP/**`
- `doc/BO/BackofficeUserGuide-pl_basic.adoc`
- 'doc/CB/**'
