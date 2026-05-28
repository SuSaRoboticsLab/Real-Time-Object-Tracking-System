import cv2


class TrajectoryDrawer:

    def __init__(self):

        self.trajectories = {}

    def update_trajectory(
        self,
        object_id,
        center
    ):

        if object_id not in self.trajectories:

            self.trajectories[object_id] = []

        self.trajectories[object_id].append(center)

    def draw_trajectory(
        self,
        frame
    ):

        for points in self.trajectories.values():

            for i in range(1, len(points)):

                cv2.line(
                    frame,
                    points[i - 1],
                    points[i],
                    (0, 0, 255),
                    2
                )