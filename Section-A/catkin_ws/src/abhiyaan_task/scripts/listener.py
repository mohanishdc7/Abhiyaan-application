#!usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("%s", data.data)

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("team_abhiyaan", String, callback)
    
    # spin() simply keeps python from exiting until this node is stopped 
    rospy.spin()

if __name__ == '__main__':
    listener()
