#importing opencv

import cv2
import time
#  now i can load my image
cap=cv2.VideoCapture(0)

#check activeness of camera
print(cap.isOpened())

# now taking picture
while cap.isOpened():
    status,frame=cap.read()
    print(frame.shape)
    print(frame)
    #to show image
    cv2.imshow('live',frame)
    if cv2.waitKey(10) & 0xff == 'q' : # 0xff means capture keyboard input
        break

#destroy or close window if hanged
cv2.destroyAllWindows()




