import cv2
#loading camera driver
cap = cv2.VideoCapture(0)
#loading face dataset
face_detect = cv2.CascadeClassifier('face1.xml')
eye_detect = cv2.CascadeClassifier('eye.xml')


 #all function by var
#print(dir(face_detect))

#taking pictures
while cap.isOpened() :
    #reading images
    status, frame = cap.read()
    #converting image to gray scale
    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(grayimg)
    #using cascade function
    face = face_detect.detectMultiScale(grayimg, 1.15,5)
    print(face)
    
    #analysis
    for(x,y,w,h) in face :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        onlyface = frame[y:y+h,x:x+w]
    
    cv2.imshow('liveface',frame)
    cv2.imshow('face1',onlyface)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()