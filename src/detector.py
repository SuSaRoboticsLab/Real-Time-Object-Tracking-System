import cv2


class MotionDetector:

    def __init__(self):

        self.detector = cv2.createBackgroundSubtractorMOG2(
            history=100,
            varThreshold=40
        )

    def detect_objects(self, frame):

        mask = self.detector.apply(frame)

        _, mask = cv2.threshold(
            mask,
            254,
            255,
            cv2.THRESH_BINARY
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )

        detections = []

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area > 800:

                x, y, w, h = cv2.boundingRect(cnt)

                detections.append([x, y, w, h])

        return detections, mask