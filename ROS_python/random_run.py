#!/usr/bin/env python
import rospy
import random
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def random_run():
    rospy.init_node('random_run', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10) 
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rand = random.uniform(0,1)     #random value 0 to 1
        cmd = Twist()
        cmd.linear.x = rand
        cmd.angular.z = rand*5-3
        rospy.loginfo("linear= %f", cmd.linear.x) 
        rospy.loginfo("angular= %f", cmd.angular.z) 
        pub.publish(cmd)
        rate.sleep()    #Interval time


if __name__ == '__main__':
	try:
		random_run()
	except rospy.ROSInterruptException:     ##error hanndle
		pass
