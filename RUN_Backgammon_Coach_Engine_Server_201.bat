@echo off
setlocal
cd /d "%~dp0.."
if not exist engine_server\.venv\Scripts\python.exe (
  echo ERROR: Runtime not installed.
  echo Run automation\INSTALL_Backgammon_Coach_Engine_Server_201.bat first.
  pause
  exit /b 1
)
echo Starting Backgammon Coach Engine Server v2.0.1...
echo Configuration: engine_server\configuration\engine_config.json
echo Health URL: http://127.0.0.1:8765/health
echo.
engine_server\.venv\Scripts\python.exe engine_server\run_waitress.py
