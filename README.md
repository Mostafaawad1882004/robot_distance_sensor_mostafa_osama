# Robot Distance Sensor Program

A Python-based navigation decision controller for a mobile robot equipped with a front-facing distance sensor. This program processes incoming real-time sensor streams, maps distances to specific obstacle-avoidance actions, and incorporates comprehensive error handling.

---

## How It Works

The core of this application revolves around the Robot class, which manages the robot's state (Name and Battery level) and encapsulates the distance processing logic.

### Navigation Logic:
* Distance < 0.5m: Returns STOP (Obstacle is too close to the robot).
* Distance 0.5m to 1.0m: Returns SLOW (Obstacle detected nearby).
* Distance > 1.0m: Returns MOVE FAST (The path is entirely clear).

---

## Methods and Functionality

### 1. __init__(name, battery)
* Purpose: Initializes the robot object with its unique identifier and sets the initial battery percentage.

### 2. process_distances(distance_list)
* Purpose: Loops through a sequence of distance inputs to generate corresponding control commands.
* Error Handling: 
  * Gracefully handles unexpected string values (e.g., "bad_data") without crashing.
  * Detects and flags physical anomalies like negative distances (e.g., -0.5m).

---

## How to Run the Code

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/Mostafaawad1882004/robot_distance_sensor_mostafa_osama.git](https://github.com/Mostafaawad1882004/robot_distance_sensor_mostafa_osama.git)
