#!/usr/bin/env python3
"""
Create an animated GIF from screenshots using PIL/Pillow
"""

from pathlib import Path
from PIL import Image


def create_gif():
    print("🎨 Creating RoamEN Demo Animated GIF")
    print("====================================")
    print()

    screenshots_dir = Path(__file__).parent / "screenshots"
    output_file = Path(__file__).parent / "roamen-demo.gif"

    # Check if screenshots exist
    if not screenshots_dir.exists():
        print("❌ Screenshots directory not found. Run generate_screenshots.py first.")
        return False

    # Get all PNG files
    images_paths = sorted(screenshots_dir.glob("*.png"))

    if not images_paths:
        print("❌ No screenshots found. Run generate_screenshots.py first.")
        return False

    print(f"📸 Found {len(images_paths)} screenshots")
    print(f"⏱️  Duration per frame: 5s")
    print()

    # Load images
    print("📂 Loading images...")
    images = []
    for i, img_path in enumerate(images_paths, 1):
        img = Image.open(img_path)
        # Resize for smaller file size if needed
        # img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)
        images.append(img)
        print(f"   ✓ {img_path.name}")

    if not images:
        print("❌ No images loaded")
        return False

    print()
    print("🎨 Creating animated GIF...")

    # Save as animated GIF
    # duration=5000 means 5000ms = 5 seconds per frame
    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:],
        duration=5000,  # milliseconds
        loop=0,  # loop forever
        optimize=True
    )

    # Get file size
    file_size_mb = output_file.stat().st_size / (1024 * 1024)
    total_duration = len(images) * 5

    print()
    print("✅ Animated GIF created!")
    print(f"📹 Output: {output_file}")
    print(f"📦 Size: {file_size_mb:.2f} MB")
    print(f"⏱️  Duration: {total_duration}s ({len(images)} frames)")
    print()
    print("💡 Tip: Open in browser or image viewer to see animation")
    print()
    print("🎉 Done!")

    return True


if __name__ == "__main__":
    try:
        success = create_gif()
        if not success:
            exit(1)
    except ImportError as e:
        print("❌ PIL/Pillow not found. Install: pip install Pillow")
        exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
