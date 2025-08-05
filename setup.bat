@echo off
setlocal EnableDelayedExpansion

title Technical ATS Resume Expert - Setup & Launch
color 0A

echo.
echo ================================================================
echo                🚀 Technical ATS Resume Expert
echo                    Setup and Launch Tool
echo ================================================================
echo.

REM Check if Python is installed
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)
echo ✅ Python found

REM Check if virtual environment exists, create if not
echo.
echo [2/5] Setting up virtual environment...
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo.
echo [3/5] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment activated

REM Install/upgrade dependencies
echo.
echo [4/5] Installing dependencies...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    echo.
    echo Trying with additional flags...
    pip install --upgrade --force-reinstall -r requirements.txt
    if errorlevel 1 (
        echo ❌ Still failed. Please check your internet connection and try again.
        pause
        exit /b 1
    )
)
echo ✅ Dependencies installed successfully

REM Check for API key
echo.
echo [5/5] Checking API key configuration...
if not exist ".env" (
    echo ⚠️  No .env file found. Creating from template...
    copy .env.example .env >nul 2>&1
    echo.
    echo 🔑 Please edit .env file and add your Google Gemini API key
    echo    Get your API key from: https://makersuite.google.com/app/apikey
    echo.
    set /p api_key="Enter your Google Gemini API key (or press Enter to skip): "
    if not "!api_key!"=="" (
        echo GOOGLE_API_KEY=!api_key!> .env.tmp
        echo # Application Configuration>> .env.tmp
        echo APP_NAME=Technical ATS Resume Expert>> .env.tmp
        echo DEBUG_MODE=False>> .env.tmp
        echo LOG_LEVEL=INFO>> .env.tmp
        echo # File Upload Limits>> .env.tmp
        echo MAX_FILE_SIZE_MB=10>> .env.tmp
        echo SUPPORTED_FILE_TYPES=pdf>> .env.tmp
        move .env.tmp .env >nul 2>&1
        echo ✅ API key configured
    ) else (
        echo ⚠️  API key not configured. You'll need to edit .env file manually.
    )
) else (
    echo ✅ .env file exists
)

REM Create logs directory if it doesn't exist
if not exist "logs" mkdir logs

echo.
echo ================================================================
echo                     🎉 Setup Complete!
echo ================================================================
echo.

REM Test the application first
echo Testing application...
python -c "import sys; sys.path.append('src'); from src.config import Config; print('✅ Application ready')" 2>nul
if errorlevel 1 (
    echo ⚠️  There might be some issues. Attempting to start anyway...
)

echo.
echo Starting Technical ATS Resume Expert...
echo.
echo 📱 The application will open in your default browser
echo 🌐 URL: http://localhost:8501
echo 🛑 Press Ctrl+C in this window to stop the application
echo.

REM Launch the application
streamlit run app.py --server.headless=true --server.port=8501 --browser.gatherUsageStats=false

echo.
echo 👋 Application stopped. Thank you for using Technical ATS Resume Expert!
pause
