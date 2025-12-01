#!/bin/bash
# Simple video recorder using FFmpeg and a headless browser
# This script uses xvfb-run to create a virtual display and captures it

set -e

WIDTH=1920
HEIGHT=1080
FPS=30
DURATION=57
OUTPUT="roamen-demo.mp4"

echo "🎬 RoamEN UI Demo - Simple Video Recorder"
echo "=========================================="
echo "📐 Resolution: ${WIDTH}x${HEIGHT}"
echo "🎞️  Frame rate: ${FPS} fps"
echo "⏱️  Duration: ${DURATION} seconds"
echo ""

# Check dependencies
echo "🔍 Checking dependencies..."
command -v ffmpeg >/dev/null 2>&1 || { echo "❌ ffmpeg not found. Install: apt install ffmpeg"; exit 1; }
command -v chromium-browser >/dev/null 2>&1 || command -v google-chrome >/dev/null 2>&1 || { echo "⚠️  Chrome/Chromium not found"; }
command -v xvfb-run >/dev/null 2>&1 || { echo "❌ xvfb not found. Install: apt install xvfb"; exit 1; }

echo "✅ Dependencies OK"
echo ""

# Get absolute path to HTML file
HTML_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/index.html"
echo "📄 HTML file: ${HTML_PATH}"

# Determine browser command
if command -v chromium-browser >/dev/null 2>&1; then
    BROWSER="chromium-browser"
elif command -v google-chrome >/dev/null 2>&1; then
    BROWSER="google-chrome"
else
    echo "❌ No suitable browser found"
    exit 1
fi

echo "🌐 Browser: ${BROWSER}"
echo ""

# Create temp directory for screenshots
TEMP_DIR=$(mktemp -d)
echo "📁 Temp directory: ${TEMP_DIR}"

echo "🔴 Starting recording..."
echo ""

# Start virtual display and capture
DISPLAY=:99

# Method 1: Using FFmpeg with X11 capture
xvfb-run -n 99 -s "-screen 0 ${WIDTH}x${HEIGHT}x24" \
    bash -c "
        # Start browser in background
        ${BROWSER} --headless=new \
            --window-size=${WIDTH},${HEIGHT} \
            --disable-gpu \
            --no-sandbox \
            --disable-dev-shm-usage \
            --disable-software-rasterizer \
            --disable-extensions \
            --autoplay-policy=no-user-gesture-required \
            'file://${HTML_PATH}' &

        BROWSER_PID=\$!

        # Wait for browser to start
        sleep 3

        # Capture screen with FFmpeg
        timeout ${DURATION} ffmpeg -y \
            -f x11grab \
            -video_size ${WIDTH}x${HEIGHT} \
            -framerate ${FPS} \
            -i :99.0 \
            -c:v libx264 \
            -preset medium \
            -crf 18 \
            -pix_fmt yuv420p \
            -movflags +faststart \
            '${OUTPUT}' \
            2>&1 | grep -v 'deprecated'

        # Kill browser
        kill \$BROWSER_PID 2>/dev/null || true
    " || echo "⚠️  Recording completed"

# Cleanup
rm -rf "$TEMP_DIR"

if [ -f "$OUTPUT" ]; then
    FILE_SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo ""
    echo "✅ Recording complete!"
    echo "📹 Video saved to: $OUTPUT"
    echo "📦 File size: $FILE_SIZE"
    echo ""
    echo "🎉 Done!"
else
    echo "❌ Recording failed - output file not created"
    exit 1
fi
