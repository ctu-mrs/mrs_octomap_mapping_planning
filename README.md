# Octomap Mapping & Planning

Metapackage containing MRS Octomap-based 3D mapper and planner.

![](./.fig/octomap_server.png)

| Build status | [![Build Status](https://github.com/ctu-mrs/octomap_mapping_planning/workflows/Noetic/badge.svg)](https://github.com/ctu-mrs/octomap_mapping_planning/actions) |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Dependencies

* [uav_core](http://github.com/ctu-mrs/uav_core)
* [uav_modules](http://github.com/ctu-mrs/uav_modules)

## Packages

* octomap_mapping_planning - launch files, example tmux session
* [mrs_octomap_server](https://github.com/ctu-mrs/mrs_octomap_server) - Uses Octomap to build global & local map
* [mrs_octomap_planner](https://github.com/ctu-mrs/mrs_octomap_planner) - 3D planner for UAVs
* [octomap](https://github.com/ctu-mrs/octomap) - Custom fork of the original Octomap
* [octomap_tools](https://github.com/ctu-mrs/octomap_tools) - MRS Tools and libraries for Octomap
* [octomap_ros](https://github.com/ctu-mrs/octomap_ros)
* [octomap_rviz_plugins](https://github.com/ctu-mrs/octomap_rviz_plugins)
* [octomap_msgs](https://github.com/ctu-mrs/octomap_msgs)

## Example session

Example tmuxinator session is provided in `tmux/example/`.

## Main launch file

The [launch file](./ros_packages/octomap_mapping_planning/launch/mapplan.launch)
```
./ros_packages/octomap_mapping_planning/launch/mapplan.launch
```
was prepared to launch

* PointCloud filter ([mrs_pcl_tools](https://github.com/ctu-mrs/mrs_pcl_tools)),
* Octomap server,
* Octomap Planner,
* Octomap RVIZ visualizer,
* Nodelet manager.

Plase, use provided arguments and custom config files to customize the behaviour of the nodes.
