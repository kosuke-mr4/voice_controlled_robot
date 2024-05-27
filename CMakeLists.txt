cmake_minimum_required(VERSION 3.0.2)
project(voice_controlled_robot)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  geometry_msgs
  rospy
  sensor_msgs
  std_msgs
)

# Enable catkin python setup
catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS gazebo_ros geometry_msgs rospy sensor_msgs std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Install Python scripts
catkin_install_python(PROGRAMS
  scripts/voice_controlled_robot_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
