# prevents error from circular importing
from bonus_features.main_menu import main_menu
import sys
import time
import os
from enum import Enum
import argparse
from utils import clear
from bonus_features.restart import restart_game
from bonus_features.leaderboard import update_leaderboard


class Move(Enum):
    LEFT = ('l', 'L')
    RIGHT = ('r', 'R')
    FORWARD = ('f', 'F')
    BACKWARD = ('b', 'B')


def _input_to_move_converter(ch: str) -> Move:
    """ 
    Takes a single string character.
    Returns a Move object.
    Raises a ValueError if character cannot be converted.
    """
    for move in Move:
        if ch in move.value:

            # Invariant/s
            assert ch in set('lLrRfFbB')

            return move
    raise ValueError("Invalid move character: {ch}")


def move_checker(raw_moves: str) -> list[Move]:
    """ 
    Takes a string.
    Returns a list of Move objects.
    """
    legal_moves = []
    for move in raw_moves:
        try:
            dum_var = _input_to_move_converter(move)
        except ValueError:
            continue
        else:
            legal_moves.append(dum_var)
    return legal_moves


def ask_move(mode: str = "basic"):
    """ 
    Prompts the player to input their moves.
    Returns either a list of legal moves, 'restart', or 'undo'.
    """
    while True:
        match mode:
            case "enhanced":
                moves = input(
                    "Enter move/s (or 'restart' to restart) (or 'undo' to undo): ")
                if moves == "restart":
                    return "restart"
                elif moves == "undo":
                    return "undo"
                elif moves == "quit":
                    return "quit"
            case "basic":
                moves = input("Enter move/s: ")
        legal_moves = move_checker(moves)
        if legal_moves:
            return legal_moves


class GameState:
    """Game state represented as attributes of an object"""

    def __init__(self, grid: list[list[str]], av_moves: int, prev_moves: str = '', points: int = 0):
        self.grid = grid
        self.initial_grid = [[*row] for row in grid]
        self.row = len(grid)
        self.col = len(grid[0])
        self.av_moves = av_moves
        self.initial_av_moves = av_moves
        self.prev_moves = prev_moves
        self.points = points
        self.history = []
        self.egg_locs = self._find_eggs()
        super(GameState, self).__init__()

    def display(self, move: str = '') -> None:
        """ Displays current game state."""
        if (not self.history) or (self.av_moves == 0) or (len(self.egg_locs) == 0) or ((len(self.prev_moves) > 1) and (self.prev_moves[-2] == self.prev_moves[-1])):
            clear()
            for row in self.grid:
                print(''.join(row))
        elif move == 'undo':
            clear()
            for row in self.grid:
                print(''.join(row))
            return
        print(f'Previous moves: {self.prev_moves} \nRemaining moves: {self.av_moves} \nPoints: {self.points}')

    def _find_eggs(self) -> list[tuple[int, int]]:
        """ Finds the coordinates of eggs (🥚) in the grid. Coordinates in the form of (y, x), where x is col num and y is row num. """
        return [(i, j) for i in range(self.row) for j in range(self.col) if self.grid[i][j] == '🥚']

    def apply_moves(self, legal_moves: list[str]) -> None:
        """ 
        Takes in legal moves list.
        Applies legal moves to current game state.
        """
        # Invariant/s
        assert all(isinstance(move, Move) for move in legal_moves) == True
        assert self.av_moves > 0

        self.save_current_state()

        for move in legal_moves:
            if not self.av_moves:
                break
            self.prev_moves += {"LEFT": "←", "RIGHT": "→",
                                "FORWARD": "↑", "BACKWARD": "↓"}[move.name]
            self._go(move)

    def _go(self, move: Move) -> None:
        """ 
        Takes in Move object.
        Handles egg movements until they cannot move.
        """
        # Invariant/s
        assert self.av_moves > 0

        dy, dx = self._get_direction(move)
        eggs = self._sort_eggs_by_direction(self.egg_locs, move)

        new_grid = [[*row] for row in self.grid]

        # Assures new_grid is a different object
        assert not (new_grid is self.grid)

        updated = True      # Initialize the loop

        while updated:
            # There are eggs in the grid
            assert len(self.egg_locs) > 0

            # So that the loop stops when eggs can no longer move.
            updated = False
            new_egg_locs = []

            for (y, x) in eggs:
                ny, nx = y + dy, x + dx

                # Invariant/s
                assert isinstance(x, int)
                assert isinstance(y, int)
                assert isinstance(nx, int)
                assert isinstance(ny, int)
                assert 0 <= nx < self.col, nx
                assert 0 <= ny < self.row, ny

                # True if coordinate is out of bounds
                if not ((0 <= nx < self.col) and (0 <= ny < self.row)):
                    new_egg_locs.append((y, x))
                    continue
                elif (ny, nx) in set(new_egg_locs):  # Checks if an egg is in the target location
                    new_egg_locs.append((y, x))
                    continue

                result = self._target_cell_processor(x, y, nx, ny, new_grid)
                if result['moved']:
                    updated = True
                    if 'loc' not in result:
                        pass
                    else:
                        egg_loc = result['loc']
                        new_egg_locs.append(egg_loc)
                else:
                    egg_loc = result['loc']
                    new_egg_locs.append(egg_loc)

            eggs = self._sort_eggs_by_direction(new_egg_locs, move)

            if move == Move.BACKWARD:
                assert eggs == sorted(new_egg_locs, reverse=True)

            if not updated:
                break

            self._temp_display(new_grid)

        self._finalize_changes(new_grid, eggs)

    def _temp_display(self, grid: list[list[str]]) -> None:
        """Used to display grid changes as the _go method does its job."""
        clear()
        for row in grid:
            print(''.join(row))
        time.sleep(0.2)

    def _get_direction(self, move: Move) -> tuple[int, int]:
        """ 
        Takes in Move object.
        Outputs (y, x) changes based on direction. 
        """
        direction = {
            Move.LEFT: (0, -1),
            Move.RIGHT: (0, 1),
            Move.FORWARD: (-1, 0),
            Move.BACKWARD: (1, 0),
        }

        return direction[move]

    def _sort_eggs_by_direction(self, egg_locs, move: Move = Move.LEFT) -> list[tuple[int, int]]:
        """
        Takes in list of egg locations and Move object.
        Returns a sorted copy based on direction.
        """
        if move in {Move.RIGHT, Move.BACKWARD}:
            return sorted(egg_locs, reverse=True)
        else:
            return sorted(egg_locs)

    def _target_cell_processor(self, x: int, y: int, nx: int, ny: int, grid: list[list[str]]) -> dict:
        """
        Takes in old and new coordinates, as well as the new grid (grid copy).
        Returns a dictionary with move update status and new (or old) location of the egg if any.
        Raises ValueError for wild case.
        """
        target = grid[ny][nx]

        match target:
            case '🧱' | '🪺':
                return {"moved": False, "loc": (y, x)}
            case '🍳':
                self.points -= 5
                grid[y][x] = '🟩'
                return {"moved": True}
            case '🪹':
                grid[ny][nx] = '🪺'
                self.points += 10 + self.av_moves
                grid[y][x] = '🟩'
                return {"moved": True}
            case '🟩':
                grid[y][x] = '🟩'
                grid[ny][nx] = '🥚'
                return {"moved": True, "loc": (ny, nx)}
            case _:
                raise ValueError(f"Shouldn't reach here! Target is {target}.")

    def _finalize_changes(self, new_grid: list[list[str]], new_egg_locs: list[tuple[int, int]]):
        """
        Takes new grid and list of new egg locations.
        Changes are moved from temporary grid to the grid attribute of the GameState object."""
        self.grid = new_grid
        self.egg_locs = new_egg_locs
        self.av_moves -= 1

    def restart(self):
        """Sets the game state back to the initial conditions."""
        self.grid = [[*row] for row in self.initial_grid]
        self.av_moves = self.initial_av_moves
        self.prev_moves = ''
        self.points = 0
        self.history = []
        self.egg_locs = self._find_eggs()

    def save_current_state(self):
        """Stores the current state of the game in a list."""
        cs = {                                   # cs = Current State
            "grid": [[*row] for row in self.grid],
            "av_moves": self.av_moves,
            "prev_moves": self.prev_moves,
            "points": self.points,
            "egg_locs": list(self.egg_locs),
        }

        self.history.append(cs)

    def undo(self):
        """Undos a previous move until self.history is empty."""
        if self.history:
            cs = self.history.pop()
            self.grid = cs["grid"]
            self.av_moves = cs["av_moves"]
            self.prev_moves = cs["prev_moves"]
            self.points = cs["points"]
            self.egg_locs = cs["egg_locs"]
            self.display('undo')
        else:
            print("No moves to undo.")


def read_level_file(lfp: str):
    """
    Takes level file path.
    Retrieves initial level information from a given file path"""
    try:
        with open(lfp, encoding='utf-8') as f:
            info = [line for line in f.readlines()]
        r = info[0]  # number of rows in the grid
        av_moves = int(info[1])
        grid = [[*row[:-1]] for row in info[2:]]
    except Exception as e:
        print(f"Error loading level file: {e}")
    else:
        return grid, av_moves


def init_main(lfp: str) -> GameState:
    """
    Takes level file path.
    Initializes the game by loading the grid and available moves from a file.
    """
    if lfp:
        grid, av_moves = read_level_file(lfp)
    else:
        if len(sys.argv) < 2:
            print("The game requires filename to start.", file=sys.stderr)
            sys.exit(1)
        print(sys.argv[1])
        grid, av_moves = read_level_file(sys.argv[1])

    return GameState(grid, av_moves)


def main(lfp=None, mode="basic") -> None:  # lfp - Level File Path
    """
    Takes level file path and mode.
    Entry point for the game. Manages game loop and termination conditions.
    """
    clear()
    state = init_main(lfp)

    # Invaraint/s
    assert isinstance(state, GameState), type(state)

    while True:
        while state.av_moves > 0 and state.egg_locs:
            state.display()
            match mode:
                case "enhanced":
                    legal_moves = ask_move(mode="enhanced")
                    if legal_moves == "restart":
                        state = restart_game(state)
                        continue
                    elif legal_moves == "undo":
                        state.undo()
                        continue
                    elif legal_moves == "quit":
                        break
                case "basic":
                    legal_moves = ask_move()
            state.apply_moves(legal_moves)

        clear()
        state.display()

        if mode == "enhanced":
            if input("Want to save your score on the leaderboards? (y if yes, anything else if no):").lower() == "y":
                player_name = input(
                    "\nEnter your name for the leaderboard:\n>>> ").strip()
                update_leaderboard(lfp[7:], player_name, state.points)
            if input("\nGG's! Enter 'restart' to play again or press Enter to go back to the main menu.\n>>> ") == "restart":
                state = restart_game(state)
                continue
        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Game Mode')
    parser.add_argument('--mode', choices=["basic", "enhanced"],
                        default="basic", type=str, help='Choose game mode (default: basic)')

    args, remaining_args = parser.parse_known_args()

    if args.mode == "basic":
        parser.add_argument('path', metavar="path",
                            type=str, help='Path of level file.')

    args = parser.parse_args()

    if args.mode == "enhanced":
        main_menu()
    else:
        main()
