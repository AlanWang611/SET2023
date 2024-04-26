import os
from enum import IntEnum
import time
import shutil
import math

from PIL import Image
import cv2
# import serial
import requests
from pp.distance_measurement import bounding_box_angle, distance_estimation
from pp.config import *


"""
camera
navigation movement
sensors (lidar)
navigation algorithm


e-meet camera
horizontal: 68.61668666 degrees
vertical: 65.68702522 z
at 640x480
"""


class RobotState(IntEnum):
    SEEKING_TRASH = 0
    MOVING_TO_TRASH = 1
    AT_TRASH = 2


class TrashTarget:
    def __init__(self, horizontal_angle: float, distance: float):
        self.horizontal_angle = horizontal_angle
        self.distance = distance


class RobotStateVariables:
    def __init__(self, robot_state: RobotState, trash_target: TrashTarget):
        self.robot = Robot()
        self.robot_state = robot_state
        self.trash_target = trash_target


class Robot:
    def rotate(self, angle_rad: float):
        pass

    def move_forward(self, distance_meters: float):
        pass

    def collect_trash(self):
        pass


image_count = 0
YOLO_INFERENCE_SERVER_ADDRESS = os.environ.get('YOLO_INFERENCE_SERVER_ADDRESS')
IMAGE_SAVE_DIR = os.environ.get('IMAGE_SAVE_DIR')


def setup():

    if not os.path.exists(IMAGE_SAVE_DIR):
        os.makedirs(IMAGE_SAVE_DIR)
    else:
        for filename in os.listdir(IMAGE_SAVE_DIR):
            file_path = os.path.join(IMAGE_SAVE_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    # make image saving directory if not already
    # if it exists already clear it
    # check if yolo inference server is running

    pass


def read_image(cap: cv2.VideoCapture, save_directory):
    global image_count
    _, frame = cap.read()
    im = Image.fromarray(frame)
    save_path = save_directory + '/' + str(image_count) + '.jpg'
    image_count += 1
    im.save(save_path)
    return save_path


def do_yolo_inference(image_path: str) -> dict:
    with open(image_path, 'rb') as f:
        data = f.read()

    print("Sending image")
    r = requests.post(YOLO_INFERENCE_SERVER_ADDRESS, data=data)
    resp = r.json()
    return resp


def do_seeking_trash(robot_state: RobotStateVariables, cap: cv2.VideoCapture):
    image_path = read_image(cap, IMAGE_SAVE_DIR)
    yolo_results = do_yolo_inference(image_path)
    if len(yolo_results) == 0:
        return
    first_piece_of_trash = yolo_results[0]
    box = first_piece_of_trash['box']
    x1, y1, x2, y2 = box['x1'], box['y1'], box['x2'], box['y2']
    p = ((x1 + x2) / 2, y1)
    res1 = bounding_box_angle([p], CAMERA_DIMENSIONS_PIXELS, CAMERA_FOV_RADIANS)
    res2 = distance_estimation(res1[0], CAMERA_HEIGHT_ABOVE_GROUND_METERS)

    robot_state.trash_target = TrashTarget(res1[0][0], math.sqrt(pow(res2[0], 2) + pow(res2[1], 2)))


def do_moving_to_trash(robot_state: RobotStateVariables, cap: cv2.VideoCapture):
    if robot_state.trash_target is None:
        robot_state.robot_state = RobotState(0)
        return

    robot_state.robot.rotate(robot_state.trash_target.horizontal_angle)
    robot_state.robot.move_forward(robot_state.trash_target.distance)


def do_at_trash(robot_state: RobotStateVariables, cap: cv2.VideoCapture):
    robot_state.robot.collect_trash()



handler_functions = {
    0: do_seeking_trash,
    1: do_moving_to_trash,
    2: do_at_trash,
}


def main():
    cap = cv2.VideoCapture('/dev/video0')
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    state = RobotStateVariables(RobotState(0), None)
    setup()

    # main loop
    while True:
        (handler_functions[state.robot_state])(state, cap)
        time.sleep(1)


if __name__ == "__main__":
    main()
