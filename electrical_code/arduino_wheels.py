import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
time_divisor = 10

def write_serial(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)


def turnRight(angle):
    command = "0" + str(angle).zfill(3) + "0000"
    write_serial(command)
    time.sleep(angle * (time_divisor) / 1000)


def turnLeft(angle):
    command = "1" + str(angle).zfill(3) + "0000"
    write_serial(command)
    time.sleep(angle * (time_divisor) / 1000)


def goForward(dist):
    print('hello')
    command = "00001" + str(dist).zfill(3)
    print("forward: " + command)
    write_serial(command)
    time.sleep(dist * (time_divisor) / 1000)


def goBackward(dist):
    command = "00000" + str(dist).zfill(3)
    print("backward: " + command)
    write_serial(command)
    time.sleep(dist * (time_divisor) / 1000)

if __name__ == "__main__":
    goForward(100)
    time.sleep(2)