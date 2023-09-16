cmake_minimum_required(VERSION 3.16)
project(mrs_octomap_mapping_planning)

find_package(catkin REQUIRED)

catkin_package()

## --------------------------------------------------------------
## |                           Install                          |
## --------------------------------------------------------------

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )

install(DIRECTORY tmux/
  USE_SOURCE_PERMISSIONS
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/tmux
  )
