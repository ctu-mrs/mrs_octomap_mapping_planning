#!/usr/bin/env python3

import launch
import os
import sys

from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import ComposableNodeContainer, LoadComposableNodes
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import (
        LaunchConfiguration,
        IfElseSubstitution,
        PythonExpression,
        PathJoinSubstitution,
        EnvironmentVariable,
        )

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    ld = launch.LaunchDescription()

    # #{ uav_name

    uav_name = LaunchConfiguration('uav_name')

    ld.add_action(DeclareLaunchArgument(
        'uav_name',
        default_value=os.getenv('UAV_NAME', "uav1"),
        description="The uav name used for namespacing.",
    ))

    # #} end of custom_config

    # #{ standalone

    standalone = LaunchConfiguration('standalone')

    declare_standalone = DeclareLaunchArgument(
        'standalone',
        default_value='false',
        description='Whether to start a as a standalone or load into an existing container.'
    )

    ld.add_action(declare_standalone)

    # #} end of standalone

    # #{ custom_config

    custom_config = LaunchConfiguration('custom_config')

    # this adds the args to the list of args available for this launch files
    # these args can be listed at runtime using -s flag
    # default_value is required to if the arg is supposed to be optional at launch time
    ld.add_action(DeclareLaunchArgument(
        'custom_config',
        default_value="",
        description="Path to the custom configuration file. The path can be absolute, starting with '/' or relative to the current working directory",
        ))

    # behaviour:
    #     custom_config == "" => custom_config: ""
    #     custom_config == "/<path>" => custom_config: "/<path>"
    #     custom_config == "<path>" => custom_config: "$(pwd)/<path>"
    custom_config = IfElseSubstitution(
            condition=PythonExpression(['"', custom_config, '" != "" and ', 'not "', custom_config, '".startswith("/")']),
            if_value=PathJoinSubstitution([EnvironmentVariable('PWD'), custom_config]),
            else_value=custom_config
            )

    # #} end of custom_config

    # #{ use_sim_time

    use_sim_time = LaunchConfiguration('use_sim_time')

    ld.add_action(DeclareLaunchArgument(
        'use_sim_time',
        default_value=os.getenv('USE_SIM_TIME', "false"),
        description="Should the node subscribe to sim time?",
    ))

    # #} end of custom_config

    # #{ subscriber topics through arguments

    # id 0

    # #{ lidar_3d_0

    lidar_3d_0 = LaunchConfiguration('lidar_3d_0')

    ld.add_action(DeclareLaunchArgument(
        'lidar_3d_0',
        default_value='~/lidar_3d_0/points_in',
        description='Lidar 3D #0 points topic'
    ))

    # #} end of lidar_3d_0

    # #{ lidar_3d_0_free

    lidar_3d_0_free = LaunchConfiguration('lidar_3d_0_free')

    ld.add_action(DeclareLaunchArgument(
        'lidar_3d_0_free',
        default_value='~/lidar_3d_0/free_points_in',
        description='Lidar 3D #0 free points topic'
    ))

    # #} end of lidar_3d_0_free

    # #{ depth_camera_0

    depth_camera_0 = LaunchConfiguration('depth_camera_0')

    ld.add_action(DeclareLaunchArgument(
        'depth_camera_0',
        default_value='~/depth_camera_0/points_in',
        description='Depth camera #0 points topic'
    ))

    # #} end of depth_camera_0

    # #{ camera_info_0

    camera_info_0 = LaunchConfiguration('camera_info_0')

    ld.add_action(DeclareLaunchArgument(
        'camera_info_0',
        default_value='~/depth_camera/camera_info_in',
        description='Depth camera #0 info'
    ))

    # #} end of camera_info_0

    # #{ depth_camera_0_free

    depth_camera_0_free = LaunchConfiguration('depth_camera_0_free')

    ld.add_action(DeclareLaunchArgument(
        'depth_camera_0_free',
        default_value='~/depth_camera_0/free_points_in',
        description='Depth camera #0 free points topic'
    ))

    # #} end of depth_camera_0_free

    # id 1

    # #{ lidar_3d_1

    lidar_3d_1 = LaunchConfiguration('lidar_3d_1')

    ld.add_action(DeclareLaunchArgument(
        'lidar_3d_1',
        default_value='~/lidar_3d_1/points_in',
        description='Lidar 3D #0 points topic'
    ))

    # #} end of lidar_3d_1

    # #{ lidar_3d_1_free

    lidar_3d_1_free = LaunchConfiguration('lidar_3d_1_free')

    ld.add_action(DeclareLaunchArgument(
        'lidar_3d_1_free',
        default_value='~/lidar_3d_1/free_points_in',
        description='Lidar 3D #0 free points topic'
    ))

    # #} end of lidar_3d_1_free

    # #{ depth_camera_1

    depth_camera_1 = LaunchConfiguration('depth_camera_1')

    ld.add_action(DeclareLaunchArgument(
        'depth_camera_1',
        default_value='~/depth_camera_1/points_in',
        description='Depth camera #0 points topic'
    ))

    # #} end of depth_camera_1

    # #{ camera_info_1

    camera_info_1 = LaunchConfiguration('camera_info_1')

    ld.add_action(DeclareLaunchArgument(
        'camera_info_1',
        default_value='~/depth_camera/camera_info_in',
        description='Depth camera #0 info'
    ))

    # #} end of camera_info_1

    # #{ depth_camera_free_1

    depth_camera_1_free = LaunchConfiguration('depth_camera_1_free')

    ld.add_action(DeclareLaunchArgument(
        'depth_camera_1_free',
        default_value='~/depth_camera_1/free_points_in',
        description='Depth camera #0 free points topic'
    ))

    # #} end of depth_camera_1_free

    # #} end of topics in

    # #{ frame ids

    # #{ world_frame

    world_frame = LaunchConfiguration('world_frame')

    ld.add_action(DeclareLaunchArgument(
        'world_frame',
        default_value=[uav_name, "/fixed_origin"],
        description='The frame id of the world frame for the mapping.'
    ))

    # #} end of world_frame

    # #{ robot_frame

    robot_frame = LaunchConfiguration('robot_frame')

    ld.add_action(DeclareLaunchArgument(
        'robot_frame',
        default_value=[uav_name, "/fcu"],
        description='The frame id of the robots body.',
    ))

    # #} end of robot_frame

    # #} end of frame ids

    container_name = ["/", uav_name, "/mapplan_container"]

    mapplan_container = ComposableNodeContainer(
        namespace=uav_name,
        name='mapplan_container',
        package='rclcpp_components',
        executable='component_container_mt',
        output="screen",
        parameters=[
            {'use_intra_process_comms': True},
            {'thread_num': os.cpu_count()},
            {'use_sim_time': use_sim_time},
        ],
        # prefix=['debug_roslaunch ' + os.ttyname(sys.stdout.fileno())],
        # prefix="valgrind --tool=memcheck --leak-check=no --track-origins=no --show-reachable=no --errors-for-leak-kinds=definite --num-callers=12",
        condition=UnlessCondition(standalone)
    )

    ld.add_action(mapplan_container)

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_octomap_server'), '/launch/octomap_server.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'standalone': standalone,
                'container_name': container_name,
                "world_frame": world_frame,
                "robot_frame": robot_frame,
                # sensors #0
                "lidar_3d_0": lidar_3d_0,
                "lidar_3d_0_free": lidar_3d_0_free,
                "depth_camera_0": depth_camera_0,
                "depth_camera_0_free": depth_camera_0_free,
                "camera_info_0": camera_info_0,
                # sensors #1
                "lidar_3d_1": lidar_3d_1,
                "lidar_3d_1_free": lidar_3d_1_free,
                "depth_camera_1": depth_camera_1,
                "depth_camera_1_free": depth_camera_1_free,
                "camera_info_1": camera_info_1,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_octomap_planner'), '/launch/octomap_planner.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    return ld
