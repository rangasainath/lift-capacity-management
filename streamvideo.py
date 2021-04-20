import numpy as np
import time
import cv2 as cv
#from camera import VideoCamera
from flask import Flask,render_template,request,url_for,Response
app = Flask(__name__, instance_relative_config=True, template_folder='template')
@app.route('/hellos')
def hellos():
    return render_template('home.html')
    #app.debug="TRUE"
    #return app
def gen():
    """Video streaming generator function."""
    cap = cv.VideoCapture(0)

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
            break
@app.route('/through_image')
def through_image():
    return render_template('home.html')
@app.route('/through_video')
def through_video():
     return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug="True")
    

