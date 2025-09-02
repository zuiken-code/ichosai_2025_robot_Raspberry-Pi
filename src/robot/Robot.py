import time
from robot import mode
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

def get_mode():
    return now_mode

def set_enable():
    robot_state["enabled"] = True
    print("set_enable")

def set_disable():
    robot_state["enabled"] = False
    print("set_disable")

def loop(robot_state):
    while True:
        run(robot_state)
        time.sleep(0.01)

if __name__ == '__main__':
    while True:
        run()
        time.sleep(0.01)
