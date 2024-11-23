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

def main():
    print("RUNNING MAIN")
    print(terminal(
        [
            [O, X, X],
            [X, EMPTY, EMPTY],
            [O, X, O]
        ]
    ))
    
    #raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nextplayer = player(board)
    newboard = copy.deepcopy(board)
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
            print("row win detected")
            return rows[0]
        # collect columns
        for cell in rows:
            cases.append(cell)
    
    for i in range(0, 2):
        # check columns
        if cases[i] == cases[i + 3] == cases[i + 6] and cases[i] != None:
            print("column win detected")
            return cases[0]

    # check diagonals
    if cases[0] == cases[4] == cases[8] and cases[0] != None:
            print("diag 048 win detected")
            return cases[0]

    if cases[2] == cases[4] == cases[6] and cases[0] != None:
            print("diag 246 win detected")
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
    raise NotImplementedError

if __name__ == "__main__":
    main()