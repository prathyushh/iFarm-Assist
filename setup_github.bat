@echo off
echo ===================================================
echo   iFarmAssist - GitHub Auto-Uploader
echo ===================================================
echo.
echo This script will initialize Git and prepare your files.
echo (Your secrets are ALREADY hidden by .gitignore)
echo.

:: Initialize Git
echo 1. Initializing Git...
git init

:: Add Files
echo 2. Adding files (this may take a moment)...
git add .

:: Commit
echo 3. Committing files...
git commit -m "Initial Commit: iFarmAssist Phase 1-4 Complete"

:: Instructions for Remote
echo.
echo ===================================================
echo   ALMOST DONE!
echo ===================================================
echo Now you need to link this to your GitHub account.
echo.
echo OPTION A: If you have GitHub CLI installed (Recommended):
echo    Run: gh repo create iFarmAssist --public --source=. --remote=origin --push
echo.
echo OPTION B: Manual Way:
echo    1. Go to github.com and create a new repository named "iFarmAssist"
echo    2. Copy the URL (e.g., https://github.com/YourName/iFarmAssist.git)
echo    3. Run: git remote add origin ^<PASTE_URL_HERE^>
echo    4. Run: git push -u origin master
echo.
pause
