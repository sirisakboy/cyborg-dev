@echo off
echo Starting CYBORG NEXUS v3.5...
echo.
python main.py
if errorlevel 1 (
    echo.
    echo Application exited with error.
    echo Check that:
    echo 1. Python dependencies are installed (pip install -r requirements.txt)
    echo 2. TGPT is installed or you're using alternative providers
    echo 3. API keys are set in .env file (if using paid providers)
    echo.
    pause
)