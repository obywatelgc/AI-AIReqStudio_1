# Opis projektu
ZbudowaĹ‚em workspace w Visual Studio Code, ktĂłrego zadaniem jest generowanie specyfikacji wymagaĹ„ na podstawie materiaĹ‚Ăłw (wymagaĹ„) klienta oraz dokumentacji systemĂłw informatycznych.
NarzÄ™dzie bÄ™dzie wykorzystywaĹ‚o model LLM (GPT) oraz rozszerzenie COdex. Specyfikacja bÄ™dzie posiadaĹ‚o okreĹ›lonÄ… strukturÄ™ - opisanÄ… w /spec/10-spw.md

ObsĹ‚uga narzÄ™dzie bÄ™dzie realizowna przez wykonywanie odpowiednich promptĂłw w codex i praca na plikach projektu.

ChciaĹ‚bym w pliku project-parameters.md zawrzeÄ‡ najwaĹĽniejsze parametry projektu np. 
-nazwÄ™ projektu, 
- nazwÄ™ klienta 
- Styl i JÄ™zyk Generowania dokumentĂłe

Dodatkowo w pliku (project-prompt.md) bÄ™dzie gĹ‚owny prompt ktĂłry okreĹ›la sposĂłb pracy LLM.

Jak to obsĹ‚uĹĽyÄ‡, jak z tym pracowaÄ‡ w VSC i Codex?

# Struktura katalogĂłw
/doc - dokumetnacja systemĂłw ktĂłrych dotyczy analiza w formacie MD
    /cpb - dokumentacja CBP w podzile na obszary /Przelewy, Rachunki itd. w soobnych plikach
    /ebp
/scr - wymagania Banku w formacie 
    /Bank - pliki z Banku np. PDF, DOCX itd (format inny niĹĽ MD)
    /MD - wymagania banku w formacie tesktowym MD
/spec - dokument specyfikacji wymagaĹ„

Utrzymanie kontroli nad AI
- JeĹ›li informacja jest ze ĹşrĂłdeĹ‚ â†’ AI dopisuje znacznik Source: (np. plik/sekcja)
- JeĹ›li AI nie ma podstawy â†’ musi oznaczyÄ‡ ASSUMPTION albo OPEN-QUESTION
- Zakaz: AI nie moĹĽe tworzyÄ‡ endpointĂłw, pĂłl, statusĂłw â€žz gĹ‚owyâ€ť

## Implementacja w repo (MVP)
1. WejĹ›cie:
- wrzuÄ‡ materiaĹ‚y klienta do `scr/Bank` i (opcjonalnie) wersje markdown do `scr/MD`
Opcje dzialania narzedzia
1. Tryb konfiguracji: wczytanie `project-parameters.md` i `project-prompt.md`, potwierdzenie projektu, klienta, jezyka, stylu i zakresu.
2. Tryb generowania: tworzenie tresci specyfikacji na podstawie plikow z `doc/` i `scr/` zgodnie ze struktura `spec/00-outline.md`.
3. Tryb walidacji: sprawdzenie spojnosci dokumentu, unikalnosci ID, terminologii oraz wypisanie brakow i pytan otwartych.
4. Tryb aktualizacji: modyfikacja istniejacych rozdzialow specyfikacji po doslaniu nowych materialow z zachowaniem historii zmian.

- wrzuÄ‡ dokumentacjÄ™ systemowÄ… do `doc/`
2. Konfiguracja:
- uzupeĹ‚nij `project-parameters.md` (projekt, klient, jÄ™zyk, styl, zakres)
- trzymaj staĹ‚e reguĹ‚y pracy w `project-prompt.md`
3. Generowanie:
- najpierw generuj szkic i plan sekcji do `spec/00-outline.md`
- potem uzupeĹ‚niaj wĹ‚aĹ›ciwÄ… specyfikacjÄ™ w `spec/10-spw.md`
4. Kontrola jakoĹ›ci:
- kaĹĽdy punkt musi mieÄ‡ ĹşrĂłdĹ‚o lub znacznik `ASSUMPTION`/`OPEN-QUESTION`
- wymagania muszÄ… mieÄ‡ unikalne ID i kryteria akceptacji (Given/When/Then)

# Praca z narzÄ™dziem

1. UzupeĹ‚niasz tylko parametry w project-parameters.md (nazwa projektu, klient, jÄ™zyk, styl, Ĺ›cieĹĽki).
2. Trzymasz staĹ‚y â€žsilnikâ€ť w project-prompt.md (bez danych klienta).
3. W kaĹĽdej sesji odpalasz prompt startowy do Codex:

Propmpty:
```markdown
Pracujemy w tym repo. Najpierw wczytaj:
- project-parameters.md
- project-prompt.md
- spec/00-outline.md
- pliki ĹşrĂłdĹ‚owe z doc/

NastÄ™pnie potwierdĹş: projekt, klient, jÄ™zyk, styl, zakres.
Nie generuj treĹ›ci, dopĂłki nie potwierdzisz konfiguracji.
```

4. Potem prompt zadaniowy, np. dla rozdziaĹ‚u:
```
Na podstawie doc/* uzupeĹ‚nij spec/10-spw.md.
Wymagania:
- ID: RQ-ACT-###
- kaĹĽde wymaganie: opis, uzasadnienie, AC (Given/When/Then)
- sekcje: ObsĹ‚uga bĹ‚Ä™dĂłw i Zagadnienia otwarte muszÄ… pozostaÄ‡
- bez domysĹ‚Ăłw: brak danych -> OPEN-QUESTION-###
```

5. Na koĹ„cu prompt walidacyjny:
```
ZrĂłb review spĂłjnoĹ›ci:
- zgodnoĹ›Ä‡ z spec/00-outline.md
- unikalnoĹ›Ä‡ ID wymagaĹ„
- spĂłjnoĹ›Ä‡ terminologii
- lista brakĂłw i pytaĹ„ otwartych
```


##################################### POPRZEDNI OPIS


# Minimalny â€žstandard promptĂłwâ€ť do pracy w czacie w VSC
Ĺ»eby praca byĹ‚a powtarzalna, przygotuj sobie 6â€“8 gotowych komend (snippetĂłw). PrzykĹ‚ady (do uĹĽywania na zaznaczeniu albo pliku):

* â€žZrĂłb wymagania z materiaĹ‚Ăłw od Kkientaâ€ť
â€žNa podstawie /scr/ zaproponuj wymagania w formacie RQ-###. Dodaj kryteria akceptacji i przypadki negatywne.â€ť

* â€žUtestowalnijâ€ť
â€žPrzerĂłb wymagania na testowalne. KaĹĽde wymaganie ma mieÄ‡: warunek, dziaĹ‚anie, wynik. UsuĹ„ ogĂłlniki.â€ť

* â€žWykryj lukiâ€ť
â€žWskaĹĽ brakujÄ…ce wymagania: bezpieczeĹ„stwo, audyt, bĹ‚Ä™dy, retry, idempotency, zgodnoĹ›Ä‡ danych.â€ť

* â€žZrĂłb macierz Ĺ›ledzeniaâ€ť
â€žZrĂłb tabelÄ™: ID wymagania â†’ ĹşrĂłdĹ‚o â†’ test/AC â†’ zaleĹĽnoĹ›ci.â€ť

* â€žWersja na reviewâ€ť
â€žPrzeredaguj pod czytelnika biznesowego, bez utraty jednoznacznoĹ›ci.â€ť

* â€žLista pytaĹ„ otwartychâ€ť
â€žWypisz decyzje wymagane od biznesu/architekta + konsekwencje wyborĂłw.â€ť


TODO

TODO - skrypt ktĂłry dzieli caĹ‚Ä… dokumentacjÄ™ na obszary
