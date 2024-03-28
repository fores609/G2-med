# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-button-piezo-buzzer


import RPi.GPIO as GPIO
import time

# Set the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number to which the buzzer is connected
BUZZER_PIN = 18

# Define the GPIO pin number to which the button is connected
#BUTTON_PIN = 16

# Set up the GPIO pins
#GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up resistor
GPIO.setup(BUZZER_PIN, GPIO.OUT)                          # Output


# Constants for note names and their corresponding frequencies
C4 = 261
D4 = 293
E4 = 329
F4 = 349
G4 = 392
A4 = 440
B4 = 493

# Dictionary to map numeric values to note names
note_names = {
    C4: "C4",
    D4: "D4",
    E4: "E4",
    F4: "F4",
    G4: "G4",
    A4: "A4",
    B4: "B4",
}


# List of notes in the "Jingle Bells" melody
melody = [
    E4, E4, E4, E4, E4, E4, E4, G4, C4, D4, E4, F4, F4, F4, F4, F4, E4, E4, E4, E4, E4, D4, D4, E4, D4, G4
]

# List of note durations (in milliseconds)
note_durations = [
    200, 200, 400, 200, 200, 400, 200, 200, 200, 200, 200, 200, 200, 400, 200, 200, 200, 200, 200, 200, 200, 200, 200, 400, 200, 200
]

# Pause duration between notes (in milliseconds)
pause_duration = 300

def play_tone(pin, frequency, duration):
    # Calculate the period based on the frequency
    period = 1.0 / frequency
    
    # Calculate the time for half of the period
    half_period = period / 2.0
    
    # Calculate the number of cycles for the given duration
    cycles = int(duration / period)
    
    for _ in range(cycles):
        # Set the GPIO pin to HIGH
        GPIO.output(pin, GPIO.HIGH)
        
        # Wait for half of the period
        time.sleep(half_period)
        
        # Set the GPIO pin to LOW
        GPIO.output(pin, GPIO.LOW)
        
        # Wait for the other half of the period
        time.sleep(half_period)


def play_jingle_bells():
    for i in range(len(melody)):
        note_duration = note_durations[i] / 1000.0
        note_freq = melody[i]
        note_name = note_names.get(note_freq, "Pause")

        print(f"Playing {note_name} (Frequency: {note_freq} Hz) for {note_duration} seconds")
        
        play_tone(BUZZER_PIN, note_freq, note_duration)
        
        time.sleep(pause_duration / 1000.0)
        
        GPIO.output(BUZZER_PIN, GPIO.LOW)



try:
    while True:

        #button_state = GPIO.input(BUTTON_PIN)

       # if button_state == GPIO.LOW:
            
            print("The button is being pressed")
         #  GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn the buzzer on
            play_jingle_bells()
         

       # else:
            print("The button is unpressed")
            GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn the buzzer off

        # Add a slight delay to d
        # ebounce the button (optional)
       #time.sleep(0.1)

# Allow the user to stop the buzzer by pressing Ctrl+C
except KeyboardInterrupt:
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off the buzzer
    GPIO.cleanup()
