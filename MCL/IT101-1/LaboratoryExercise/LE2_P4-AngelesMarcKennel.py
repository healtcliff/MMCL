# Initialize the package rates and total number of hours
package_rate = 0
total_hours = 0

# ask the user to enter the package,and month.
while package not in ["A","B","C"]:
        package = input("Enter package: ").upper()
        if package not in ["A","B","C"]:
            print("Invalid Code!")
        if package.upper() == "C":
            print("Total amount due is Php 900.00")
            quit()

month = int(input("Enter month: "))
while month < 1 or month > 12:
    print("Invalid Month!")
    month = int(input("Enter month: "))



# Calculate the total number of hours based on the month
if month == 2:
    total_hours = 672  # February has 28 days
elif month in [4, 6, 9, 11]:
    total_hours = 720  # April, June, September, November have 30 days
else:
    total_hours = 744  # All other months have 31 days


# ask the user to enter the hours.
hours_used = int(input("Enter hours: "))
while hours_used < 1 or hours_used >total_hours:
    print("Invalid Hours!")
    hours_used = int(input("Enter hours: "))

# calculate the package rate
if package == "A":
    package_rate = 200 + max(0, hours_used - 10) * 15
elif package == "B":
    package_rate = 500 + max(0, hours_used - 20) * 10


# Display the total amount due
if package_rate > 0:
    print(f"Total amount due is Php {package_rate:.2f}")
