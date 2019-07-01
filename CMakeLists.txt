cmake_minimum_required(VERSION 2.8.3)
project(tf2_client)

find_package(catkin REQUIRED COMPONENTS rospy tf2_ros)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS rospy tf2_ros
)
