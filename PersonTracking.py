# Denis O'Leary / T00191862 / Final year project

import cv2


WEBCAM = 1
LAP_CAM = 0
BORDER_WIDTH = 2
OURSIDE_CAM = "rtsp://cam1.oleary.com/Streaming/Channels/2"
# outside cam is linked to local hostnames, change to IP or FQDN of camera!

# Importing Haar Cascades into program
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(OURSIDE_CAM)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray)

    for (x,y,w,h) in body:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), BORDER_WIDTH)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print("Body Detected on stream")

        faces = face_cascade.detectMultiScale(gray)
        for (fx,fy,fw,fh) in faces:
            cv2.rectangle(img, (fx,fy), (fx+fw, fy+fh), (0,255,0), BORDER_WIDTH)
            roi_gray = gray[fy:fy+fh, fx:fx+fw]
            roi_color = img[fy:fy+fh, fx:fx+fw]
            print("Face detected on stream")

            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
               #cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,0,255), 2)


    cv2.imshow('Image rec', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print("Now closing down Stream")
        break

cap.release()
cv2.destroyAllWindows()
