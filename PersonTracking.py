# Denis O'Leary / T00191862 / Final year project

import cv2
import os


WEBCAM = 1
LAP_CAM = 0
BORDER_WIDTH = 2
OURSIDE_CAM = "rtsp://cam1.oleary.com/Streaming/Channels/2"

# Importing Haar Cascades into program
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')



cap = cv2.VideoCapture(LAP_CAM)

while True: # setting up the system
    ret, img = cap.read() # pulling feed from webcam
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting camera to gray scale
    body = body_cascade.detectMultiScale(gray, 1.3, 5) # setting the body cascade to read the gray scale image

    for (x,y,w,h) in body: # first checking for body
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), BORDER_WIDTH) # adds a border around body
        fce_gray = gray[y:y+h, x:x+w] # sets up the
        fce_color = img[y:y+h, x:x+w]

        print("Body Detected on stream")
        os.system('python SendEmail.py') # sends email about body detection

        faces = face_cascade.detectMultiScale(fce_gray)
        for (fx,fy,fw,fh) in faces:
            cv2.rectangle(fce_color, (fx,fy), (fx+fw, fy+fh), (0,255,0), BORDER_WIDTH)

            print("Face detected on stream")


    cv2.imshow('Image rec', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print("Now closing down Stream")
        break

cap.release()
cv2.destroyAllWindows()
