def load_flashcards(filename):
    flashcards = {}
    with open(filename, 'r') as file:
        for line in file:
            question, answer = line.strip().split(',')
            flashcards[question] = answer
    return flashcards

def quiz_user(flashcards):
    for question, answer in flashcards.items():
        user_answer = input(f"{question}: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {answer}.")

flashcards = load_flashcards('flashcards.txt')
quiz_user(flashcards)