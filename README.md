# 🥚 Welcome to **Egg Roll!** 🐣

## For Players:

### About the game:
The goal in this game is to guide as many eggs into nests possible, but you can only move them around by tilting the whole grid! 
The eggs can roll into walls and other eggs just fine, but beware of the frying pans strewn about in the field! Get eggs cooked and you lose points!
The less moves you use, the more points you get, so use your head to figure out the best course for the eggs! Have fun~

### 🤔 How to run the game:
1. Ensuring Pre-requisites
    - Install python 3.10 or later.
2. Seting-up the Game
     - Download or clone this repository onto your local machine.
     - Navigate to the repository folder.
3. Game Launch
     - Open your terminal or command prompt inside the folder.
     - Choose one of the following modes to start the game:

#### 🔹Basic Mode (Default):
  Start game in basic mode by entering :
  ```bash
  python3 mp1.py levels/<insert level name here>.in
  ```

#### 🔹Enhanced Mode:
  Start game in basic mode by entering :
  ```bash
  python3 mp1.py --mode enhanced
  ```

### 🎮 Game Controls
- **Left**: Enter `l` or `L`
- **Right**: Enter `r` or `R`
- **Forward**: Enter `f` or `F`
- **Backward**: Enter `b` or `B`
- **Undo**: Enter `undo` 
- **Restart**: Enter `restart`
- **Quit**: Enter `quit`
- Please follow on-screen instructions for specific circumstances.
- Note: if you wish to undo, restart, or quit, please only input "undo", "restart", or "quit",  or else the input will be treated as an input containing moves.
- Double Note: the undo and restart functionalities are only available in the enhanced mode.
  
## For program validators:
### Code Organization
- The project was structured as follows:
  - Main Directory
    - mp1.py: Responsible for the core game logic.
    - utils.py: Contains the utility function clear().
    - bonus_features: A Package that contains modules for enhanced game mode implementation.
      - main_menu.py: Handles the display and functionality of the main menu.
      - leaderboards.py: Manages the leaderboard system, including updating, displaying, and saving high scores.
      - restart.py: Has a single function that resets level state to the beginning
    - leaderboards: A sub-directory that contains all level-specific leaderboard.txt files
    - levels: A sub-directory where users can input their own levels.
    - 
### Algorithms and Implementation
- The salient feature of the program is a GameState class that tracks all the information about the game state in its attributes, with the most important being the grid, points, remaning moves and the coordinates of all the eggs in the grid.
- Enums are also used to make the Move type, representing the directions the grid can be tilted. These are used to match with the inputs made by the player and the coordinate changes of the eggs once the input is proccessed. 
- The main() function is called when a game starts, beginning by loading the grid and number of possible moves from the file path in the typed command and using the retrieved information to create an object of the GameState class.
- From there the programs repeatedy asks for inputs from the player until no more moves can be made or there are no more eggs in the grid.
- Once a valid input is made, each character is either converted to its corresponding Move or ignored. The resulting list of Moves is then passed into the GameState object's apply_changes() function.
- The apply_changes(), _go(), and _target_cell_processor() do the bulk of the work. For each Move object in the passed list, the egg is moved one tile in the corresponding direction. The _target_cell_processor() method handles an egg's interaction with it's destination, be it not moving, getting nested, getting fried, or moving one tile.
- If at least one egg is moved, the loop in the _go() method keeps going until no change in the grid is detected. For each iteration the state of the grid as the eggs move tile by tile is printed. 
### Implemented Bonus Features
- The bonus features in this project are encapsulated in an "enhanced" mode. These features include a main menu, persistent level-based leaderboard system, being able to restart, being able to undo moves, and level selection.
- The undo functionality uses an attribute of the GameState object to store previous game states. Once an input is made the current game state is added to a list before the changes are applied. If the player types "undo", the last item in the list is used to change GameState's attributes to the past version.
- When a GameState object is created, its initial grid and available moves are stored as attributes, so when the player inputs "restart", the GameState's main grid and number of moves left are simplet set back to these, and the rest of the stats are reset.
-  Leaderboards make use of a LBE (Leaderboard Entry) dataclass, consisting of a name and score. If the player wishes to save their score on the leaderboard, a leaderboards directory is automatically made if none exists. A corrresponding leaderboard in the form of a text file is made for each level automatically as well. When leaderboards are displayed, the text in the files are converted to LBE objects, whose attributes are then printed. When a score is saved, the program simply writes to the level's text file.
-  The main menu offers the player to start a game, see the leaderboards, or exit, using the numbers 1-3 as inputs. It asks for inputs until a valid input is made.
-  Typing "1" leads to level select. The files in the levels directory are loaded and displayed, and the player is asked for integer inputs once again. Once a level is chosen, the game begins with "enhanced" mode on, letting the player use the restart and undo functionalities.
### Unit Tests
- Assertions for the following are present:
    - _input_to_move_converter()
    - move_checker()
    - apply_moves()
    - go()
    - _target_cell_processor()
    - undo()
    - restart()
- Assertions cover empty inputs, single inputs, multiple inputs, special characters, and interactions with each type of tile
