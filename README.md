

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

