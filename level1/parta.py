import math
def main():
    print("Enter the origin coordinates of the rover:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nEnter the DESTINATION coordinates of the rover:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"Distance  is {distance} units")
main()
   