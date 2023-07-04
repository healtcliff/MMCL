import createFile

# Hey there, start typing your Python code here...

f = open('empRec.txt', 'r')
users = f.read()
f.close

empNo = list()
fnames = list()
lnames = list()
address = list()
city = list()
county = list()
state = list()
birthdate = list()
zip = list()
phone_1 = list()
phone_2 = list()
mail = list()
web = list()

for u in users.split('\n'):
    data = u.split(',')
    empNo.append(data[0])
    fnames.append(data[1])
    lnames.append(data[2])
    address.append(data[3])
    city.append(data[4])
    county.append(data[5])
    state.append(data[6])
    birthdate.append(data[7])
    zip.append(data[8])
    phone_1.append(data[9])
    phone_2.append(data[10])
    mail.append(data[11])
    web.append(data[12])
    

def main():
    while True:
        emPno = input("Enter employee no.: ")
        if emPno in empNo:
            pos = empNo.index(emPno)
            print(f"Name: {fnames[pos]} {lnames[pos]}")
            print(f'Adress: {address[pos]}')
            print(f'City: {city[pos]}')
            print(f'County: {county[pos]}')
            print(f'State: {state[pos]}')
            print(f'Birth Date: {birthdate[pos]}')
            print(f'zip: {zip[pos]}')
            print(f'phone 1: {phone_1[pos]}')
            print(f'phone 2: {phone_2[pos]}')
            print(f'Email: {mail[pos]}')
            print(f'web: {web[pos].replace(";","")}')
            return
        else:
            print("Employee does not exist.")
            break

    

main()

