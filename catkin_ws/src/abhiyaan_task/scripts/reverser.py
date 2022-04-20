#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# function to reverse a string
def reverse(string):
    return " ".join([i[::-1] for i in string.split()])


def callback(data):
    pub = rospy.Publisher(reverse('team_abhiyaan'), String, queue_size=10)

    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown():
        reverse_str = reverse(data.data)
        rospy.loginfo(reverse_str)
        pub.publish(reverse_str)
        rate.sleep()

def reverser():
    rospy.init_node('reverser', anonymous=True)

    rospy.Subscriber("/team_abhiyaan", String, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        reverser()
    except rospy.ROSInterruptException:
        pass
