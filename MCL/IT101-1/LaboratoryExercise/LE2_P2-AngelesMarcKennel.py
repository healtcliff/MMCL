num1 = int(input("Start: "))
num2 = int(input("End: "))

if num1 >= num2:
    print("Sorry! Invalid input! The first number should be less than the second number.")

else:
    total = 0
    for num in range(num1, num2+1):
        total+=num
    print(f"The sum of the integers between {num1} and {num2} inclusive is {total}.")