import cv2,time

first_frame = None
video=cv2.VideoCapture(0)
check=True

while check==True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    cv2.imshow("captured",frame)
    key=cv2.waitKey(1)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    _,thresh=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=0)
    cnts,_=cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,3),3)

    cv2.imshow('frame',frame)
    cv2.imshow('gray', gray)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('thresh',thresh)
    key=cv2.waitKey(1)
    if key == ord('x'):
        break
video.release()
cv2.destroyAllWindows()