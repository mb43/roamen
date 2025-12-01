// RoamEN Demo Automation Script
// This script automatically demonstrates all features of the UI

const demoSequence = [
    { time: 1000, action: 'intro', text: 'Welcome to RoamEN - Emergency Communication System' },
    { time: 3000, action: 'message', text: 'Team, systems are online and ready', from: 'You', type: 'sent' },
    { time: 5000, action: 'message', text: 'Copy that. All relay stations operational', from: 'Relay Station A', node: 1001, type: 'received' },
    { time: 7000, action: 'message', text: 'Emergency response team standing by', from: 'Emergency Team', node: 3021, type: 'received' },
    { time: 9500, action: 'alert', alertType: 'standard', message: 'Regular check-in: All stations report status', source: 'Control Center', node: 1001 },
    { time: 12000, action: 'switchView', view: 'alerts' },
    { time: 15000, action: 'alert', alertType: 'urgent', message: 'Power failure in Building B. Switch to battery backup', source: 'Facilities', node: 2056 },
    { time: 18000, action: 'switchView', view: 'voice' },
    { time: 20000, action: 'voice', duration: 3000 },
    { time: 24000, action: 'switchView', view: 'network' },
    { time: 28000, action: 'switchView', view: 'messages' },
    { time: 30000, action: 'message', text: 'Switching to backup power now', from: 'You', type: 'sent' },
    { time: 32000, action: 'message', text: 'Backup power confirmed. All systems green', from: 'Relay Station C', node: 1003, type: 'received' },
    { time: 35000, action: 'alert', alertType: 'emergency', message: 'CODE RED: Medical emergency in A&E. All available staff respond immediately', source: 'Emergency Response', node: 3021 },
    { time: 40000, action: 'closeModal' },
    { time: 41000, action: 'switchView', view: 'alerts' },
    { time: 44000, action: 'message', text: 'Emergency team dispatched', from: 'Control', node: 1001, type: 'received' },
    { time: 45000, action: 'switchView', view: 'messages' },
    { time: 47000, action: 'message', text: 'En route to A&E', from: 'You', type: 'sent' },
    { time: 50000, action: 'outro', text: 'RoamEN - Reliable communication when everything else fails' }
];

let demoRunning = false;
let demoTimeouts = [];

function startDemo() {
    if (demoRunning) return;
    demoRunning = true;

    console.log('🎬 Starting RoamEN demo...');

    demoSequence.forEach(step => {
        const timeout = setTimeout(() => {
            executeStep(step);
        }, step.time);
        demoTimeouts.push(timeout);
    });
}

function stopDemo() {
    demoRunning = false;
    demoTimeouts.forEach(timeout => clearTimeout(timeout));
    demoTimeouts = [];
    console.log('⏹️ Demo stopped');
}

function executeStep(step) {
    console.log(`▶️ Executing: ${step.action}`, step);

    switch (step.action) {
        case 'intro':
            console.log(`📢 ${step.text}`);
            break;

        case 'message':
            if (step.type === 'sent') {
                window.roamenUI.addMessage(step.text, 'sent');
            } else {
                window.roamenUI.addMessage(step.text, 'received', step.from, step.node);
            }
            break;

        case 'alert':
            window.roamenUI.addAlert(step.alertType, step.message, step.source, step.node);
            break;

        case 'switchView':
            window.roamenUI.switchView(step.view);
            // Update active nav
            document.querySelectorAll('.nav-item').forEach(nav => {
                nav.classList.remove('active');
                if (nav.dataset.view === step.view) {
                    nav.classList.add('active');
                }
            });
            break;

        case 'voice':
            simulateVoiceTransmission(step.duration);
            break;

        case 'closeModal':
            window.roamenUI.closeAlertModal();
            break;

        case 'outro':
            console.log(`🎬 ${step.text}`);
            setTimeout(() => {
                console.log('✅ Demo complete! Restarting in 5 seconds...');
                setTimeout(() => {
                    resetDemo();
                    startDemo();
                }, 5000);
            }, 2000);
            break;
    }
}

function simulateVoiceTransmission(duration) {
    const pttBtn = document.getElementById('ptt-btn');
    const voiceIndicator = document.querySelector('.voice-indicator');
    const voiceStatusText = document.getElementById('voice-status-text');

    // Start transmission
    pttBtn.classList.add('active');
    voiceIndicator.classList.add('active');
    voiceStatusText.textContent = 'Transmitting...';

    // Stop after duration
    setTimeout(() => {
        pttBtn.classList.remove('active');
        voiceIndicator.classList.remove('active');
        voiceStatusText.textContent = 'Ready';
    }, duration);
}

function resetDemo() {
    // Clear messages
    const messageList = document.getElementById('message-list');
    messageList.innerHTML = '';

    // Clear alerts
    const alertList = document.getElementById('alert-list');
    alertList.innerHTML = '';

    // Update badge
    const badge = document.querySelector('.nav-item[data-view="alerts"] .badge');
    if (badge) {
        badge.textContent = '0';
    }

    // Switch to messages view
    window.roamenUI.switchView('messages');
    document.querySelectorAll('.nav-item').forEach(nav => {
        nav.classList.remove('active');
        if (nav.dataset.view === 'messages') {
            nav.classList.add('active');
        }
    });

    demoRunning = false;
}

// Auto-start demo when page loads
window.addEventListener('load', () => {
    console.log('🚀 RoamEN UI Demo loaded');
    setTimeout(() => {
        startDemo();
    }, 1000);
});

// Keyboard shortcut to restart demo (Ctrl+D)
window.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'd') {
        e.preventDefault();
        stopDemo();
        resetDemo();
        setTimeout(startDemo, 500);
    }
});

// Export for manual control
window.roamenDemo = {
    start: startDemo,
    stop: stopDemo,
    reset: resetDemo
};
