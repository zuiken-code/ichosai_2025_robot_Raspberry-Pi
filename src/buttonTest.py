import pygame
import sys
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

deadband = 0.1  # 小さい入力を無視するしきい値

def dead_band(value, threshold):
    """スティックの微小入力をゼロにする"""
    return 0 if abs(value) < threshold else value

def listen_for_buttons():
    """ゲームコントローラーのボタン入力とスティック値を監視する"""
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("ジョイスティック/コントローラーが接続されていません。")
        pygame.quit()
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"ジョイスティック '{joystick.get_name()}' が接続されました。")
    print("入力を監視しています... (終了するにはCtrl+C)")

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print(f"[BUTTON] ID: {event.button} pressed")

                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt

            # 全軸の値を取得
            axes_values = []
            for i in range(joystick.get_numaxes()):
                axes_values.append(dead_band(joystick.get_axis(i), deadband))

            # 軸の値を出力（リアルタイム）
            print(f"[AXES] {axes_values}")

            pygame.time.wait(50)  # 50ms待機
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    finally:
        pygame.quit()

if __name__ == "__main__":
    listen_for_buttons()

