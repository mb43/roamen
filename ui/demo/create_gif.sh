#!/bin/bash
# Create an animated GIF from the screenshots
# This is a lighter alternative to full video

set -e

SCREENSHOTS_DIR="screenshots"
OUTPUT="roamen-demo.gif"
DELAY=500  # delay between frames in centiseconds (500 = 5 seconds)
OPTIMIZE=true

echo "🎨 Creating RoamEN Demo Animated GIF"
echo "===================================="
echo ""

# Check if screenshots exist
if [ ! -d "$SCREENSHOTS_DIR" ]; then
    echo "❌ Screenshots directory not found. Run generate_screenshots.py first."
    exit 1
fi

# Count screenshots
COUNT=$(ls -1 "$SCREENSHOTS_DIR"/*.png 2>/dev/null | wc -l)
if [ "$COUNT" -eq 0 ]; then
    echo "❌ No screenshots found. Run generate_screenshots.py first."
    exit 1
fi

echo "📸 Found $COUNT screenshots"
echo "⏱️  Delay between frames: $(echo "$DELAY/100" | bc)s"
echo ""

# Check for ImageMagick
if command -v convert &> /dev/null; then
    echo "🎨 Using ImageMagick..."

    # Create GIF using ImageMagick
    convert -delay $DELAY -loop 0 \
        $SCREENSHOTS_DIR/*.png \
        "$OUTPUT"

    if [ "$OPTIMIZE" = true ] && command -v gifsicle &> /dev/null; then
        echo "🔧 Optimizing GIF with gifsicle..."
        TMP_OUTPUT="${OUTPUT}.tmp"
        gifsicle -O3 --colors 256 "$OUTPUT" -o "$TMP_OUTPUT"
        mv "$TMP_OUTPUT" "$OUTPUT"
    fi

elif command -v ffmpeg &> /dev/null; then
    echo "🎨 Using FFmpeg..."

    # Create GIF using FFmpeg
    FPS=$(echo "100/$DELAY" | bc -l)
    ffmpeg -y -framerate $FPS \
        -pattern_type glob -i "$SCREENSHOTS_DIR/*.png" \
        -vf "fps=$FPS,scale=1280:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
        -loop 0 \
        "$OUTPUT" \
        2>&1 | grep -v "deprecated" || true

else
    echo "❌ Neither ImageMagick nor FFmpeg found."
    echo "   Install one of: apt install imagemagick OR apt install ffmpeg"
    exit 1
fi

if [ -f "$OUTPUT" ]; then
    FILE_SIZE=$(du -h "$OUTPUT" | cut -f1)
    TOTAL_DURATION=$(echo "$COUNT * $DELAY / 100" | bc)

    echo ""
    echo "✅ Animated GIF created!"
    echo "📹 Output: $OUTPUT"
    echo "📦 Size: $FILE_SIZE"
    echo "⏱️  Duration: ${TOTAL_DURATION}s (${COUNT} frames)"
    echo ""
    echo "💡 Tip: Open in browser or image viewer to see animation"
    echo ""
    echo "🎉 Done!"
else
    echo ""
    echo "❌ Failed to create GIF"
    exit 1
fi
