import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
from typing import List, Tuple

CAMERA_FOV_RADIANS = (52.31 * math.pi / 180, 51.83 * math.pi / 180)
CAMERA_DIMENSIONS_PIXELS = (640, 480)
CAMERA_HEIGHT_ABOVE_GROUND_METERS = 0.263


def conversion(x: int, c: int, theta: float):
    return math.atan2((x - c / 2) * math.tan(theta / 2), c / 2)


def get_point_angle(point: Tuple[int, int], camera_dimension: Tuple[int, int], camera_fov: Tuple[float, float]) -> Tuple[float, float]:
    return (conversion(point[0], camera_dimension[0], camera_fov[0]),
            conversion(point[1], camera_dimension[1], camera_fov[1]))


def bounding_box_angle(box: List[Tuple[int, int]], camera_dimension: Tuple[int, int], camera_fov: Tuple[float, float]) -> List[Tuple[float, float]]:
    return [get_point_angle(point, camera_dimension, camera_fov) for point in box]


def distance_estimation(angles: Tuple[float, float], h: float) -> Tuple[float, float]:
    l = h / math.tan(angles[1])
    w = l * math.tan(angles[0])
    return w, l


def main():
    vid = cv2.VideoCapture(0)

    p = (1, 1)
    target = 0.0775
    differential = 0.0001

    while True:
        ret, frame = vid.read()
        if not ret:
            print("Failed to capture frame")
            break

        l, r, m = 0, math.pi, 0

        while (r - l) > differential:
            m = (l + r) / 2

            m_angles = bounding_box_angle(
                [p] * 4,
                CAMERA_DIMENSIONS_PIXELS, (m, CAMERA_FOV_RADIANS[1]))[0]

            distances = distance_estimation(m_angles, CAMERA_HEIGHT_ABOVE_GROUND_METERS)

            distance = distances[0]

            if distance > target:
                r = m - differential
            elif distance < target:
                l = m + differential
            else:
                break

        # Convert distance to string for display
        distance_str = "Distance: {:.2f} meters".format(distance)

        # Convert pixel measurements to string for display
        pixel_measure_str = "Pixel measurement: {} pixels".format(p)

        # Update text on the frame
        cv2.putText(frame, distance_str, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, pixel_measure_str, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the frame
        cv2.imshow('Webcam Feed', frame)

        # Wait for a small amount of time (1 millisecond)
        # If 'q' is pressed, exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Read the next frame
        ret, frame = vid.read()

    # Release the video capture object and close all windows
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
