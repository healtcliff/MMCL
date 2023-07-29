code_map = {
    "1": "n",
    "2": "E",
    "3": "M",
    "4": "a",
    "5": "L",
    "6": "@",
    "7": "Y",
    "8": "A",
    "9": "N",
    "0": "O"
}
while True:
    # Enter the student name and ID number
    student_name = input("Enter the student name: ")
    student_id = input("Enter student ID Number: ")

    print(f"Student Name: {student_name.upper()}")

    # Store the encoded values in a list
    encoded_values = [code_map.get(char, "Invalid price code!") for char in student_id]

    # Print the encoded values with spaces
    print(f"Coded Value: {''.join(encoded_values)}")
    print("end of process")
    
    choice = input("Do you want to continue? (yes/no): ")
    
    # Check the user's choice
    if choice.lower() != "yes":
        break