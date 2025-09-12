import cv2
import apriltag
import time

class Camera(object):
    def __init__(self, width=320, height=240):
        print("カメラのモジュールが読み込まれました")
        self.video = cv2.VideoCapture(0, cv2.CAP_V4L2)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        # apriltag detector (tag16h5)
        options = apriltag.DetectorOptions(families="tag16h5")
        self.detector = apriltag.Detector(options)

        # FPS計測用
        self.last_time = time.time()
        self.fps = 0.0

        # 検出IDを蓄積
        self.detected_ids_list = []
        self.data = {"id": [], "score": 0}

    def __del__(self):
        self.video.release()

    def _update_fps(self):
        now = time.time()
        dt = now - self.last_time
        if dt > 0:
            self.fps = 1.0 / dt
        self.last_time = now

    def detect_apriltag_ids(self):
        success, image = self.video.read()
        if not success:
            #print("カメラが認識していません")
            return []

        self._update_fps()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        tags = self.detector.detect(gray)

        return [tag.tag_id for tag in tags]

    def run(self):
        """1回分だけカメラを見て data を更新"""
        ids = self.detect_apriltag_ids()
        if ids:
            self.detected_ids_list.extend(ids)
            unique_ids = set(self.detected_ids_list)
            self.data = {
                "id": list(unique_ids),
                "score": len(unique_ids)
            }

    def reset(self):
        """検出結果をリセット"""
        self.detected_ids_list = []
        self.data = {"id": [], "score": 0}

    def get_data(self):
        """最新の data を返す"""
        return dict(self.data)

    def get_fps(self):
        return self.fps


if __name__ == "__main__":
    cam = Camera()

    print("Start detecting... (Ctrl+C to stop)")
    try:
        while True:
            cam.run()  # ここで1回分更新
            print(cam.get_data(), f"FPS = {cam.get_fps():.2f}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped.")
        print("Final data:", cam.get_data())

