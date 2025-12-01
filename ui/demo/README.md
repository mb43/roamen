# RoamEN UI Demo & Video Recorder

This directory contains an interactive demo of the RoamEN Emergency Communication System UI and tools to generate demonstration videos.

## Features

The demo showcases:

- 💬 **Text Messaging** - Send and receive messages between nodes
- 🚨 **Alert System** - Standard, Urgent, and Emergency alerts with priority-based notifications
- 🎙️ **Voice Communication** - Push-to-talk interface with Codec2 digital voice
- 🌐 **Network Mesh** - Visualization of connected nodes and relay stations
- 🔋 **System Status** - Battery level, node count, and connection status

## Quick Start

### Option 1: View Demo in Browser

1. Start a local web server:
   ```bash
   python3 -m http.server 8000
   ```

2. Open your browser to:
   ```
   http://localhost:8000
   ```

3. The demo will automatically play through a complete scenario showing all features

### Option 2: Generate Video (Node.js/Puppeteer)

1. Install dependencies:
   ```bash
   npm install
   ```

2. Record the demo:
   ```bash
   npm run record
   ```

3. Output: `roamen-demo.mp4` (1920x1080, 30fps)

### Option 3: Generate Video (Python/Playwright)

1. Install Playwright:
   ```bash
   pip install playwright
   playwright install chromium
   ```

2. Record the demo:
   ```bash
   python3 record_video.py
   ```

3. Output: `roamen-demo.webm` (1920x1080, 30fps)

## Demo Scenario

The automated demo runs through the following scenario (57 seconds):

1. **System Initialization** (0-3s)
   - UI loads, shows RoamEN branding and status

2. **Normal Operations** (3-9s)
   - Team messages confirming systems online
   - Relay stations reporting operational status

3. **Standard Alert** (9-12s)
   - Regular check-in alert from control center

4. **Urgent Situation** (12-18s)
   - Power failure alert (Building B)
   - Switch to alerts view to show notification

5. **Voice Communication** (18-24s)
   - Demonstrate push-to-talk voice interface
   - Show Codec2 voice parameters

6. **Network Visualization** (24-28s)
   - Display mesh network topology
   - Show connected nodes and relay stations

7. **Emergency Response** (28-41s)
   - CODE RED emergency alert (Medical emergency in A&E)
   - Full-screen emergency modal
   - Team coordination messages

8. **Resolution** (41-50s)
   - Emergency response dispatched
   - Status updates from team

9. **Outro** (50-57s)
   - Final messaging
   - Demo loops back to start

## Interactive Controls

### Keyboard Shortcuts

- **Ctrl+D** - Restart demo from beginning

### Manual Controls

Open browser console and use:

```javascript
// Start demo
roamenDemo.start()

// Stop demo
roamenDemo.stop()

// Reset demo
roamenDemo.reset()

// Add custom message
roamenUI.addMessage('Your message', 'sent')

// Add custom alert
roamenUI.addAlert('emergency', 'Alert message', 'Source', 1042)

// Switch view
roamenUI.switchView('alerts')  // 'messages', 'alerts', 'voice', 'network'
```

## File Structure

```
ui/demo/
├── index.html          # Main HTML structure
├── style.css           # UI styling (dark theme, animations)
├── app.js              # Interactive functionality
├── demo.js             # Automated demo script
├── record-video.js     # Node.js video recorder
├── record_video.py     # Python video recorder
├── package.json        # Node dependencies
└── README.md           # This file
```

## Customization

### Modify Demo Sequence

Edit `demo.js` and update the `demoSequence` array:

```javascript
const demoSequence = [
    { time: 1000, action: 'message', text: 'Your message', type: 'sent' },
    { time: 3000, action: 'alert', alertType: 'emergency', message: 'Alert!', source: 'Control', node: 1001 },
    // ... add more steps
];
```

### Change Video Settings

**Node.js version** (`record-video.js`):
```javascript
const CONFIG = {
    width: 1920,
    height: 1080,
    fps: 30,
    videoBitrate: 5000,
    // ... modify as needed
};
```

**Python version** (`record_video.py`):
```python
class DemoRecorder:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.fps = 30
        # ... modify as needed
```

### Customize UI Theme

Edit `style.css` CSS variables:

```css
:root {
    --primary-color: #2563eb;
    --emergency-color: #dc2626;
    --dark-bg: #1f2937;
    /* ... customize colors */
}
```

## Requirements

### Browser Demo
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x (for local server)

### Video Recording (Node.js)
- Node.js 16+
- npm
- ffmpeg (system dependency)

### Video Recording (Python)
- Python 3.8+
- playwright
- Chromium (installed via playwright)

## Troubleshooting

### Demo doesn't auto-play
- Check browser console for errors
- Ensure all files are in the same directory
- Try hard refresh (Ctrl+Shift+R)

### Video recording fails (Node.js)
- Install ffmpeg: `sudo apt install ffmpeg` (Ubuntu/Debian)
- Check puppeteer installation: `npm list puppeteer`

### Video recording fails (Python)
- Ensure Playwright is installed: `playwright install chromium`
- Check Python version: `python3 --version` (needs 3.8+)

### Video is too large
- Reduce resolution in config
- Lower bitrate setting
- Use webm format (smaller than mp4)

## Technical Details

### Video Specifications

| Parameter | Value |
|-----------|-------|
| Resolution | 1920x1080 (Full HD) |
| Frame Rate | 30 fps |
| Duration | ~57 seconds |
| Codec | H.264 (mp4) or VP9 (webm) |
| Bitrate | 5000 kbps |
| File Size | ~35-50 MB |

### Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Fully supported |
| Firefox | 88+ | ✅ Fully supported |
| Safari | 14+ | ✅ Fully supported |
| Edge | 90+ | ✅ Fully supported |

## License

GPL-3.0 - Same as main RoamEN project

## Contributing

To improve the demo:

1. Fork the repository
2. Make your changes to the demo files
3. Test thoroughly in multiple browsers
4. Submit a pull request

## Contact

For issues or questions about the demo:
- GitHub Issues: [github.com/mb43/roamen/issues](https://github.com/mb43/roamen/issues)
- Discussions: [github.com/mb43/roamen/discussions](https://github.com/mb43/roamen/discussions)
