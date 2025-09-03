from flask import Flask, render_template, request, jsonify

import robot.Robot as Robot
import threading
import time

app = Flask(__name__)

# グローバルで現在の状態を管理する
robot_state = {
    "mode": "TeleOperated",
    "enabled": False
}

@app.route("/", methods=["GET", "POST"])
def index():
    global robot_state

    #if request.method == "POST":
        # モード変更があれば反映
        #mode = request.form.get("mode")

        
        #if mode:
            #robot_state["mode"] = mode

        # enable/disable の切り替えがあれば反映
    if request.method == "POST":
        enable_value = request.form.get("enable")
        if enable_value == "true":
            print("enabled")   # Enable ボタンが押されたとき
            robot_state["enabled"] = True
        elif enable_value == "false":
            print("disabled")  # Disable ボタンが押されたとき
            robot_state["enabled"] = False
        # 📌 デバッグ用に現在の状態を出力
        print(f"[DEBUG] robot_state updated: {robot_state}")

    return render_template(
        "index.html",
        selected_mode=robot_state["mode"],
        enabled=robot_state["enabled"],
    )

def print_state():
    while True:
        print(robot_state)
        time.sleep(0.1)


if __name__ == "__main__":
    # ロボットスレッドを起動
    #t = threading.Thread(target=Robot.loop, args=(robot_state,), daemon=True)
    #t.start()
    t = threading.Thread(target=print_state, daemon=True)
    t.start()

    # Flaskサーバー起動
    app.run(debug=True, host="0.0.0.0", port=5000)

