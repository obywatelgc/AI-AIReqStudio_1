<!-- AI-CONSTRAINTS
Zakres: Uzupełnienie rozdziału „Aktywacja usługi CashDirector” na podstawie dokumentacji systemu BE z `doc/*`.
Format: RQ-ACT-###
Źródła: 
    Wymagania klienta: /src/*, 
    Dokumentacja systemu: /doc/*
    Parametry projektu: /project-parameters.md
-->

# Aktywacja usługi CashDirector

## 1.1 Cel biznesowy projektu
Celem rozwiązania jest udostępnienie w systemie BE (bankowości elektronicznej) możliwości aktywacji usługi CashDirector (system księgowy) dla klientów firmowych, z uwzględnieniem mechanizmów pracy w kontekstach, dostępu do funkcjonalności z poziomu pulpitu (miniaplikacje/widżety) oraz zarządzania uprawnieniami użytkowników.

## 1.2 Wymagania klienta
Na podstawie `doc/*` nie zidentyfikowano wymagań klienta specyficznych dla aktywacji usługi CashDirector. Wymagania eksperckie domykające kwestie procesu aktywacji zostały ujęte w wymaganiach RQ-ACT-007–RQ-ACT-011.

---

## 3. Wymagania szczegółowe
### RQ-ACT-001: Dostęp do aktywacji w kontekście firmowym
**Opis:** System BE musi udostępniać możliwość rozpoczęcia procesu aktywacji usługi CashDirector wyłącznie w kontekście firmowym użytkownika (mikro i korporacyjny).

**Uzasadnienie:** Dokumentacja BE opisuje działanie systemu w wielu kontekstach (indywidualny oraz firmowy, z rozróżnieniem obszarów roboczych) oraz przełączanie kontekstu w trakcie pracy.

**AC:**
- Given Użytkownik jest zalogowany i posiada aktywny kontekst firmowy
- When Użytkownik przechodzi do punktu wejścia procesu aktywacji usługi CashDirector
- Then system umożliwia rozpoczęcie procesu aktywacji
- Given Użytkownik jest zalogowany w kontekście indywidualnym lub nie posiada aktywnego kontekstu firmowego
- When Użytkownik próbuje rozpocząć proces aktywacji usługi CashDirector
- Then system nie udostępnia tej możliwości i prezentuje informację o braku dostępności w bieżącym kontekście
- Given Użytkownik posiada dostęp do kontekstu firmowego mikro lub korporacyjnego
- When Użytkownik loguje się do BE i wybiera kontekst firmowy (mikro albo korporacyjny)
- Then funkcjonalność aktywacji usługi CashDirector jest dostępna w wybranym kontekście firmowym (mikro albo korporacyjnym)

---

### RQ-ACT-002: Punkt wejścia z poziomu pulpitu
**Opis:** System BE musi udostępniać punkt wejścia procesu aktywacji usługi CashDirector z poziomu pulpitu (obszar z miniaplikacjami/widżetami) dla użytkowników, dla których funkcja jest dostępna.

**Uzasadnienie:** Dokumentacja BE wskazuje, że po zalogowaniu użytkownik widzi pulpit z miniaplikacjami, a dostępność miniaplikacji zależy od kontekstu, w jakim użytkownik jest zalogowany.

**AC:**
- Given Użytkownik jest zalogowany w kontekście firmowym
- When system prezentuje pulpit użytkownika
- Then system prezentuje punkt wejścia do aktywacji CashDirector, jeżeli funkcjonalność jest dostępna dla tego użytkownika/kontekstu
- Given Użytkownik jest zalogowany w kontekście firmowym
- When Użytkownik wybiera punkt wejścia do aktywacji CashDirector na pulpicie
- Then system przechodzi do procesu aktywacji usługi CashDirector

---

### RQ-ACT-003: Kontrola uprawnień do funkcjonalności
**Opis:** System BE musi kontrolować dostęp do punktu wejścia aktywacji usługi CashDirector na podstawie uprawnień funkcjonalnych użytkownika w kontekście firmowym.

**Uzasadnienie:** Dokumentacja BE opisuje zarządzanie uprawnieniami użytkowników (w tym uprawnienia funkcjonalne) przez administratora klienta w kontekście firmowym oraz wpływ uprawnień na widoczność miniaplikacji/widżetów.

**AC:**
- Given Użytkownik nie posiada dedykowanego uprawnienia funkcjonalnego „CashDirector” (miniaplikacja: Inne → CashDirector)
- When system prezentuje pulpit w kontekście firmowym
- Then punkt wejścia aktywacji CashDirector jest ukryty lub nieaktywny
- Given Użytkownik posiada dedykowane uprawnienie funkcjonalne „CashDirector” (miniaplikacja: Inne → CashDirector)
- When system prezentuje pulpit w kontekście firmowym
- Then punkt wejścia aktywacji CashDirector jest widoczny i umożliwia przejście do procesu aktywacji

---

### RQ-ACT-004: Informacja o braku dedykowanego produktu/usługi
**Opis:** Jeżeli w danym kontekście użytkownika usługa CashDirector nie jest dostępna, system BE musi zaprezentować na pulpicie stosowną informację o braku dedykowanego produktu/usługi zamiast punktu wejścia do aktywacji.

**Uzasadnienie:** Dokumentacja BE opisuje, że w przypadku braku dedykowanego produktu na widżecie prezentowana jest stosowna informacja.

**AC:**
- Given Użytkownik jest zalogowany w kontekście firmowym
- And usługa CashDirector nie jest dostępna dla tego kontekstu
- When system prezentuje pulpit użytkownika
- Then system prezentuje informację o braku dostępności usługi (braku dedykowanego produktu/usługi) zamiast punktu wejścia do aktywacji

---

### RQ-ACT-005: Rejestracja akcji w Rejestrze zdarzeń
**Opis:** System BE musi rejestrować rozpoczęcie procesu aktywacji usługi CashDirector jako akcję użytkownika możliwą do przeglądania w Rejestrze zdarzeń.

**Uzasadnienie:** Dokumentacja BE opisuje funkcję _Ustawienia → Rejestr zdarzeń_ jako przegląd akcji wykonanych przez użytkownika w danym kanale, z możliwością filtrowania m.in. po kanale oraz typie zdarzenia.

**AC:**
- Given Użytkownik jest zalogowany i rozpoczyna proces aktywacji CashDirector
- When proces aktywacji zostaje uruchomiony
- Then system zapisuje zdarzenie w Rejestrze zdarzeń użytkownika dla właściwego kanału (np. WWW/MOB) jako nowy typ zdarzenia „Aktywacja usługi CashDirector”
- Given Użytkownik przechodzi do _Ustawienia → Rejestr zdarzeń_
- When filtruje zdarzenia w zakresie obejmującym moment uruchomienia aktywacji
- Then system prezentuje zdarzenie odpowiadające uruchomieniu aktywacji CashDirector

---

### RQ-ACT-006: Zachowanie przy wygaśnięciu sesji
**Opis:** Jeżeli sesja użytkownika w systemie BE wygaśnie w trakcie procesu aktywacji usługi CashDirector, system musi przerwać proces aktywacji i wymagać ponownego zalogowania, zgodnie z ogólnymi zasadami zakończenia sesji.

**Uzasadnienie:** Dokumentacja BE wskazuje, że system automatycznie kończy sesję użytkownika po okresie bezczynności, a po upływie czasu trwania sesji wybranie dowolnej akcji powoduje zaprezentowanie strony wylogowania.

**AC:**
- Given Użytkownik jest w trakcie procesu aktywacji CashDirector
- And sesja użytkownika w systemie BE wygasa
- When Użytkownik wykonuje dowolną akcję w ramach procesu aktywacji
- Then system prezentuje stronę wylogowania i nie kontynuuje procesu aktywacji bez ponownego zalogowania

---

### RQ-ACT-007: Rozpoznanie statusu aktywacji usługi
**Opis:** System BE musi rozpoznawać status aktywacji usługi CashDirector dla firmy w bieżącym kontekście firmowym i wykorzystywać go do sterowania dalszym przebiegiem procesu.

**Uzasadnienie:** Proces aktywacji musi rozróżniać co najmniej dwa stany: usługa nieaktywna (użytkownik przechodzi przez aktywację) oraz usługa aktywna (użytkownik przechodzi do korzystania z usługi CashDirector).

**AC:**
- Given Użytkownik jest zalogowany w kontekście firmowym
- When Użytkownik wchodzi w obszar CashDirector w BE
- Then system ustala status aktywacji usługi CashDirector dla bieżącej firmy
- Given status aktywacji usługi CashDirector jest „nieaktywna”
- When system obsługuje wejście użytkownika w obszar CashDirector
- Then system prezentuje ekran aktywacji usługi
- Given status aktywacji usługi CashDirector jest „aktywna”
- When system obsługuje wejście użytkownika w obszar CashDirector
- Then system przekierowuje użytkownika do CashDirector

---

### RQ-ACT-008: Udostępnienie punktu wejścia „CashDirector” w BE
**Opis:** System BE musi udostępnić w interfejsie użytkownika punkt wejścia do obsługi usługi CashDirector (miniaplikacja: Inne → CashDirector), dostępny w kontekście firmowym zgodnie z uprawnieniami.

**Uzasadnienie:** Użytkownik musi posiadać jednoznaczny, stały punkt wejścia do aktywacji lub wejścia do usługi CashDirector.

**AC:**
- Given Użytkownik jest zalogowany w kontekście firmowym
- And Użytkownik posiada uprawnienie „CashDirector” (miniaplikacja: Inne → CashDirector)
- When system prezentuje pulpit / listę miniaplikacji
- Then system prezentuje punkt wejścia „CashDirector”
- Given Użytkownik wybiera punkt wejścia „CashDirector”
- When system rozpoczyna obsługę żądania
- Then system realizuje logikę zależną od statusu aktywacji usługi (zgodnie z RQ-ACT-007)

---

### RQ-ACT-009: Prezentacja zgód/regulaminów/umów oraz rejestracja akceptacji
**Opis:** System BE musi umożliwiać prezentację zgód, regulaminów i umów wymaganych do aktywacji usługi CashDirector oraz rejestrować akceptację użytkownika; dodatkowo system musi udostępnić pliki wskazane przez Bank do pobrania.

**Uzasadnienie:** Aktywacja usługi wymaga przedstawienia treści formalnych oraz rejestracji akceptacji. W ramach procesu nie zakłada się generowania, podpisywania ani wysyłania umów po stronie BE.

**AC:**
- Given Użytkownik jest na ekranie aktywacji usługi CashDirector
- When system prezentuje wymagane zgody/regulaminy/umowy
- Then system umożliwia użytkownikowi zapoznanie się z treściami oraz pobranie plików wskazanych przez Bank
- Given Użytkownik nie zaakceptował wszystkich wymaganych zgód/regulaminów/umów
- When Użytkownik próbuje kontynuować aktywację usługi
- Then system blokuje przejście do kolejnego kroku i prezentuje informację o brakujących akceptacjach
- Given Użytkownik zaakceptował wszystkie wymagane zgody/regulaminy/umowy
- When Użytkownik zatwierdza aktywację
- Then system rejestruje akceptację w BE

---

### RQ-ACT-010: Rejestracja firmy i użytkownika w CashDirector
**Opis:** System BE musi przekazać do CashDirector dane identyfikacyjne firmy oraz użytkownika inicjującego aktywację w celu rejestracji usługi.

**Uzasadnienie:** Aby usługa CashDirector była możliwa do uruchomienia i powiązania z klientem, wymagane jest utworzenie/powiązanie rekordów firmy i użytkownika w systemie zewnętrznym.

**AC:**
- Given Użytkownik znajduje się na etapie finalizacji aktywacji usługi CashDirector
- And Użytkownik zaakceptował wymagane zgody/regulaminy/umowy
- When system BE uruchamia rejestrację usługi
- Then system przekazuje do CashDirector dane identyfikacyjne firmy oraz użytkownika

---

### RQ-ACT-011: Obsługa błędu aktywacji
**Opis:** System BE musi przerwać proces aktywacji i zaprezentować użytkownikowi komunikat o błędzie, jeżeli rejestracja usługi w CashDirector zakończy się niepowodzeniem.

**Uzasadnienie:** Użytkownik musi otrzymać jednoznaczną informację o niepowodzeniu aktywacji, aby mógł podjąć dalsze kroki (ponowienie, kontakt z bankiem).

**AC:**
- Given Użytkownik jest w trakcie procesu aktywacji usługi CashDirector
- When rejestracja usługi w CashDirector kończy się niepowodzeniem
- Then system przerywa proces aktywacji
- And system prezentuje użytkownikowi komunikat o błędzie aktywacji

---

# 7. Obsługa błędów
(Ta sekcja MUSI istnieć)

- Brak dostępu do aktywacji w bieżącym kontekście (np. kontekst indywidualny / nieaktywny kontekst firmowy).
- Brak uprawnień funkcjonalnych użytkownika do uruchomienia aktywacji.
- Brak dostępności usługi (brak „dedykowanego produktu/usługi”) w danym kontekście.
- Brak akceptacji wszystkich wymaganych zgód/regulaminów/umów dla aktywacji usługi.
- Niepowodzenie rejestracji usługi w CashDirector (błąd aktywacji).
- Wygaśnięcie sesji użytkownika w trakcie aktywacji.

---

# 8. Zagadnienia otwarte
- Brak.
