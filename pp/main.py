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


# width, height
def get_point_angle(point: Tuple[int, int], camera_dimension: Tuple[int, int], camera_fov: Tuple[float, float]) -> Tuple[float, float]:
    

    return (conversion(point[0], camera_dimension[0], camera_fov[0]),
            conversion(point[1], camera_dimension[1], camera_fov[1]))


def bounding_box_angle(box: List[Tuple[int, int]], camera_dimension: Tuple[int, int], camera_fov: Tuple[float, float]) -> List[Tuple[float, float]]:
    return [get_point_angle(point, camera_dimension, camera_fov) for point in box]


def distance_estimation(angles: Tuple[float, float], h: float) -> Tuple[float, float]:
    l = h / math.tan(angles[1])
    w = l * math.tan(angles[0])

    return w, l


# 26.5cm + 35.3cm = 61.8cm

def main():
    p = (400, 446)

    l, r, m = 0, math.pi, 0

    # distance should be (0.0775, .835)
    # calculated fov : (, 45.55) degrees
    target = 0.0775
    differential = 0.0001

    while (r - l) > differential:
        m = (l + r) / 2

        m_angles = bounding_box_angle(
            [p] * 4,
            CAMERA_DIMENSIONS_PIXELS, (m, CAMERA_FOV_RADIANS[1]))[0]

        distances = distance_estimation(m_angles, CAMERA_HEIGHT_ABOVE_GROUND_METERS)

        distance = distances[0]

        print(l, r, m, distances)

        if distance > target:
            r = m - differential
        elif distance < target:
            l = m + differential
        else:
            break

    print(m)




    vid = cv2.VideoCapture(0)
    #
    ret, frame = vid.read()
    #
    plt.imshow(frame)
    plt.plot([0, CAMERA_DIMENSIONS_PIXELS[0]], [p[1]]*2, color='white', linewidth=3)
    plt.plot([p[0]]*2, [0, CAMERA_DIMENSIONS_PIXELS[1]], color='white', linewidth=3)
    #
    plt.show()
    #
    print(frame.shape)
    #
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
