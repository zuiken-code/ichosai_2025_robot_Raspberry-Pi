import time
import pygame
import os

# ダミービデオドライバ設定（表示なしで使うため）
os.environ["SDL_VIDEODRIVER"] = "dummy"

# pygameの初期化はモジュール読み込み時に一度だけ
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
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        return {"is_accelerator": False, "status": "disconnected"}

    # 最初のジョイスティックを取得
    joystick = pygame.joystick.Joystick(0)

    # joystick.init() は一度だけで十分（ここでは毎回呼ばなくても良い）
    if not joystick.get_init():
        joystick.init()

    # 状態更新
    pygame.event.pump()

    x_push = joystick.get_button(X_button)
    b_push = joystick.get_button(B_button)

    stick_value = dead_band(joystick.get_axis(stick_x), deadband)

    is_accelerator = x_push or b_push

    return {
        "status": "connected",
        "x_push": x_push,
        "b_push": b_push,
        "is_accelerator": is_accelerator,
        "stick_value": stick_value,
    }

def main():
    while True:
        print(get_joycon_data())
        time.sleep(0.1)

if __name__ == '__main__':
    main()

