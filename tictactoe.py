"""
Tic Tac Toe Player
"""

import math

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

def main():
    print("RUNNING MAIN")
    available = actions([[O, X, EMPTY],
            [X, EMPTY, X],
            [EMPTY, X, EMPTY]])
    print(available)
    #raise NotImplementedError

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
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

if __name__ == "__main__":
    main()