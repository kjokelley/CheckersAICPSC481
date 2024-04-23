from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)
#added time delay variable to set time delay
timedelay = 0
#added alpha/beta values for A/B pruning, also added 'maxer' to keep track of which color is the root of minimax tree
def minimax(position, depth, max_player, maxer, game, alpha, beta):
    #print(alpha)
    #Added this ifelse to determine which player is max/min
    if(maxer == WHITE):
        miner = RED
    else:
        miner = WHITE
    #after this initial 
    #print(maxer)
    #print(miner)

    if depth == 0 or position.winner() != None:
        #if(miner == RED):
            #return position.evaluate(miner), position
        #else:
        #if max_player:
            return position.evaluate(maxer), position
        #else:
            return position.evaluate(miner), position
    
    #changed second parameter in get_all_moves to max/min_player so either side can be AI
    if max_player:
        #print('maxing')    
        maxEval = float('-inf')
        best_move = None
        #moves = get_all_moves(position, maxer, game)

        for move in get_all_moves(position, maxer, game):
            evaluation = minimax(move, depth-1, False, maxer, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            #print("MAXER: value ", maxEval, " alpha: ", alpha, " Beta: ", beta)
            alpha = max(alpha, maxEval)
            if(maxEval > beta):
                #print("max prune, depth: ", depth)
                if maxEval == evaluation:
                    best_move = move
                return maxEval, best_move  
                #break 
            #if beta <= alpha:
                #break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        #print('mining')
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, miner, game):
            evaluation = minimax(move, depth-1, True, maxer, game, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            #print("MINER: value ", minEval, " alpha: ", alpha, " Beta: ", beta)
            beta = min(beta, minEval)
            if(minEval < alpha):
                if(minEval == evaluation):
                    best_move = move
                #print("min prune, depth: ", depth)
                #   best_move = move
                return minEval, best_move
                #break
            #if(beta <= alpha):
                #break

            if minEval == evaluation:
                best_move = move
        return minEval, best_move

    """if depth == 0 or position.winner() != None:
        #if(miner == RED):
            #return position.evaluate(miner), position
        #else:
        return position.evaluate(maxer), position
    
    #changed second parameter in get_all_moves to max/min_player so either side can be AI
    if max_player:
        #print('maxing')
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, maxer, game):
            evaluation = minimax(move, depth-1, False, maxer, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, maxEval)
            print("MAXER: value ", maxEval, " alpha: ", alpha, " Beta: ", beta)
            print('max')
            print(maxEval)
            print('beta')
            print(beta)
            if(maxEval >= beta):
                print("max prune")
                if maxEval == evaluation:
                    best_move = move
                return maxEval, best_move  
                #break 
            #if beta <= alpha:
                #break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        #print('mining')
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, miner, game):
            evaluation = minimax(move, depth-1, True, maxer, game, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, minEval)
            print("MINER: value ", minEval, " alpha: ", alpha, " Beta: ", beta)
            print('min')
            print(minEval)
            print('beta')
            print(beta)
            if(minEval <= alpha):
                print("min prune")
                if minEval == evaluation:
                    best_move = move
                return minEval, best_move
                #break
            #if(beta <= alpha):
                #break
            if minEval == evaluation:
                best_move = move
        return minEval, best_move"""


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    #Reverse the order for RED to ensure that both colored pieces are being evaluated in the same order to ensure equality of play
    if(color == RED):
        moves.reverse()
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(0)

#added time delay function to change timedelay
def set_time_delay(time):
    timedelay = time


