# myArea.py module

circle_area = lambda radius: 3.14159 * radius ** 2
rectangle_area = lambda length, width: length * width
triangle_area = lambda base, height: 0.5 * base * height


# main.py program
#import myArea


def validateInt(a,b):
    if not (isinstance(a, int) or a.isdigit()) or not (isinstance(b, int) or b.isdigit()):
        print("Invalid Input!")
        return False
    else:
        return True
    

def display_menu():
    print("Geometry Calculator")
    print("1. Calculate the Area of a Circle")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Triangle")
    print("4. Quit")

def calculate_circle_area():
    radius = input("Enter radius: ")
    if validateInt(radius,b=1):
        area = circle_area(int(radius))
        area = "{:.2f}".format(area)
        print(f"The area of the circle with radius {radius} is {area}.")

def calculate_rectangle_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    if validateInt(length,width):
        area = rectangle_area(int(length), int(width))
        print(f"The area of the rectangle with length {length} and width {width} is {area}.")

def calculate_triangle_area():
    base = input("Enter base: ")
    height = input("Enter height: ")
    if validateInt(base,height):
        area = triangle_area(int(base), int(height))
        area = "{:.0f}".format(area)
        print(f"The area of the triangle with length of base {base} and height {height} is {area}.")


def main(choice):
    while True:
        try:
            display_menu()
            choice = input("Choice: ")
            if choice == "1":
                calculate_circle_area()
            elif choice == "2":
                calculate_rectangle_area()
            elif choice == "3":
                calculate_triangle_area()
            elif choice == "4":
                print("Bye!")
                break
        except ValueError:
            print("Invalid Input!")
choice = 0
main(choice)
