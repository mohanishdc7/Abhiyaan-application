#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("team_abhiyaan", String, queue_size=10)
    rospy.init_node("talker", anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    while not rospy.is_shutdown():
        cheer_str = "Team Abhiyaan Rocks"
      # rospy.loginfo(cheer_str)
        pub.publish(cheer_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
