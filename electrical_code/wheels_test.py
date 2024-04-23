from wheels import Wheels

# Instantiate the Wheels class with your port number
myFirstWheel = Wheels("COM5")


# Test movement commands
# myFirstWheel.move(1,000,110)
myFirstWheel.goForward(100)  # Go forward 100 units
myFirstWheel.goBackward(111)  # Go backward 50 units
# myFirstWheel.turnRight("90")  # Turn right by 90 degrees
# myFirstWheel.turnLeft("45")  # Turn left by 45 degrees

