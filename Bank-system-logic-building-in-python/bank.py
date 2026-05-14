import os

File_Name = "bank.txt"
print("\n------------------MAINU------------------")
def create_account():
    name = input("Enter your name: ")
    print("-------------------------------------------------------------------")
    account_number = input("Enter your account number: ")    
    print("-------------------------------------------------------------------")
    password = input("Create a password: ")
    print("-------------------------------------------------------------------")
    balance = input("Enter your initial deposit minimum 500: ")
    print("_________________________________________________________________________________________________________\n")


    if account_exists(account_number):
        print ("Account number already exists!")
        print("_________________________________________________________________________________________________________\n")
        return
    
    with open(File_Name, "a") as file:
        file.write(f"{name},{account_number},{password},{balance}\n")
    print("Account created successfully!")
    print("_________________________________________________________________________________________________________\n")


def account_exists(account_number):
    if not os.path.exists(File_Name):
        return False
    
    with open(File_Name, "r") as file:
        for line in file:
            account_details = line.strip().split(',')
            if account_details[1] == account_number:
                return True
    return False


def authenticate(account_number):
    print("-------------------------------------------------------------------")
    password = input("Enter your password: ")

    with open(File_Name, "r") as file:
        for line in file:
            account_details = line.strip().split(',')
            if account_details[1] == account_number and account_details[2] == password:
                return account_details
            
    print("-------------------------------------------------------------------")
    print("Athentication failed!")
    print("_________________________________________________________________________________________________________\n")
    return None


def Credit(account_number):
    account_details = authenticate(account_number)
    if account_details:
        print("-------------------------------------------------------------------")
        credit_amount = float(input("Enter amount to credit: "))
        new_balance = float(account_details[3]) + credit_amount
        update_account(account_number,new_balance)
        print("-------------------------------------------------------------------")
        print(f"Amount credited successfully! New balance: {new_balance}")
        print("_________________________________________________________________________________________________________\n")



def Deposit(account_number):
    account_deatils = authenticate(account_number)
    if account_deatils:
        print("-------------------------------------------------------------------")
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > float(account_deatils[3]):
            print("-------------------------------------------------------------------")
            print("Insufficient balance!")
        else:
            new_balance = float(account_deatils[3]) - deposit_amount
            update_account(account_number, new_balance)
            print("-------------------------------------------------------------------")
            print(f"Amount deposited successfully! New balance: {new_balance}")    
            print("_________________________________________________________________________________________________________\n")



def Check_balance(account_number):
    account_details = authenticate(account_number)
    if account_details:
        print("-------------------------------------------------------------------")
        print(f"Current balance: {account_details[3]}")
        print("_________________________________________________________________________________________________________\n")



def update_account(account_number, new_balance):
    with open(File_Name, "r") as file:
        lines = file.readlines()

    with open(File_Name, "w") as file:
        for line in lines:
            account_deatails = line.strip().split(',')
            if account_deatails[1] == account_number:
                file.write(f"{account_deatails[0]},{account_number},{account_deatails[2]},{new_balance}\n")
            else:
                file.write(line)


def main_menu():
    while True:
        print("\n1. Create Account")
        print("2. Credit")
        print("3. Deposit")
        print("4. Checck Balance")
        print("5. Exit")
        print("---------------------------------------------------------------------------------------------------------")

        


        choice = input("Enter your choice: ")
        print("_________________________________________________________________________________________________________\n")

        if choice == '1':
            create_account()
        elif choice in ["2", "3", "4"]:
            account_number = input("Enter your account number: ")
            if not account_exists(account_number):
                print("-------------------------------------------------------------------")
                print("Account number doesn't exist!")
                print("_________________________________________________________________________________________________________\n")
            else:
                if choice == '2':
                    Credit(account_number)
                elif choice == '3':
                    Deposit(account_number)
                elif choice == '4':
                    Check_balance(account_number)

        elif choice == '5':
            print("Good bye!")
            print("_________________________________________________________________________________________________________\n")
            break
        else:
            print("Invalid choose!\n""Try again.")
            print("_________________________________________________________________________________________________________\n")

if __name__ == "__main__":
    main_menu()