Param(
  [switch]$NoDemo  # rulează doar testele (fără main.py) dacă adaugi -NoDemo
)

$ErrorActionPreference = 'Stop'

function Get-PyCmd {
  try { & py -3.12 --version *> $null; return 'py -3.12' } catch {}
  try { & py --version *> $null; return 'py' } catch {}
  return 'python'
}

$py = Get-PyCmd
Write-Host "Using Python launcher: $py"

# creează venv dacă lipsește
if (!(Test-Path ".\.venv")) {
  Write-Host "Creating virtual environment (.venv)..."
  & $py -m venv .venv
}

# încearcă să activezi venv
$activate = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $activate) {
  try {
    . $activate
  } catch {
    Write-Warning "Activation policy blocked. Run this command first in your terminal:"
    Write-Host "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
    throw
  }
} else {
  throw "Virtual environment activation script not found at $activate"
}

Write-Host "Upgrading pip and installing dependencies..."
python -m pip install -U pip
if (Test-Path ".\requirements.txt") {
  pip install -r .\requirements.txt
} else {
  pip install -U pytest pytest-cov
}

# setează PYTHONPATH pentru sesiune
$env:PYTHONPATH = (Get-Location).Path

Write-Host "Running tests..."
python -m pytest

if (-not $NoDemo) {
  Write-Host "`nRunning demo (main.py)..."
  python .\main.py
}

Write-Host "`nAll done ✅"
