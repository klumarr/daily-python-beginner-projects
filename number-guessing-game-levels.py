import random

def get_level():
    print("Choose a level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    return int(input("Enter your choice: "))

def get_random_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)
    else:
        print("Invalid level choice. Please restart the game.")
        exit()

level = get_level()
number_to_guess = get_random_number(level)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess the number: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
