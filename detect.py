import numpy as np
import cv2 as cv
from werkzeug.utils import secure_filename
#from camera import VideoCamera
from flask import Flask,render_template,request,url_for,Response
app = Flask(__name__, instance_relative_config=True, template_folder='template')
@app.route('/hellos')
def hellos():
    return render_template('home.html')
    #app.debug="TRUE"
    #return app
@app.route('/through_image')
def through_image():
    return render_template('image.html')
def gen1(image):
    img=cv.resize(image,(0,0),fx=0.5,fy=0.5)
    img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    face_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
    detect=face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
    i=0
    #rectangle=[]
    for x,y,w,h in detect:
        rectangle=cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        i=i+1
        rectangle=cv.putText(rectangle,'face num'+str(i),(x-15,y-15),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    #print(type(rectangle))
    imjpeg=cv.imencode('.jpg',rectangle)[1].tobytes()
    #imjpeg=cv.imshow('img',rectangle)
    #print(i)
    yield(b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + imjpeg + b'\r\n\r\n')

@app.route('/through_images',methods=['GET','POST'])
def through_images():
    if request.method=='POST':
        f=request.files['image[]']
        f.save('/Users/saikscbs/Documents/project2/proj3/Upload_Folder/'+secure_filename(f.filename))
        face_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
        img=cv.imread('/Users/saikscbs/Documents/project2/proj3/Upload_Folder/'+secure_filename(f.filename))
    return Response(gen1(img),mimetype='multipart/x-mixed-replace; boundary=frame')
def gen():
    """Video streaming generator function."""
    '''cap = cv.VideoCapture(0)
    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
            frame = cv.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        else: 
            break'''
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
        img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
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
            #print(height,width)
@app.route('/through_video')
def through_video():
    #cap.release()
    #cv.destroyALLWindows()
    #return Response(f,mimetype='multipart/x-mixed-replace; boundary=frame')
    #return Response(cv.imshow('ractangled image',rectangle),mimetype='multipart/x-mixed-replace; boundary=frame')
    #return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
    return render_template('outputvideo.html')   
@app.route('/through_videos')
def through_videos():
    
    #cap.release()
    #cv.destroyALLWindows()
    #return Response(f,mimetype='multipart/x-mixed-replace; boundary=frame')
    #return Response(cv.imshow('ractangled image',rectangle),mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug="True")