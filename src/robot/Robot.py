import time
from robot import mode
import robot.components.right_controller as right_controller
from robot.mode import ControllMode
import robot.components.motor as motor

motor_connected = False

def run(robot_state):
    controller_state = right_controller.get_joycon_data()
   
    now_mode = mode.changeControllMode(controller_state)

    print(now_mode)

    motor.applyMode(robot_state["enabled"], motor_connected,now_mode,controller_state["stick_value"])

if __name__ == '__main__':
    while True:
        run()
        time.sleep(0.01)
