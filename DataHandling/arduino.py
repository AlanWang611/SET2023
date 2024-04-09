import serial
import math

# Configure the serial port. Change the port and baud rate as needed.
# 50 units is equal to 1 CM
ser = serial.Serial('/dev/cu.usbmodem101', 9600)  # COM3 is an example, you need to specify your port

try:
    distance = True
    while True:
        data = ser.readline().decode().strip()
        if distance:
            print("Distance:", data/50)
            distance = not distance
        else:
            print("Strength:", data)
            distance = not distance
except KeyboardInterrupt:
    ser.close()  # Close the serial port on Ctrl+C


def convert_xy(angle, distance):
    angle_radians = math.radians(angle)

    # Calculate the relative x and y coordinates
    x = distance * math.cos(angle_radians)
    y = distance * math.sin(angle_radians)

    return x, y



