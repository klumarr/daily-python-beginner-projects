import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    return input("Enter rock, paper or scissors: ").lower()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
         return "You win!"
    else:
        return "You lose!"

user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(f"Computer chose: {computer_choice}")
print(determine_winner(user_choice, computer_choice))

