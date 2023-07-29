import csv
"""
Employee Payroll System

Object-Oriented Programming (OOP) Approach:
    This code follows an Object-Oriented Programming (OOP) approach to model an employee payroll system.
    OOP is a programming paradigm that organizes the code into objects, which are instances of classes.
    Classes define the blueprint for creating objects, and objects represent real-world entities with their attributes and behaviors.

Employee Class:
    - The `Employee` class represents a generic employee and contains information about the employee, such as name, position, rate per day, etc.
    - It has methods to calculate the salary, increase pay, and generate pay slips.

Manager, AssistantManager, Secretary, Staff Classes:
    - These classes are subclasses of the `Employee` class and represent specific types of employees with fixed positions.
    - Each subclass inherits attributes and methods from the `Employee` class but can also have their own specialized behaviors.

Department Class:
    - The `Department` class represents a department in the company and contains a list of employees assigned to that department.
    - It provides methods to add employees to the department and retrieve employees based on their position.

Company Class:
    - The `Company` class models the entire company and contains a collection of departments.
    - It has methods to add departments, add employees to departments, update employee data, increase pay for all employees,
    generate pay slips for all employees, display employees in a department, display employees by position,
    and calculate the total salary expenditure for the company.
    - It also provides a method to save employee records to a CSV file.

CompanyMenu Class:
    - The `CompanyMenu` class provides a text-based menu interface for interacting with the company and its functionalities.
    - It allows users to add employees, update employee data, increase pay, generate pay slips, display employees in a department,
    display employees by position, check total salary expenditure, and exit the program.

Main Program:
    - In the main program, an instance of the `CompanyMenu` class is created to start the application.
    - Several departments are added to the company.
    - Users can then interact with the company through the text-based menu provided by the `CompanyMenu` class.

Object-Oriented Programming (OOP) Features that is being used here are:
    1. Encapsulation: The classes encapsulate data and methods related to specific entities (e.g., Employee, Department, Company),
    making it easy to manage and organize code.
    2. Inheritance: The `Manager`, `AssistantManager`, `Secretary`, and `Staff` classes inherit attributes and methods from the `Employee` class,
    reducing code duplication and providing a hierarchy for different types of employees.
    3. Polymorphism: The different employee types (Manager, AssistantManager, etc.) can be treated as instances of the base `Employee` class,
    allowing for flexible code that can work with various employee types interchangeably.
    4. Abstraction: The classes hide their internal implementation details, exposing only the necessary methods for users (e.g., calculate_salary, generate_pay_slip).
    5. Composition: The `Company` class contains multiple `Department` objects, and each `Department` object contains a list of `Employee` objects,
    demonstrating the composition relationship between classes.

Note:
    - The code has a built-in functionality to save employee records to a CSV file after interacting with the menu.
    - Make sure to enter valid data when interacting with the menu to avoid unexpected errors.
    - This code serves as a simplified example and may not cover all real-world use cases. In a production environment, additional error handling, input validation, and data persistence mechanisms might be necessary.
"""


class Employee:
    def __init__(self, emp_num, last_name, first_name, position, department, birth_date, rate_per_day, days_worked_per_month):
        self.emp_num = emp_num
        self.last_name = last_name
        self.first_name = first_name
        self.position = position
        self.department = department
        self.birth_date = birth_date
        self.rate_per_day = rate_per_day
        self.days_worked_per_month = days_worked_per_month

    def calculate_salary(self):
        # Fixed rate based on position
        position_rates = {
            'Manager': 1000,
            'Asst. Manager': 750,
            'Secretary': 500,
            'Staff': 475
        }

        # Allowances for manager and assistant manager
        allowances = {
            'Manager': 5000,
            'Asst. Manager': 3000,
            'Secretary': 0,
            'Staff': 0
        }

        # Calculate salary based on position and number of days worked
        basic_salary = self.rate_per_day * self.days_worked_per_month
        allowance = allowances[self.position]
        total_salary = basic_salary + allowance + position_rates[self.position]

        return total_salary

    def increase_pay(self):
        if self.position == 'Manager':
            self.rate_per_day *= 2
        else:
            self.rate_per_day *= 1.5

    def generate_pay_slip(self, month, year):
        total_salary = self.calculate_salary()
        pay_slip = f"Pay Slip for {self.first_name} {self.last_name} ({self.position}) - {month}/{year}\n"
        pay_slip += f"Employee Number: {self.emp_num}\n"
        pay_slip += f"Department: {self.department}\n"
        pay_slip += f"Rate per day: {self.rate_per_day}\n"
        pay_slip += f"Days worked this month: {self.days_worked_per_month}\n"
        pay_slip += f"Total Salary: {total_salary}\n"
        return pay_slip


class Manager(Employee):
    pass


class AssistantManager(Employee):
    pass


class Secretary(Employee):
    pass


class Staff(Employee):
    pass


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.manager_count = 0
        self.assistant_manager_count = 0
        self.secretary_count = 0

    def add_employee(self, employee):
        if employee.position == 'Manager':
            if self.manager_count >= 1:
                raise ValueError("A department can only have one manager.")
            self.manager_count += 1
        elif employee.position == 'Asst. Manager':
            if self.assistant_manager_count >= 1:
                raise ValueError("A department can only have one assistant manager.")
            self.assistant_manager_count += 1
        elif employee.position == 'Secretary':
            if self.secretary_count >= 1:
                raise ValueError("A department can only have one secretary.")
            self.secretary_count += 1

        self.employees.append(employee)

    def get_employees_by_position(self, position):
        return [emp for emp in self.employees if emp.position == position]


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        department = Department(department_name)
        self.departments[department_name] = department

    def add_employee(self, department_name, employee):
        if department_name not in self.departments:
            raise ValueError(f"Department '{department_name}' does not exist.")

        department = self.departments[department_name]
        department.add_employee(employee)

    def update_employee(self, emp_num, new_rate_per_day):
        for department in self.departments.values():
            for emp in department.employees:
                if emp.emp_num == emp_num:
                    emp.rate_per_day = new_rate_per_day
                    break

    def increase_pay(self):
        for department in self.departments.values():
            for emp in department.employees:
                emp.increase_pay()

    def generate_pay_slips(self, month, year):
        pay_slips = []
        for department in self.departments.values():
            for emp in department.employees:
                pay_slips.append(emp.generate_pay_slip(month, year))
        return pay_slips

    def display_department_employees(self, department_name):
        if department_name not in self.departments:
            raise ValueError(f"Department '{department_name}' does not exist.")

        department = self.departments[department_name]
        for emp in department.employees:
            print(emp)

    def display_employees_by_position(self, position):
        employees = []
        for department in self.departments.values():
            employees.extend(department.get_employees_by_position(position))

        if employees:
            for emp in employees:
                print(emp)
        else:
            print(f"No employees found with position: {position}")

    def total_salary_expenditure(self):
        total_salary = 0
        for department in self.departments.values():
            for emp in department.employees:
                total_salary += emp.calculate_salary()

        return total_salary
    def save_employee_records_to_file(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee Number", "Last Name", "First Name", "Position", "Department", "Birth Date", "Rate per Day", "Days Worked per Month"])
            for department in self.departments.values():
                for emp in department.employees:
                    writer.writerow([emp.emp_num, emp.last_name, emp.first_name, emp.position, emp.department, emp.birth_date, emp.rate_per_day, emp.days_worked_per_month])


class CompanyMenu:
    def __init__(self):
        self.company = Company()

    def show_menu(self):
        while True:
            print("\nCompany Menu:")
            print("1. Add Employee")
            print("2. Update Employee Data")
            print("3. Increase Pay")
            print("4. Generate Pay Slip")
            print("5. Display Employees in a Department")
            print("6. Display Employees by Position")
            print("7. Total Salary Expenditure")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee_menu()
            elif choice == '2':
                self.update_employee_menu()
            elif choice == '3':
                self.company.increase_pay()
                print("Pay increased for all employees.")
            elif choice == '4':
                self.generate_pay_slip_menu()
            elif choice == '5':
                self.display_department_employees_menu()
            elif choice == '6':
                self.display_employees_by_position_menu()
            elif choice == '7':
                total_salary_expenditure = self.company.total_salary_expenditure()
                print(f"Total Salary Expenditure: {total_salary_expenditure}")
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")
        

    def add_employee_menu(self):
        print("\nAdding Employee:")
        emp_num = int(input("Employee Number: "))
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        position = input("Position (Manager, Asst. Manager, Secretary, Staff): ")
        department = input("Department: ")
        birth_date = input("Birth Date (YYYY-MM-DD): ")
        rate_per_day = float(input("Rate per Day: "))
        days_worked_per_month = int(input("Number of Days Worked per Month: "))

        if position == 'Manager':
            emp = Manager(emp_num, last_name, first_name, position, department, birth_date, rate_per_day,days_worked_per_month)
        elif position == 'Asst. Manager':
            emp = AssistantManager(emp_num, last_name, first_name, position, department, birth_date, rate_per_day,days_worked_per_month)
        elif position == 'Secretary':
            emp = Secretary(emp_num, last_name, first_name, position, department, birth_date, rate_per_day, days_worked_per_month)
        elif position == 'Staff':
            emp = Staff(emp_num, last_name, first_name, position, department, birth_date, rate_per_day,
                        days_worked_per_month)
        else:
            print("Invalid position. Employee not added.")
            return

        self.company.add_employee(department, emp)
        print(f"{emp.first_name} {emp.last_name} added to {department} department.")

    def update_employee_menu(self):
        emp_num = int(input("Enter employee number to update: "))
        new_rate_per_day = float(input("Enter new rate per day: "))
        self.company.update_employee(emp_num, new_rate_per_day)
        print(f"Rate per day updated for employee number {emp_num}.")

    def generate_pay_slip_menu(self):
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year: "))
        pay_slips = self.company.generate_pay_slips(month, year)
        for pay_slip in pay_slips:
            print(pay_slip)

    def display_department_employees_menu(self):
        department_name = input("Enter department name: ")
        self.company.display_department_employees(department_name)

    def display_employees_by_position_menu(self):
        position = input("Enter position: ")
        self.company.display_employees_by_position(position)


if __name__ == "__main__":
    company_menu = CompanyMenu()
    company_menu.company.add_department("Accounting")
    company_menu.company.add_department("Human Resources")
    company_menu.company.add_department("Sales and Marketing")
    company_menu.company.add_department("Manufacturing")
    company_menu.company.add_department("Admin")
    company_menu.show_menu()

# Save employee records to a text file
    file_path = "employee_records.txt"
    company_menu.company.save_employee_records_to_file(file_path)
    print("Employee records have been saved to 'employee_records.txt'.")