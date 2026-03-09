# ROS2 ROV Camera Streaming System

## Overview

This project implements a simple ROS2-based system for streaming camera data from a robot/ROV and making it available through a web interface. The system integrates ROS2 nodes with MAVROS communication and a lightweight web server for visualization.

The repository is structured as a ROS2 workspace containing a Python package named **rov**.

---

## System Architecture

Camera Node → ROS2 Topic → Web Server → Browser View

Components:

* **camera.py** – Captures video from the webcam and publishes frames.
* **mavros.py** – Handles communication with MAVROS for integration with vehicle telemetry.
* **website.py** – Hosts a web interface to stream the camera feed.

---

## Workspace Structure

```
sub_ws
│
├── src
│   └── rov
│       ├── rov
│       │   ├── camera.py
│       │   ├── mavros.py
│       │   └── website.py
│       │
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
│
├── build
├── install
├── log
└── README.md
```

---

## Requirements

* ROS2 (Humble or compatible)
* Python 3
* MAVROS
* OpenCV

Check MAVROS installation:

```
ros2 pkg list | grep mavros
```

---

## Build Instructions

Navigate to the workspace:

```
cd ~/sub_ws
```

Build the workspace:

```
colcon build
```

Source the workspace:

```
source install/setup.bash
```

---

## Running the System

Run individual nodes depending on functionality.

Example:

```
ros2 run rov camera
```

This will start the camera node and publish video frames.

---

## Notes

* The `build`, `install`, and `log` directories are ignored in version control.
* The repository only tracks the ROS2 package source code.

---

## Author

Amrutha S Araballi
