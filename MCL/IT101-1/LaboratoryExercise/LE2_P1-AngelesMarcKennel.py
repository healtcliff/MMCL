#promt the user to enter the package, month, and hours used
package = input("Enter package: ").upper
month = input ("Enter month: ")
hours = input("Enterh hours: ")

#initialize the package rates and total number of hours
package_rate = 0
total_hours = 0

#calculation the total number of houors basing on the the month
if month == 2:
    total_hours = 672 #feb has 28 days
elif month in [4, 6, 9, 11]:
    total_hours = 720 #april, june ,september, november has 30 days
else:
    total_hours = 744 # all other months 31 days

#validate the input and calculate the package rate
if package == "A":
    if hours > total_hours:
        print(f"Invalid Input. Total hours for the month should not exceed {total_hours}.")
    else:
        package_rate = 200 + max(0, hours - 10) * 15
elif package == "B":
    if hours > total_hours:
        print(f"Invalid Input. Total hours for the month should not exceed {total_hours}.")
    else:
        package_rate = 500 + max(0, hours - 20) * 10
elif package == "C":
    package_rate = 900

#display the total amount 
if package_rate > 0:
    print(f"Total amount due :Php {package_rate:.2f}")
    