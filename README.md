# AI-AIReqStudio_1

Framework dokumentacyjny do generowania i utrzymywania specyfikacji wymagan na podstawie zrodel w `src/` i `doc_basic/`.

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

4. Uruchom parser wymagan:

```powershell
python .\tools\parse_requirements.py
```

## Przydatne komendy

Uruchomienie parsera z niestandardowymi sciezkami:

```powershell
python .\tools\parse_requirements.py `
  --input "src/wymagania.md" `
  --output "spec/_trace/requirements_index.json" `
  --work-items-dir "spec/_trace/work_items" `
  --report "spec/_trace/requirements_parse_report.md"
```

Uruchomienie z bledem procesu, gdy parser wykryje bledy:

```powershell
python .\tools\parse_requirements.py --fail-on-error
```

## Wyjscie parsera

- `spec/_trace/requirements_index.json`
- `spec/_trace/work_items/*.md`
- `spec/_trace/requirements_parse_report.md`

