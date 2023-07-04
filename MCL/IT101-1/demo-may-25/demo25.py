import createFile

f = open('txtUsers.txt','r')
users = f.readline()
users = f.read()
f.close()

unames = list()
upws = list()
ufnames = list()
uTypes = list()

#user get data in text fiile
for u in users.split('\n'):
    data = u.split(",")
    unames.append(data[0])
    ufnames.append(data[1])
    upws.append(data[2])
    uTypes.append(data[3])

#def menu display by the position

def menu(utype):
    if utype == "OWNER":
        print("""1 - View items
        2. View Sales
        3.Add User
        4.Log Out""")

    elif utype == "CLERK":
        print("""1. View Items
        2. Add Product
        3. Update Product
        4. Log Out""")

    else:
        print("""1. View Items
        2. Orders
        3. View Sales
        4. Log Out""")

def main():
    while True:
        ans = input("Start Yes/No?: ").upper()
        if ans == "NO":
            print("Good Bye!")
        elif ans == "YES":
            while True:
                uname = input("Enter username: ")
                pw = input("Enter password: ")
                if uname in unames:
                    pos = unames.index(uname)
                    if pw != upws.index(pos):
                        print("Password Incorrect.")
                        continue
                    break
                print("User does not exists.")

    print(f"Welcome, {uTypes[pos].title()} {ufnames[pos]}")
    while True:
        menu(uTypes[pos])
        choice = input("Enter your choice: ")
        if choice == "4":
            print(f"Bye, {uTypes[pos].title()} {ufnames[pos]}")
            break
    else:
        print("Invlid Code.")

menu()