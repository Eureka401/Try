import time
import sys
import os
from utils import clear
from .leaderboard import display_leaderboard


def get_level_names(d: str = "levels") -> list[str]: 
    """ List all .in files in passed directory. """
    try:
        levels = [f for f in os.listdir(d) if f.endswith(".in")]
        if not levels:
            print(f"No .in files found in {d}. What kinda game has no levels?!. Go and add some please... ")
            sys.exit(1)
        return levels
    except FileNotFoundError:
        print(f"Directory {d} not found. Don't mess with the names please! The game needs its {d} directory.")
        sys.exit(1)


def choose_level() -> tuple[str,str]:
    """ Allows players to choose level. """
    levels = get_level_names()
    print("\nAvailable Levels")
    for i, level in enumerate(levels):
        print(f"{i+1}. {level[:-3]}")
    while True:
            lvl_choice = input(f"\nChoose a level (1-{len(levels)}): ").strip()
            if lvl_choice.isdigit() and 1 <= int(lvl_choice) <= len(levels):
                lvl_name = levels[int(lvl_choice) - 1]
                return os.path.join("levels", lvl_name), lvl_name[:-3] 
            else:
                print(f"\nInvalid choice. Integers from 1 to {len(levels)} only please!")


def display_main_menu() -> list[str]:
    """ Displays main menu."""
    clear()
    print("="*5 + " Main Menu " + "="*5)
    choices = ["Start Game", "View Leaderboard", "Exit"] # Player choices
    for i, c in enumerate(choices):
        print(f"{i+1}. {c}")

    return choices



def main_menu() -> None:
    """ Main menu logic. """
    from mp1 import main as start_game # Here to avoid import error
    while True:
        choices = display_main_menu()
        player_choice = input(f"\nEnter your choice (1-{len(choices)}): ").strip()
        match player_choice:
            case "1":
                clear()
                print("Choose a level to play:")
                lvl_file, lvl_name = choose_level()
                clear()
                print(f"Loading level: {lvl_name} ", end = "", flush = "True")
                print(".", end = "", flush = "True")
                time.sleep(0.3)
                print(".", end = "", flush = "True")
                time.sleep(0.3)
                print(".", end = "\n", flush = "True")
                time.sleep(0.6)
                print("Starting game ", end = "", flush = "True")
                print(".", end = "", flush = "True")
                time.sleep(0.3)
                print(".", end = "", flush = "True")
                time.sleep(0.3)
                print(".", end = "", flush = "True")
                time.sleep(0.6)
                try:
                    start_game(lvl_file, mode="enhanced")
                except Exception as e:
                    print(f"Error: {e}")
            case "2":
                clear()
                display_leaderboard()
            case "3":
                clear()
                print("Exiting the game. Goodbye!")
                time.sleep(1)
                clear()
                sys.exit(0)
            case _ if not player_choice.isdigit():
                print("Please enter a valid number.")
                time.sleep(1)
            case _:
                print(f"\nInvalid input. Please enter a number between 1 and {len(choices)}.")
                time.sleep(1.5)


if __name__ == "__main__":
    main_menu()




