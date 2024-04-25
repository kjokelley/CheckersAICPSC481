# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
import time
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    #Timer so we can check how long games run for
    start = time.time()
    clock = pygame.time.Clock()

    run = True
    game = Game(WIN)
    
    while run:
        
       
            
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, True, WHITE, game, float('-inf'), float('inf'))

            #added "if new_board == None" to check if player cannot play and therefore loses
            if new_board == None:
                print("Red Wins")
                break
            game.ai_move(new_board)
            print('white made a move ', value)
            

        
        if game.winner() != None:
            print(game.winner())
            run = False

        #took out manual control and added another turn check for if its currently RED players turn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #added event to quit on hitting space bar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
            #This is what allows for the game to be played by a person
            """if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)"""

            #checks current turn to allow AI to play for RED, disable above event check to allow AI vs. AI
        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 3, True, RED, game, float('-inf'), float('inf'))

            #added "if new_board == None" to check if player cannot play and therefore loses
            if new_board == None:
                print("White Wins")
                break
            game.ai_move(new_board)
            print('red made a move ', value)
            


        

        game.update()
        
    
    pygame.quit()
    end = time.time()
    print(end - start)

main()