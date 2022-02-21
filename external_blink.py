# from gpiozero import LED
# from time import sleep
# led = LED(17)

# while True:
#     led.on()
#     sleep(1)
#     led.off()
#     sleep(1)

import RPi.GPIO as GPIO
from time import sleep

led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    GPIO.output(led, True)
    sleep(1)
    GPIO.output(led, False)
    sleep(1)