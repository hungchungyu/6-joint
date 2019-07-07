#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)#topic名稱，訊息格式,可以放幾個訊息
    rospy.init_node('talker', anonymous=True)#anonymous=True是表示要不要匿名
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "hello world"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:#攔截錯誤發生時，所產生的錯誤訊息
        pass