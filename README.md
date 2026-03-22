


Part A involves calculating the distance between two coordinates on a 2D plane using the Euclidean distance formula. It also calculates the time required for the rover to travel that distance using the kinematic equation s = ut + ½at². The program handles invalid inputs like letters, negative velocity, zero acceleration and max speed lower than initial velocity.

Part B extends Part A by adding motion parameters. The rover's initial velocity, acceleration and maximum allowed top speed are taken as inputs. The time is calculated and the program checks if the rover exceeds the speed limit.

Part C adds proper error handling to the program. If the user enters invalid values the program asks them to re-enter instead of crashing.

To run any of the programs

py parta.py
py partb.py
py partc.py

Sample run for Part C:
Origin: (0, 0), Destination: (100, 40)
Initial velocity: 2, Acceleration: 1, Max speed: 10
Distance to destination: 107.7 m
Time required: 12.8 seconds
Status: Within speed limit

=======
# lenaelizabethminto_horizon_s4
This project was done to understand how communication works in ROS 2 using Python. In the first part, I created a simple publisher and subscriber system. The publisher node sends distance values through a topic, and the subscriber node receives those values and displays them in the terminal. This helped me understand the basic concept of topics and how data is shared between nodes.

In the second part, I extended the project by adding a decision node. Instead of only printing the distance values, this node processes the data and decides what action should be taken. If the distance is less than 30, it sends a command to stop, and if the distance is 30 or more, it sends a command to move forward.

I also created another node that listens to these commands and prints them. This completes the flow from receiving sensor data to making a decision and displaying the final action.

Through this project, I was able to understand how multiple nodes can work together in ROS 2 and how simple data can be used to make decisions in a system like a rover.

