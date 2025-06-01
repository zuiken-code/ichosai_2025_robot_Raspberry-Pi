import cv2
from flask import Flask, render_template, Response, jsonify

from components.camera import Camera

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World!"

@app.route("/user")
def stream():
	return render_template("user.html")

def gen(camera):
	while True:
		frame = camera.get_frame()

		if frame is not None:
			yield (b"--frame\r\n"
				b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
		else:
			print("frame is none")

@app.route("/video_feed")
def video_feed():
	return Response(gen(Camera()),
			mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/status")
def check_joycon():
	return jsonify({"status": "disconnected"})

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000, threaded=True)

