#!/bin/bash
# Quick Start Script untuk Research Log Generator dengan File Upload

echo "======================================"
echo "🚀 RESEARCH LOG GENERATOR - STARTUP"
echo "======================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 tidak ditemukan. Silakan install Python terlebih dahulu."
    exit 1
fi

echo "✅ Python3 detected"

# Check Flask installation
if ! python3 -c "import flask" &> /dev/null; then
    echo "📦 Installing Flask..."
    pip3 install flask
else
    echo "✅ Flask already installed"
fi

# Create necessary folders
echo "📁 Creating folders..."
mkdir -p assets/img
mkdir -p assets/pdf
mkdir -p reviews
mkdir -p templates
mkdir -p static

echo "✅ Folders created"

# Check if papers.json exists
if [ ! -f "papers.json" ]; then
    echo "📝 Creating papers.json..."
    echo "[]" > papers.json
fi

echo "✅ papers.json ready"

echo ""
echo "======================================"
echo "🔥 Starting Flask Server..."
echo "======================================"
echo ""
echo "📍 Server akan berjalan di: http://localhost:5000"
echo "📍 Untuk stop server: Ctrl+C"
echo ""
echo "Fitur Baru:"
echo "  • Upload Image dengan auto-naming"
echo "  • Upload PDF dengan auto-naming"
echo "  • Preview image langsung di form"
echo ""

# Start Flask app
python3 app.py
