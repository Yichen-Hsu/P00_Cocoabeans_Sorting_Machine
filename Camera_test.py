import cv2 

capture = cv2.VideoCapture(0)
while(capture.isOpened()):
    ret, frame = capture.read()
    cv2.imshow('Frame', frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
capture.release()
cv2.destroyAllWindows()

