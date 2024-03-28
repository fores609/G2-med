# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-button-servo-motor


import RPi.GPIO as GPIO
import time

# Constants won't change
BUTTON_PIN = 18  # Raspberry Pi GPIO pin connected to the button's pin
SERVO_PIN = 12  # Raspberry Pi GPIO pin connected to the servo motor's pin

# Variables will change
angle = 0  # The current angle of the servo motor
prev_button_state = None  # The previous state of the button
button_state = None  # The current state of the button

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create PWM instance for servo
servo_pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frequency

# Initialize servo position
servo_pwm.start(0)

try:
    while True:
        prev_button_state = button_state  # Save the last state
        button_state = GPIO.input(BUTTON_PIN)  # Read new state

        if prev_button_state == GPIO.HIGH and button_state == GPIO.LOW:
            print("The button is pressed")

            # Change angle of servo motor
            if angle == 0:
                angle = 180
            else:
                angle = 0
              

            # Control servo motor according to the angle
            duty_cycle = (angle / 18) + 2.5  # Convert angle to duty cycle
            servo_pwm.ChangeDutyCycle(duty_cycle)

        time.sleep(0.1)  # Add a small delay to avoid rapid button presses

except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()
dir