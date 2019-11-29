cmake_minimum_required(VERSION 2.8.3)
project(tf2_client)

find_package(catkin REQUIRED
    COMPONENTS
        roscpp
        rospy
        tf2
        tf2_ros
)

catkin_python_setup()

catkin_package(
    CATKIN_DEPENDS
        roscpp
        rospy
        tf2
        tf2_ros
    INCLUDE_DIRS include
    LIBRARIES ${PROJECT_NAME}
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_library(${PROJECT_NAME} src/tf2_client.cpp)
link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})

install(DIRECTORY include/${PROJECT_NAME}/
    DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)
install(TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)