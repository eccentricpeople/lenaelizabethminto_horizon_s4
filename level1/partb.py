import math

def main():
    print("Enter the origin coordinates of the rover:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nEnter the DESTINATION coordinates of the rover:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"\nDistance: {distance} units")

    u = float(input("Enter the Initial velocity: "))
    a = float(input("Enter the Acceleration: "))
    s = float(input("Enter the Maximum allowed top speed: "))

    time = (-u + math.sqrt(u**2 + 2 * a * distance)) / a
    print(f"Time taken: {time} seconds")

    v = u + a * time
    if v > s:
        print(f"Exceeds max speed of {s} units/s!")
    else:
        print(f"Within speed limit")

main()