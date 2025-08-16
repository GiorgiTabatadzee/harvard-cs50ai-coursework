"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    if terminal(board):
        return None
    x_count = sum(cell == X for row in board for cell in row)
    o_count = sum(cell == O for row in board for cell in row)

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return  set()
    return {(i,j)
            for i in range(3)
            for j in range(3)
            if board[i][j] is EMPTY
            }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise ValueError("Action cannot be None. ")
    i,j = action
    if i not in range(3) or j not in range(3):
        raise IndexError("Action out of bounds. ")
    if board[i][j] is not EMPTY:
        raise  ValueError("Invalid action: cell is already occupied. ")
    if terminal(board):
        raise ValueError("Invalid action: game already over.")

    new_board = deepcopy(board)
    p = player(board)
    new_board[i][j]=p
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    #Checking winner in rows nd columns
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i],board[1][i],board[2][i]])
    lines.append([board[0][0],board[1][1],board[2][2]])
    lines.append([board[0][2],board[1][1],board[2][0]])
    for line in lines:
        if line[0] is not None and line.count(line[0]) == 3:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current = player(board)

    def max_value (b,alpha ,beta):
        if terminal(b):
            return utility(b),None
        v=-math.inf
        best_move=None
        for act in sorted(actions(b)):
            val,_=min_value(result(b,act),alpha,beta)
            if val > v:
                v = val
                best_move = act
                alpha = max(alpha,v)

            if v>=beta:
                break
        return v,best_move

    def min_value(b,alpha,beta):
        if terminal(b):
            return utility(b),None
        v=math.inf
        best_move=None
        for act in sorted(actions(b)):
            val,_=max_value(result(b,act),alpha,beta)
            if val<v:
                v=val
                best_move=act
                beta=min(beta,v)
            if v<=alpha:
                break
        return v,best_move

    if current == X:
        _,move = max_value(board,-math.inf,math.inf)
    else:
        _,move = min_value(board,-math.inf,math.inf)
    return move

