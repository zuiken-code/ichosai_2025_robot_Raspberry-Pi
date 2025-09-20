from flask import Flask, render_template, request, jsonify, redirect
from robot.components.camera import Camera
import robot.Robot as Robot
import threading
import time

app = Flask(__name__)
cam = Camera()

def camera_loop():
    while True:
        cam.run()
        time.sleep(0.1)

# グローバルで現在の状態を管理する
robot_state = {
    "mode": "TeleOperated",
    "enabled": False
}

@app.route("/set_mode", methods=["POST"])
def set_mode():
    mode = request.form.get("mode")
    if mode:
        robot_state["mode"] = mode
    print(f"[DEBUG] Mode set: {robot_state}")
    return redirect("/")

@app.route("/set_enable", methods=["POST"])
def set_enable():
    enable_value = request.form.get("enable")
    robot_state["enabled"] = (enable_value == "true")
    print("[DEBUG] /set_enable called:", robot_state)
    return redirect("/")


@app.route("/", methods=["GET"])
def index():
    global robot_state
    return render_template(
        "index.html",
        selected_mode=robot_state["mode"],
        enabled=robot_state["enabled"],
    )

@app.route("/state")
def get_state():
    return jsonify(robot_state)

@app.route("/score")
def status():
    data = {
    "id": [3, 5, 7, 9],
    "score": 4
    }
    return jsonify(cam.get_data())

def print_state():
    last = None
    while True:
        if robot_state != last:
            #print("[MONITOR]", robot_state)
            Robot.get_state(robot_state)
            last = robot_state.copy()

        Robot.loop()

        # time.sleep(0.1)


if __name__ == "__main__":

    c = threading.Thread(target=camera_loop, daemon=True)
    #c.start()
    # ロボットスレッドを起動
    t = threading.Thread(target=print_state, daemon=True)
    t.start()
    # Flaskサーバー起動
    app.run(debug=True, host="0.0.0.0", port=5000)

