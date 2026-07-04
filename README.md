# Wafer Automation Cell

### PLC-Controlled Multi-Robot Semiconductor Handling System

🚀 A semiconductor wafer-handling automation system combining collaborative robotics, industrial controls, computer vision, and real-time system integration.

---

# Demo

<p align="center">
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/VID_20260505_194533-ezgif.com-video-to-gif-converter.gif" width="750"/>
</p>

---

# System Overview

This project integrates:

* Dobot M1 SCARA Robot
* Elephant Robotics Pro600 6-DoF Cobot
* Allen Bradley Micro820 PLC
* Sensor-Driven Conveyor System
* Camera-Based Inspection Station
* Python-Based Robot Communication and Automation
* Custom HMI Interface
* CAD-Designed & 3D-Printed Fixtures / End Effectors

The system autonomously transfers semiconductor wafers between robotic stations while coordinating sensors, conveyors, PLC logic, robot motion, and inspection stages.

---

# Full Automation Cell

<p align="center">
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Gemini_Generated_Image_krdefukrdefukrde.png" width="750"/>
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot1.png" width="750"/>
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot2.png" width="750"/>
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot3.png" width="750"/>
</p>

---

# HMI Interface

<p align="center">
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/WhatsApp%20Image%202026-05-08%20at%2018.45.39%20(1).jpeg" width="650"/>
</p>

The HMI was designed to:

* Start / Stop the automation process
* Display process stage and system state
* Track wafer count
* Monitor overall automation workflow

---

# Automation Workflow

1. Dobot M1 SCARA robot retrieves wafers from a stacked rack
2. Wafer is transferred onto the conveyor stand
3. Infrared sensors trigger conveyor movement
4. Conveyor pauses at camera station for image capture and assessment
5. Conveyor advances to robotic transfer location
6. Pro600 cobot retrieves wafer and places it onto a rotating platform
7. Conveyor returns to starting position
8. Process repeats autonomously

---

# Engineering Challenges

⚡ Reliable robot-to-robot synchronization
⚡ Ethernet/TCP robot communication in Python
⚡ PLC-style I/O logic and relay interfacing
⚡ Industrial sourcing/sinking compatibility
⚡ Dynamic waypoint generation and inverse kinematics
⚡ Multi-device system integration
⚡ Real-time debugging and hardware synchronization
⚡ CAD design and rapid prototyping of custom fixtures and end effectors

---

# Technologies Used

## Robotics

* Dobot M1 SCARA
* Elephant Robotics Pro600
* RoboFlow

<p align="center">
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot%202026-05-05%20191945.png" width="420"/>
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot%202026-05-11%20161342.png" width="420"/>
</p>

---

## Controls & Automation

* Allen Bradley Micro820 PLC
* Ladder Logic
* Industrial I/O Relays
* Infrared Sensors

---

## Software

* Python
* TCP/Ethernet Communication
* Computer Vision
* Inverse Kinematics

---

## Mechanical Design

* SolidWorks
* 3D Printing
* Custom End Effectors
* Wafer Stands & Fixtures

<p align="center">
  <img src="https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/MixCollage-08-May-2026-07-38-PM-1804.jpg" width="700"/>
</p>

---

# Repository Structure

```text
PLC/         → PLC logic and HMI
conveyor/    → Conveyor automation scripts
dobot/       → Dobot M1 automation files
cobot/       → Pro600 cobot automation files
media/       → Images, GIFs, screenshots, videos
```

---

# Team

* Sameerjeet Singh Chhabra
* Vishavjit Singh Khinda
* Shao-Chi Cheng

Special thanks to Dr. Sangram Redkar for his guidance, support, and mentorship throughout this project.

---

# Skills Demonstrated

* Robotics Integration
* Industrial Automation
* PLC Controls
* Motion Planning
* Computer Vision
* System Integration
* Embedded / Real-Time Debugging
* Mechanical Design & Rapid Prototyping

---

# Future Improvements

* Closed-loop conveyor positioning
* Advanced vision-based wafer alignment
* ROS2 integration
* Improved trajectory optimization
* Industrial safety interlocks

---

# Contact

Feel free to connect with me regarding robotics, controls, automation, collaborative robotics, and intelligent manufacturing systems.
