import serial
import time

class Wheels:
    time_divisor = 10

    def __init__(self, port_num):
        self.arduino = serial.Serial(port=port_num, baudrate=115200, timeout=0.1)

    def write_serial(self, x):
        self.arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)

    def move(self, dir, angle, dist):
        direction_str = str(dir)
        angle_str = str(angle).zfill(3)
        dist_str = str(dist).zfill(3)
        command = dir + angle_str + dist_str
        self.write_serial(command)

    def turnRight(self, angle):
        command = "0" + str(angle).zfill(3) + "0000"
        self.write_serial(command)
        time.sleep(angle*(self.time_divisor)/1000)


    def turnLeft(self, angle):
        command = "1" + str(angle).zfill(3) + "0000"
        self.write_serial(command)
        time.sleep(angle*(self.time_divisor)/1000)


    def goForward(self, dist):
        print('hello')
        command = "00001" + str(dist).zfill(3)
        self.write_serial(command)
        time.sleep(dist*(self.time_divisor)/1000)


    def goBackward(self, dist):
        command = "00000" + str(dist).zfill(3)
        self.write_serial(command)
        time.sleep(dist*(self.time_divisor)/1000)


if __name__ == "__main__":
    myFirstWheel = Wheels("your_port_number_here")
    myFirstWheel.move(direction, angle_value, distance_value)
