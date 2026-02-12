cmake_minimum_required(VERSION 3.8)
project(mrs_octomap_mapping_planning)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(
  ${DEPENDENCIES}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# install(
#   DIRECTORY config
#   DESTINATION share/${PROJECT_NAME}
# )

install(
  DIRECTORY tmux
  USE_SOURCE_PERMISSIONS
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
