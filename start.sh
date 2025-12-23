#!/bin/bash
# Simple script to start local web server

echo "🚀 Starting Research Log Server..."
echo "📍 Server running at: http://localhost:8000"
echo "📱 Open browser: http://localhost:8000/index.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================"
echo ""

python3 -m http.server 8000
