import random
from words import words 

# print(words)

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0 and "_" in guessed:
    print("\nYou have used these letters: ", ' '.join(guessed_letters))

    print("\nCurrent word: " + " ".join(guessed))
    guess = input("Guess a letter: ").lower()


    if guess in guessed_letters:
        print("You already guessed that letter.")
    
    elif guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                guessed[index] = guess

    else:
        attempts -= 1
        print(f"\nWrong guess. You have {attempts} left.")

    guessed_letters.append(guess)

if "_" not in guessed:
    print(f"\nBitch you guessed it! The word is: {word}")
else:
    print(f"\nSorry, you ran out of attempts. The word was: {word}")