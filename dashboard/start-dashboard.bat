@echo off
REM Windows: double-click. Starts the dashboard and opens it in Microsoft Edge.
cd /d "%~dp0"
set PORT=7777
start "" cmd /c "timeout /t 2 >nul & start msedge http://localhost:%PORT%"
where py >nul 2>nul && (py server.py --port %PORT% %*) || (python server.py --port %PORT% %*)
pause
