data_labels = ["Strongly Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Strongly Satisfied"]
data = [] # Initialize an empty list to store the data values
# Prompt the user to enter a value for each data variable
for label in data_labels:
    while True:
        value = input("Enter value for {}: ".format(label))
        # Check if the input consists only of digits
        if value.isdigit(): 
            # Convert the value to an integer and append it to the data list
            data.append(int(value))
            break
        else:
            print("Invalid input!")
# Display the histogram representation
for label, value in zip(data_labels, data):
    print("{}: {}".format(label, '*' * value))
