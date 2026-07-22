@echo off
setlocal
cd /d "%~dp0.."
echo Backgammon Coach Grandmaster Engine Server v2.0.1
echo Installing Python dependencies only. GNU Backgammon is not bundled.
echo =====================================================================
where py >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python launcher "py" was not found.
  exit /b 1
)
py -3 -m venv engine_server\.venv
if errorlevel 1 exit /b 1
call engine_server\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r engine_server\requirements.txt
if errorlevel 1 exit /b 1
echo.
echo INSTALL_COMPLETE
echo Next: run automation\DIAGNOSE_GNU_Backgammon_Installation_201.bat
