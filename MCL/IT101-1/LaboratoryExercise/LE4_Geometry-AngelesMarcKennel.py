def circle_area():
    while True:
        try:
            radius = int(input("Enter radius: "))
            area = 3.14159 * radius * radius
            area = "{:.2f}".format(area)
            print(f"The area of the circle with radius {radius} is {area}.")
            break  # Break the loop and exit after a valid input is provided
        except ValueError:
            print("Invalid Input!")


def rectangle_area(length, width):
    area = length * width
    return area


def triangle_area(b, h):
    area = int(0.5 * int(b) * int(h))
    return area


def menu(choice):
    while True:
        print("""Geometry Calculator
1. Calculate the Area of a Circle
2. Calculate the Area of a Rectangle
3. Calculate the Area of a Triangle
4. Quit""")
        try:
            
            choice = int(input("Choice: "))
            #No parameter,Nonvalue returning function
            if choice == 1:
                circle_area()
            #with parameter,Value returning function
            elif choice == 2:
                while True:
                    try:
                        length = int(input("Enter length: "))
                        break
                    except ValueError:
                        print("Invalid Input!")
                while True:
                    try:
                        width = int(input("Enter width: "))
                        break  # Break the inner loop after successfully obtaining valid inputs
                    except ValueError:
                        print("Invalid Input!")

                result = rectangle_area(length, width)
                print(f"The area of the rectangle with length {length} and width {width} is {result}.")
            #With keyword parameter, Value returning function
            elif choice == 3:
                while True:
                    try:
                        base = int(input("Enter base: "))
                        break
                    except ValueError:
                        print("Invalid Input!")
                while True:
                    try:
                        height = int(input("Enter height: "))
                        break  # Break the inner loop after successfully obtaining valid inputs
                    except ValueError:
                        print("Invalid Input!")

                result = triangle_area(b=base, h=height)
                print(f"The area of the triangle with length of base {base} and height {height} is {result}.")

            elif choice == 4:
                print("Bye!")
                break

            else:
                print("Invalid Input!")

        except ValueError:
            print("Invalid Input!")


choice = 0
menu(choice)