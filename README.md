# Wafer Automation Cell

### PLC-Controlled Multi-Robot Semiconductor Handling System

🚀 A semiconductor wafer handling automation system combining collaborative robotics, industrial controls, computer vision, and real-time system integration.

![Demo](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/VID_20260505_194533-ezgif.com-video-to-gif-converter.gif)

---

# System Overview

This project integrates:

* Dobot M1 SCARA robot
* Elephant Robotics Pro600 6-DoF cobot
* Allen Bradley Micro820 PLC
* Sensor-driven conveyor system
* Camera-based inspection station
* Python-based robot communication and automation
* Custom HMI interface
* CAD-designed and 3D-printed fixtures/end effectors

The system autonomously transfers semiconductor wafers between robotic stations while coordinating sensors, conveyors, PLC logic, robot motion, and inspection stages.

---

# System Demonstration

## Full Automation Cell

![Automation Cell](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Recording2026-05-08185129-ezgif.com-video-to-gif-converter.gif)

## HMI

![Automation Cell](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/WhatsApp%20Image%202026-05-08%20at%2018.45.39%20(1).jpeg)

---

# Automation Workflow

1. Dobot M1 SCARA robot retrieves wafers from stacked rack
2. Wafer is transferred onto conveyor stand
3. Infrared sensors trigger conveyor movement
4. Conveyor pauses at camera station for image capture and assessment
5. Conveyor advances to robotic transfer location
6. Pro600 cobot retrieves wafer and places it onto rotating platform
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
⚡ CAD design and rapid prototyping of custom 3D-printed fixtures and end effectors

---

# Technologies Used

## Robotics

* Dobot M1 SCARA
* Elephant Robotics Pro600
* RoboFlow
![Demo](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot%202026-05-05%20191945.png)
![Demo](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/Screenshot%202026-05-11%20161342.png)

## Controls & Automation

* Allen Bradley Micro820 PLC
* Ladder Logic
* Industrial I/O Relays
* Infrared Sensors

## Software

* Python
* TCP/Ethernet Communication
* Computer Vision
* Inverse Kinematics

## Mechanical

* SolidWorks
* 3D Printing
* Custom End Effectors
* Wafer Stands and Fixtures

![Demo](https://raw.githubusercontent.com/Sjschhabra/wafer-automation-cell/refs/heads/main/media/MixCollage-08-May-2026-07-38-PM-1804.jpg)
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
* Embedded/Real-Time Debugging
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

Feel free to connect with me on LinkedIn or reach out regarding robotics, controls, automation, or collaborative robotics opportunities.

