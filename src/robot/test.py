import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("ジョイスティックが見つかりません")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("ジョイスティック名:", joystick.get_name())
print("ボタン数:", joystick.get_numbuttons())

try:
    while True:
        pygame.event.pump()
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                print(f"ボタン {i} が押されています")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("終了")
    pygame.quit()