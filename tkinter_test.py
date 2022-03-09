from tkinter import *
from tkinter import ttk
import cv2 
import os

# def camera_on():
#     capture = cv2.VideoCapture(0)
#     while(capture.isOpened()):
#         ret, frame = capture.read()
#         cv2.imshow('Frame', frame)
#         c = cv2.waitKey(1)
#         if c == ord(' '):
#             break
#     capture.release()
#     cv2.destroyAllWindows()

def detect_on():
    os.system('YOUR FIEL/detect.py --source 0')

window = Tk()
window.title('Function Board')
window.geometry("300x200")
l1 = ttk.Label(text="hello world")
exitbt = ttk.Button(window, text="exit", command=window.destroy)
camera = ttk.Button(window, text="camera test", command=detect_on)
exitbt.pack(anchor=S, side=RIGHT, padx=5, pady=5)
camera.pack(anchor=S, side=RIGHT, padx=5, pady=5)
l1.pack()
window.mainloop()


