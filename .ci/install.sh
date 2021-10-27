#!/bin/bash
set -e

distro=`lsb_release -r | awk '{ print $2 }'`
[ "$distro" = "18.04" ] && ROS_DISTRO="melodic"
[ "$distro" = "20.04" ] && ROS_DISTRO="noetic"

echo "Starting install"

MY_PATH=`pwd`

sudo apt-get -y install git

## | ------------------------ uav core ------------------------ |

echo "clone uav_core"
cd
git clone https://github.com/ctu-mrs/uav_core.git
cd uav_core

echo "running the main install.sh"
./installation/install.sh

cd $MY_PATH
gitman install

echo "running the uav_modules install.sh"
./installation/install.sh --unattended

## | ----------------------- uav modules ---------------------- |

echo "clone uav_modules"
cd
git clone https://github.com/ctu-mrs/uav_modules.git
cd uav_core

echo "running the main install.sh"
./installation/install.sh

cd $MY_PATH
gitman install

echo "running the uav_modules install.sh"
./installation/install.sh --unattended

## | ---------------- octomap mapping planning ---------------- |

"$MY_PATH"/installation/install.sh

## | ------------------ link the repositories ----------------- |

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
ln -s ~/uav_core
ln -s ~/uav_modules
ln -s "$MY_PATH" octomap_mapping_planning
source /opt/ros/$ROS_DISTRO/setup.bash
cd ~/catkin_ws

echo "install ended"
