import cv2
import time


class FPSCounter:

    def __init__(self):

        self.prev_frame_time = 0
        self.new_frame_time = 0

    def calculate_fps(self):

        self.new_frame_time = time.time()

        fps = 1 / (
            self.new_frame_time -
            self.prev_frame_time
        )

        self.prev_frame_time = self.new_frame_time

        return int(fps)

    def draw_fps(
        self,
        frame,
        fps
    ):

        cv2.putText(
            frame,
            f"FPS: {fps}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )