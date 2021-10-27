#!/bin/bash

set -e

trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
trap 'echo "$0: \"${last_command}\" command failed with exit code $?"' ERR

# get the path to this script
MY_PATH=`dirname "$0"`
MY_PATH=`( cd "$MY_PATH" && pwd )`

unattended=0
subinstall_params=""
for param in "$@"
do
  echo $param
  if [[ $param == "--unattended" ]]; then
    echo "installing in unattended mode"
    unattended=1
    subinstall_params="--unattended"
  fi
done

cd "$MY_PATH"
gitman install

## | ------------------------- planner ------------------------ |
bash $MY_PATH/../ros_packages/mrs_octomap_planner/install/install.sh $subinstall_params

echo "$0: Done"
