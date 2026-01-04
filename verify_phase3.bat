@echo off
echo ==========================================
echo   iFarmAssist Phase 3 Verification Tool
echo ==========================================

echo [1/3] Starting Backend Server in a new window...
start "iFarmAssist Backend" cmd /k "backend\venv\Scripts\python -m backend.main"

echo [2/3] Waiting 15 seconds for server to initialize...
timeout /t 15

echo [3/3] Running Integration Test (Register -> Login -> RAG Query)...
backend\venv\Scripts\python backend\test_pipeline.py

echo.
echo ==========================================
echo If you see "Query Success" above, Phase 3 is COMPLETE.
echo You can check the server window for detailed logs.
echo ==========================================
pause
