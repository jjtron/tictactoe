"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for rows in board:
        for cell in rows:
            if cell != EMPTY:
                count += 1

    if count == 0:
        return X        
    if count % 2 == 1:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i, rows in enumerate(board):
        for j, cell in enumerate(rows):
            if cell == None:
                available.add((i, j))

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nextplayer = player(board)
    newboard = copy.deepcopy(board)
    if newboard[action[0]][action[1]] != None:
        raise Exception
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception
    newboard[action[0]][action[1]] = nextplayer
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    cases = []
    for rows in board:
        # check rows
        if rows[0] == rows[1] == rows[2] and rows[0] != None:
            return rows[0]
        # collect columns
        for cell in rows:
            cases.append(cell)
    
    for i in range(0, 2):
        # check columns
        if cases[i] == cases[i + 3] == cases[i + 6] and cases[i] != None:
            return cases[i]

    # check diagonals
    if cases[0] == cases[4] == cases[8] and cases[0] != None:
            return cases[0]

    if cases[2] == cases[4] == cases[6] and cases[0] != None:
            return cases[2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_winner = winner(board)
    if is_winner == O or is_winner == X:
        return True

    for rows in board:
        for cell in rows:
            if cell == None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    is_winner = winner(board)
    if is_winner == O:
        return -1
    if is_winner == X:
        return 1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    options = []
    results = []
    best_result = None
    for action in actions(board):
        board_result = result(board, action)
        if player(board) == O:
            v = max_value(board_result)
        if player(board) == X:
            v = min_value(board_result)
        results.append(v)
        options.append([v, action])

    if player(board) == O:
        best_result = min(results)

    if player(board) == X:
        best_result = max(results)

    for i in range(0, len(options)):
        if best_result == options[i][0]:
            return options[i][1]
            

def max_value(board):
    if terminal(board) == True:
        return utility(board)

    v = -math.inf
    for action in actions(board):
        r = result(board, action)
        v = max(v, min_value(r))
    return v

def min_value(board):
    if terminal(board) == True:
        return utility(board)

    v = math.inf
    for action in actions(board):
        r = result(board, action)
        v = min(v, max_value(r))
    return v

if __name__ == "__main__":
    print(minimax(
        [
            [X, O, O],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, X]
        ]
    ))