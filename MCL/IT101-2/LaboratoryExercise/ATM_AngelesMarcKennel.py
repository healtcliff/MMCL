#The getpass module provides a platform-independent way to enter a password in a command-line program
import getpass

#data bank of users, PINs, and Bank statement
users = {
    "ken": {"pin" : "1234", "amount" : 1500},
    "mac": {"pin" : "4321", "amount" : 3000},
    "nel": {"pin" : "2213", "amount" : 6000},
}

#Welcome message
def welcome_banks():
    print("**********************************")
    print("**                              **")
    print("*       Welcome to ATM banks     *")
    print("**                              **")
    print("**********************************")

#user login
def login():
    while True:
        user = input("Enter USERNAME: ").lower()
        if user in users:
            return user
        else:
            print("****************")
            print("**            **")
            print("INVALID USERNAME")
            print("**            **")
            print("****************")
def correctPin(user):   
    #checking if the pint is correct
    count = 0 
    while count < 3:
        print("-------------------")
        print("*******************")
        pin = getpass.getpass("Enter PIN: ", stream="*")
        print("*******************")
        print("-------------------")
        if pin.isdigit():
            if pin == users[user]["pin"]:
                return True
            else:
                count+=1
                print("***********")
                print("**       **")
                print("INVALID PIN")
                print("**       **")
                print("***********")
        else:
            print('------------------------')
            print('************************')
            print('PIN CONSISTS OF 4 DIGITS')
            print('************************')
            print('------------------------')
            count += 1
    return False
#display menu
def menu(user):
    while True:
        print("**********************")
        print("**                 **")
        print(str.capitalize(user), "Welcome to banks")
        print("**                 **")
        print("*********************")
        print("----------------------------------------------")
        print("**********************************************")
        response = input("Select from The Following Options: \n(1)Balance\n(2)Withdraw\n(3)Deposit\n(4)Change PIN\n(5)Exit\nEnter The Number Of Your Choices: ")
        print("**********************************************")
        print("----------------------------------------------")
        valid_responeses = ["1","2","3","4","5"]
        if response not in valid_responeses:
            print("------------------")
            print("******************")
            print("RESPONSE NOT VALID")
            print("******************")
            print("------------------")
            continue
        #choice statement
        if response == "1":
            print("-----------------------------------------")
            print("*****************************************")
            print(str.capitalize(user),"You Have",users[user]["amount"], "Pesos On Your Account")
            print("*****************************************")
            print("-----------------------------------------")

        elif response == "2":
            print("-----------------------------------------------------")
            print("*****************************************************")
            CashOut = int(input("Enter The Amount You Would like to Withdraw: "))
            print("*****************************************************")
            print("-----------------------------------------------------")
            if CashOut % 10 != 0:
                print("---------------------------------------------------------------")
                print("***************************************************************")
                print("The Amount You Want To Withdraw Must be Match of 100 Pesos bill")
                print("***************************************************************")
                print("---------------------------------------------------------------")
            else:
                users[user]["amount"] -= CashOut
                print("-----------------------------------------")
                print("*****************************************")
                print("Your New Balance Is:",users[user]["amount"], "Pesos")
                print("*****************************************")
                print("-----------------------------------------")

        elif response == "3":
            print("-----------------------------------------------------")
            print("*****************************************************")
            CashIN = int(input("Enter The Amount You Would like to Deposit: "))
            print("*****************************************************")
            print("-----------------------------------------------------")
            if CashIN % 10 != 0:
                print("---------------------------------------------------------------")
                print("***************************************************************")
                print("The Amount You Want To Deposit Must be Match of 100 Pesos bill")
                print("***************************************************************")
                print("---------------------------------------------------------------")
            else:
                users[user]["amount"] += CashOut
                print("-----------------------------------------")
                print("*****************************************")
                print("Your New Balance Is:",users[user]["amount"], "Pesos")
                print("*****************************************")
                print("-----------------------------------------")


        elif response == "4":
            print("------------------------")
            print("************************")
            NewPin = getpass.getpass("Enter New PIN: ", stream="*")
            print("************************")
            print("------------------------")
            print("------------------------")
            print("************************")
            Newpin = getpass.getpass("Confirm New PIN: ",stream="*")
            print("************************")
            print("------------------------")
            if Newpin != NewPin:
                print("---------------")
                print("***************")
                print("PIN Mismatch")
                print("***************")
                print("---------------")
            else:
                users[user]["pin"] = NewPin
                print("---------------")
                print("***************")
                print("New PIN Saved")
                print("***************")
                print("---------------")

        elif response == "5":
            exit()

def main():
    welcome_banks()
    user = login()
    if correctPin(user):
        menu(user)
    else:
        print('-----------------------------------')
        print('***********************************')
        print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
        print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
        print('***********************************')
        print('-----------------------------------')
        exit()

if __name__ == "__main__":
    main()


#https://github.com/Suresh142/atm_machine_python