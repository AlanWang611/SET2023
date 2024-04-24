import serial
import socket
import cv2

"""
camera
navigation movement
sensors (lidar)
navigation algorithm
"""

# def main():
#     ser = serial.Serial('/dev/ttyUSB0', 9600)
#
#     try:
#         distance = True
#         while True:
#             data = ser.readline().decode().strip()
#             if distance:
#                 print("Distance:", data)
#                 distance = not distance
#             else:
#                 print("Strength:", data)
#                 distance = not distance
#     except KeyboardInterrupt:
#         ser.close()




HOST = "10.138.148.113"
PORT = 65432

def main():
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    try:
        data = ser.readline().decode().strip()
        distance = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message = f"{data},{distance}"
            s.sendall(message.encode())
            distance = not distance
            data = s.recv(1024)
    except KeyboardInterrupt:
        ser.close()

    print(f"Received {data!r}")


if __name__ == "__main__":
    main()
