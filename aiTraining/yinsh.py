#Main game file for Yinsh

class Board:
    
    def __init__(self, dimensions):
        #Make an empty board with the inputted dimensions (board is NOT dxd, as d describes the side length of the board hexagon)
        #Board number identifiers:
            #0 = invalid space
            #1 = empty space
            #2 = player 1 ring
            #3 = player 1 marker
            #4 = player 2 ring
            #5 = player 2 marker
        self.board = [1 for i in range (((dimensions * 2) + 1) ** 2)]
    
    def displayBoard(self):
        #Display the board
        for i in range (len(self.board)):
            if i % 5 == 0:
                print()
            print(self.board[i], end = " ")
        
board = Board(5)
board.displayBoard()