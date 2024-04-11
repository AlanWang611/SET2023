import serial
import time

class Wheels:
    def __init__(self, port_num):
        self.arduino = serial.Serial(port=port_num, baudrate=115200, timeout=0.1)

    def write_read(self, x):
        self.arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)

    def move(self, angle, dist):
        angle_str = str(angle).zfill(3)
        dist_str = str(dist).zfill(3)
        command = angle_str + dist_str
        self.write_read(command)

if __name__ == "__main__":
    myFirstWheel = Wheels("your_port_number_here")
    myFirstWheel.move(angle_value, distance_value)
