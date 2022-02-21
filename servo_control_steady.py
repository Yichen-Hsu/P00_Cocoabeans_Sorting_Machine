import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
servo1 = GPIO.PWM(26, 50)

servo1.start(0)
print("Waiting for 2 seconds")
time.sleep(2)

print("Rotating 180 degrees in 10 steps")

duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1

time.sleep(2)

print("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(1.5)

print("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()
print("Goodbye")