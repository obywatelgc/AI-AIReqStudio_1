# AI-AIReqStudio_1

Framework dokumentacyjny do generowania i utrzymywania specyfikacji wymagan na podstawie zrodel w `src/` i `doc/`.

## Quick start (PowerShell, Windows)

1. Przejdz do katalogu projektu:

```powershell
cd C:\AI\AI-AIReqStudio_1\AI-AIReqStudio_1
```

2. Utworz i aktywuj srodowisko wirtualne:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Zainstaluj zaleznosci:

```powershell
python -m pip install -U pip
pip install -r requirements.txt
```

4. Uzupelnij dane wejsciowe i parametry projektu:

```powershell
# wymagania klienta
notepad .\src\wymagania.md

# parametry projektu
notepad .\project-parameters.md
```

5. Pracuj na aktywnym szablonie:

```powershell
notepad .\spec\10-spw.md
```

## Dostepne narzedzia

Repo zawiera narzedzie:

- `tools/render-placeholders.ps1`

Przykladowe uruchomienia:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render-placeholders.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render-placeholders.ps1 -InPlace
```

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\render-placeholders.ps1 `
  -ParametersPath ".\project-parameters.md" `
  -InputPaths @("spec","src","doc")
```


