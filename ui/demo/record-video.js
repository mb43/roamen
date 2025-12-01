#!/usr/bin/env node

/**
 * RoamEN UI Demo Video Recorder
 * Records the demo UI in action and generates a video file
 *
 * Requirements: puppeteer, puppeteer-screen-recorder
 * Install: npm install puppeteer puppeteer-screen-recorder
 */

const puppeteer = require('puppeteer');
const { PuppeteerScreenRecorder } = require('puppeteer-screen-recorder');
const path = require('path');
const fs = require('fs');

const CONFIG = {
    width: 1920,
    height: 1080,
    fps: 30,
    videoBitrate: 5000,
    videoCodec: 'libx264',
    videoPreset: 'medium',
    videoCrf: 18,
    aspectRatio: '16:9'
};

async function recordDemo() {
    console.log('🎬 Starting RoamEN UI Demo Recording...');
    console.log('📐 Resolution:', `${CONFIG.width}x${CONFIG.height}`);
    console.log('🎞️  Frame rate:', `${CONFIG.fps} fps`);

    let browser;
    let recorder;

    try {
        // Launch browser
        console.log('🌐 Launching browser...');
        browser = await puppeteer.launch({
            headless: true,
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                `--window-size=${CONFIG.width},${CONFIG.height}`
            ]
        });

        const page = await browser.newPage();

        // Set viewport
        await page.setViewport({
            width: CONFIG.width,
            height: CONFIG.height,
            deviceScaleFactor: 1
        });

        // Setup screen recorder
        recorder = new PuppeteerScreenRecorder(page, {
            followNewTab: false,
            fps: CONFIG.fps,
            ffmpeg_Path: null, // Uses system ffmpeg
            videoFrame: {
                width: CONFIG.width,
                height: CONFIG.height
            },
            aspectRatio: CONFIG.aspectRatio,
            videoCrf: CONFIG.videoCrf,
            videoCodec: CONFIG.videoCodec,
            videoPreset: CONFIG.videoPreset,
            videoBitrate: CONFIG.videoBitrate
        });

        // Navigate to the demo page
        const htmlPath = path.join(__dirname, 'index.html');
        console.log('📄 Loading UI from:', htmlPath);
        await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

        // Wait for page to be fully loaded
        await page.waitForTimeout(2000);

        // Start recording
        const outputPath = path.join(__dirname, 'roamen-demo.mp4');
        console.log('🔴 Recording started...');
        console.log('💾 Output file:', outputPath);

        await recorder.start(outputPath);

        // Wait for demo to complete (52 seconds + 5 second buffer)
        const recordingDuration = 57000;
        console.log(`⏱️  Recording for ${recordingDuration / 1000} seconds...`);

        // Show progress
        const progressInterval = setInterval(() => {
            const elapsed = Date.now() - startTime;
            const percentage = Math.min(100, (elapsed / recordingDuration) * 100);
            process.stdout.write(`\r⏳ Progress: ${percentage.toFixed(1)}%`);
        }, 1000);

        const startTime = Date.now();
        await page.waitForTimeout(recordingDuration);

        clearInterval(progressInterval);
        process.stdout.write('\r⏳ Progress: 100.0%\n');

        // Stop recording
        console.log('⏹️  Stopping recording...');
        await recorder.stop();

        console.log('✅ Recording complete!');
        console.log('📹 Video saved to:', outputPath);

        // Get file size
        const stats = fs.statSync(outputPath);
        const fileSizeMB = (stats.size / (1024 * 1024)).toFixed(2);
        console.log('📦 File size:', `${fileSizeMB} MB`);

    } catch (error) {
        console.error('❌ Error during recording:', error);
        throw error;
    } finally {
        // Cleanup
        if (recorder) {
            try {
                await recorder.stop();
            } catch (e) {
                // Ignore errors during cleanup
            }
        }
        if (browser) {
            await browser.close();
        }
    }
}

// Main execution
if (require.main === module) {
    recordDemo()
        .then(() => {
            console.log('🎉 Done!');
            process.exit(0);
        })
        .catch(error => {
            console.error('💥 Fatal error:', error);
            process.exit(1);
        });
}

module.exports = { recordDemo };
