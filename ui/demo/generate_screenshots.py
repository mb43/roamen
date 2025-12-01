#!/usr/bin/env python3
"""
Generate screenshots of the RoamEN UI at key moments during the demo
This creates a series of PNG images showing different features
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright


class ScreenshotGenerator:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.output_dir = Path(__file__).parent / "screenshots"

    async def generate(self):
        print("📸 Generating RoamEN UI Screenshots...")
        print(f"📐 Resolution: {self.width}x{self.height}")

        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        print(f"📁 Output directory: {self.output_dir}")
        print()

        async with async_playwright() as p:
            # Launch browser
            print("🌐 Launching browser...")
            browser = await p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-accelerated-2d-canvas',
                    '--disable-gpu',
                    '--single-process',
                ]
            )

            page = await browser.new_page(
                viewport={'width': self.width, 'height': self.height}
            )

            # Navigate to demo page
            html_path = Path(__file__).parent / 'index.html'
            await page.goto(f'file://{html_path.absolute()}')
            await page.wait_for_timeout(2000)

            # Screenshots at key moments
            screenshots = [
                {
                    'name': '01-startup',
                    'time': 500,
                    'description': 'Initial startup screen'
                },
                {
                    'name': '02-messages',
                    'time': 8000,
                    'description': 'Message exchange view'
                },
                {
                    'name': '03-standard-alert',
                    'time': 11000,
                    'description': 'Standard alert notification'
                },
                {
                    'name': '04-alerts-view',
                    'time': 14000,
                    'description': 'Alerts view with multiple alerts'
                },
                {
                    'name': '05-urgent-alert',
                    'time': 17000,
                    'description': 'Urgent alert (power failure)'
                },
                {
                    'name': '06-voice-communication',
                    'time': 22000,
                    'description': 'Voice communication interface'
                },
                {
                    'name': '07-network-mesh',
                    'time': 26000,
                    'description': 'Network mesh visualization'
                },
                {
                    'name': '08-emergency-alert',
                    'time': 36000,
                    'description': 'Emergency alert modal'
                },
                {
                    'name': '09-alerts-list',
                    'time': 43000,
                    'description': 'Full alerts list'
                },
                {
                    'name': '10-final-messages',
                    'time': 48000,
                    'description': 'Final message coordination'
                }
            ]

            for i, shot in enumerate(screenshots, 1):
                # Wait until the specified time
                await page.wait_for_timeout(shot['time'] if i == 1 else (shot['time'] - screenshots[i-2]['time']))

                # Take screenshot
                output_path = self.output_dir / f"{shot['name']}.png"
                await page.screenshot(path=str(output_path), full_page=False)

                print(f"✅ [{i}/{len(screenshots)}] {shot['description']}")
                print(f"   📸 {output_path.name}")

            await browser.close()

        print()
        print("🎉 All screenshots generated!")
        print(f"📁 Location: {self.output_dir}")

        # List all generated files
        files = sorted(self.output_dir.glob("*.png"))
        total_size = sum(f.stat().st_size for f in files)
        print(f"📦 Total size: {total_size / (1024*1024):.2f} MB")


async def main():
    generator = ScreenshotGenerator()
    try:
        await generator.generate()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    asyncio.run(main())
