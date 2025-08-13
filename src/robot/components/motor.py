import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mode import ControllMode
from smbus import SMBus

arduino = 0x8
i2cbus = SMBus(1)

# 前に進むときの両輪に流すパワー (0〜255)
front_power = 20

right_power = 0
left_power = 0

# ジョイスティックの値をパワーの増減に変換する倍率
# 完全に倒した (1 or -1)の時に倒した側の車輪のパワーが0になるように
# よってfront_powerと同じ値になった (操作感によって変更する可能性あり)
magnification = front_power

def set_power(stick_value,magnification):
    right = front_power + stick_value * magnification
    left = front_power - stick_value * magnification
    return right, left

def moveFront():
    print("front")
    print(front_power,front_power)

def stop():
    print("stop")
    print(0,0)

def moveRight(stick_value):
    right_power, left_power = set_power(stick_value,magnification)
    print("right")
    print(left_power, right_power)

def moveLeft(stick_value):
    right_power, left_power = set_power(stick_value,magnification)
    print("left")
    print(left_power, right_power)

def applyMode(mode,stick_value):
    if mode == ControllMode.Stop:
        stop()
    elif mode == ControllMode.MoveFront:
        moveFront()
    elif mode == ControllMode.MoveRight:
        moveRight(stick_value)
    elif mode == ControllMode.MoveLeft:
        moveLeft(stick_value)
    else:
        stop()
