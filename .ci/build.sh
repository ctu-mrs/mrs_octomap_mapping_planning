#!/bin/bash
set -e

distro=`lsb_release -r | awk '{ print $2 }'`
[ "$distro" = "18.04" ] && ROS_DISTRO="melodic"
[ "$distro" = "20.04" ] && ROS_DISTRO="noetic"

[ -z "$GITHUB_CI" ] && N_PROC="-j$[$(nproc) - 1]"
[ ! -z "$GITHUB_CI" ] && N_PROC="-j$[$(nproc) / 2]"

echo "Starting build using $N_PROC threads"
cd ~/catkin_ws
source /opt/ros/$ROS_DISTRO/setup.bash
catkin build --limit-status-rate 0.2 --summarize $N_PROC
echo "Ended build"
