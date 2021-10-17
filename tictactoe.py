"""
Tic Tac Toe Player
"""

import math
import itertools
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
    #variable c which counts 
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #initializing an empty set
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result    

              
              


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):
        raise ValueError("Invalid action.")
    else:
        p = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i][j] = p

    return result_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking horizontally
    if board[0][0]==board[0][1]==board[0][2] !=None:
        if board[0][0]==X:
            return X
        else:
            return  O
    elif board[1][0]==board[1][1]==board[1][2] !=None:
        if board[1][0]==X:
            return X
        else:
            return  O  
    elif board[2][0]==board[2][1]==board[2][2] !=None:
        if board[2][0]==X:
            return X
        else:
            return  O    
    #checking vertically
    elif board[0][0]==board[1][0]==board[2][0] !=None:
        if board[0][0]==X:
            return X
        else:
            return  O    
    elif board[0][1]==board[1][1]==board[2][1] !=None:
        if board[0][1]==X:
            return X
        else:
            return  O  
    elif board[0][2]==board[1][2]==board[2][2] !=None:
        if board[0][2]==X:
            return X
        else:
            return  O      
    #check diagonals 
    elif board[0][0]==board[1][1]==board[2][2] !=None:
        if board[0][0]==X:
            return X
        else:
            return  O  
    elif board[0][2]==board[1][1]==board[2][0] !=None:
        if board[0][2]==X:
            return X
        else:
            return  O 
    else:
        return None                 
        
                
    
   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    #if all cells filled
    for i in board:
        for j in i:
            if j==EMPTY:
                return False
    return True                
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0     

   


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p=player(board)
    if board == [[EMPTY]*3]*3:
        return (0,0)
    
    if p==X:
        v=float("-inf")
        move=None
        for action in actions(board):
            minValueResult=minValue(result(board,action))
            if minValueResult>v:
                v=minValueResult
                move=action
        
    elif p==O:
        v=float("inf")
        move=None
        for action in actions(board):
            maxValueResult=maxValue(result(board,action))
            if maxValueResult<v:
                v=maxValueResult
                move=action
    return move  




def maxValue(board):
    if terminal(board):
        return utility(board)
    v=float("-inf")    
    for action in actions(board):
        v=max(v,minValue(result(board,action)))
    return v    
def minValue(board):
    if terminal(board):
        return utility(board)
    v=float("inf")    
    for action in actions(board):
        v=min(v,maxValue(result(board,action)))
    return v    

