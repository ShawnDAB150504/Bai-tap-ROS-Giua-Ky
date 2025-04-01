#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import sys
import tty
import termios

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def arm_controller():
    rospy.init_node('arm_teleop_keyboard', anonymous=True)
    arm_1_pub = rospy.Publisher('/arm_1_controller/command', Float64, queue_size=10)
    arm_2_pub = rospy.Publisher('/arm_2_controller/command', Float64, queue_size=10)
    arm_1_pos = 0.0
    arm_2_pos = 0.0
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        key = get_key()
        if key == 'u':
            arm_2_pos += 0.5
            if arm_2_pos > 3.14:
                arm_2_pos = 3.14
        elif key == 'i':
            arm_2_pos -= 0.5
            if arm_2_pos < -3.14:
                arm_2_pos = -3.14
        elif key == 'j':
            arm_1_pos += 0.1
            if arm_1_pos > 0.6:
                arm_1_pos = 0.6
        elif key == 'k':
            arm_1_pos -= 0.1
            if arm_1_pos < 0.0:
                arm_1_pos = 0.0
        elif (key == 'p'):
            break
        arm_1_pub.publish(arm_1_pos)
        arm_2_pub.publish(arm_2_pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        arm_controller()
    except rospy.ROSInterruptException:
        pass
