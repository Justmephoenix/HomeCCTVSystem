import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():#See cmaera is open or not
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff=cv2.absdiff(frame1,frame2)#find difference between two frames
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)#converting motion to gray
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(220,255,0),2)
    for i in contours:
        if cv2.contourArea(i)<5000:
            continue
        x,y,w,h=cv2.boundingRect(i)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(220,255,0),3)#frme1,point of cornes, cornor point+ withd and height,color,width
        winsound.PlaySound('E:\python\CCTV\civilalert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10)== ord('q'):# if we enter q then the cam will be broke
        break
    cv2.imshow('Phoenix Cam',frame1)#text=cam name, frame
    