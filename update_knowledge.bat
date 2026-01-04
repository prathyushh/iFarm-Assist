@echo off
echo ===================================================
echo   iFarmAssist - Knowledge Base Updater
echo ===================================================
echo.
echo 1. Ensure you have pasted your new PDF into: project_root/data/
echo 2. This script will now READ the PDFs and UPDATE the AI Brain.
echo.
pause

echo Activating Virtual Environment...
call backend\venv\Scripts\activate

echo Running Ingestion Script...
python backend/services/ingest.py

echo.
echo ===================================================
echo   Done! The AI has learned the new documents.
echo ===================================================
pause
