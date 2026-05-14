import random

def play_game():
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
        possible_choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(possible_choices)
        print(f"\nComputer chose {computer_choice}")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Usage
play_game()