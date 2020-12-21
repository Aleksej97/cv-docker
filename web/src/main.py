from flask import Flask, render_template, Response
import os
import requests

PORT = int(os.environ.get("PORT"))
CV_API_URL = str(os.environ.get("CV_API_URL"))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        request = requests.post(CV_API_URL, json={'message':"get_video"})
        frame = request.content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = PORT)


