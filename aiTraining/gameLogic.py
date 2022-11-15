#Main game logic file for Yinsh

class Board:
    
    def __init__(self):
        #Board number identifiers:
            #0 = invalid space
            #1 = empty space
            #2 = player 1 ring
            #3 = player 1 marker
            #4 = player 2 ring
            #5 = player 2 marker
        self.boarditems = {'invalid': '⬛', 'empty': '🟡', 'redRing': '⭕', 'redMarker': '🔴', 'whiteRing': '🛟', 'whiteMarker': '⚪'} #store some emojis for the board, not really useful for final program, but makes debugging 10x easier than working in numbers
        self.board = [[1 for i in range(11)] for i in range (19)]
        for i in range(19):
            for j in range(11):
                if not((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)): #Valid spaces are only those on even-even or odd-odd coordinates
                    self.board[i][j] = 0
        #Now remove edge case invalid spaces
        #this is a disgusting solution but doing it properly would probably take far longer than just writing it out manually
        self.edgeCases = [[0,0],[0,1],[0,2],[0,3],[0,5],[0,7],[0,8],[0,9],[0,10],[1,0],[1,1],[1,2],[1,8],[1,9],[1,10],[2,0],[2,1],[2,9],[2,10],[3,0],[3,10],[4,0],[4,10],[14,0],[14,1],[14,9],[14,10],[16,0],[16,1],[16,9],[16,10],[17,0],[17,1],[17,2],[17,8],[17,9],[17,10],[18,0],[18,1],[18,2],[18,3],[18,5],[18,7],[18,8],[18,9],[18,10]]
        for i in self.edgeCases:
            self.board[i[0]][i[1]] = 0
            
            
    def displayBoard(self):
        #Display the board
        for i in range(11):
            print(i, end = " ")
        print()
        print("-"*22)
        for i in range(19):
            for j in range(11):
                block = self.board[i][j]
                if block == 1:
                    block = self.boarditems['empty']
                elif block == 2:
                    block = self.boarditems['redRing']
                elif block == 3:
                    block = self.boarditems['redMarker']
                elif block == 4:
                    block = self.boarditems['whiteRing']
                elif block == 5:
                    block = self.boarditems['whiteMakrer']
                elif block == 0:
                    block = self.boarditems['invalid']
                print(block, end = " ")
            print('|', i)
            
    def placeRing(self, player, x, y):
        if self.board[x][y] == 1:
            if player == 1:
                self.board[x][y] = 2
            elif player == 2:
                self.board[x][y] = 4
            else:
                print("Invalid player number")
        else:
            print("Invalid placement")
        
board = Board()
