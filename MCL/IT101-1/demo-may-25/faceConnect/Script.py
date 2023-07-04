#=================================================================
#Do not modify this code. This will create the userCredentials.txt
import createFile
createFile.x()
#=================================================================
import os 
# Hey there, start typing your Python code here...
import os

def script():
    username = input("Enter username: ")

    if username.lower() == 'x':
        print("Good Bye!")
        return

    if not userExists(username):
        print("Username does not exist!.")
        return script()

    password = input("Enter password: ")

    while not myLogin(username, password):
        print("Incorrect password!")
        password = input("Enter password: ")

    user_info = getUserInfo(username)
    print("Welcome, {} {}!".format(user_info[2], user_info[3]))
    menu(username)

def userExists(username):
    global usernames
    usernames = []
    with open("userCredentials.txt", "r") as file:
        for line in file:
            user_info = line.strip().split(";")
            usernames.append(user_info[0])
            if user_info[0] == username:
                return True
    return False

def myLogin(username, password):
    with open("userCredentials.txt", "r") as file:
        for line in file:
            user_info = line.strip().split(";")
            if user_info[0] == username and user_info[1] == password:
                return True
    return False

def getUserInfo(username):
    with open("userCredentials.txt", "r") as file:
        for line in file:
            user_info = line.strip().split(";")
            if user_info[0] == username:
                return user_info

def menu(username):
    while True:
        print("\n1 - View Friend")
        print("2 - Add Friend")
        print("3 - Delete Friend")
        print("X - Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            viewFriends(username)
        elif choice == "2":
            addFriend(username)
        elif choice == "3":
            deleteFriend(username)
        elif choice.lower() == "x":
            print("Succesfully LogOut.")
            return script()  # Return to the beginning of the script
        else:
            print("Invalid Choice")

def viewFriends(username):
    friend_filename = "{}.txt".format(username)

    if not os.path.isfile(friend_filename):
        print("Make friends first")
        return

    with open(friend_filename, "r") as file:
        friend_list = file.read().splitlines()

    if len(friend_list) == 0:
        print("Make friends first")
    else:
        for friend in friend_list:
            print(friend)

def addFriend(username):
    friend_username = input("Enter friend's username: ")

    if not userExists(friend_username):
        print("Friend's username does not exist.")
        return

    friend_filename = "{}.txt".format(username)

    if friend_filename in os.listdir():
        with open(friend_filename, "r") as file:
            for line in file:
                if line.strip() == friend_username:
                    print("You are already friends with {}".format(friend_username))
                    return
    else:
        # Create the friend list file for the user
        with open(friend_filename, "w") as file:
            pass

    with open(friend_filename, "a") as file:
        file.write("{}\n".format(friend_username))

    print("Success")

def deleteFriend(username):
    friend_filename = "{}.txt".format(username)
    friend_list = []

    try:
        with open(friend_filename, "r") as file:
            friend_list = file.read().splitlines()
    except FileNotFoundError:
        pass

    if len(friend_list) == 0:
        print("No friend to delete.")
        return

    friend_name = input("Enter username to unfriend: ")

    if friend_name in friend_list:
        friend_list.remove(friend_name)

        with open(friend_filename, "w") as file:
            for friend in friend_list:
                file.write(friend + "\n")

        print("Success")
    else:
        print("Friend not found. No friend was deleted.")

script()
usernames = []
with open("userCredentials.txt", "r") as file:
    for line in file:
        user_info = line.strip().split(";")
        usernames.append(user_info[0])
        username_file = user_info[0] + ".txt"
        if not os.path.isfile(username_file):
            open(username_file, 'w').close()


#================================================================
#Do not delete or edit this part 
#The following code will display the list of friends for each
#user from the textfiles created by your code
print()
for x in usernames:
    l = open(x+'.txt','r')
    friends = l.read().split()
    print(f"{x} friend\'s {friends}")