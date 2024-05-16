<h1 align="center"> Traffic Light Optimization With Reinforcement Learning </h1>

This project offers a framework for optimizing traffic flow at complex intersections using a Deep Q-Learning Reinforcement Learning agent. By intelligently selecting traffic light phases, the agent aims to maximize traffic efficiency.

## Deep Q-Learning Agent

- **Framework**: Q-Learning with a deep neural network.
- **Context**: Traffic signal control at a single intersection.
- **Environment**: Features a 4-way intersection with 4 incoming and outgoing lanes per arm, each 750 meters long. Traffic lights are positioned such that each arm has dedicated lanes for specific movements.
- **Traffic Generation**: Each episode generates 1000 cars following a dynamic pattern, contributing to the complexity of the environment.
- **Agent (Traffic Signal Control System - TLCS)**:
  - **State**: Discretized representation of oncoming lanes, identifying vehicle presence in cells.
  - **Action**: Selection of traffic light phases from predetermined options, each lasting 10 seconds.
  - **Reward**: Based on cumulative waiting time reduction, incentivizing efficient traffic management.
  - **Learning Mechanism**: Utilizes Q-learning equation and a deep neural network to update action values and learn state-action relationships.

## Getting Started

Follow these steps to set up the project on your local machine:

1. Download and install Anaconda from the [official website](https://www.anaconda.com/distribution/#download-section).
2. Download and install SUMO from the [official website](https://www.dlr.de/ts/en/desktopdefault.aspx/tabid-9883/16931_read-41000/).

Ensure your system meets the software version requirements listed below:

- Python 3.11
- SUMO traffic simulator 1.2.0
- tensorflow 2.16.1
- tensorflow-gpu 2.5.0
- matplotlib 3.6.0
- numpy 1.19.5

## Running the Algorithm

1. Clone or download the repository.
2. Navigate to the root folder in the terminal.
3. Run `python training_main.py` to start the training process.

## Code Structure

The project is structured around several classes handling different aspects of the training process:

- **Model**: Defines the deep neural network architecture.
- **Memory**: Manages experience replay for training stability.
- **Simulation**: Controls the simulation environment and interaction with SUMO.
- **TrafficGenerator**: Handles route definition for vehicles in each episode.
- **Visualization**: Provides functions for plotting data.
- **Utils**: Contains utility functions for file handling and directory management.

## Settings Explained

The settings used during training and testing are specified in the `training_settings.ini` and `testing_settings.ini` files. Key parameters include episode duration, traffic generation details, neural network architecture, and simulation settings.

## Contributors

This project was developed by:

- [Aadith Sukumar](https://www.linkedin.com/in/aadith-sukumar)
- [Aniket Singh](https://www.linkedin.com/in/aniket-singh-0a6b54220/)
- [Apoorv Gupta](https://www.linkedin.com/in/er-apoorv-gupta/)

For additional information or inquiries, please feel free to open an issue on the repository's issues page.

### References

- Amazon AWS Documentation
- Dr. Rahee Walambe - Symbiosis Institute of Technology, Symbiosis International (Deemed) University
- Dr. Smita Mahajan - Symbiosis Institute of Technology, Symbiosis International (Deemed) University
- Analytics Vidhya
- Towards Data Science (Medium)
- Andrea Vidali - University of Milano-Bicocca
- "Deep Reinforcement Learning for Traffic Light Control in Intelligent Transportation Systems" - Xiao-Yang Liu, Ming Zhu, Sem Borst, Anwar Walid
