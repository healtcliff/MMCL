# Define a function to compute the value of 'r' based on the difference between 'x' and 'y'.
def computation(x, y):
    difference = x - y
    if difference > 0:
        r = x * y
    elif difference < 0:
        r = x + y
    else:
        r = 2 * x + 2 * y
    return difference, x, y, r

while True:
    # Prompt the user to enter values for variables 'x' and 'y'.
    x = int(input("Enter the value for X: "))
    y = int(input("Enter the value for Y: "))
    print("---------------------------------------------------------------")

    # Call the computation function to perform calculations and store the results in variables.
    #It assigns the returned values (difference, x, y, and r) to the respective variables.
    difference, x, y, r = computation(x, y)
    
    #display the difference between x and y.
    #the calculated value of R.
    print("Difference of X-Y:", difference)
    print(f"the calculation of x = {x} and y = {y} is {r}")
    print("---------------------------------------------------------------")
    
    another_calculation = input("Do you want to perform another calculation? (Y/N): ")
    #break out of the loop  once N is entered.
    if another_calculation.upper() == "N":
        break