import time

import cv2
from PIL import Image

image_count = 0
SAVE_DIR = ""


def read_image(cap: cv2.VideoCapture, save_directory):
    global image_count
    _, frame = cap.read()
    im = Image.fromarray(frame)
    save_path = save_directory + '/' + str(image_count) + '.jpg'
    image_count += 1
    im.save(save_path)
    return save_path


def main():
    cap = cv2.VideoCapture('/dev/video0')
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    for i in range(10):
        read_image(cap, 'images')
        print("Sleep")
        time.sleep(3)


if __name__ == "__main__":
    main()
