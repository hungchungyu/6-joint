#!/usr/bin/env python
import rospy
import random
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data): 
    rospy.loginfo("(x=%f, y=%f)", data.x, data.y) 
    rospy.loginfo("theta= %f", data.theta) 

def get_turtle_fb():
    rospy.init_node('get_turtle', anonymous=True)
    rospy.Subscriber("turtle1/pose",Pose ,callback) 
    rospy.spin()    

if __name__ == '__main__':
	try:
		get_turtle_fb()
	except rospy.ROSInterruptException:     ##error hanndle
		pass