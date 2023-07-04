#A regular expression (or RE) specifies a set of strings that matches it
import re
# import the datetime module to handle dates and times
from datetime import datetime

# initialize an empty list to store friends data
friends = []

# loop until the user enters "No" to stop adding more friends
while True:
    # ask for the friend's Last name
    last_name = input("Enter Last name: ")
    # check if the input is empty, display an error message and continue to the next iteration
    while not last_name:
        print("Invalid input!")
        last_name = input("Enter Last name: ")

    # ask for the friend's first name
    first_name = input("Enter First name: ")
    # check if the input is empty, display an error message and continue to the next iteration
    while not first_name:
        print("Invalid input!")
        first_name = input("Enter First name: ")

    birthdate_str = input("Enter Birthdate: ")
    # check if the input is empty, display an error message and continue to the next iteration
    while True:
        try:
            # ask for the friend's birthdate
            #try to convert the input to a datetime object, if it fails, display an error message and ask again
            birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid Input!")
            birthdate_str = input("Enter Birthdate: ")

    # ask for the friend's gender
    gender = input("Enter Gender: ").upper()
    # check if the input is valid (either F or M), display an error message and continue to the next iteration if not
    while gender not in ("F", "M"):
        print("Invalid Input!")
        gender = input("Enter Gender: ").upper()

    # ask for the friend's contact number
    contact_no = input("Enter Contact Number: ")
    # check if the input contains only digits and has a length of exactly 11 digits,
    # display an error message and ask again if the input is invalid
    while not re.match(r"^\d{11}$", contact_no):
        print("Invalid Input!")
        contact_no = input("Enter Contact Number: ")
    # create a dictionary containing the friend's data
    friend_data = {
        "last_name": last_name,
        "first_name": first_name,
        "birthdate": birthdate,
        "gender": gender,
        "contact_no": contact_no,
    }
    # add the friend's data to the friends list
    friends.append(friend_data)
    # ask the user if they want to add another friend
    more_friends = input("Add More? ")
    print()
    # if the user enters "No", exit the loop
    if more_friends.lower() == "no":
        break
# display the contents of the friend list in the desired format
for friend in friends:
    print(f"Name: {friend['first_name']} {friend['last_name']}")
    print(f"Birthdate: {friend['birthdate'].strftime('%B %d, %Y')}")
    print(f"Gender: {'Female' if friend['gender'] == 'F' else 'Male'}")
    print(f"Contact No.: {friend['contact_no']}\n")
