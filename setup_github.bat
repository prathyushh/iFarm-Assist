@echo off
echo ===================================================
echo   iFarmAssist - GitHub Setup Script
echo ===================================================
echo.
echo 1. Adding all project files to Git...
git add .
echo.

echo 2. Committing changes...
git commit -m "Phase 4 Complete: Mobile App + Backend + RAG Engine"
echo.

echo 3. Status Check:
git status

echo.
echo ===================================================
echo   Local setup complete!
echo   Now follow the instructions in the chat to PUSH.
echo ===================================================
pause
