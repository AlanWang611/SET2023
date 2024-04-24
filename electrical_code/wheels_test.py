from wheels import Wheels
import serial

while True:
    arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

    # Instantiate the Wheels class with your port number
    myFirstWheel = Wheels('COM5')

    # Test movement commands
    # myFirstWheel.move(1,000,110)
    # myFirstWheel.goForward(100)  # Go forward 100 units
    myFirstWheel.move("", 100, 431)
    # myFirstWheel.goBackward(111)  # Go backward 50 units
    # myFirstWheel.turnRight("90")  # Turn right by 90 degrees
    # myFirstWheel.turnLeft("45")  # Turn left by 45 degrees
