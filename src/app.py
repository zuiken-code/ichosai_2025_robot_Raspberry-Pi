from flask import Flask, render_template, request, jsonify

import robot.Robot as Robot
import threading

app = Flask(__name__)

# グローバルで現在の状態を管理する
robot_state = {
    "mode": "TeleOperated",
    "enabled": False
}

@app.route("/", methods=["GET", "POST"])
def index():
    global robot_state

    if request.method == "POST":
        # モード変更があれば反映
        mode = request.form.get("mode")

        
        if mode:
            robot_state["mode"] = mode

        # enable/disable の切り替えがあれば反映
        enable_str = request.form.get("enable")
        if enable_str is not None:
            robot_state["enabled"] = (enable_str.lower() == "true")

        if robot_state["enabled"] == True:
            Robot.set_enable()
        else:
            Robot.set_disable()

        # 📌 デバッグ用に現在の状態を出力
        print(f"[DEBUG] robot_state updated: {robot_state}")

    return render_template(
        "index.html",
        selected_mode=robot_state["mode"],
        enabled=robot_state["enabled"],
    )



if __name__ == "__main__":
    # ロボットスレッドを起動
    t = threading.Thread(target=Robot.loop, args=(), daemon=True)
    t.start()

    # Flaskサーバー起動
    app.run(debug=True, host="0.0.0.0", port=5000)

