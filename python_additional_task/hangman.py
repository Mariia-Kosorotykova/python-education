"""This module implements Hangman game"""


import sys
import random
from pictures import HANGMAN_PICS

print("Hello! Rules: You must guess the word and you have 7 attempts for it. Start game!")

word_list = [
    "loop", "python", "random", "education", "django", "flask",
    "condition", "environment", "interface", "docker"
]

past_words = []

def enter_letter():
    """This module describe game logic"""
    secret_word = word_list[random.randint(0, len(word_list) - 1)]

    print(secret_word)

    past_words.append(secret_word)

    show_secret_word = "_" * len(secret_word)
    print(show_secret_word)
    secret_word_list = list(show_secret_word)

    remaining_attempts = 7
    attempts = 0
    user_attempts = []

    while attempts < 7:
        if secret_word_list == list(secret_word):
            print("_" * 7)
            print("Congratulations! You won! :)")
            print(f"The hidden word is: {str(secret_word).upper()}.")
            print("_" * 7)
            menu()

        user_letter = input("Enter letter: ").lower()

        if not user_letter.isalpha() or len(user_letter) > 1:
            print("Invalid input. Only single letter accepted!")
            continue

        elif user_letter in user_attempts:
            print("You've already entered this letter")
            print(f"Your inputs: {' '.join(user_attempts)}")
            continue

        elif user_letter in secret_word:
            print("You guessed right!")

            for i, j in enumerate(secret_word):
                if j == user_letter:
                    secret_word_list[i] = j

            show_secret_word = "".join(secret_word_list)
            user_attempts.append(user_letter)
            print(show_secret_word)
            print(f"You have {remaining_attempts} attempts remaining")
            print(f"Your inputs: {' '.join(user_attempts)}")

        else:
            print("Oh, no! There is no such letter in the hidden word!")
            print(HANGMAN_PICS[attempts])
            attempts += 1
            remaining_attempts -= 1
            print(f"You have {remaining_attempts} attempts remaining")
            print(show_secret_word)
            print(f"Your inputs: {' '.join(user_attempts)}")
            user_attempts.append(user_letter)
    print(f"The hidden word is: {str(secret_word).upper()}.")
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
            sys.exit("Bye!")
        else:
            print("Choice doesn't correct!")

if __name__ == "__main__":
    menu()
