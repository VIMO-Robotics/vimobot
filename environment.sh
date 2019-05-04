#!/bin/bash

# Do not compile Lisp messages
# XXX: not sure if this is the place to put this.
export ROS_LANG_DISABLE=gennodejs:geneus:genlisp

shell=`basename $SHELL`
echo "Activating ROS with shell: $SHELL"
source /opt/ros/kinetic/setup.$shell
if [ 2015 -ge $(date +%Y) ];
then
    >&2 echo "Error! Time travel detected. System time is: $(date)"
fi

exec "$@" #Passes arguments. Need this for ROS remote launching to work.

source $HOME/vimobot/catkin_ws/devel/setup.bash