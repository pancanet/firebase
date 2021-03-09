#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    r = rospy.Rate(20) # 10hz
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    sspeed = input("Input your speed:")
    speed = int(sspeed) 
    while not rospy.is_shutdown():

        #After the loop, stops the robot
        vel_msg.linear.x = speed
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        r.sleep()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
