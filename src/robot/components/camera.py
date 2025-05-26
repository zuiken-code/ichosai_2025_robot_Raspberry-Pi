
# camera.py

import cv2
from pupil_apriltags import Detector

detector = Detector()

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        tags = detector.detect(gray)
        for tag in tags:
            for corner in tag.corners:
                x, y = int(corner[0]), int(corner[1])
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
                cv2.putText(image, f"ID: {tag.tag_id}", (int(tag.center[0]), int(tag.center[1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        ret, frame = cv2.imencode('.jpg', image)
        return frame

