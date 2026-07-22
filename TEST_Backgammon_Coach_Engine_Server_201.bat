@echo off
setlocal
cd /d "%~dp0.."
if not exist engine_server\.venv\Scripts\python.exe (
  echo ERROR: Runtime not installed.
  exit /b 1
)
engine_server\.venv\Scripts\python.exe tests\test_payload_validation.py
echo.
powershell -NoProfile -Command "try { $r=Invoke-RestMethod http://127.0.0.1:8765/health; $r | ConvertTo-Json -Depth 8 } catch { Write-Host 'Server health test unavailable:' $_.Exception.Message; exit 2 }"
pause
