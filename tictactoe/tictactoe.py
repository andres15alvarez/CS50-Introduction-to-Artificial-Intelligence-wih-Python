"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math
import random

X = "X"
O = "O"
EMPTY = None
options = [X, O]

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

    countx = 0
    counto = 0
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == X:
    			countx += 1
    		elif board[i][j] == O:
    			counto += 1 
    if countx > counto:
    	return O
    elif countx == counto:
    	return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    copyboard = deepcopy(board)

    if action in actions(board):
    	copyboard[action[0]][action[1]] = player(board) 
    else:
    	raise Exception("Invalid action.")
    return copyboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
    	for o in options:
	    	# Check for rows
	    	if board[i][0] == board[i][1] == board[i][2] and board[i][0] == o:
	    		return o
	    	# Check for columns
	    	if board[0][i] == board[1][i] == board[2][i] and board[0][i] == o:
	    		return o

    # Check for diagonal
    for o in options:
	    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == o:
	    	return o
	    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == o:
	    	return o
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
    	return True
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
    	return 1
    elif winner(board) == O:
    	return -1
    else:
    	return 0

def max_value(board):
    v = -math.inf 
    if terminal(board):
    	return utility(board)
    for action in actions(board):
    	v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
    	return utility(board)
    for action in actions(board):
    	v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    move = None
    if player(board) == O:
    	bestscore = math.inf
    	for action in actions(board):
    		score = max_value(result(board, action))
    		if score < bestscore:
    			bestscore = score
    			move = action
    	return move

    else:
    	if board == initial_state():
    		i = random.randint(0,2)
    		j = random.randint(0,2)
    		return (i,j)
    	bestscore = -math.inf
    	for action in actions(board):
    		score = min_value(result(board, action))
    		if score > bestscore:
    			bestscore = score
    			move = action
    	return move