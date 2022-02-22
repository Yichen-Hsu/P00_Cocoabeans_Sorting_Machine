import RPi.GPIO as GPIO


ena = 16
n1  = 20
n2  = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(n1, GPIO.OUT)
GPIO.setup(n2, GPIO.OUT)

while True:
    GPIO.output(ena, True)
    GPIO.output(n1, True)
    GPIO.output(n2, False)
    stop = int(input("stop please push 1: "))
    if stop == 1 :
        GPIO.output(ena, False)
        GPIO.cleanup()
        break
    else:
        continue