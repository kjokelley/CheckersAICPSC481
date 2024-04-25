from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

#added alpha/beta values for A/B pruning, also added 'maxer' to keep track of which color is the root of minimax tree
def minimax(position, depth, is_max_player, maxer, game, alpha, beta):
    #Added this ifelse to determine which player is max/min
    if(maxer == WHITE):
        miner = RED
    else:
        miner = WHITE


    if depth == 0 or position.winner() != None:
            return position.evaluate(maxer), position
        
    
    #changed second parameter in get_all_moves to max/min_player so either side can be AI
    if is_max_player:
        maxEval = float('-inf')
        best_move = None
        
        #Used these print statements for debugging. Leaving them in for future use
        #maxval = 1
        #print(maxer, " ", maxval, " ", maxEval, " ", alpha, " ", beta)

        for move in get_all_moves(position, maxer, game):
            #maxval += 1
            evaluation = minimax(move, depth-1, False, maxer, game, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, maxEval)
            if(maxEval > beta):
                return maxEval, move  
            
            if maxEval == evaluation:
                best_move = move
            #print(maxer, " ", maxval, " ", maxEval, " ", alpha, " ", beta)

        return maxEval, best_move
    else:
        #minval = 0
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, miner, game):
            #minval += 1
            evaluation = minimax(move, depth-1, True, maxer, game, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, minEval)
            if(minEval < alpha):  
                return minEval, move
            
            if minEval == evaluation:
                best_move = move
            #print(miner, " ", minval, " ", minEval, " ", alpha, " ", beta)
        return minEval, best_move


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




