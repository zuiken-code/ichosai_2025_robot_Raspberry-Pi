import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mode import ControllMode
from smbus import SMBus

arduino = 0x8
i2cbus = SMBus(1)

def moveFront():
    print("front")

def stop():
    print("stop")

def moveRight():
    print("right")

def moveLeft():
    print("left")

def applyMode(mode):
    if mode == ControllMode.Stop:
        stop()
    elif mode == ControllMode.MoveFront:
        moveFront()
    elif mode == ControllMode.MoveRight:
        moveRight()
    elif mode == ControllMode.MoveLeft:
        moveLeft()
    else:
        stop()
