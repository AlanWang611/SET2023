# SET Image Listener
# 1/23/2024

import time
# import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

# Function to call when new image is published
def callback(data):
    try:
        # Convert ROS Image message to OpenCV Image
        cv_image = bridge.imgmsg_to_cv2(data)

        print("Displaying Image...")

        # Display Image
        cv2.imshow("Subscriber Window", cv_image)

        cv2.waitKey(1)

    # Print error if something fails    
    except CvBridgeError as e:
        print(e)

def main():
    # Initialize this node
    rospy.init_node('image_listener', anonymous=True)

    # Create the Image Subscriber
    rospy.Subscriber("img_sub", Image, callback)

    # Keep running this program until keyboard is pressed
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()