# Python-Checkers-AI
A checkers AI using the minimax algorithm.

Original checkers and minimax algorithm pulled from Techwithtim

The game is run inside a while loop of the main.py file
The minimax algorithm is in the minimax/algorithm.py file
All data related to the checkers gameplay is stored in the checkers folder.
The evaluation function is kept in the checkers/board.py file
The assets folder holds the image for the crown

This game requires the PyGame library in order to run. After pulling the code, the easiest way to run this program is by loading it into an IDE such as VScode.

At current, the game runs to players with depths of 2 against each other. Output data in the console displays who last made a move, and the associated evaluation with that move.
When a cycle is detected, the output will state that. After it is detected a number of times (at current, 10), the game will terminate, and the player with the most pieces on the board (kings counted higher) will win).
