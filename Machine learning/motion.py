import cv2
cap=cv2.VideoCapture(0)
#motion detect function
def mdetect(a,b,c):
    #diff of first two take
    f_diff=cv2.absdiff(a,b) # using absdiff
    s_diff=cv2.absdiff(b,c) #using absdiff
    #bitwise diff of relativeimage
    final=cv2.bitwise_and(f_diff,s_diff)
    return final

# now taking image
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]

# converting into gray scale
gray1 = cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)
while True:
    # applying gray images to functions
    m_img=mdetect(gray1,gray2,gray3)
    # taking more pictures
    satus,frame=cap.read()
    #showng diff
    cv2.imshow('motion',m_img)
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # live image show
    
    if cv2.waitKey(10) & 0xff == 'q' : # 0xff means capture keyboard input
        break

#destroy or close window if hanged
cv2.destroyAllWindows()
    