import manageData

def main():
    while True:
        print("A - Add Student")
        print("B - View Classroom")
        print("C - View Total Score")
        print("X - Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "A":
            manageData.addstudent()
        elif choice == "B":
            manageData.viewclassroom()
        elif choice =="C":
            manageData.viewtotalscore()
        elif choice == "X":
            print("Good Bye!")
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()