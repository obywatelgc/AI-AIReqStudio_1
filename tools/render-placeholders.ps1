param(
  [Parameter(Mandatory = $false)]
  [string]$ParametersPath = "project-parameters.md",

  [Parameter(Mandatory = $false)]
  [string[]]$InputPaths = @("spec", "src", "doc", "opis.md", "project-prompt.md"),

  [Parameter(Mandatory = $false)]
  [string]$OutDir = "rendered",

  [Parameter(Mandatory = $false)]
  [switch]$InPlace
)

$ErrorActionPreference = "Stop"

function Get-ProjectParameters {
  param([Parameter(Mandatory = $true)][string]$Path)

  if (-not (Test-Path -LiteralPath $Path)) {
    throw "Nie znaleziono pliku parametrow: $Path"
  }

  $lines = Get-Content -LiteralPath $Path -Encoding utf8
  $map = @{}

  foreach ($line in $lines) {
    $matches = [regex]::Matches($line, '`([^`]+)`')
    if ($matches.Count -ge 2) {
      $name = $matches[0].Groups[1].Value
      $value = $matches[1].Groups[1].Value
      if ($name -match '^[A-Z0-9_]+$') {
        $map[$name] = $value
      }
    }
  }

  if ($map.Count -eq 0) {
    throw "Nie znaleziono parametrow w formacie: - **... (`VAR`):** `WARTOSC` w pliku: $Path"
  }

  return $map
}

function Resolve-InputFiles {
  param([Parameter(Mandatory = $true)][string[]]$Paths)

  $extensions = @(".md", ".adoc", ".txt")
  $files = New-Object System.Collections.Generic.List[string]

  foreach ($p in $Paths) {
    if (Test-Path -LiteralPath $p -PathType Container) {
      Get-ChildItem -LiteralPath $p -Recurse -File |
        Where-Object { $extensions -contains $_.Extension.ToLowerInvariant() } |
        ForEach-Object { [void]$files.Add($_.FullName) }
      continue
    }

    if (Test-Path -LiteralPath $p -PathType Leaf) {
      [void]$files.Add((Resolve-Path -LiteralPath $p).Path)
      continue
    }

    throw "Nie znaleziono sciezki wejsciowej: $p"
  }

  return $files
}

function Apply-Placeholders {
  param(
    [Parameter(Mandatory = $true)][string]$Content,
    [Parameter(Mandatory = $true)][hashtable]$Parameters
  )

  $result = $Content
  foreach ($key in $Parameters.Keys) {
    $value = [string]$Parameters[$key]
    $pattern = '\{\{\s*' + [regex]::Escape($key) + '\s*\}\}'
    $result = [regex]::Replace($result, $pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $value })
  }
  return $result
}

$parameters = Get-ProjectParameters -Path $ParametersPath
$files = Resolve-InputFiles -Paths $InputPaths

foreach ($file in $files) {
  if ((Split-Path -Leaf $file) -ieq (Split-Path -Leaf $ParametersPath)) {
    continue
  }

  $original = Get-Content -LiteralPath $file -Raw -Encoding utf8
  $rendered = Apply-Placeholders -Content $original -Parameters $parameters

  if ($InPlace) {
    if ($rendered -ne $original) {
      Set-Content -LiteralPath $file -Value $rendered -Encoding utf8
    }
    continue
  }

  $relative = Resolve-Path -LiteralPath $file | ForEach-Object {
    $_.Path.Substring((Resolve-Path -LiteralPath ".").Path.Length).TrimStart('\','/')
  }
  $outPath = Join-Path $OutDir $relative
  $outFolder = Split-Path -Parent $outPath
  New-Item -ItemType Directory -Force -Path $outFolder | Out-Null
  Set-Content -LiteralPath $outPath -Value $rendered -Encoding utf8
}

if ($InPlace) {
  "OK: podstawiono placeholdery w plikach (tryb in-place)."
} else {
  "OK: wygenerowano pliki w katalogu: $OutDir"
}
