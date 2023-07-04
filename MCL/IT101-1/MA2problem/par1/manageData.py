classroom_data = {}
student_order = []  # List to store the order of student additions

def addstudent():
    while True:
        classroom_number = input("Enter classroom no.: ")
        if classroom_number in classroom_data and len(classroom_data[classroom_number]) >= 10:
            print("Room already full." )
            print("Invalid Room no.")
        elif not classroom_number.isdigit() or int(classroom_number) < 1 or int(classroom_number) > 10:
            print("Invalid Room no.")
        
        else:
            break
            
    student_id = input("Enter student ID: ")
    while True:
        score = input("Score: ")
        if not score.isdigit() or int(score) <0 or int(score) > 100:
            print("Invalid Score.")
        else:
            break
    student_data = [classroom_number, student_id, score]
    
    if classroom_number in classroom_data:
        classroom_data[classroom_number].append(student_data)
    else:
        classroom_data[classroom_number] = [student_data]
    
    student_order.append(student_data)  # Add student data to the order list
    
    print("Student Record Added.")
    
    for student in student_order:
        print(student)

def viewclassroom():
    classroom_number = input("Enter classroom no. to view:")
    if classroom_number in classroom_data:
        students = classroom_data[classroom_number]
        for student in students:
            print(student)
        total_score = sum(int(student[2]) for student in students)
        print(f"Classroom total score: {total_score}")
    else:
        print("No classroom exists.")

def viewtotalscore():
    for classroom_number in range(1, 11):
        if str(classroom_number) in classroom_data:
            students = classroom_data[str(classroom_number)]
            total_score = sum(int(student[2]) for student in students)
            print(f"Classroom {classroom_number}: {total_score}")
        else:
            print(f"Classroom {classroom_number}: 0")