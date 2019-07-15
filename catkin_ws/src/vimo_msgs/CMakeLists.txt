cmake_minimum_required(VERSION 2.8.3)
project(vimo_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

add_message_files(
  FILES
  motor_pwm.msg
)

add_service_files(
   FILES
   SetValue.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
   geometry_msgs
   sensor_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES robotx_msgs
   CATKIN_DEPENDS 
   geometry_msgs 
   message_runtime 
   roscpp 
   rospy 
   sensor_msgs 
   std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)