#product information
pID = [1,2,3]
pName = ["Lotion","Shampoo", "Soap"]
pPrice = [500, 510, 545]

products = [[1,"Lotion",500],[2,"Shampoo",510],[3,"Soap",545]]


#customer information
custID = ['1','2','3']
custName = ['Juan','Pedro','Maria']
customers =[['1','Juan'],['2','Pedro'],['3','Maria']]

cName = []
cProduct = []
cQuantity = []
ProductPrice = []
prodCtr = [0,0,0]
CustomerPF = [0,0,0]
totalIncome = 0
# Hey there, start typing your Python code here...
def purchaseOrder():
    while True:
        stc = input("Enter customer no.: ")
        if stc in custID:
            break
        else:
            print("Customer does not exist.")
            continue
    while True:
        pCode = input("Enter product code: ")
        if pCode.isdigit() and int(pCode) in pID:
            break
        else:
            print("Invalid product code.")
            continue
    while True:
        quantity = input("Enter quantity: ")
        if not quantity.isdigit():
            print("Invalid input.")
            continue
        break
    cName.append(stc)
    cProduct.append(pCode)
    cQuantity.append(quantity)
    ProductPrice.append(pPrice[pID.index(int(pCode))] * int(quantity))
while True:
    print("""MENU
(A) Display Products
(B) Display Customer
(C) Purchase Order
(D) Display Orders
(E) Delete an order based on order number in the list
(F) Clear Orders
(G) Display Summary (count) of sold products
(H) Display Summary of total purchase per customer
(I) Display Total Sales.
(X) Exit""")
    choice = input("Enter your choice: ").upper()
    if choice == "X":
        print("Thank you")
        break
    
    elif choice == "A":
        for i in range(len(pID)):
            print(f"{pID[i]}\t{pName[i]}\t{pPrice[i]}")
    
    elif choice == "B":
        for i in range(len(custID)):
            print(f"{custID[i]}\t{custName[i]}")
    
    elif choice == "C":
        while True:
            stc = input("Enter customer no.: ")
            if stc in custID:
                break
            else:
                print("Customer does not exist.")
                continue
        while True:
            pCode = input("Enter product code: ")
            if pCode.isdigit() and int(pCode) in pID:
                break
            else:
                print("Invalid product code.")
                continue
        while True:
            quantity = input("Enter quantity: ")
            if not quantity.isdigit():
                print("Invalid input.")
                continue
            break
        cName.append(stc)
        cProduct.append(pCode)
        cQuantity.append(quantity)
        ProductPrice.append(pPrice[pID.index(int(pCode))] * int(quantity))
        while True:
            Again = input("Add more items [Y/N]? ").upper()
            if Again == "Y":
                new_cid = str(int(stc) + 1)
                while True:
                    pCode = input("Enter product code: ")
                    if int(pCode) in pID:
                        break
                    else:
                        print("Invalid product code.")
                        continue
                while True:
                    quantity = input("Enter quantity: ")
                    if not quantity.isdigit():
                        print("Invalid input.")
                        continue
                    break
                cName.append(stc)
                cProduct.append(pCode)
                cQuantity.append(quantity)
                ProductPrice.append(pPrice[pID.index(int(pCode))] * int(quantity))
            elif Again == "N":
                break
    elif choice == "D":
        if len(cName) == 0:
            print("No order in the list.")
        #for i in range(len(cName)):
            #print(f"{cName[i]}\t{custName[custID.index(cName[i])]}\t{pName[pID.index(int(cProduct[i]))]}\t{cQuantity[i]}")
        customer_names = {}
        order_count = 1
        for i in range(len(cName)):
            cid = cName[i]
            customer_name = custName[custID.index(cid)]
            if customer_name not in customer_names:
                customer_names[customer_name] = 1
                incremented_name = customer_name
            else:
                customer_names[customer_name] += 1
                incremented_name = f"{customer_name}"
            print(f"{order_count}\t{incremented_name}\t{pName[pID.index(int(cProduct[i]))]}\t{cQuantity[i]}")
            order_count += 1
            
    elif choice == "E":
        if len(cName) == 0:
            print("No order in the list.")
        else:
            cn = input("Enter record no.: ")
            if cn in cName:
                i == cName.index(cn)
                cProduct.pop(i)
                cQuantity.pop(i)
                ProductPrice.pop(i)
                cName.pop(i)
            else:
                print("Customer ID not found")
                
    elif choice == "F":
        cProduct.clear()
        cQuantity.clear()
        ProductPrice.clear()
        cName.clear()
        print("Orders Deleted")
        
    elif choice == "G":
        product_quantities = {}
        for i in range(len(pID)):
            p_name = pName[i]
            product_quantities[p_name] = 0
        for i in range(len(cName)):
            p_code = cProduct[i]
            p_name = pName[pID.index(int(p_code))]
            product_quantities[p_name] += int(cQuantity[i])
        for product in pName:
            quantity = product_quantities[product]
            print(f"{product}\t{quantity}")
            
    elif choice == "H":
        customer_total_purchase = {}
        for i in range(len(custID)):
            customer_total_purchase[custName[i]] = 0
        for i in range(len(cName)):
            p_code = cProduct[i]
            p_price = pPrice[pID.index(int(p_code))]
            quantity = int(cQuantity[i])
            customer_total_purchase[custName[custID.index(cName[i])]] += p_price * quantity
        for customer, total_purchase in customer_total_purchase.items():
            print(f"{customer}\t{total_purchase}")

            
    elif choice == "I":
        total_sales = sum(ProductPrice)
        total_sales_formatted = "{:.2f}".format(total_sales)
        print(f"Total Sales: {total_sales_formatted}")
    else:
        print("Choice not in the list.")