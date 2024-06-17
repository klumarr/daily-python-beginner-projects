import random
import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# length = int(input("Enter the desired password length: "))
# print(f"Generated password: {generate_password(length)}")


def generate_password(length, min_uppercase, min_lowercase, min_digits, min_punctuation):
    if min_uppercase + min_lowercase + min_digits + min_punctuation > length:
        raise ValueError("Minimum requirements exceed the desired password length")

    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    punctuation_chars = string.punctuation

    # Select required number of characters from each set
    password_chars = [
        random.choice(uppercase_chars) for _ in range(min_uppercase)
    ] + [
        random.choice(lowercase_chars) for _ in range(min_lowercase)
    ] + [
        random.choice(digit_chars) for _ in range(min_digits)
    ] + [
        random.choice(punctuation_chars) for _ in range(min_punctuation)
    ]

    # Fill the rest of the password length with random choices from all characters
    all_chars = uppercase_chars + lowercase_chars + digit_chars + punctuation_chars
    password_chars += [
        random.choice(all_chars) for _ in range(length - len(password_chars))
    ]

    # Shuffle the characters to ensure randomness
    random.shuffle(password_chars)

    # Join the list to form the final password
    password = ''.join(password_chars)
    return password

# Prompt the user for password requirements
length = int(input("Enter the desired password length: "))
min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
min_digits = int(input("Enter the minimum number of digits: "))
min_punctuation = int(input("Enter the minimum number of punctuation characters: "))

# Generate and print the password
try:
    password = generate_password(length, min_uppercase, min_lowercase, min_digits, min_punctuation)
    print(f"Generated password: {password}")
except ValueError as e:
    print(e)
