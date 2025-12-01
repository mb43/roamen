#!/bin/bash
# Create a video slideshow from the screenshots
# Each screenshot is shown for 5 seconds

set -e

SCREENSHOTS_DIR="screenshots"
OUTPUT="roamen-demo-slideshow.mp4"
DURATION=5  # seconds per image
FPS=30

echo "🎬 Creating RoamEN Demo Slideshow"
echo "================================="
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
echo "⏱️  Duration per image: ${DURATION}s"
echo "🎞️  Output FPS: ${FPS}"
echo ""

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg not found. Install: apt install ffmpeg"
    exit 1
fi

echo "🎥 Creating video slideshow..."

# Create video from images using ffmpeg
ffmpeg -y -framerate $(echo "1/$DURATION" | bc -l) \
    -pattern_type glob -i "$SCREENSHOTS_DIR/*.png" \
    -vf "fps=$FPS,format=yuv420p,scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" \
    -c:v libx264 \
    -preset medium \
    -crf 23 \
    -movflags +faststart \
    "$OUTPUT" \
    2>&1 | grep -v "deprecated" || true

if [ -f "$OUTPUT" ]; then
    FILE_SIZE=$(du -h "$OUTPUT" | cut -f1)
    TOTAL_DURATION=$(echo "$COUNT * $DURATION" | bc)

    echo ""
    echo "✅ Slideshow created successfully!"
    echo "📹 Output: $OUTPUT"
    echo "📦 Size: $FILE_SIZE"
    echo "⏱️  Duration: ${TOTAL_DURATION}s (${COUNT} slides × ${DURATION}s)"
    echo ""
    echo "🎉 Done!"
else
    echo ""
    echo "❌ Failed to create slideshow"
    exit 1
fi
