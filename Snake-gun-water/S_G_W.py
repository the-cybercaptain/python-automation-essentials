print("\n--------------------------------(Snake, Gun, Water)--------------------------------\n")

import random

while True:
    print("Enter your number where: \n1. Snake \n2. Gun \n3. water\n")
    player_Choice = int(input("Enter your number: "))
    print("\n-----------------------------------------------------------\n")

    computer = random.randint(1,3)
    print(f"Computer chose: {computer}")
    print("\n-----------------------------------------------------------\n")

    if player_Choice == computer:
        print("It's a tie!")
        print("-----------------------------------------------------------")

    elif player_Choice == 1:
        if computer == 2:
            print("You lose! Gun shoots the snake!")
            print("-----------------------------------------------------------")
        else:
            print("You win! Snake eats the water!")
            print("-----------------------------------------------------------\n")

    elif player_Choice == 2:
        if computer == 3:
            print("You lose! Water drowns the gun!")
            print("-----------------------------------------------------------\n")
        else:
            print("You win! Gun shoots the snake!")
            print("-----------------------------------------------------------\n")

    elif player_Choice == 3:
        if computer == 1:
            print("You lose! Snake eats the water!")
            print("-----------------------------------------------------------\n")
        else:
            print("You win! Water drowns the gun!")
            print("-----------------------------------------------------------\n")

    else:
        print("Invalid input. Please enter a number between 1 and 3.")
        print("-----------------------------------------------------------\n")


    play_again = input("Play again? (y/n): ").lower()
    print("-----------------------------------------------------------\n")

    if play_again != "y":
        print("Thanks for playing!")
        print("\n-----------------------------------------------------------\n")
        break