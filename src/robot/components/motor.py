import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from robot.mode import ControllMode
from smbus import SMBus

arduino = 0x8
i2cbus = SMBus(1)

# 前に進むときの両輪に流すパワー (0〜255)
front_power = 125

right_power = 0
left_power = 0

# ジョイスティックの値をパワーの増減に変換する倍率
# 完全に倒した (1 or -1)の時に倒した側の車輪のパワーが0になるように
# よってfront_powerと同じ値になった (操作感によって変更する可能性あり)
magnification = front_power

def send_motor(left, right):
    """モーターにパワーを送る（I2C）。例外が起きても無視して再試行可能"""
    try:
        i2cbus.write_i2c_block_data(arduino, 0, [int(left), int(right)])
    except Exception as e:
        # すべての例外を捕まえて警告だけ出す
        print(f"[WARN] I2C送信中に例外発生: {e}")
        # 再送は次回send_motor呼び出し時に行われる



def set_power(stick_value,magnification):
    right = front_power + stick_value * magnification
    left = front_power - stick_value * magnification
    return right, left

def moveFront(motor_connected):
    print("front")
    print(front_power,front_power)
    if motor_connected:
        send_motor(front_power,front_power)

def stop(motor_connected):
    print("stop")
    print(0,0)
    if motor_connected:
        send_motor(0,0)

def moveRight(motor_connected, stick_value):
    right_power, left_power = set_power(stick_value,magnification)
    print("right")
    print(left_power, right_power)
    if motor_connected:
        send_motor(left_power,right_power)

def moveLeft(motor_connected, stick_value):
    right_power, left_power = set_power(stick_value,magnification)
    print("left")
    print(left_power, right_power)
    if motor_connected:
        send_motor(left_power, right_power)

def applyMode(enabled,motor_connected,mode,stick_value):
    if enabled == False:
        print("not enable")
        stop(motor_connected)
    elif mode == ControllMode.Stop:
        stop(motor_connected)
        print("mode = stop")
    elif mode == ControllMode.MoveFront:
        moveFront(motor_connected)
    elif mode == ControllMode.MoveRight:
        moveRight(motor_connected,stick_value)
    elif mode == ControllMode.MoveLeft:
        moveLeft(motor_connected,stick_value)
    else:
        stop(motor_connected)
        print("else")
