#stylist information
sID = [1,2,3]
sName = ["Marimar","Bella", "Bea"]
sPF = [500, 300, 250]

stylist = [[1,"Marimar",500],[2,"Bella",300],[3,"Bea",250]]


#services
sCode = ['A','B','C']
sDesc = ['Hair Rebond','Manicure&Pedicure','Hair Spa']
sPrice = [999,299,499]

services =[['A','Hair Rebond',999],['B','Manicure&Pedicure',299],
['C','Hair Spa',499]]

cName = []
cStylist = []
cService = []
ServicePrice = []
servCtr = [0,0,0]
stylistPF = [0,0,0]
totaLIncome = 0 
# Hey there, start typing your Python code here...
def display_Service():
    for i in range (len(sCode)):
        print(f"{sCode[i]}\t{sDesc[i]}\t{sPrice[i]}")
        print("-----------------------------------------------")

def display_Stylist():
    for i in range (len(sID)):
        print(f"{sID[i]}\t{sName[i]}\t{sPF[i]}")
        print("-----------------------------------------------")
    
def avail_Service():
    #making it loop for not inputing correct value
    while True:  
        Cn = input('Enter customer name: ')
        if Cn.strip() != "":
            break
        print("Please enter a name!")
    #making it loop for not inputing correct value
    while True:
        stc = int(input('Enter stylist code: '))
        if stc in sID:
            break
        print("Invalid Stylist ID.")
        #making it loop for not inputing correct value
    while True:
        cOde = input('Enter service code: ').upper()
        if cOde in sCode:
            break
        print("Invalid Service code.")
    #to store in list
    cName.append(Cn)
    cStylist.append(stc)
    cService.append(cOde)
    ServicePrice.append(sPF[sID.index(stc)]+sPrice[sCode.index(cOde)])
        
    print(f"Hi {Cn} You choose {sName[sID.index(stc)]}. To do your {sDesc[sCode.index(cOde)]}.")
    print("---------------------------------------------------------")
def display_listCustomer():
    if len(cName) == 0:
        print("No customer in the list.")
        print("-----------------------------------------------")
    for i in range (len(cName)):
        print(f'{cName[i]}\t{sName[sID.index(cStylist[i])]}\t{sDesc[sCode.index(cService[i])]}\t{ServicePrice[i]}')
        print("---------------------------------------------------------")
def delete_customer():
    if len(cName) == 0:
        print("No customer in the list.")
        print("-----------------------------------------------")
    else:
        cn = input("Enter customer name:")
        #to delete a list using .pop method
        if cn in cName:
            i = cName.index(cn)
            cStylist.pop(i)
            cService.pop(i)
            ServicePrice.pop(i)
            cName.pop(i)
            print("Deleted")
            print("-----------------------------------------------")
        else:
            print("Customer not found!")
            print("-----------------------------------------------")
def Clear_customer():
    #clear the list using .clear method
    cStylist.clear()
    cService.clear()
    ServicePrice.clear()
    cName.clear()
    print("All Records are deleted")
    print("-----------------------------------------------")
def display_summary_availed_service():
    #reset the counter
    servCtr = [0,0,0]
    #to get counter for the service available
    for i in cService:
        servCtr[sCode.index(i)] += 1
    for i in range(len(sCode)):
        print(f"{sDesc[i]} {servCtr[i]}")
        print("-----------------------------------------------")

def prof_feePerStylist():
    stylist = [0,0,0]
    #calculate the total fee of the stylist he get on one day service
    for i in cStylist:
        stylistPF[sID.index(int(i))] += sPF[sID.index(int(i))]
    #printing of every stylist total fee
    for i in range(len(sName)):
        print(f"{sName[i]} {stylistPF[i]}")
        print("-----------------------------------------------")

def total_Income():
    #calculating the total income
    totaLIncome = 0
    for i in cService:
        totaLIncome+= sPrice[sCode.index(i)]
    print(f"The total income of the store {totaLIncome}")
    print("-----------------------------------------------")

def add_service():
    new_code = input("Enter new service code: ").upper()
    new_desc = input("Enter new service description: ")
    new_price = float(input("Enter new service price: "))

    sCode.append(new_code)
    sDesc.append(new_desc)
    sPrice.append(new_price)
    services.append([new_code, new_desc, new_price])

    print("New service added successfully!")
    print("-----------------------------------------------")

def bill_Out():
    cn = input("Enter customer name: ")
    total_payment = 0
    for i in range(len(cName)):
        if cName[i] == cn:
            total_payment += ServicePrice[i]
        if total_payment > 0:
            print(f"{cn} will pay: {total_payment:.2f}")
            payment = float(input("Enter the payment amount: "))
            if payment >= total_payment:
                change = payment - total_payment
                print(f"Payment successful! Change: {change:.2f}")
                # Deduct the payment amount from the customer's account
                for i in range(len(cName)):
                    if cName[i] == cn:
                        ServicePrice[i] -= total_payment
                        break
            else:
                print("Insufficient payment amount.")
        print("-----------------------------------------------")

while True:
    
    print("""MENU
(A) Display Services
(B) Display Stylist
(C) Avail Service
(D) Display list of Customers
(E) Delete a customer based on customer number in the list
(F) Clear customers
(G) Display Summary (count per service) of availed services
(H) Display Total Professional Fee per stylist
(I) Display Total Income
(j) Add Service
(K) Bill Out
(X) Exit""")
    choice = input("Enter your choice: ").upper()
    print("-----------------------------------------------")
    if choice == "X":
        break
    elif choice == "A":
        display_Service()
    elif choice == "B":
        display_Stylist()
    elif choice == "C":
        avail_Service()
    elif choice == "D":
        display_listCustomer()
    elif choice == "E":
        delete_customer()
    elif choice == "F":
        Clear_customer()
    elif choice == "G":
        display_summary_availed_service()
    elif choice == "H":
        prof_feePerStylist()
    elif choice == "I":
        total_Income()
    elif choice == "J":
        add_service()
    elif choice == "K":
        bill_Out()
    else:
        print("Invalid choice!")
        print("-----------------------------------------------")
        
print("Thank you!")   