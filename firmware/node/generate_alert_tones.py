#!/usr/bin/env python3
"""Generate alert tone WAV files for RoamEN"""

import numpy as np
import wave
import struct
import os

def generate_tone(filename, frequencies, durations, sample_rate=8000):
    """Generate a tone WAV file"""
    samples = []
    
    for freq, duration in zip(frequencies, durations):
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        if freq == 0:
            # Silence
            wave_data = np.zeros(len(t))
        else:
            # Generate sine wave
            wave_data = np.sin(2 * np.pi * freq * t)
        
        samples.extend(wave_data)
    
    # Convert to 16-bit PCM
    samples = np.array(samples)
    samples = np.int16(samples * 32767)
    
    # Write WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(samples.tobytes())
    
    print(f"✅ Generated: {filename}")

# Create alert tones directory
os.makedirs('ui/assets/alert_tones', exist_ok=True)

print("🎵 Generating RoamEN Alert Tones...\n")

# STANDARD ALERT - Two-tone (like pager beep)
generate_tone(
    'ui/assets/alert_tones/standard.wav',
    frequencies=[800, 1000],
    durations=[0.3, 0.3]
)

# URGENT ALERT - Warbling alarm
generate_tone(
    'ui/assets/alert_tones/urgent.wav',
    frequencies=[800, 1200, 800, 1200, 800],
    durations=[0.2, 0.2, 0.2, 0.2, 0.2]
)

# EMERGENCY ALERT - Aggressive siren
generate_tone(
    'ui/assets/alert_tones/emergency.wav',
    frequencies=[600, 1200, 600, 1200, 600, 1200],
    durations=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15]
)

print("\n🎉 All alert tones generated!")
print("\nTest them with:")
print("  afplay ui/assets/alert_tones/standard.wav")
print("  afplay ui/assets/alert_tones/urgent.wav")
print("  afplay ui/assets/alert_tones/emergency.wav")
