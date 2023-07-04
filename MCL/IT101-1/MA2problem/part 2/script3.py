import createFiles

city_name = input("Enter city: ")

with open("empRec.txt", "r") as file:
    empoloyee_data = file.read().splitlines()

filtered_employee = []
for employee in empoloyee_data:
    details = employee.split(",")
    if details[4].strip() == city_name:
        filtered_employee.append(f"{details[1]} {details[2]}")

for employee in filtered_employee:
    print(employee)

filename = city_name.replace(" ","_") + ".txt"

with open(filename, 'w') as file:
    for employee in filtered_employee:
        file.write(employee + "\n")

print(f"\n{filename} successfully generated.")