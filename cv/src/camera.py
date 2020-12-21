import cv2
import numpy as np
from flask import Flask, request
import os
import requests

PORT = int(os.environ.get("PORT"))
MODEL_API_URL = str(os.environ.get('MODEL_API_URL'))

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_TRIPLEX
video = cv2.VideoCapture("facial_exp.mkv")

app = Flask(__name__)

#returns camera frames along with bounding boxes and predictions
@app.route('/', methods=['POST'])
def get_frame():
    _, fr = video.read()
    gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    
    #detect faces and returns the position as rect(x,y,w,h)
    face = face_detector.detectMultiScale(gray_fr, 1.3, 5) 

    for (x, y, w, h) in face:
        fc = gray_fr[y:y+h, x:x+w]

        roi = cv2.resize(fc, (48, 48)) #returns numpy array
        
        data = {'image': roi[np.newaxis, :, :, np.newaxis].tolist()} 
        request = requests.post(MODEL_API_URL, json=data)
        #response
        prediction = request.text
        cv2.putText(img=fr, text=prediction, org=(x, y), fontFace=font, fontScale=2, color=(255, 255, 255), thickness=4)
        cv2.rectangle(img=fr,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,255),thickness=4)

    _, jpeg = cv2.imencode('.jpg', fr)
    return jpeg.tobytes()


if __name__ == '__main__':
    app.run('0.0.0.0',port=PORT)