import cv2

from detector import MotionDetector
from tracker import EuclideanDistTracker
from trajectory import TrajectoryDrawer
from utils import FPSCounter


cap = cv2.VideoCapture(0)

detector = MotionDetector()

tracker = EuclideanDistTracker()

trajectory = TrajectoryDrawer()

fps_counter = FPSCounter()


while True:

    ret, frame = cap.read()

    if not ret:
        break

    detections, mask = detector.detect_objects(
        frame
    )

    tracked_objects = tracker.update(
        detections
    )

    for obj in tracked_objects:

        x, y, w, h, object_id = obj

        center = (
            x + w // 2,
            y + h // 2
        )

        trajectory.update_trajectory(
            object_id,
            center
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID: {object_id}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    trajectory.draw_trajectory(frame)

    fps = fps_counter.calculate_fps()

    fps_counter.draw_fps(frame, fps)

    cv2.imshow(
        "Object Tracking System",
        frame
    )

    cv2.imshow(
        "Foreground Mask",
        mask
    )

    key = cv2.waitKey(30)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()