@echo off
setlocal
cd /d "%~dp0.."
if exist engine_server\.venv\Scripts\python.exe (
  engine_server\.venv\Scripts\python.exe engine_server\diagnose_installation.py
) else (
  py -3 engine_server\diagnose_installation.py
)
pause
