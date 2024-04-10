import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    score = {"user": 0, "computer": 0}

    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print("Computer's choice:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            score["user"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print("Score - User:", score["user"], "Computer:", score["computer"])

play_game()


