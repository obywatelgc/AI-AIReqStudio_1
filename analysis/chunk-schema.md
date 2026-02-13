# Chunk Schema (Przyklad)

Ten plik opisuje minimalny format "atomu wiedzy" (chunk), ktory mozesz
generowac z dokumentow w `./doc/*.md` i `./src/*.md`.

## Zasady

1. Jeden chunk = jedno zagadnienie.
2. Kazdy chunk musi miec `source_file` i `section`.
3. Gdy nie da sie ustalic wartosci, wpisz `N/A`.

## Pola

- `chunk_id`: unikalny identyfikator, np. `CH-0001`
- `text`: krotki fragment wiedzy (1 temat)
- `service`: serwis/modul odpowiedzialny za funkcje
- `api`: endpoint lub nazwa operacji API
- `event`: zdarzenie domenowe/integracyjne
- `data_object`: obiekt danych (DTO/encja/token)
- `security`: mechanizm bezpieczenstwa lub ograniczenia
- `source_file`: plik zrodlowy
- `section`: sekcja w pliku zrodlowym

## Przykladowy rekord JSON

```json
{
  "chunk_id": "CH-0001",
  "text": "Operacja customerContext pobiera kontekst klienta na potrzeby SSO i zwraca accessToken.",
  "service": "CashDirector-BE Integration",
  "api": "customerContext",
  "event": "N/A",
  "data_object": "ssoToken, accessToken, externalCompanyId, externalUserId",
  "security": "Jednorazowy krotkoterminowy ssoToken",
  "source_file": "doc/banki-api-uslugi-banku.md",
  "section": "customerContext"
}
```
