import math

def calculate_area():
    print("Choose a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Trapezoid")
    print("5. Rectangle")
    print("6. Ellipse")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius**2
        print(f"The area of the circle is: {area}")
    elif choice == 2:
        side_length = float(input("Enter the side length of the square: "))
        area = side_length**2
        print(f"The area of the square is: {area}")
    elif choice == 3:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area}")
    elif choice == 4:
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        height = float(input("Enter the vertical height of the trapezoid: "))
        area = base1 + base2
        area *= 0.5 * height
        print(f"The area of the trapezoid is: {area}")
    elif choice == 5:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
         
        print(f"The area of the rectangle is: {area}")
    elif choice == 6:
        a = float(input("Enter the radius of the major axis: "))
        b = float(input("Enter the radius of the minor axis: "))
        area = math.pi * a * b
        print(f"The area of the ellipse is: {area}")
    else:
        print("Invalid choice. Please choose a valid shape.")

# Example usage:
calculate_area()