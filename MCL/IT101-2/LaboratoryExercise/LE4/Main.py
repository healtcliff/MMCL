import empData
empData.createFiles()
import employeeForm as empF

monthh = ["January", "February", "March", "April",
                "May", "June", "July", "August", "September",
                "October", "November", "December"]

#Function to check if an employee NO exists in the employee record
def employList(Record):
    while True:
        employeeNO = input("Enter NO.: ")
        if employeeNO in Record:
            return employeeNO
        print("Employee does not exist.")


#Function to create a dictionary from employee records.
def MakeDictEmployee(employeeRec):
    try:
        empRecord = dict()
        employ = employeeRec.split(';\n')
        for e in employ:
            data = e.split(',')
            empRecord[data[0]] = {
                'First name': data[1],
                'Last name': data[2],
                'Department': data[3],
                'Rate per hour': data[4]
                }
        return empRecord
    except Exception as e:
        print(f"An Error Occured: {str(e)}")
        return None


#Function to create a dictionary from monthly records.
def PayrollDict(employee):
    try:
        employeePay = dict()
        record = employee.split(";\n")
        for employ in record:
            day = employ.split(",")
            employeePay[day[0] + '-' + day[1]] = day[2]
        return employeePay
    except Exception as e:
        print(f"An Error Occured: {str(e)}")
        return None

#Function to check if the entered employee NO is a valid 9-digit number.
def Ifdigit():
    while True:
        try:
            newNO = int(input("Enter employee NO.: "))
            newNO = str(newNO)
            if len(newNO) == 9:
                return newNO
            else:
                print("Employee NO. must be 9 digits.")
        except ValueError:
            print("NO. must be a number")

#Function to check if the entered number of days is valid for a given month.
def numDays(month):
    while True:
        try:
            month = int(month)
            days = int(input("Enter number of days: "))
            #If the month is odd (Jan, Mar, May, Jul, Aug, Oct, Dec), check if days <= 31.
            if month in list(range(1, 13))[::2]:
                if days <= 31:
                    return str(days)
                print("Invalid number of days.")
            #If the month is even (Apr, Jun, Sep, Nov), check if days <= 30.
            elif month in list(range(1, 13))[1::2][1:]:
                if days <= 30:
                    return str(days)
                print("Invalid number of days.")
            #If the month is February (2), check if days <= 28.
            elif month == 2:
                if days <= 28:
                    return str(days)
                print("Invalid days.")
        except ValueError:
            print("Invalid days.")

#Function to get a unique employee NO that does not exist in the employee record.
def TakeEmployeeNO(employeeRecord):
    while True:
        e = Ifdigit()
        if e not in employeeRecord:
            break
        print('Employee ID already exist.')
    return e


#Function to get input from the user.
def userInput(myInput):
    while True:
        try:
            data = input("%s: " %(myInput))
            if data[0].isalpha():
                if data[0].isupper():
                    return data
                else:
                    print("Capitalize the FIRST LETTER")
            else:
                print("Invalid Name: Number or Special Character detected")
        except Exception as e:
            print(f"An Error Occured: {str(e)}")

#Function to check if the entered department is available.
def validateDepartment():
        try:
            depDict = empF.getList()
            while True:
                department = input("Enter your department: ")
                if department in depDict:
                    return department
                else:
                    print("Department is not available")
        except Exception as e:
            print(f"An error occured: {str(e)}")

#Function to check if the entered rate per hour is a valid integer.
def checkRate():
    while True:
        try:
            rph = int(input('Enter rate per hour: '))
            rph = str(rph)
            return rph
        except ValueError:
            print("Rate should be numbers")

#Function to check if the entered month is valid.
def Months():
    while True:
        try:
            month = input('Enter Month: ')
            if int(month) in range(1, 13):
                break
            print('Invalid month')
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return month

#The main function that runs the program.
def main():
    employeeRec = empF.retrieveData("empList.txt")
    employeeRecord = MakeDictEmployee(employeeRec)
    employeePayroll = empF.retrieveData("empMR.txt")
    employeePayrollRec = PayrollDict(employeePayroll)
    while True:
        print("="*65)
        choice = input("""A: Display Employee List
B: Add Employee
C: Add Payroll Record
D: Generate Pay Slip
X: Exit
Your choice: """)
        print("="*65)

        if choice.upper() == "X":
            print("Thank you")
            break

        elif choice.upper() == "A":
            print("*"*65)
            empF.displayEmployee(employeeRecord)
            print("*"*65)

        elif choice.upper() == "B":
            print("="*65)
            employeeID = TakeEmployeeNO(employeeRecord)
            lname = userInput('Enter last name')
            fname = userInput('Enter first name')
            dep = validateDepartment()
            rph = checkRate()
            employeeRecord = empF.addEmployee(employeeRecord, employeeID, fname, lname, dep, rph)
            empF.displayEmployee(employeeRecord)
            print("="*65)

        elif choice.upper() == "C":
            print("="*65)
            empNO = employList(employeeRecord)
            while True:
                month = Months()
                if empNO + '-' + month not in employeeRecord:
                    break
                print("Record already exist.")
            days = numDays(month)
            employeePayrollRec[empNO + "-" + month] = days
            print("Success")
            s = ";\n" + empNO + "," + month + "," + days
            f = open("empMR.txt", "a")
            f.write(s)
            f.close()
            print("="*65)

        elif choice.upper() == "D":
            print("="*65)
            employeeNo = employList(employeeRecord)
            while True:
                month = input("Enter payslip for the month of: ")
                print("=" *65)
                if employeeNo + "-" + month in employeePayrollRec:
                    break
                print("Record does not exist.")
            rateperday = int(employeeRecord[employeeNo]["Rate per hour"]) * 8
            payrol = rateperday * int(employeePayrollRec[employeeNo + "-" + month])
            print("#"*65)
            print("*"*65)
            print(f"Payslip for the Month of:{monthh[int(month)-1]}")
            print('Employee NO.:', employeeNo,   '   Employee Name:', employeeRecord[employeeNo]['First name'], employeeRecord[employeeNo]['Last name'])
            print(f"Department: {employeeRecord[employeeNo]['Department']}")
            print(f"Rate per Day: {rateperday:,.2f}      No. of Days Worked:{employeePayrollRec[employeeNo + '-' + month]}" )
            print(f"Gross Pay: {payrol:,.2f}")
            print("*"*65)
            print("#"*65)


            #to create a record payroll in list note
            '''The block of code is wrapped in a try-except block to handle any exceptions that may occur during its execution.
            The code within the try block remains the same, creating the payslip information and writing it to a file.
            If an exception occurs, it is caught in the except block, and an error message is printed.
            The str(e) converts the exception to a string to display a meaningful error message.'''
            try:
                s = f"Payslip for the MONTH of: {monthh[int(month) - 1]}\n"\
                    f"Employee NO.: {employeeNo}\n" \
                    f"Employee Name: {employeeRecord[employeeNo]['First name']} {employeeRecord[employeeNo]['Last name']}\n" \
                    f"Department: {employeeRecord[employeeNo]['Department']}\n" \
                    f"Rate per Day: {rateperday:,.2f}\n" \
                    f"No. of Days worked: {employeePayrollRec[employeeNo + '-' + month]}\n" \
                    f"Gross Pay: {payrol:,.2f}"
                #the uses of "with open" statement is to open the file, which ensures that the file is automatically closed after writing.
                #This is a better practice than manually opening and closing the file using the open and close functions.
                with open(f"{employeeNo}-{month}payslip.txt","w") as f:
                    f.write(s)
            except Exception as e:
                print(f"An Error Occured: {str(e)}")



main()

# This check if textfiles are updated
# do not alter/modify this code
f = open("empList.txt", "r")
x = f.readlines()
f.close()

f = open("empMR.txt", "r")
x = f.readlines()
f.close()
