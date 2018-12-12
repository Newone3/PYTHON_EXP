# >>> import cv2
# >>> print(cv2.__file__)
# open path a zkopirovat data do projektu


import numpy as np
import cv2

face_casdade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 640, 500)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_casdade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w ,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]   # x y souradnice
        roi_color = frame[y:y+h, x:x+w]

        # face recognition deep model predict keras tensorflow pytorch scikit




        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0)   # barva obelniku
        stroke = 1
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # Display the resulting frame
    cv2.imshow('frame', frame)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()