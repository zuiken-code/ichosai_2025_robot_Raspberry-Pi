import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mode import ControllMode

def moveFront():
    print("front")

def stop():
    print("stop")

def applyMode(mode):
    if mode == ControllMode.MoveFront:
        moveFront()
    elif mode == ControllMode.Stop:
        stop()
    else:
        stop()