# 🚀 Quick Start Guide

## Windows Users - Easy Setup

### Option 1: Complete Setup (First Time)
Double-click `setup.bat` for complete automated setup:
- ✅ Checks Python installation
- ✅ Creates virtual environment
- ✅ Installs all dependencies
- ✅ Configures API key (interactive)
- ✅ Starts the application

### Option 2: Quick Launch (After Setup)
Double-click `start.bat` for quick application launch:
- ✅ Activates virtual environment
- ✅ Starts the application immediately

## Manual Setup (All Platforms)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
```bash
# Copy template
cp .env.example .env

# Edit .env file and add your Google Gemini API key
GOOGLE_API_KEY=your_actual_api_key_here
```

### 3. Run Application
```bash
streamlit run app.py
```

## Getting Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the generated key
5. Add it to your `.env` file

## Troubleshooting

### Common Issues

**Python not found:**
- Install Python 3.8+ from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

**Dependencies fail to install:**
- Check internet connection
- Try: `pip install --upgrade pip`
- Run: `pip install --upgrade --force-reinstall -r requirements.txt`

**Application won't start:**
- Ensure API key is configured in `.env` file
- Run `python test_app.py` to check for issues
- Check `logs/app.log` for error details

### Support

- 📖 Check the main [README.md](README.md) for full documentation
- 🐛 Report issues on [GitHub Issues](https://github.com/ivocreates/Technical-ATS-Resume-Expert/issues)
- 💬 Ask questions in [Discussions](https://github.com/ivocreates/Technical-ATS-Resume-Expert/discussions)
