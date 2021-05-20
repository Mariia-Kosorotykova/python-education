"""This module implements Hangman game"""


import logging
import sys
import random
from pictures import HANGMAN_PICS

class Hangman:
    """This class describes the logic of the game"""

    print("Hello! Rules: you have to guess the word and you have 7 attempts.")

    word_list = [
        "loop", "python", "random", "education", "django", "flask",
        "condition", "environment", "interface", "docker"
    ]

    @staticmethod
    def watch_condition_hangman(attempts):
        """Shows hangman according to remaining attempts"""
        print(HANGMAN_PICS[attempts])

    def play_game(self):
        """This module describe game logic"""
        secret_word = self.word_list[random.randint(0, len(self.word_list) - 1)]

        show_secret_word = "_" * len(secret_word)
        print(show_secret_word)
        secret_word_list = list(show_secret_word)

        remaining_attempts = 7
        attempts = 0
        user_attempts = []
        game_won = True

        while attempts < 7:
            if secret_word_list == list(secret_word):
                print("_" * 7)
                print("Congratulations! You won! :)")
                print(f"The hidden word is: {str(secret_word).upper()}.")
                print("_" * 7)
                self.write_to_file(game_won, secret_word)
                menu()

            user_letter = input("Enter letter: ")

            if not user_letter.isalpha() or len(user_letter) > 1:
                print("Invalid input. Only single letter accepted!")
                continue

            if user_letter in user_attempts:
                print("You've already entered this letter")
                print(f"Your inputs: {' '.join(user_attempts)}")
                continue

            if user_letter in secret_word:
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
                self.watch_condition_hangman(attempts)
                attempts += 1
                remaining_attempts -= 1
                user_attempts.append(user_letter)
                print(f"You have {remaining_attempts} attempts remaining")
                print(show_secret_word)
                print(f"Your inputs: {' '.join(user_attempts)}")
                game_won = False
        print(f"The hidden word is: {str(secret_word).upper()}.")
        print("You lose... Try again :)")
        self.write_to_file(game_won, secret_word)
        menu()

    @staticmethod
    def write_to_file(game_won, secret_word):
        """This module write to file logs"""
        logging.basicConfig(filename='log_file.txt',
                            format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)
        if game_won:
            logging.info(f"Won game with word: {secret_word}")
        else:
            logging.info(f"Won game with word: {secret_word}")

    @staticmethod
    def view_prev_words(filename):
        """Shows words from previous games"""
        with open(filename, "r") as file:
            previous_words = file.read()
            print(previous_words)

def menu():
    """This method implements menu and starts game"""
    while True:
        print("1 - Start new game")
        print("2 - View game history")
        print("3 - Exit")
        choice_user = int(input("Please, enter your choice: "))
        player = Hangman()
        if choice_user == 1:
            player.play_game()
        elif choice_user == 2:
            player.view_prev_words("log_file.txt")
        elif choice_user == 3:
            with open("log_file.txt", "r+") as file:
                file.truncate(0)
            sys.exit("Bye!")
        else:
            print("Choice doesn't correct!")

if __name__ == "__main__":
    menu()
