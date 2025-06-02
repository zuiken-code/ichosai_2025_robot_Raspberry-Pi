import time
import mode
import components.right_controller as right_controller
from mode import ControllMode
import components.motor as motor

def run():
    controller_state = right_controller.get_joycon_data()
    print(controller_state)
    now_mode = mode.changeControllMode(controller_state)
    print(mode.changeControllMode(controller_state))

    motor.applyMode(now_mode)

if __name__ == '__main__':
    while True:
        run()
        time.sleep(0.01)