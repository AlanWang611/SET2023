import serial
import time
import sys

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
def write_read(x):
   arduino.write(bytes(x, 'utf-8'))
   time.sleep(0.05)
   # data = arduino.readline()
   # return data

def move(angle, dist):
   dist, angle = str(dist), str(angle)
   angle = '0' * (3 - len(angle))  + angle
   dist = '0' * (3 - len(dist)) + dist
   command = angle + dist
   write_read(command)
   # print(command)

while True:
    move(100, 431)
'''

while True:
   command = sys.stdin.readline() # Taking input from user
   comm1 = write_read(command)
   print(command) # printing the value
   '''