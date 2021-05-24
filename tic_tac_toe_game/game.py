"""This module describe game Tic Tac Toe"""


import sys
import logging

logging.basicConfig(filename='history_game.txt',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

def add_new_username():
    """This method adds names of new players"""
    player1 = input("Please, enter name first user: ")
    player2 = input("Please, enter name second user: ")
    player_sign = {"X": player1, "0": player2}
    return player1, player2, player_sign

def check_win(table_cells):
    """This method checked matches with winner combinations"""
    winner_sets = [(1, 2, 3), (4, 5, 6),
                   (7, 8, 9), (1, 4, 7),
                   (2, 5, 8), (3, 6, 9),
                   (1, 5, 9), (3, 5, 7)

    ]
    for i in winner_sets:
        if table_cells[i[0]] == table_cells[i[1]] == table_cells[i[2]]:
            return table_cells[i[0]]
    return False

def play(player1, player2, player_sign, players_success):
    """This method implements game core logic"""
    print(f"{player1} vs {player2} game has begun! ")
    print(f"{player1} will play - 'X'")
    print(f"{player2} will play - '0'")

    table_cells = list(range(10))
    display_game_field(table_cells)
    counter = 0
    winner_exists = True

    while True:
        if counter == 9:
            print("Draw! :)")
            winner_exists = False
            break
        if counter >= 5:
            finish_game = check_win(table_cells)
            if finish_game:
                print(f"Winner {player_sign[finish_game]}")
                break
        try:
            if not counter % 2:
                player1_turn = int(input(f"{player1} your turn: "))
                if str(table_cells[player1_turn]) not in "X0":
                    table_cells[player1_turn] = "X"
                else:
                    print("This cell is already booked.")
                    continue
            else:
                player2_turn = int(input(f"{player2} your turn: "))
                if str(table_cells[player2_turn]) not in "X0":
                    table_cells[player2_turn] = "0"
                else:
                    print("This cell is already booked.")
                    continue

        except(IndexError, ValueError):
            print("Please, enter number of free cell.")
            continue
        else:
            counter += 1
            display_game_field(table_cells)
    write_to_file(winner_exists, finish_game, player_sign)
    restart_game(player1, player2, finish_game, player_sign, players_success)

def display_game_field(table_cells):
    """This method shows the game field state"""
    print("-" * 13)
    for i in range(3):
        print("|", table_cells[i*3 + 1], "|",
              table_cells[i*3 + 2], "|",
              table_cells[i*3 + 3], "|")
        print("-" * 13)

def write_to_file(winner_exists, finish_game, player_sign):
    """This module write to file logs"""
    if winner_exists:
        logging.info("Winner: %s", player_sign[finish_game])
    else:
        logging.info("Game finished with DRAW")

def restart_game(player1, player2, finish_game, player_sign, players_success):
    """Implements restart game with players from previous game"""
    while True:
        print("1 - Restart game")
        print("2 - Exit to menu")

        try:
            user_choice = int(input("Please, enter your choice: "))
        except (ValueError, TypeError):
            print("Enter NUMBER, please.")
            continue
        else:
            if user_choice == 1:
                if finish_game:
                    players_success[player_sign[finish_game]] += 1
                    for key, value in players_success.items():
                        print(f"Player {key} has {value} score")
                play(player1, player2, player_sign, players_success)
            elif user_choice == 2:
                menu()
            else:
                print("Enter, please, number 1 or 4.")

def view_prev_games(filename):
    """Displays games history and winners"""
    with open(filename, "r") as file:
        previous_games = file.read()
    if len(previous_games) == 0:
        print("File is empty")
    else:
        print(previous_games)

def menu():
    """Implements players menu"""
    player1, player2, player_sign = add_new_username()

    while True:
        print("1 - Start new game")
        print("2 - Change name user")
        print("3 - View game history")
        print("4 - Delete game history")
        print("5 - Exit")
        try:
            choice = int(input("Please, enter your choice: "))
        except (ValueError, TypeError):
            print("Enter NUMBER, please.")
            continue
        else:
            if choice == 1:
                players_success = {player1: 0, player2: 0}
                finish_game = play(player1, player2, player_sign, players_success)
                restart_game(player1, player2, finish_game, player_sign, players_success)
            elif choice == 2:
                player1, player2, player_sign = add_new_username()
            elif choice == 3:
                view_prev_games("history_game.txt")
            elif choice == 4:
                with open("history_game.txt", "r+") as file:
                    file.truncate(0)
            elif choice == 5:
                sys.exit("Bye!")
            else:
                print("Enter, please, number between 1 and 4.")

if __name__ == "__main__":
    print("Welcome to the game of Tic-Tac-Toe!")
    print("_" * 8)
    menu()
