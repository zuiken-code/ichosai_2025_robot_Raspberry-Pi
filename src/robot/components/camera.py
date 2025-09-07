import cv2
import apriltag
import time

class Camera(object):
    def __init__(self, width=320, height=240):
        print("カメラのモジュールが読み込まれました")
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        # apriltag detector (tag16h5)
        options = apriltag.DetectorOptions(families="tag16h5")
        self.detector = apriltag.Detector(options)

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

    def detect_apriltag_ids(self):
        """
        検出されたAprilTagのIDリストを返す（なければ空リスト）
        """
        success, image = self.video.read()
        if not success:
            return []

        self._update_fps()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        tags = self.detector.detect(gray)

        return [tag.tag_id for tag in tags]

    def get_fps(self):
        """最新のFPSを返す"""
        return self.fps


if __name__ == "__main__":
    cam = Camera()
    detected_ids_list = []  # 検出IDを保存するリスト

    print("Start detecting... (Ctrl+C to stop)")
    try:
        while True:
            ids = cam.detect_apriltag_ids()
            fps = cam.get_fps()

            if ids:
                detected_ids_list.extend(ids)
                unique_ids = set(detected_ids_list)  # 重複削除した集合を作成
                print(f"Detected IDs: {unique_ids}, FPS = {fps:.2f}")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopped.")
        unique_ids = set(detected_ids_list)
        print(f"Final unique detected IDs: {unique_ids}")

