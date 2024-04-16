from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

"""
camera
navigation movement
sensors (lidar)
navigation algorithm
"""


def main():
    net = detectNet("ssd-mobilenet-v2", threshold=0.5)
    camera = videoSource("csi://0")      # '/dev/video0' for V4L2

    img = camera.Capture()
    detections = net.Detect(img)


if __name__ == "__main__":
    main()
