import os
from dataclasses import dataclass, field
from utils import clear 

LEADERBOARD_DIR = "leaderboards"


@dataclass(order=True)
class LBE: # Leaderboard Entry
    name: str = field(compare=False)
    score: int = field(compare=True)


def get_leaderboard(level: str) -> str:
    """Retrieves the file path for the leaderboard file of a level."""
    if not os.path.exists(LEADERBOARD_DIR):
        os.makedirs(LEADERBOARD_DIR)
    return os.path.join(LEADERBOARD_DIR, f"leaderboard_{level}.txt")


def load_leaderboard(level: str) -> list[LBE]:
    """Retrives a given level's leaderboard in the form of a list."""
    leaderboard = []
    fp = get_leaderboard(level)

    if os.path.exists(fp):
        try:
            with open(fp, 'r', encoding = "utf-8") as f:
                for line in f.readlines():
                    name, score = line.split(', ')
                    leaderboard.append(LBE(name,int(score)))

        except Exception as e:
            print(f"Error loading leaderboard: {e}")

    return leaderboard


def save_leaderboard(level: str, leaderboard:list[LBE]):
    """Writes new entries in a level's leaderboard."""
    fp = get_leaderboard(level)
    try:
        with open(fp, 'w', encoding = "utf-8") as f:
            for entry in leaderboard:
                f.write(f"{entry.name}, {entry.score}\n")
    except Exception as e:
        print(f"Error saving leaderboard: {e}")


def update_leaderboard(level:str, p_name:str, score:int):
    """Adds new leaderboards entry to the level's leaderboard file"""
    leaderboard = load_leaderboard(level)
    leaderboard.append(LBE(p_name, score))
    leaderboard = sorted(leaderboard, reverse=True)
    save_leaderboard(level, leaderboard)


def display_leaderboard():
    """Displays the leaderboard entries for each level in the levels directory."""
    clear()
    if not os.path.exists(LEADERBOARD_DIR):
        print("No leaderboard data available. Sorry!")
        input("\nPress Enter to return to the main menu.")
        return

    leaderboards = [file for file in os.listdir(LEADERBOARD_DIR) if file.startswith("leaderboard_") and file.endswith(".txt")]

    if not leaderboards:
        print("No leaderboard data available. Not make anything worth even saving yet?")
    else:
        for leaderboard in leaderboards:
            level = leaderboard[len("leaderboard_"):-4]
            fp = os.path.join(LEADERBOARD_DIR, leaderboard)

            print("="*5 + f"* Leaderboard for {level[:-3]} *" + "="*5)
            try:
                dis_ldb = load_leaderboard(level) # dis_ldb - Display Leaderboard
                if dis_ldb:
                    for i, entry in enumerate(dis_ldb):
                        print(f"{i+1}. {entry.name} - {entry.score}")
                else:
                    print(f"Dry as a desert. Go set a record!")
            except Exception as e:
                print(f"Error displaying level leaderboards: {e}")
            print() # Buffer

    input("\nPress Enter to return to the main menu.")
