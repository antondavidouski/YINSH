#Main game logic file for Yinsh

from gui import GameWindow
import tkinter as tk
class Board:
    
    def __init__(self, moveSafeMode):
        #Board number identifiers:
            #0 = invalid space
            #1 = empty space
            #--Player 1--
            #2 = red ring
            #3 = red marker
            #--Player 2--
            #4 = white ring
            #5 = white marker
        self.moveSafeMode = moveSafeMode #setting this to false will skip move validation, which will speed training up, as the AI will only make valid moves
        self.boarditems = {'invalid': '  ', 
                           'empty': '⬛', 
                           'redRing': '⭕', 
                           'redMarker': '🔴', 
                           'whiteRing': '🛟', 
                           'whiteMarker': '⚪'} #store some emojis for displaying the board, not really useful for final program, but makes debugging 10x easier than working in numbers
        self.board = [[1 for i in range(11)] for i in range (19)]
        for i in range(19):
            for j in range(11):
                if not((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)): #Valid spaces are only those on even-even or odd-odd coordinates
                    self.board[i][j] = 0
        #Now remove edge case invalid spaces
        #this is a horrible solution but doing it properly would take far longer than just writing it out manually
        self.edgeCases = [[0,0],[0,1],[0,2],[0,3],[0,5],[0,7],[0,8],[0,9],[0,10],[1,0],[1,1],[1,2],[1,8],[1,9],[1,10],[2,0],[2,1],[2,9],[2,10],[3,0],[3,10],[4,0],[4,10],[14,0],[14,1],[14,9],[14,10],[16,0],[16,1],[16,9],[16,10],[17,0],[17,1],[17,2],[17,8],[17,9],[17,10],[18,0],[18,1],[18,2],[18,3],[18,5],[18,7],[18,8],[18,9],[18,10]]
        for i in self.edgeCases:
            self.board[i[0]][i[1]] = 0
        window = tk.Tk()
        window.geometry('900x1000+540+0')
        window.attributes('-topmost', True)
        self.game = GameWindow(window)
        self.game.drawNumbers()
        self.game.drawBoard(self.board)
        counter = 0
        for i in range(19):
            for j in range(11):
                if self.board[i][j] == 1:
                    counter += 1
        print(counter)
        
        
    def displayBoard(self):
        #Display the board
        # for i in range(11):
        #     print(i, end = "  ")
    
        # print()
        # print("-"*33)
        # for i in range(19):
        #     for j in range(11):
        #         block = self.board[i][j]
        #         if type(block) == int:
        #             if block == 1:
        #                 block = self.boarditems['empty']
        #             elif block == 0:
        #                 block = self.boarditems['invalid']
        #         else:
        #             block = block.what()
        #             if block == 2:
        #                 block = self.boarditems['redRing']
        #             elif block == 3:
        #                 block = self.boarditems['redMarker']
        #             elif block == 4:
        #                 block = self.boarditems['whiteRing']
        #             elif block == 5:
        #                 block = self.boarditems['whiteMarker']
                
        #         print(block, end = " ")
        #     print('|', i)
        self.game.drawBoard(self.generateSimpleBoard(self.board))
        
    def placeRing(self, player, y, x):
        #x and y inputs are swapped becuasse the board is stored as 2D list with each row an element, so the first index is the y coordinate
        if self.board[x][y] == 1:
            if player == 1:
                self.board[x][y] = Ring(1, x, y)
            elif player == 2:
                self.board[x][y] = Ring(2, x, y)
            else:
                print("Invalid player number")
        else:
            print("Invalid placement")
     
    def moveRing(self, y, x, ny, nx):
        try:
            self.player = self.board[x][y].owner() #figure out which player the ring belongs to
        except AssertionError:
            print("Invalid ring")
        if self.isMoveValid(x, y, nx, ny) or not self.moveSafeMode: #check if the move is valid
            self.board[x][y], self.board[nx][ny] = 1, Ring(self.player, nx, ny) #move the ring
            self.board[x][y] = Marker(self.player) #place a marker on the old ring position
        else:
            print("Invalid move")
        self.generateSimpleBoard(self.board)
            
    def isMoveValid(self, y, x, ny, nx):
        print(f'Checking if move from {x}, {y} to {nx}, {ny} is valid')
        if ny == y:
            print("Invalid move: Cannot move horizontally")
            return False #cannot move horizontally
        #determine which direction the move is going
        if nx == x:
            if ny > y:
                direction = 'up'
                dx, dy = 0, 2
            else:
                direction = 'down'
                dx, dy = 0, -2
        elif ny > y:
            #piece is moving up
            if nx > x:
                direction = 'upright'
                dx, dy = 1, 1
            else:
                direction = 'upleft'
                dx, dy = -1, 1
        elif ny < y:
            #piece is moving down
            if nx > x:
                direction = 'downright'
                dx, dy = 1, -1
            else:
                direction = 'downleft'
                dx, dy = -1, -1
                
        if self.board[ny][nx] != 1:
            print('Invalid move: space is occupied')
            return False #cannot move to a space that is not empty
        
        #now take "steps" in the direction of the move until the new position is reached or return False if any step violates a rule
        currPos = [x, y]
        markersHaveBeenFlipped = False
        flippedMarkers = []
        reachedNewPos = False
        try:
            while not reachedNewPos:
                currPos[0] += dx
                currPos[1] += dy
                if currPos[0] == nx and currPos[1] == ny:
                    break
                newBlock = self.board[currPos[1]][currPos[0]].what() if type(self.board[currPos[0]][currPos[1]]) != int else self.board[currPos[1]][currPos[0]] #get the type of the block at the current position 
                if newBlock == 0:
                    print('Invalid move: cannot move through invalid spaces')
                    return False
                if newBlock == 1 and markersHaveBeenFlipped:
                    #ring must stop on next available space if it has flipped markers
                    if currPos[0] == ny and currPos[1] == nx:
                        reachedNewPos = True
                    else:
                        print('Invalid move: ring must stop on next available space if it has flipped markers')
                        return False
                if newBlock == 2 or newBlock == 4:
                    #if the next block is a ring, the move is invalid
                    print('Invalid move: cannot move through rings')
                    return False
                if newBlock == 3 or newBlock == 5:
                    #if the next block is a marker, flip it
                    markersHaveBeenFlipped = True
                    flippedMarkers.append(self.board[currPos[0]][currPos[1]])
        except IndexError:
            print('Invalid move: cannot move off the board')
            return False
        print(flippedMarkers)
        self.flipMarkers(flippedMarkers)
        return True
            
    def flipMarkers(self, markers):
        #flip the markers
        for marker in markers:
            marker.flip()           
            
    
    def generateSimpleBoard(self, board):
        #will return a simplified board, with objects replaced by their associated number, useful for GUI and input into AI
        self.simpleBoard = [[1 for i in range(11)] for i in range (19)]
        for i in range(19):
            for j in range(11):
                if type(board[i][j]) == int:
                    self.simpleBoard[i][j] = board[i][j]
                else:
                    self.simpleBoard[i][j] = board[i][j].what()
        return self.simpleBoard
class Ring:
    
    def __init__(self, player, x, y):
        self.colour = player
        self.x = x
        self.y = y
    
    def owner(self):
        return self.colour
    
    def what(self):
        #returns what the object is
        if self.colour == 1:
            return 2
        else:
            return 4
        
class Marker:
    
    def __init__(self, player):
        self.colour = player
    
    def flip(self):
        if self.colour == 1:
            self.colour = 2
        elif self.colour == 2:
            self.colour = 1
            
    def get(self):
        return self.colour
    
    def what(self):
        if self.colour == 1:
            return 3
        else:
            return 5
    
board = Board(True)
board.displayBoard()

while True:
    a = input('Place or move? ')
    if a == 'place':
        b = int(input('Player: '))
        c = int(input('x: '))
        d = int(input('y: '))
        board.placeRing(b,c,d)
    elif a == 'move':
        b = int(input('x: '))
        c = int(input('y: '))
        d = int(input('nx: '))
        e = int(input('ny: '))
        board.moveRing(b,c,d,e)
    board.displayBoard()
