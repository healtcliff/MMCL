try:
    n = int(input("Enter a number: "))
    if  n < 2 or n > 25:
        print("Invalid value!")
    else:
        for i in range(1,n+1):
            for j in range(1,n+1):
                print("{:<3d}".format(i*j), end=" ")
            print()
except ValueError:
    print("Input a number.")
