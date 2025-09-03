import time
from robot import mode
import requests
import robot.components.right_controller as right_controller
from robot.mode import ControllMode
import robot.components.motor as motor

motor_connected = False

def run(robot_state):
    global now_mode

    controller_state = right_controller.get_joycon_data()

    now_mode = mode.changeControllMode(controller_state)

    print(robot_state)

    motor.applyMode(robot_state["enabled"], motor_connected,now_mode,controller_state["stick_value"])

def get_robot_state():
    try:
        # 同じマシンなので127.0.0.1を指定
        response = requests.get("http://127.0.0.1:5000/state")
        if response.status_code == 200:
            return response.json()  # JSONを辞書に変換
    except Exception as e:
        print("通信エラー:", e)
    return None

def get_state(state):
    global robot_state
    robot_state = state
    print(robot_state)

def set_disable():
    robot_state["enabled"] = False
    print("set_disable")

def loop():
    while True:
        robot_state = get_robot_state()
        print(robot_state)
        #run(robot_state)
        time.sleep(0.01)

if __name__ == '__main__':
    while True:
        run()
        time.sleep(0.01)
