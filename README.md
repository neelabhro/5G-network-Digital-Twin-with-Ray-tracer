# 5G-network-Digital-Twin-with-Ray-tracer
Software for 3D model of KTH R1: https://www.blender.org/
Software for Ray tracer: MATLAB
Other softwares of interest: Unity 3D, Nvidia Sionna

  
Tips for setup and connection:
1. When the robot automatically connects the wifi, just read the ip from the screen and SSH into the Raspberry Pi. Password: turtlebot4
2. When the ip of the robot is unknown, connect directly to the Raspberry Pi using an ethernet cable(ssh ubuntu@192.168.185.3). Don't forget to configure the wired connection to use the same subnet: 
![image](https://github.com/user-attachments/assets/7cea9ef2-949e-4f1b-80ea-e887f8688b62)
After that, use command: turtlebot4-setup, navigate to the "Wi-Fi Setup" menu and configure wifi connection.(SSID: KTH-IoT password: Robot12!)
3. Before using any ros2 command, enter this command first: source /opt/ros/humble/setup.bash

  
Packages for signal strength:

sudo apt install net-tools

sudo apt install iw

Commands for measuring signal strength:  

iwconfig wlan0  

sudo iw dev wlan0 station dump

Navigation Part:
1. SLAM (create the map):

sudo apt install ros-humble-turtlebot4-navigation

ros2 launch turtlebot4_navigation slam_sync.launch.py

ros2 launch turtlebot4_navigation slam_async.launch.py

2. Rviz2 (visualize the map):

ros2 launch turtlebot4_viz view_robot.launch.py
