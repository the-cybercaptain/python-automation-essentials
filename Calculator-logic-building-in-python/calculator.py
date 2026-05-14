print("\n--------------------------------------(Calculator)-----------------------------------\n")
print("==>  Here is your calculator!")
print("\n-------------------------------------------------------------------------------------\n")


def sum():
    sum = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            sum = num
        elif number == 2:
            print(f"\nThe addition of value {sum} and 'value {number}' {num}")
            sum += num
            print("------------------------------\n")
            print(f"The final result is: {sum}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                print(f"\nThe addition of value {sum} and 'value {number}' {num}")
                sum += num
                print("------------------------------\n")
                print(f"The final result is: {sum}")
                print("\n-------------------------------------------------------------------------------------\n")


def subtraction():
    sub = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            sub = num
        elif number == 2:
            print(f"\nThe subtraction from value {sub} to 'value {number}' {num}")
            sub -= num
            print("------------------------------\n")
            print(f"The final result is: {sub}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                print(f"\nThe subtraction from value {sub} to 'value {number}' {num}")
                sub -= num
                print("------------------------------\n")
                print(f"The final result is: {sub}")
                print("\n-------------------------------------------------------------------------------------\n")


def multiplication():
    mul = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            mul = num
        elif number == 2:
            print(f"\nThe multiplication of value {mul} with 'value {number}' {num}")
            mul *= num
            print("------------------------------\n")
            print(f"The final result is: {mul}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                print(f"\nThe multiplication of value {mul} with 'value {number}' {num}")
                mul *= num
                print("------------------------------\n")
                print(f"The final result is: {mul}")
                print("\n-------------------------------------------------------------------------------------\n")


def division():
    div = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            div = num
        elif number ==2 :
            print(f"\nThe division of value {div} with 'value {number}' {num}")
            div /= num
            print("------------------------------\n")
            print(f"The final result is: {div}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                print(f"\nThe division of value {div} with 'value {number}' {num}")
                div /= num
                print("------------------------------\n")
                print(f"The final result is: {div}")
                print("\n-------------------------------------------------------------------------------------\n")


def division_int():
    div_int = 0
    rm = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            division_int = num
            rm = num
        elif number == 2:
            print(f"\nThe division of value {division_int} with 'value {number}' {num}")
            division_int //= num
            rm = rm - (division_int * num)
            print("------------------------------\n")
            print(f"The final result is: {division_int} and The Reminder is {rm}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                if rm > num:
                    print(f"\nThe division of value {rm} with 'value {number}' {num}")
                    division_int = rm // num
                    rm = rm - (division_int * num)
                    print("------------------------------\n")
                    print(f"The final result is: {division_int} and The Reminder is {rm}")
                    print("\n-------------------------------------------------------------------------------------\n")
                else:
                    print(f"The Loop has stopped because the Reminder is already equal to zero. \nSo, The final result is: {division_int} and The Reminder is {rm}")
                    print("\n-------------------------------------------------------------------------------------\n")
                    break

def reminder():
    rem = 0
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1:
            rem = num
        elif number == 2:
            print(f"\nThe division of value {rem} with 'value {number}' {num}")
            rem %= num
            print("------------------------------\n")
            print(f"The final result is: {rem}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                print(f"\nThe division of value {rem} with 'value {number}' {num}")
                rem %= num
                print("------------------------------\n")
                print(f"The final result is: {rem}")
                print("\n-------------------------------------------------------------------------------------\n")

            
def square():
    for number in range(1, length+1):
        num = float(input(f"Enter value {number}: "))
        print("------------------------------")
        if number == 1 or number == 2:
            sq = num **2
            print(f"\nThe square of 'value {number}' {num} is: {sq}")
            print("\n-------------------------------------------------------------------------------------\n")
        elif number >= 3:
            choice = input("Do you want to continue y/n ?: ").lower()
            print("------------------------------")
            if choice != "y":
                print("\nThanks for using this feature of calculator")
                print("\n-------------------------------------------------------------------------------------\n")
                break
            else:
                sq = num **2
                print(f"\nThe square of 'value {number}' {num} is: {sq}")
                print("\n-------------------------------------------------------------------------------------\n")


def exit_():
    print("Thanks for using this calculator.\n\nThe Developer of this Calculator is ** Phoenix King **")
    print("\n-------------------------------------------------------------------------------------\n")
    exit()


while True:

    print("\nEnter your choice:\n\n1 ==>  Addition \n2 ==>  Subtraction \n3 ==>  Multiplication \n4 ==>  Division  \n5 ==>  Division_int \n6 ==>  Reminder \n7 ==>  Taking Square \n8 ==>  Exit")
    print("\n-------------------------------------------------------------------------------------\n")
    choice = int(input("Your choice is: "))
    print("\n-------------------------------------------------------------------------------------")


    if  choice == 1:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        sum()

    elif choice == 2:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        subtraction()

    elif choice == 3:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        multiplication()
    
    elif choice == 4:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        division()

    elif choice == 5:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        division_int()

    elif choice == 6: 
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        reminder()

    elif choice == 7:
        length = int(input("Enter number length you want to work: "))
        print("-------------------------------------------------------------------------------------\n")
        square()
    
    elif choice == 8:
        exit_()

    else:
        print("You entered an invalid number. Please enter a valid number.")
        print("\n-------------------------------------------------------------------------------------\n")  