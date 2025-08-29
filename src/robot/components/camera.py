import cv2
import apriltag
import time

class Camera(object):
    def __init__(self, width=320, height=240):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        # apriltag detector
        self.detector = apriltag.Detector()

        # FPS計測用
        self.last_time = time.time()
        self.fps = 0.0

    def __del__(self):
        self.video.release()

    def _update_fps(self):
        now = time.time()
        dt = now - self.last_time
        if dt > 0:
            self.fps = 1.0 / dt
        self.last_time = now

    def detect_apriltag(self):
        """Apriltagを検出したら True を返す"""
        success, image = self.video.read()
        if not success:
            return False

        self._update_fps()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        tags = self.detector.detect(gray)

        return len(tags) > 0

    def get_fps(self):
        """最新のFPSを返す"""
        return self.fps


if __name__ == "__main__":
    cam = Camera()
    detect_count = 0
    was_detected = False
    # 新たに追加する変数
    last_detected_time = 0  # 最後に検出された時刻
    cooldown_period = 1.0  # 再検出を許可するまでの待機時間（秒）

    print("Start detecting... (Ctrl+C to stop)")
    try:
        while True:
            detected = cam.detect_apriltag()
            fps = cam.get_fps()
            now = time.time() # 現在時刻を取得

            # AprilTagが検出された場合
            if detected:
                print("detected!!!!!!!!!!")
                # 前回検出されておらず、かつクールダウン期間が過ぎている場合
                if not was_detected and (now - last_detected_time > cooldown_period):
                    detect_count += 1
                    print(f"[+] AprilTag appeared! Count = {detect_count}, FPS = {fps:.2f}")
                
                # 検出された時間を更新
                last_detected_time = now

            # AprilTagが非検出の場合
            else:
                if was_detected:
                    print("[-] AprilTag disappeared")

            was_detected = detected
            time.sleep(0.1)  # CPU負荷軽減

    except KeyboardInterrupt:
        print("\nStopped.")
        print(f"Total appeared count: {detect_count}")
