import cv2
import serial

"""
camera
navigation movement
sensors (lidar)
navigation algorithm
"""


def main():
    ser = serial.Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', 9600)

    try:
        distance = True
        while True:
            data = ser.readline().decode().strip()
            if distance:
                print("Distance:", data)
                distance = not distance
            else:
                print("Strength:", data)
                distance = not distance
    except KeyboardInterrupt:
        ser.close()


if __name__ == "__main__":
    main()
