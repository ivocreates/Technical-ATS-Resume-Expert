@echo off
title Technical ATS Resume Expert

echo ================================================================
echo            🚀 Technical ATS Resume Expert
echo ================================================================
echo.

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
) else (
    echo ⚠️  Virtual environment not found. Run setup.bat first.
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    echo ⚠️  .env file not found. Please configure your API key first.
    echo    Run setup.bat or copy .env.example to .env
    pause
    exit /b 1
)

echo.
echo 🚀 Starting Technical ATS Resume Expert...
echo 📱 Opening in your default browser...
echo 🛑 Press Ctrl+C to stop the application
echo.

REM Start the application
streamlit run app.py --server.port=8501 --browser.gatherUsageStats=false

echo.
echo 👋 Application stopped.
pause
