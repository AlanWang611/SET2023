#Tiger Cao
#1/15/2024

import math

def main():
    #main loop
    while True:
        #calls method to get data
        output=process.stdout.readline().decode('utf-8').strip()
        if output:
            print("Received:", output)


        # #fill headers of point cloud message
        # lidar_msg.header.stamp=rospy.Time.now()
        # lidar_msg.header.frame_id="placeholder" #replace with SET Robot base link
        #
        # #for points in lidar_data retrieved, convert to x y
        # for point in lidar_data:
        #     x = point * math.cos(0) # replace 0 with angle given in parsed data
        #     y = point * math.sin(0) # replace 0 with angle given in parsed data
        #     z=0.0
        #     #populate point cloud message with points
        #     lidar_msg.points.append(Point32(x=x, y=y, z=z))
        #
        # #pulish
        # lidar_pub.publish(lidar_msg)
        #
        # #sleep to match publishing rate
        # rate.sleep()



#method to get parsed Lidar data
def get_parsed_lidar():
    pass


if __name__ == '__main__':
    main()

