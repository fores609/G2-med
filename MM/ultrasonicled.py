# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-ultrasonic-sensor-led


import RPi.GPIO as GPIO
import time

#import buzzbut




# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)


# Define the GPIO pin number to which the buzzer is connected
BUZZER_PIN = 18

# Define the GPIO pins for the ultrasonic sensor
TRIG_PIN = 14
ECHO_PIN = 15


# Define the GPIO pin for the LED
LED_PIN = 16

# Set up the ultrasonic sensor pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Set up the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up the BUZZER pin as an output
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Define the distance threshold in cm (adjust as needed)
DISTANCE_THRESHOLD = 10 #  cm

def get_distance():
    # Send a trigger signal
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Wait for the echo response
    pulse_start = time.time()
    pulse_end = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate the distance in centimeters
    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300  # Speed of sound in cm/s
    distance = (pulse_duration * speed_of_sound) / 2

    return distance






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
        # Get the distance from the ultrasonic sensor
        distance = get_distance()
        print("Distance:", distance, "cm")

        # If the distance is below the threshold, turn on the LED
        if distance < DISTANCE_THRESHOLD:
            print("Distance below threshold. Turning on the LED.")
            GPIO.output(LED_PIN, GPIO.HIGH)

            play_jingle_bells()  # play sound 


        else:
            print("Distance above threshold. Turning off the LED.")
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn the light off

            GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn the buzzer off




        # Add a small delay to avoid excessive readings
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up the GPIO on exiting the script
    GPIO.cleanup()

    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off the buzzer
    
