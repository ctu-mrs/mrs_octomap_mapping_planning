cmake_minimum_required(VERSION 3.5)
project(octomap_mapping_planning)

set(PACKAGE_DEPENDENCIES
  )

find_package(catkin REQUIRED COMPONENTS ${PACKAGE_DEPENDENCIES})

catkin_package(
  # INCLUDE_DIRS include
  CATKIN_DEPENDS ${PACKAGE_DEPENDENCIES}
  )
