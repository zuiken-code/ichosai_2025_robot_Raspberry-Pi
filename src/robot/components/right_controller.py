import time
import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.joystick.init()

X_button = 2
B_button = 0

stick_x = 1
deadband = 0.1

def dead_band(number, deadband):
    if abs(number) < deadband:
        return 0
    else:
        return number

def get_joycon_data():
    pygame.joystick.quit()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("接続出来てません")
        return {"status": "disconnected"}

    # 1つ目のジョイスティックを取得（Joy-Conが1台だけ接続されている前提）
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # イベントポンプを通さないとボタン状態が更新されない
    pygame.event.pump()

    x_push = joystick.get_button(X_button)
    b_push = joystick.get_button(B_button)

    stick_value = dead_band(joystick.get_axis(stick_x),deadband)

    is_accelerator = x_push or b_push

    return {"status": "connected", "x_push": x_push, "b_push": b_push, "is_accelerator": is_accelerator, "stick_value": stick_value}

def main():
    while True:
        print(get_joycon_data())
        time.sleep(0.1)

if __name__ == '__main__':
    main()
