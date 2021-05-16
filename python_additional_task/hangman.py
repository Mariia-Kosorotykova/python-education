"""This module implements Hangman game"""


import random
from pictures import HANGMAN_PICS

print("Hello! Rules: ... . Start game!")

word_list = [
    "loop", "python", "random", "education", "django", "flask",
    "condition", "environment", "interface", "docker"
]

past_words = []

def enter_letter():
    """This module describe game logic"""
    idx_secret_word = random.randint(0, len(word_list) - 1)
    secret_word = word_list[idx_secret_word]

    print(secret_word)

    past_words.append(secret_word)

    show_secret_word = ['_' for i in secret_word]
    print(show_secret_word)

    remaining_attempts = 7
    attempts = 0
    while attempts < 7:
        user_letter = input("Enter letter: ")
        if user_letter in secret_word:
            print("You guessed right!")
            guess_idx_let = secret_word.index(user_letter)
            show_secret_word[guess_idx_let] = user_letter
            print(show_secret_word)
            print(f"You have {remaining_attempts} attempts remaining")
        else:
            print("Oh, no! There is no such letter in the hidden word!")
            print(HANGMAN_PICS[attempts])
            attempts += 1
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} attempts remaining")
            print(show_secret_word)
    print("You lose... Try again :)")
    menu()

def menu():
    """This method implements menu"""
    while True:
        print("1 - Start new game")
        print("2 - See past words")
        print("3 - Exit")
        choice_user = int(input("Please, enter your choice: "))
        if choice_user == 1:
            enter_letter()
        elif choice_user == 2:
            print(f"List of past word: {past_words}")
        elif choice_user == 3:
            exit()
        else:
            print("Choice doesn't correct!")

if __name__ == "__main__":
    menu()
