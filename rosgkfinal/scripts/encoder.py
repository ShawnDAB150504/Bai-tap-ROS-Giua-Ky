#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState

def joint_state_callback(msg):
    # Danh sách các khớp cần hiển thị
    joints_to_display = ['right_front_omni', 'right_back_omni', 'left_back_omni', 'left_front_omni']
    
    # Duyệt qua danh sách khớp và hiển thị giá trị
    for i, joint_name in enumerate(msg.name):
        if joint_name in joints_to_display:
            position = msg.position[i]
            velocity = msg.velocity[i] if i < len(msg.velocity) else 0.0  # Đảm bảo không lỗi nếu velocity rỗng
            rospy.loginfo("%s: Position = %.3f rad, Velocity = %.3f rad/s", joint_name, position, velocity)

def encoder_display():
    # Khởi tạo node
    rospy.init_node('encoder', anonymous=True)
    
    # Đăng ký subscriber để đọc topic /joint_states
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)
    
    # Giữ node chạy
    rospy.loginfo("Hiển thị giá trị encoder của các khớp...")
    rospy.spin()

if __name__ == '__main__':
    try:
        encoder_display()
    except rospy.ROSInterruptException:
        pass
