# Bai-tap-ROS-Giua-Ky

Bài tập mô phỏng về xe omni 4 bánh có 2 khớp tay:
   Khớp 1: khớp tịnh tiến
   Khớp 2: khớp xoay 

Đi theo cùng là cảm biến IMU, Camera và Encoder

Bài tập được mô phỏng trên gazebo và vriz 

Các bước để chạy được package: 
B1: Đưa package vào catkin_ws/src
B2: Quay trở lai về catkin_ws và chạy dòng catkin_make sau khi đã catkin_make thì tạo source bằng lệnh source ~/.bashrc  
B3: Tạo quyền truy cập cho các file trong thư mục bằng các dòng lệnh sau:
'chmod +x controller.py'
chmod +x encoder.py
chmod +x jointcontrol.py
B4: Khởi chạy đồng thời cả Gazebo và Rviz bằng dòng lệnh: roslaunch rosgkfinal gazebo.launch
B5: Điều khiển robot: 
- w: tiến
- s: lùi
- q: rẽ phải
- e: rẽ trái
- j: tịnh tiến tay máy đi lên
- k: tịnh tiến tay máy đi xuống
- u: Xoay tay máy ra trước
- i: Xoay tay máy về hướng ngược lại
B6: Đọc các giá trị cảm biến bằng các dòng lệnh sau:
  rostopic echo /imu (chạy cảm biến imu)
  rosrun rosgkfinal encoder.py (chạy encorder)
