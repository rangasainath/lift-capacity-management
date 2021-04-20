import cv2 as cv
import numpy as np
def gen():
    face_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
    eyes_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_eye.xml')
    #img=cv.imread('/Users/saikscbs/Desktop/proj3/i.jpg')
    cap=cv.VideoCapture(0)
    d=cap.isOpened()
    if d==1:
        pass
    else:
        cap.Open()
    cap=cv.VideoCapture(0)
    while (cap.isOpened()):
        ret,img =cap.read()
        #print(img)
        #cv.imshow('boxer',img)
        faces=face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
        #print(faces)
        i=0                   
        for(x,y,w,h) in faces:
            #print("drawing rectangles")
            rectangle=cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            i=i+1
            rectangle=cv.putText(rectangle,'face num'+str(i),(x-10,y-10),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            #print(img,i)
            #cv.imshow('boxer',rectangle)
            #height=int(cap.get(4))
            #width=int(cap.get(3))
            #fps=cap.get(cv.CAP_PROP_FPS)
            #fourcc=cv.VideoWriter_fourcc(*'mp4v')
            #PATH='Users/saikscbs/Documents/project2/proj3/static/demo.webm'
            #frameSize=[]
            #out=cv.VideoWriter('rectangle.mp4',fourcc,20.0,(640,480))
            #out.write(rectangle)   
            jpegs = cv.imencode('.jpg', rectangle)[1].tobytes()
            yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + jpegs + b'\r\n\r\n')
            if(cv.waitKey(1) & 0xFF ==ord('q')):
                break
    cap.release()
    cv.DestroyAllWindows()
gen()