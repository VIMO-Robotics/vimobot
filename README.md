# VIMOBot
This is for an indoor robot project

|Reference | Link |
|-------|--------|
|NCTU ARG website		|[Assistive Robotics Group](https://arg-nctu.github.io)|

# Requirements environment

- ROS kinetic 
- Ubuntu 16.04
- PCL (Point Cloud Library)
- OpenCV ?
- CUDA ?
- Docker

# Hardware

|Name | Type |
|-------		|--------					|
|Vehicle		|VIMOBot					|
|IMU			|SparkFun 9DoF Razor IMU M0 |
|Laser Scanner	|YPLIDAR G4     			|
|Camera			|Pi Camera					|
|Depth Camera	|Realsense D435				|

# Rule for this repo
1. Make your own branch and do your work on your branch
2. Your branch name should be: "**devel-[your name]**"
3. Please add someone else as the reviewer when you fire a pull request

# Repo Architecture
![](https://github.com/RobotX-NCTU/robotx_nctu/blob/master/img/repo_architecture.jpg)

# Installation

## Driver
```
```

## Package

```
$ sudo apt-get install ros-kinetic-desktop-full
```

# How to build

## For ROS
```
$ cd
$ git clone https://github.com/vimo-robotics/vimobot.git
$ cd ~/vimobot/catkin_ws
$ source /opt/ros/kinetic/setup.bash
- Compile the package
$ catkin_make
```

Note:

Do the following everytime as you open new terminals
```
$ cd ~/vimobot/
$ source environment.sh
```
