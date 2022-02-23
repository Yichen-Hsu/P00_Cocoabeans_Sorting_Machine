# System Imoprt
import os
import time

# Control Import
from gpiozero import MotionSensor
import RPi.GPIO as GPIO

import cv2

# setup camera
def turn_on_cam(on):
    camera = cv2.VideoCapture(0)
    num = 1
    ret_flag, Vshow = camera.read()
    cv2.imshow("Capture_Test", Vshow)
    # k = cv2.waitKey(1) & 0xFF
    if on == 1:
        cv2.imwrite('/home/pi/Desktop/project/yolov5/data/images/'+str(num)+'.jpg', Vshow)
        print('success to save '+str(num)+'.jpg')
        print("----------------------------")
    camera.release()
    cv2.destroyAllWindows()

def classify(): 
    load_path = "/home/pi/Desktop/project/result.txt"
    temp_list=[]
    with open(load_path) as f:
        for line in f.readlines():
            dis = line.split(' ')
            temp_list.append(dis[5])

    wash1 = "".join(temp_list)
    wash2result = "".join(filter(str.isalnum, wash1))
    print(wash2result)

    class_dict = {
        "person": 1
    }

    print(class_dict[wash2result])



ena = 16
n1  = 20
n2  = 21
pir = MotionSensor(4)


GPIO.setmode(GPIO.BCM)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(n1, GPIO.OUT)
GPIO.setup(n2, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
# GPIO.setup('pings', GPIO.OUT) for servo2

servo1 = GPIO.PWM(26, 50)
servo1.start(0)
# servo2 = GPIO.PWM('pings', 50)
# servo2.start(0)

capture = cv2.VideoCapture(0)


while(capture.isOpened()):
    if pir.wait_for_motion():
        pir.wait_for_no_motion()
        print("Detected!")
        GPIO.output(ena, False) #stop the conveyor
        # turn_on_cam(1) # turn on the camera and take a picture
        os.popen('python /home/pi/Desktop/project/yolov5/detect.py') #execute yolov5 detect (success) import time approximately in 10 seconds
        time.sleep(20)
        load_path = "/home/pi/Desktop/project/result.txt"
        temp_list=[]
        with open(load_path) as f:
            for line in f.readlines():
                dis = line.split(' ')
                temp_list.append(dis[5])

        wash1 = "".join(temp_list)
        wash2result = "".join(filter(str.isalnum, wash1))
        print(wash2result)

        class_dict = {
            "person": 1
        }

        print(class_dict[wash2result])
        if class_dict[wash2result] == 1:
            servo1.ChangeDutyCycle(3.95)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            GPIO.output(ena, True)
            time.sleep(10)
            servo1.ChangeDutyCycle(2)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)

    # camera showing on user platform
    ret, frame = capture.read()
    cv2.imshow('user_frame', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
    capture.release()
    cv2.destroyAllWindows()

    # the conveyor keeps working 
    GPIO.output(ena, True)
    GPIO.output(n1, True)
    GPIO.output(n2, False)


  



