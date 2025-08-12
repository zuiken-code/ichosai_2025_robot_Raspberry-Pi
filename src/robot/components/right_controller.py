import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.joystick.init()

def get_joycon_data():
    pygame.joystick.quit()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("接続出来てません")
        return {"status": "disconnected", "button": {}}

    # 1つ目のジョイスティックを取得（Joy-Conが1台だけ接続されている前提）
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # イベントポンプを通さないとボタン状態が更新されない
    pygame.event.pump()

    # 例えば、ボタン0が "X" かどうかは Joy-Con によって異なる → 調べて使う
    x_button = joystick.get_button(2)  # 適宜ボタン番号を変えて

    return {"status": "connected", "button": x_button}
