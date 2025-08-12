import pygame
import sys
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

def listen_for_buttons():
    """ゲームコントローラーのボタン入力を待ち受ける関数"""
    pygame.init()
    pygame.joystick.init()

    # 接続されているジョイスティックの数を取得
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("ジョイスティック/コントローラーが接続されていません。")
        pygame.quit()
        return

    # 最初のジョイスティックを初期化
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"ジョイスティック '{joystick.get_name()}' が接続されました。")
    print("ボタン入力を待ち受けています... (終了するにはCtrl+Cを押してください)")

    try:
        while True:
            # イベントキューを処理
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    # どのボタンが押されたかを出力
                    print(f"Button ID: {event.button} has been pressed.")
                
                # 終了イベント
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt
            
            # CPU使用率を抑えるために少し待機
            pygame.time.wait(10)
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    finally:
        pygame.quit()

if __name__ == "__main__":
    listen_for_buttons()
