from enum import Enum

class ControllMode(Enum):
    MoveFront = 0
    Stop = 1

def changeControllMode(state):
    print(state["button"] )
    if state["button"] == 1:
        return ControllMode.MoveFront
    else:
        return ControllMode.Stop
