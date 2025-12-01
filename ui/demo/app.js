// RoamEN Demo UI - Main Application Logic

// Navigation
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
        const viewName = item.dataset.view;
        switchView(viewName);

        // Update active nav item
        document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
        item.classList.add('active');
    });
});

function switchView(viewName) {
    document.querySelectorAll('.view').forEach(view => view.classList.remove('active'));
    document.getElementById(`${viewName}-view`).classList.add('active');
}

// Messages
const messageList = document.getElementById('message-list');
const msgInput = document.getElementById('msg-input');
const sendBtn = document.getElementById('send-btn');

function addMessage(text, type = 'sent', sender = 'You', nodeId = null) {
    const message = document.createElement('div');
    message.className = `message ${type}`;

    const header = document.createElement('div');
    header.className = 'message-header';

    const senderSpan = document.createElement('span');
    senderSpan.textContent = nodeId ? `${sender} (#${nodeId})` : sender;

    const timeSpan = document.createElement('span');
    timeSpan.textContent = new Date().toLocaleTimeString();

    header.appendChild(senderSpan);
    header.appendChild(timeSpan);

    const messageText = document.createElement('div');
    messageText.className = 'message-text';
    messageText.textContent = text;

    message.appendChild(header);
    message.appendChild(messageText);

    messageList.appendChild(message);
    messageList.scrollTop = messageList.scrollHeight;

    return message;
}

sendBtn.addEventListener('click', () => {
    const text = msgInput.value.trim();
    if (text) {
        addMessage(text, 'sent');
        msgInput.value = '';
    }
});

msgInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendBtn.click();
    }
});

// Alerts
const alertList = document.getElementById('alert-list');

function addAlert(type, message, source, nodeId) {
    const alert = document.createElement('div');
    alert.className = `alert-item ${type}`;

    const header = document.createElement('div');
    header.className = 'alert-header';

    const alertType = document.createElement('span');
    alertType.className = 'alert-type';
    alertType.textContent = `${type} ALERT`;
    alertType.style.color = type === 'emergency' ? 'var(--emergency-color)' :
                            type === 'urgent' ? 'var(--warning-color)' :
                            'var(--primary-color)';

    const time = document.createElement('span');
    time.className = 'alert-time';
    time.textContent = new Date().toLocaleTimeString();

    header.appendChild(alertType);
    header.appendChild(time);

    const alertMessage = document.createElement('div');
    alertMessage.className = 'alert-message';
    alertMessage.textContent = message;

    const alertSource = document.createElement('div');
    alertSource.className = 'alert-source';
    alertSource.textContent = `From: ${source} (#${nodeId})`;

    alert.appendChild(header);
    alert.appendChild(alertMessage);
    alert.appendChild(alertSource);

    alertList.insertBefore(alert, alertList.firstChild);

    // Show modal for emergency alerts
    if (type === 'emergency') {
        showAlertModal(type, message, source, nodeId);
        playAlertSound(type);
    }

    // Update badge
    updateAlertBadge();

    return alert;
}

function updateAlertBadge() {
    const count = alertList.children.length;
    const badge = document.querySelector('.nav-item[data-view="alerts"] .badge');
    if (badge) {
        badge.textContent = count;
    }
}

// Quick Alert Buttons
document.querySelectorAll('.alert-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const type = btn.dataset.type;
        const message = prompt(`Enter ${type} alert message:`);
        if (message) {
            addAlert(type, message, 'You', '1042');
        }
    });
});

// Alert Modal
const alertModal = document.getElementById('alert-modal');

function showAlertModal(type, message, source, nodeId) {
    const modal = alertModal;
    const header = modal.querySelector('.alert-modal-header');
    const title = document.getElementById('alert-modal-title');
    const messageEl = document.getElementById('alert-modal-message');
    const sourceEl = document.getElementById('alert-modal-source');

    header.className = `alert-modal-header ${type}`;
    title.textContent = `${type.toUpperCase()} ALERT`;
    messageEl.textContent = message;
    sourceEl.textContent = `From: ${source} (#${nodeId})`;

    modal.classList.add('show');
}

function closeAlertModal() {
    alertModal.classList.remove('show');
}

window.closeAlertModal = closeAlertModal;

// Voice
const pttBtn = document.getElementById('ptt-btn');
const voiceIndicator = document.querySelector('.voice-indicator');
const voiceStatusText = document.getElementById('voice-status-text');

let isTransmitting = false;

pttBtn.addEventListener('mousedown', () => {
    startTransmission();
});

pttBtn.addEventListener('mouseup', () => {
    stopTransmission();
});

pttBtn.addEventListener('mouseleave', () => {
    if (isTransmitting) {
        stopTransmission();
    }
});

function startTransmission() {
    isTransmitting = true;
    pttBtn.classList.add('active');
    voiceIndicator.classList.add('active');
    voiceStatusText.textContent = 'Transmitting...';
}

function stopTransmission() {
    isTransmitting = false;
    pttBtn.classList.remove('active');
    voiceIndicator.classList.remove('active');
    voiceStatusText.textContent = 'Ready';
}

// Network Visualization
const networkViz = document.getElementById('network-viz');

function createNetworkVisualization() {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', '100%');
    svg.setAttribute('height', '100%');
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';

    // Define nodes
    const nodes = [
        { id: 1042, x: 50, y: 50, label: 'This Device', color: '#2563eb' },
        { id: 1001, x: 30, y: 30, label: 'Relay A', color: '#10b981' },
        { id: 2056, x: 70, y: 30, label: 'Staff', color: '#10b981' },
        { id: 3021, x: 30, y: 70, label: 'Emergency', color: '#10b981' },
        { id: 1003, x: 70, y: 70, label: 'Relay C', color: '#10b981' }
    ];

    // Draw connections
    const connections = [
        [1042, 1001],
        [1042, 2056],
        [1042, 3021],
        [1042, 1003],
        [1001, 2056],
        [3021, 1003]
    ];

    connections.forEach(([from, to]) => {
        const fromNode = nodes.find(n => n.id === from);
        const toNode = nodes.find(n => n.id === to);

        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', `${fromNode.x}%`);
        line.setAttribute('y1', `${fromNode.y}%`);
        line.setAttribute('x2', `${toNode.x}%`);
        line.setAttribute('y2', `${toNode.y}%`);
        line.setAttribute('stroke', 'rgba(37, 99, 235, 0.3)');
        line.setAttribute('stroke-width', '2');

        svg.appendChild(line);
    });

    // Draw nodes
    nodes.forEach(node => {
        const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');

        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', `${node.x}%`);
        circle.setAttribute('cy', `${node.y}%`);
        circle.setAttribute('r', '20');
        circle.setAttribute('fill', node.color);
        circle.setAttribute('stroke', 'rgba(255, 255, 255, 0.5)');
        circle.setAttribute('stroke-width', '2');

        // Pulse animation for center node
        if (node.id === 1042) {
            const pulse = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            pulse.setAttribute('cx', `${node.x}%`);
            pulse.setAttribute('cy', `${node.y}%`);
            pulse.setAttribute('r', '20');
            pulse.setAttribute('fill', 'none');
            pulse.setAttribute('stroke', node.color);
            pulse.setAttribute('stroke-width', '2');
            pulse.setAttribute('opacity', '0.6');

            const animate = document.createElementNS('http://www.w3.org/2000/svg', 'animate');
            animate.setAttribute('attributeName', 'r');
            animate.setAttribute('from', '20');
            animate.setAttribute('to', '40');
            animate.setAttribute('dur', '2s');
            animate.setAttribute('repeatCount', 'indefinite');

            const animateOpacity = document.createElementNS('http://www.w3.org/2000/svg', 'animate');
            animateOpacity.setAttribute('attributeName', 'opacity');
            animateOpacity.setAttribute('from', '0.6');
            animateOpacity.setAttribute('to', '0');
            animateOpacity.setAttribute('dur', '2s');
            animateOpacity.setAttribute('repeatCount', 'indefinite');

            pulse.appendChild(animate);
            pulse.appendChild(animateOpacity);
            g.appendChild(pulse);
        }

        g.appendChild(circle);

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', `${node.x}%`);
        text.setAttribute('y', `${node.y + 8}%`);
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('fill', 'white');
        text.setAttribute('font-size', '12');
        text.setAttribute('font-weight', 'bold');
        text.textContent = node.id;

        g.appendChild(text);
        svg.appendChild(g);
    });

    networkViz.appendChild(svg);
}

// Initialize
createNetworkVisualization();

// Simulate alert sound
function playAlertSound(type) {
    // In a real implementation, this would play the actual alert tone
    console.log(`Playing ${type} alert tone`);
}

// Export for demo script
window.roamenUI = {
    addMessage,
    addAlert,
    switchView,
    showAlertModal,
    closeAlertModal
};
