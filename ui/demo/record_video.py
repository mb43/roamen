#!/usr/bin/env python3
"""
RoamEN UI Demo Video Recorder (Python version)
Records the demo UI in action using Playwright

Requirements:
    pip install playwright
    playwright install chromium
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright


class DemoRecorder:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.fps = 30
        self.output_file = "roamen-demo.webm"

    async def record(self):
        print("🎬 Starting RoamEN UI Demo Recording...")
        print(f"📐 Resolution: {self.width}x{self.height}")
        print(f"🎞️  Frame rate: {self.fps} fps")

        async with async_playwright() as p:
            # Launch browser
            print("🌐 Launching browser...")
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                ]
            )

            # Create context with video recording
            context = await browser.new_context(
                viewport={'width': self.width, 'height': self.height},
                record_video_dir='.',
                record_video_size={'width': self.width, 'height': self.height}
            )

            page = await context.new_page()

            # Navigate to demo page
            html_path = Path(__file__).parent / 'index.html'
            print(f"📄 Loading UI from: {html_path}")
            await page.goto(f'file://{html_path.absolute()}')

            # Wait for page to load
            await page.wait_for_timeout(2000)

            print("🔴 Recording started...")

            # Record for 57 seconds (demo duration + buffer)
            recording_duration = 57000
            print(f"⏱️  Recording for {recording_duration / 1000} seconds...")

            # Show progress
            for i in range(0, recording_duration, 1000):
                await page.wait_for_timeout(1000)
                progress = min(100, (i / recording_duration) * 100)
                print(f"\r⏳ Progress: {progress:.1f}%", end='', flush=True)

            print("\r⏳ Progress: 100.0%")

            # Close context to save video
            print("⏹️  Stopping recording...")
            await context.close()
            await browser.close()

            # Rename video file
            video_path = await page.video.path()
            if video_path:
                output_path = Path(__file__).parent / self.output_file
                os.rename(video_path, output_path)
                print(f"✅ Recording complete!")
                print(f"📹 Video saved to: {output_path}")

                # Get file size
                file_size_mb = output_path.stat().st_size / (1024 * 1024)
                print(f"📦 File size: {file_size_mb:.2f} MB")
            else:
                print("❌ Video recording failed")


async def main():
    recorder = DemoRecorder()
    try:
        await recorder.record()
        print("🎉 Done!")
    except Exception as e:
        print(f"❌ Error during recording: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
