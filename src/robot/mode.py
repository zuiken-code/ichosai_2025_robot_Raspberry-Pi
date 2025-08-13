from enum import Enum

class ControllMode(Enum):
    Stop = 0
    MoveFront = 1
    MoveRight = 2
    MoveLeft = 3


def changeControllMode(state):
    if state["is_accelerator"] == 0:
        return ControllMode.Stop
    elif state["stick_value"] == 0:
        return ControllMode.MoveFront
    elif state["stick_value"] > 0:
        return ControllMode.MoveLeft
    elif state["stick_value"] < 0:
        return ControllMode.MoveRight
    else:
        return ControllMode.Stop

