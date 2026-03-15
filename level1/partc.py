import math

def get_float(num):
    while True:
        try:
            value = float(input(num))
            return value
        except ValueError:
            print("  Invalid input! Please enter a numeric value.\n")

def main():
    print("\nEnter the origin coordinates of the rover:")
    x1 = get_float("x1: ")
    y1 = get_float("y1: ")

    print("\nEnter the destination coordinates of the rover:")
    x2 = get_float("x2: ")
    y2 = get_float("y2: ")

   
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"\nDistance to destination: {distance} m")

  
    while True:
        u = get_float("Initial velocity (m/s): ")
        if u < 0:
            print("  Velocity cannot be negative!\n")
        else:
            break

    while True:
        a = get_float("Acceleration (m/s²): ")
        if a <= 0:
            print("  Acceleration must be greater than 0!\n")
        else:
            break

    while True:
        s = get_float("Maximum allowed top speed (m/s): ")
        if s <= 0:
            print("  Max speed must be greater than 0!\n")
        elif s < u:
            print("  Max speed cannot be less than initial velocity!\n")
        else:
            break

    
    time = (-u + math.sqrt(u**2 + 2 * a * distance)) / a
    print(f"Time required: {time} seconds")

    
    v = u + a * time
    if v > s:
        print(f"WARNING: Rover exceeds max speed of {s} m/s! (Reaches {v:.1f} m/s)")
    else:
        print(f"Status: Within speed limit ✓")

main()
