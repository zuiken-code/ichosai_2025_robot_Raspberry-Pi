import time
import mode
import components.right_controller as right_controller
from mode import ControllMode
import components.motor as motor

motor_connected = True

def run():
    controller_state = right_controller.get_joycon_data()
   
    now_mode = mode.changeControllMode(controller_state)

    motor.applyMode(motor_connected,now_mode,controller_state["stick_value"])

if __name__ == '__main__':
    while True:
        run()
        time.sleep(0.01)
