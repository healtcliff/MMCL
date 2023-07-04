# services
sCode = ['A', 'B', 'C']
sDesc = ['Hair Rebond', 'Manicure&Pedicure', 'Hair Spa']
sPrice = [999, 299, 499]

services = [['A', 'Hair Rebond', 999], ['B', 'Manicure&Pedicure', 299], ['C', 'Hair Spa', 499]]

cName = []
cService = []
ServicePrice = []
servCtr = [0, 0, 0]
totaLIncome = 0

# Hey there, start typing your Python code here...

while True:

    print("""MENU
(A) Display Services
(B) Avail Service
(C) Display list of Customers
(D) Display Summary (count per service) of availed services
(E) Display Total Income
(F) Add Service
(G) Calculate Payment for Customer
(X) Exit""")
    choice = input("Enter your choice: ").upper()
    print("-----------------------------------------------")

    if choice == "X":
        break

    elif choice == "A":
        for i in range(len(sCode)):
            print(f"{sCode[i]}\t{sDesc[i]}\t{sPrice[i]}")
            print("-----------------------------------------------")

    elif choice == "B":
        while True:
            Cn = input('Enter customer name: ')
            if Cn.strip() != "":
                break
            print("Please enter a name!")

        while True:
            cOde = input('Enter service code: ').upper()
            if cOde in sCode:
                break
            print("Invalid Service code.")

        cName.append(Cn)
        cService.append(cOde)
        ServicePrice.append(sPrice[sCode.index(cOde)])

        print(f"Hi {Cn} you Avail the service {sDesc[sCode.index(cOde)]}.")
        print("---------------------------------------------------------")

    elif choice == "C":
        if len(cName) == 0:
            print("No customer in the list.")
            print("-----------------------------------------------")
        else:
            print("Customer Name\tService\tService Price")
            print("-----------------------------------------------")
            for i in range(len(cName)):
                print(f'{cName[i]}\t{sDesc[sCode.index(cService[i])]}\t{ServicePrice[i]}')
            print("-----------------------------------------------")

    elif choice == "D":
        servCtr = [0] * len(sCode)
        for i in cService:
            servCtr[sCode.index(i)] += 1
        for i in range(len(sCode)):
            print(f"{sDesc[i]} {servCtr[i]}")
            print("-----------------------------------------------")

    elif choice == "E":
        totaLIncome = sum(ServicePrice)
        print(f"The total income of the store: {totaLIncome:.2f}")
        print("-----------------------------------------------")

    elif choice == "F":
        new_code = input("Enter new service code: ").upper()
        new_desc = input("Enter new service description: ")
        new_price = int(input("Enter new service price: "))

        sCode.append(new_code)
        sDesc.append(new_desc)
        sPrice.append(new_price)
        services.append([new_code, new_desc, new_price])

        print("New service added successfully!")
        print("-----------------------------------------------")

    elif choice == "G":
        cn = input("Enter customer name: ")
        total_payment = 0
        index_to_remove = None
        for i in range(len(cName)):
            if cName[i] == cn:
                total_payment += ServicePrice[i]
                index_to_remove = i

        if total_payment > 0:
            print(f"{cn} will pay: {total_payment:.2f}")
            payment = float(input("Enter the payment amount: "))
            if payment >= total_payment:
                change = payment - total_payment
                print(f"Payment successful! Change: {change:.2f}")
                if index_to_remove is not None:
                    cService.pop(index_to_remove)
                    ServicePrice.pop(index_to_remove)
                    cName.pop(index_to_remove)
            else:
                print("Insufficient payment amount.")
        else:
            print("No pending payment for this customer.")
        print("-----------------------------------------------")

    else:
        print("Invalid choice!")
        print("-----------------------------------------------")

print("Thank you!")
