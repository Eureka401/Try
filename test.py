import pytest
from mp1 import Move, GameState, _input_to_move_converter, move_checker


def test_input_to_move_converter():
    # Valid Characters w/valid length 1
    assert _input_to_move_converter('l') == Move.LEFT
    assert _input_to_move_converter('L') == Move.LEFT
    assert _input_to_move_converter('r') == Move.RIGHT
    assert _input_to_move_converter('R') == Move.RIGHT
    assert _input_to_move_converter('b') == Move.BACKWARD
    assert _input_to_move_converter('B') == Move.BACKWARD
    assert _input_to_move_converter('f') == Move.FORWARD
    assert _input_to_move_converter('F') == Move.FORWARD


    # Diactrics(letters with accents) of Valid Characters w/valid length 1
    with pytest.raises(ValueError):
        _input_to_move_converter('ĺ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ĺ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ľ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ľ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḷ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḷ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḹ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḹ')  
    with pytest.raises(ValueError):
        _input_to_move_converter('ɍ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ɍ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ř') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ř') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ŗ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ŗ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ȑ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ȑ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḃ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḃ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḅ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḅ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḇ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḇ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ƒ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ƒ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ḟ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Ḟ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ᵮ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ᶂ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ꜰ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ꬵ') 


    # Invalid Lower case Alphabet Characters
    with pytest.raises(ValueError):
        _input_to_move_converter('k') 
    with pytest.raises(ValueError):
        _input_to_move_converter('p') 
    with pytest.raises(ValueError):
        _input_to_move_converter('q') 
    with pytest.raises(ValueError):
        _input_to_move_converter('a') 
    with pytest.raises(ValueError):
        _input_to_move_converter('s') 
    with pytest.raises(ValueError):
        _input_to_move_converter('g') 
    with pytest.raises(ValueError):
        _input_to_move_converter('v') 
    with pytest.raises(ValueError):
        _input_to_move_converter('w') 
    with pytest.raises(ValueError):
        _input_to_move_converter('h') 
    with pytest.raises(ValueError):
        _input_to_move_converter('y') 
    with pytest.raises(ValueError):
        _input_to_move_converter('ñ') 


    # Invalid Upper case Alphabet Characters
    with pytest.raises(ValueError):
        _input_to_move_converter('J') 
    with pytest.raises(ValueError):
        _input_to_move_converter('Q') 
    with pytest.raises(ValueError):
        _input_to_move_converter('G') 
    with pytest.raises(ValueError):
        _input_to_move_converter('O') 
    with pytest.raises(ValueError):
        _input_to_move_converter('D') 
    with pytest.raises(ValueError):
        _input_to_move_converter('S') 
    with pytest.raises(ValueError):
        _input_to_move_converter('I') 
    with pytest.raises(ValueError):
        _input_to_move_converter('M') 
    with pytest.raises(ValueError):
        _input_to_move_converter('X') 
    with pytest.raises(ValueError):
        _input_to_move_converter('E') 


    # Invalid Special Characters
    with pytest.raises(ValueError):
        _input_to_move_converter('!') 
    with pytest.raises(ValueError):
        _input_to_move_converter('@') 
    with pytest.raises(ValueError):
        _input_to_move_converter('#') 
    with pytest.raises(ValueError):
        _input_to_move_converter('%') 
    with pytest.raises(ValueError):
        _input_to_move_converter('$') 
    with pytest.raises(ValueError):
        _input_to_move_converter('&') 
    with pytest.raises(ValueError):
        _input_to_move_converter('*') 
    with pytest.raises(ValueError):
        _input_to_move_converter('(') 
    with pytest.raises(ValueError):
        _input_to_move_converter(')') 
    with pytest.raises(ValueError):
        _input_to_move_converter('.') 
    with pytest.raises(ValueError):
        _input_to_move_converter('?') 
    with pytest.raises(ValueError):
        _input_to_move_converter('/') 
    with pytest.raises(ValueError):
        _input_to_move_converter('|') 
    with pytest.raises(ValueError):
        _input_to_move_converter('\n') 
    with pytest.raises(ValueError):
        _input_to_move_converter(' ') 
    with pytest.raises(ValueError):
        _input_to_move_converter('<') 
    with pytest.raises(ValueError):
        _input_to_move_converter('>') 


    # Invalid Numbers
    with pytest.raises(ValueError):
        _input_to_move_converter('1') 
    with pytest.raises(ValueError):
        _input_to_move_converter('2') 
    with pytest.raises(ValueError):
        _input_to_move_converter('3') 
    with pytest.raises(ValueError):
        _input_to_move_converter('4') 
    with pytest.raises(ValueError):
        _input_to_move_converter('5') 
    with pytest.raises(ValueError):
        _input_to_move_converter('6') 
    with pytest.raises(ValueError):
        _input_to_move_converter('7') 
    with pytest.raises(ValueError):
        _input_to_move_converter('8') 
    with pytest.raises(ValueError):
        _input_to_move_converter('9') 
    with pytest.raises(ValueError):
        _input_to_move_converter('0') 


    # Valid Characters w/invalid length
    with pytest.raises(ValueError):
        _input_to_move_converter('Lr') 
    with pytest.raises(ValueError):
        _input_to_move_converter('rfb') 
    with pytest.raises(ValueError):
        _input_to_move_converter('lbFR') 
    with pytest.raises(ValueError):
        _input_to_move_converter('llllllllllllllll') 
    with pytest.raises(ValueError):
        _input_to_move_converter('lbfr'*3) 
    with pytest.raises(ValueError):
        _input_to_move_converter('frrrrrr') 
    with pytest.raises(ValueError):
        _input_to_move_converter('BF'*14) 
    with pytest.raises(ValueError):
        _input_to_move_converter('FLbrbrbrbrflFL') 
    with pytest.raises(ValueError):
        _input_to_move_converter('LrRlBfFb') 
    with pytest.raises(ValueError):
        _input_to_move_converter('LrBBBBBB') 

def test_move_checker():
    # Single character inputs containing only valid moves
    assert move_checker('l') == [Move.LEFT]
    assert move_checker('r') == [Move.RIGHT]
    assert move_checker('f') == [Move.FORWARD]
    assert move_checker('b') == [Move.BACKWARD]
    assert move_checker('L') == [Move.LEFT]
    assert move_checker('R') == [Move.RIGHT]
    assert move_checker('F') == [Move.FORWARD]
    assert move_checker('B') == [Move.BACKWARD]


    # Multicharacter inputs containing only valid moves in only lowercase
    assert move_checker('lrfb') == [Move.LEFT, Move.RIGHT, Move.FORWARD, Move.BACKWARD]
    assert move_checker('l'*2) == [Move.LEFT, Move.LEFT]
    assert move_checker('r'*3) == [Move.RIGHT, Move.RIGHT, Move.RIGHT]
    assert move_checker('b'*4) == [Move.BACKWARD, Move.BACKWARD, Move.BACKWARD, Move.BACKWARD]
    assert move_checker('f'*5) == [Move.FORWARD, Move.FORWARD, Move.FORWARD, Move.FORWARD, Move.FORWARD]
    assert move_checker('lllffbbrflfllblll') == [Move.LEFT, Move.LEFT, Move.LEFT,
    Move.FORWARD, Move.FORWARD, Move.BACKWARD, Move.BACKWARD, Move.RIGHT, Move.FORWARD, 
    Move.LEFT, Move.FORWARD, Move.LEFT, Move.LEFT, Move.BACKWARD, Move.LEFT,
    Move.LEFT, Move.LEFT]


    # Multicharacter inputs containing only valid moves in only uppercase
    assert move_checker('LRFB') == [Move.LEFT, Move.RIGHT, Move.FORWARD, Move.BACKWARD]
    assert move_checker('L'*2) == [Move.LEFT, Move.LEFT]
    assert move_checker('R'*3) == [Move.RIGHT, Move.RIGHT, Move.RIGHT]
    assert move_checker('B'*4) == [Move.BACKWARD, Move.BACKWARD, Move.BACKWARD, Move.BACKWARD]
    assert move_checker('F'*5) == [Move.FORWARD, Move.FORWARD, Move.FORWARD, Move.FORWARD, Move.FORWARD]
    assert move_checker('lllffbbrflfllblll'.upper()) == [Move.LEFT, Move.LEFT, Move.LEFT,
    Move.FORWARD, Move.FORWARD, Move.BACKWARD, Move.BACKWARD, Move.RIGHT, Move.FORWARD, 
    Move.LEFT, Move.FORWARD, Move.LEFT, Move.LEFT, Move.BACKWARD, Move.LEFT,
    Move.LEFT, Move.LEFT]


    # Inputs containing no valid moves
    assert move_checker('') == []
    assert move_checker(' ') == []
    assert move_checker('  ') == []
    assert move_checker('\n') == []
    assert move_checker('ḅ') == []
    assert move_checker('Ȑ') == []
    assert move_checker('ĺḟĺĹľĽḷḶḹḸɍɌřŘŗŖȑȐḃḂḅḄḇḆƒƑḟḞᵮᶂꜰꬵ') == []
    assert move_checker('s') == []
    assert move_checker('S') == []
    assert move_checker('kpqasgvwhyñJQGODSIMXE') == []
    assert move_checker('[') == []
    assert move_checker('!@#%$&*().?/|\n <>') == []
    assert move_checker('0') == []
    assert move_checker('1234567890') == []
    assert move_checker('hYUG35ḟ@(@|}Ř{23') == []


    # Inputs containing both valid and invalid moves
    assert move_checker('      l      ') == [Move.LEFT]
    assert move_checker(' l fl fl') == [Move.LEFT, Move.FORWARD, Move.LEFT, Move.FORWARD, Move.LEFT]
    assert move_checker('\nb\nb') == [Move.BACKWARD, Move.BACKWARD]
    assert move_checker('l ') == [Move.LEFT]
    assert move_checker(' l') == [Move.LEFT]
    assert move_checker('BLĺḟĺĹľĽḸɍɌRřrŘŗŖȑḃḂḅBḄḇbḆƒƑḟḞᵮFfꜰꬵF') == [Move.BACKWARD, Move.LEFT, Move.RIGHT, Move.RIGHT, 
    Move.BACKWARD, Move.BACKWARD, Move.FORWARD, Move.FORWARD, Move.FORWARD]
    assert move_checker('ujU7676   5ḟ@(@|  \n    }LŘ{23f') == [Move.LEFT, Move.FORWARD]


def test_GameState_init():
    # Grid with eggs on the boundary
    grid1 = [
    ['🥚','🟩', '🟩'],
    ['🟩', '🟩', '🥚'],
    ['🥚','🟩', '🥚']
    ]
    state1 = GameState(grid1, 10)
    assert state1.grid == grid1
    assert state1.initial_grid == [[*row] for row in grid1]
    assert state1.row == len(grid1)
    assert state1.col == len(grid1[0])
    assert state1.av_moves == 10
    assert state1.initial_av_moves == 10
    assert state1.prev_moves == ''
    assert state1.points == 0
    assert state1.history == []
    assert state1.egg_locs == [(0,0),(1,2),(2,0),(2,2)]


    # Grid with eggs not on the boundary
    grid2 = [
    ['🟩','🟩', '🟩', '🟩'],
    ['🟩', '🥚', '🥚', '🟩'],
    ['🟩','🟩', '🥚', '🟩'],
    ['🟩', '🟩', '🟩', '🟩']
    ]
    state2 = GameState(grid2, 5)
    assert state2.grid == grid2
    assert state2.initial_grid == [[*row] for row in grid2]
    assert state2.row == len(grid2)
    assert state2.col == len(grid2[0])
    assert state2.av_moves == 5
    assert state2.initial_av_moves == 5
    assert state2.prev_moves == ''
    assert state2.points == 0
    assert state2.history == []
    assert state2.egg_locs == [(1,1),(1,2),(2,2)]


    # Grid with no eggs
    grid3 = [
    ['🟩','🟩', '🟩', '🟩'],
    ['🟩', '🟩', '🟩', '🟩'],
    ['🟩','🟩', '🟩', '🟩'],
    ['🟩', '🟩', '🟩', '🟩']
    ]
    state3 = GameState(grid3, 6)
    assert state3.grid == grid3
    assert state3.initial_grid == [[*row] for row in grid3]
    assert state3.row == len(grid3)
    assert state3.col == len(grid3[0])
    assert state3.av_moves == 6
    assert state3.initial_av_moves == 6
    assert state3.prev_moves == ''
    assert state3.points == 0
    assert state3.history == []
    assert state3.egg_locs == []


    # Grid with no available available moves
    grid4 = [
    ['🥚','🟩', '🟩'],
    ['🟩', '🟩', '🥚'],
    ['🥚','🟩', '🥚']
    ]
    state4 = GameState(grid4, 0)
    assert state4.grid == grid4
    assert state4.initial_grid == [[*row] for row in grid4]
    assert state4.row == len(grid4)
    assert state4.col == len(grid4[0])
    assert state4.av_moves == 0
    assert state4.initial_av_moves == 0
    assert state4.prev_moves == ''
    assert state4.points == 0
    assert state4.history == []
    assert state4.egg_locs == [(0,0),(1,2),(2,0),(2,2)]


    # Grid with full nests
    grid5 = [
    ['🟩','🪺', '🟩', '🟩'],
    ['🥚', '🟩', '🟩', '🟩'],
    ['🟩','🥚', '🪺', '🟩'],
    ['🟩', '🟩', '🟩', '🟩']
    ]
    state5 = GameState(grid5, 3)
    assert state5.grid == grid5
    assert state5.initial_grid == [[*row] for row in grid5]
    assert state5.row == len(grid5)
    assert state5.col == len(grid5[0])
    assert state5.av_moves == 3
    assert state5.initial_av_moves == 3
    assert state5.prev_moves == ''
    assert state5.points == 0
    assert state5.history == []
    assert state5.egg_locs == [(1,0),(2,1)]


    # Grid with walls
    grid5 = [
    ['🧱','🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🟩', '🧱'],
    ['🧱','🥚', '🪺', '🧱'],
    ['🧱', '🧱', '🧱', '🧱']
    ]
    state5 = GameState(grid5, 4)
    assert state5.grid == grid5
    assert state5.initial_grid == [[*row] for row in grid5]
    assert state5.row == len(grid5)
    assert state5.col == len(grid5[0])
    assert state5.av_moves == 4
    assert state5.initial_av_moves == 4
    assert state5.prev_moves == ''
    assert state5.points == 0
    assert state5.history == []
    assert state5.egg_locs == [(2,1)]

    # Grid with empty nests
    grid6 = [
    ['🟩','🟩', '🟩', '🟩'],
    ['🟩', '🥚', '🪹', '🟩'],
    ['🟩','🟩', '🥚', '🟩'],
    ['🪹', '🟩', '🟩', '🟩']
    ]
    state6 = GameState(grid6, 8)
    assert state6.grid == grid6
    assert state6.initial_grid == [[*row] for row in grid6]
    assert state6.row == len(grid6)
    assert state6.col == len(grid6[0])
    assert state6.av_moves == 8
    assert state6.initial_av_moves == 8
    assert state6.prev_moves == ''
    assert state6.points == 0
    assert state6.history == []
    assert state6.egg_locs == [(1,1),(2,2)]

    # Grid with frying pans
    grid5 = [
    ['🟩','🟩', '🟩', '🟩'],
    ['🍳', '🟩', '🟩', '🥚'],
    ['🟩','🥚', '🪺', '🟩'],
    ['🟩', '🟩', '🟩', '🟩']
    ]
    state5 = GameState(grid5, 3)
    assert state5.grid == grid5
    assert state5.initial_grid == [[*row] for row in grid5]
    assert state5.row == len(grid5)
    assert state5.col == len(grid5[0])
    assert state5.av_moves == 3
    assert state5.initial_av_moves == 3
    assert state5.prev_moves == ''
    assert state5.points == 0
    assert state5.history == []
    assert state5.egg_locs == [(1,3),(2,1)]


def test_GameState_apply_moves():
    # With moves/nest interaction/wall interaction/1 move
    grid1 = [
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱'],
    ['🧱','🪹','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱','🟩','🧱','🟩','🧱'],
    ['🧱','🟩','🟩','🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱','🟩','🟩','🥚','🟩','🧱'],
    ['🧱','🟩','🟩','🧱','🟩','🟩','🥚','🟩','🟩','🪹','🟩','🟩','🟩','🟩','🟩','🧱','🧱'],
    ['🧱','🍳','🧱','🟩','🟩','🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🥚','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🪹','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🍳','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🥚','🟩','🟩','🟩','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🧱','🧱','🧱','🟩','🟩','🍳','🧱','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🪹','🟩','🟩','🟩','🍳','🟩','🍳','🟩','🟩','🧱','🟩','🟩','🧱'],
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱'],
]
    state1 = GameState(grid1, 5)
    state1.apply_moves([Move.RIGHT])
    assert state1.grid[2][14] == '🟩'
    assert state1.grid[2][15] == '🥚'
    assert state1.grid[3][6] == '🟩'
    assert state1.grid[3][9] == '🪺'
    assert state1.grid[5][12] == '🟩'
    assert state1.grid[5][15] == '🥚'
    assert state1.grid[7][9] == '🟩'
    assert state1.grid[7][15] == '🥚'
    assert state1.points == 15
    assert len(state1.history) == 1


    # One move
    grid2 = [
    ['🟩','🟩', '🟩', '🟩'],
    ['🍳', '🟩', '🟩', '🥚'],
    ['🧱','🥚', '🟩', '🟩'],
    ['🟩', '🟩', '🟩', '🟩']
    ]
    state2 = GameState(grid2, 1)
    state2.apply_moves([Move.LEFT])
    assert state2.grid[1][3] == '🟩'
    assert state2.grid[1][0] == '🍳'
    assert state2.grid[2][1] == '🥚'
    assert state2.points == -5
    assert len(state1.history) == 1

def test_GameState_go():
    # Wall interaction
    grid1 = [
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱'],
    ['🧱','🪹','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱','🟩','🧱','🟩','🧱'],
    ['🧱','🟩','🟩','🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱','🟩','🟩','🥚','🟩','🧱'],
    ['🧱','🟩','🟩','🧱','🟩','🟩','🥚','🟩','🟩','🪹','🟩','🟩','🟩','🟩','🟩','🧱','🧱'],
    ['🧱','🍳','🧱','🟩','🟩','🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🥚','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🪹','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🍳','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🥚','🟩','🟩','🟩','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🟩','🟩','🧱','🧱','🧱','🟩','🟩','🍳','🧱','🟩','🟩','🟩','🧱'],
    ['🧱','🟩','🟩','🟩','🪹','🟩','🟩','🟩','🍳','🟩','🍳','🟩','🟩','🧱','🟩','🟩','🧱'],
    ['🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱','🧱'],
]
    state1 = GameState(grid1, 5)
    state1._go(Move.LEFT)
    assert state1.grid[2][14] == '🟩'
    assert state1.grid[2][12] == '🥚'
    assert state1.grid[3][6] == '🟩'
    assert state1.grid[3][4] == '🥚'
    assert state1.grid[5][12] == '🟩'
    assert state1.grid[5][1] == '🥚'
    assert state1.grid[7][9] == '🟩'
    assert state1.grid[7][1] == '🥚'
    assert state1.points == 0
    assert state1.av_moves == 4
    assert len(state1.history) == 0

    # Pan interacion/nest interaction/egg interaction
    grid2 = [
    ['🥚','🟩', '🟩', '🟩'],
    ['🍳','🟩', '🟩', '🥚'],
    ['🥚','🟩', '🟩', '🥚'],
    ['🪹','🟩', '🥚', '🟩']
    ]
    state2 = GameState(grid2, 1)
    state2._go(Move.BACKWARD)
    assert state2.grid[1][3] == '🟩'
    assert state2.grid[1][0] == '🍳'
    assert state2.grid[2][3] == '🥚'
    assert state2.grid[3][0] == '🪺'
    assert state2.grid[3][2] == '🥚'
    assert state2.grid[3][3] == '🥚'
    assert state2.points == 6
    assert state2.av_moves == 0
    assert len(state1.history) == 0

def test_GameState_target_cell_processor():
    # Wall interaction/egg interaction/pan interaction/nest/interaction/movement
    grid1 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🍳', '🥚', '🟩', '🥚', '🧱'],
    ['🧱', '🥚', '🟩', '🪹', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🥚', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]
    state1 = GameState(grid1, 5)
    assert state1._target_cell_processor(1, 3, 1, 2, grid1) == {"moved": True}
    assert state1.points == -5
    assert len(state1.history) == 0
    assert state1._target_cell_processor(3, 4, 3, 3, grid1) == {"moved": True}
    assert state1.av_moves == 5
    assert state1.points == 10
    assert state1._target_cell_processor(2, 1, 2, 0, grid1) == {"moved": False, "loc": (1, 2)}
    assert state1._target_cell_processor(2, 2, 2, 1, grid1) == {"moved": False, "loc": (2, 2)}
    assert state1._target_cell_processor(4, 2, 4, 1, grid1) == {"moved": True, "loc": (1, 4)}

def test_restart():
    #Restart after one move
    grid1 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🍳', '🥚', '🟩', '🥚', '🧱'],
    ['🧱', '🥚', '🟩', '🪹', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🥚', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]
    state1 = GameState(grid1, 5)
    state1.apply_moves([Move.LEFT])
    state1.restart()
    assert state1.grid == grid1

    #Restart after one moves    
    state1.apply_moves([Move.FORWARD, Move.LEFT, Move.BACKWARD])
    state1.restart()
    assert state1.grid == grid1

def test_undo():
    #Undo after one move
    grid1 = [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🍳', '🥚', '🟩', '🥚', '🧱'],
    ['🧱', '🥚', '🟩', '🪹', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🥚', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]
    state1 = GameState(grid1, 5)
    state1.apply_moves([Move.LEFT])
    state1.undo()
    assert state1.grid == grid1

    state1.apply_moves([Move.FORWARD])
    state1.apply_moves([Move.LEFT])
    state1.apply_moves([Move.BACKWARD])
    state1.apply_moves([Move.BACKWARD])
    state1.undo()
    assert state1.grid == [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🟩', '🟩', '🟩', '🧱'],
    ['🧱', '🍳', '🟩', '🟩', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🪺', '🟩', '🧱'],
    ['🧱', '🟩', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]
    state1.undo()
    assert state1.grid == [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🥚', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🍳', '🟩', '🟩', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🪺', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🟩', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]
    state1.undo()
    assert state1.grid == [
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱'],
    ['🧱', '🟩', '🥚', '🟩', '🥚', '🧱'],
    ['🧱', '🍳', '🥚', '🟩', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🪺', '🟩', '🧱'],
    ['🧱', '🟩', '🟩', '🟩', '🟩', '🧱'],
    ['🧱', '🧱', '🧱', '🧱', '🧱', '🧱']
    ]




