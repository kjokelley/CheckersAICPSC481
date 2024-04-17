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
    start = time.time()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    #added count to track # of while functions
    count = 0
    #values to track old evaluation functions to track cycles
    red_value = 0
    white_value = 0
    while run:
        count += 1
        if count == 10:
            count = 0
            
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game, float('-inf'), float('inf'))
            #tracks count, breaks if old white value equals new value 9 moves later
            if(count == 0):
                white_value = value
            if(count == 9):
                if(white_value == value):
                    print("cycle detected in white")
                    break

            #added "if new_board == None" to check if player cannot play and therefore loses
            if new_board == None:
                print("White Wins")
                break
            game.ai_move(new_board)
        
        

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
                #Attempt to add different time delays, doesn't work currently
                """if event.key == pygame.K_0:
                    minimax.set_time_delay(0)
                if event.key == pygame.K_1:
                    minimax.set_time_delay(100)"""
            #This is what allows for the game to be played by a person, disable turn check below to allow Player vs. AI
            """if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)"""

            #checks current turn to allow AI to play for RED, disable above event check to allow AI vs. AI
            #added "if new_board == None" to check if player cannot play and therefore loses
        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 3, RED, game, float('-inf'), float('inf'))
            #tracks count, breaks if old white value equals new value 9 moves later
            if(count == 0):
                red_value = value
            if(count == 9):
                if(red_value == value):
                    print("cycle detected in red")
                    break
            if new_board == None:
                print("White Wins")
                break
            game.ai_move(new_board)

        game.update()
    
    pygame.quit()
    end = time.time()
    print(end - start)

main()