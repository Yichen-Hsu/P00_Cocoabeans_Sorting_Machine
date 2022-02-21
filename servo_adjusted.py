import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
servo1 = GPIO.PWM(26, 50)

servo1.start(0)

try:
    while True:
        # Ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 to 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    # Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye")