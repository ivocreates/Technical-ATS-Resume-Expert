#!/bin/bash

echo "================================================================"
echo "🚀 Technical ATS Resume Expert - Unix/Linux/macOS Quick Setup"
echo "================================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed successfully!"
echo

# Run the quick setup script
echo "🔧 Running interactive setup..."
python3 quick_start.py
