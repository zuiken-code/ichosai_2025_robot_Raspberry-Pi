import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mode import ControllMode
from smbus import SMBus

arduino = 0x8
i2cbus = SMBus(1)

motorOn = 0x0
motorOff = 0x1
blueOn = 0x2
blueOff = 0x3

def moveFront():
    print("front")
    i2cbus.write_byte(arduino, motorOn)


def stop():
    print("stop")
    i2cbus.write_byte(arduino, motorOff)


def applyMode(mode):
    if mode == ControllMode.MoveFront:
        moveFront()
    elif mode == ControllMode.Stop:
        stop()
    else:
        stop()