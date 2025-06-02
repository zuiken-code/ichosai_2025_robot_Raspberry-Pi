import cv2
import time
from flask import Flask, render_template, Response, jsonify

import threading
from components.camera import Camera
import components.right_controller as right_controller

app = Flask(__name__)


# def update_joycon_data():
#     global joycon_data
#     while True:
#         joycon_data = right_controller.get_joycon_data()

# # スレッドでバックグラウンド取得
# t = threading.Thread(target=update_joycon_data, daemon=True)
# t.start()

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


# @app.route("/status")
# def check_joycon():
# 	return jsonify(joycon_data)

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000, threaded=True)

