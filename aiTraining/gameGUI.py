#Will create a GUI for the game to make to easier to visualize how good my AI is

import tkinter as tk

class Game:
    
    def __init__(self, window):
        self.window = window
        self.window.title('YINSH')
        self.xSpacing = 50
        self.ySpacing = 50
        
        
    def drawNumbers(self):
        for i in range(0, 11):
            self.number = tk.Label(self.window, text = i)
            self.number.place(x = self.xSpacing*i + 50, y = 25)
        for i in range(0, 19):
            self.number = tk.Label(self.window, text = i)
            self.number.place(x = 25, y = self.ySpacing*i + 50)
    
    def drawBoard(self, board):
        self.clearBoard()
        self.drawNumbers()
        self.board = board
        for i in range(0, 19):
            for j in range(0, 11):
                if self.board[i][j] == 1:
                    self.dot = tk.Canvas(self.window, width = 10, height = 10, bg = 'black')
                    self.dot.place(x = self.xSpacing*j + 50, y = self.ySpacing*i + 50)
        for i in range(0, 19):
            for j in range(0, 11):
                self.block = self.board[i][j]
                if self.block == 0 or self.block == 1:
                    continue
                elif self.block == 2:
                    print('red ring')
                    self.ring = tk.Canvas(self.window, width = 50, height = 50)
                    self.ring.create_oval(10, 10, 50, 50, width = 5, outline = 'red')
                    self.ring.place(x = self.xSpacing*j + 28, y = self.ySpacing*i + 28)
                elif self.block == 4:
                    print('red ')
                    self.ring = tk.Canvas(self.window, width = 50, height = 50)
                    self.ring.create_oval(10, 10, 50, 50, width = 5, outline = 'blue')
                    self.ring.place(x = self.xSpacing*j + 28, y = self.ySpacing*i + 28)
                elif self.block == 3:
                    self.marker = tk.Canvas(self.window, width = 50, height = 50)
                    self.marker.create_oval(10, 10, 50, 50, fill = 'red', outline = 'red')
                    self.marker.place(x = self.xSpacing*j + 28, y = self.ySpacing*i + 28)
                elif self.block == 5:
                    self.marker = tk.Canvas(self.window, width = 50, height = 50)
                    self.marker.create_oval(10, 10, 50, 50, fill = 'blue', outline= 'blue')
                    self.marker.place(x = self.xSpacing*j + 28, y = self.ySpacing*i + 28)
    
    def clearBoard(self):
        for item in self.window.winfo_children():
            item.destroy()
            
    def create_circle(self, x, y, r, canvasName): 
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)

                    
                    
    
            
board = [[1 for i in range(19)] for j in range(11)]


if __name__ == '__main__':
    #testing code to only run if this file is run directly
    window = tk.Tk()
    window.geometry('600x1000')
    game = Game(window)
    game.drawNumbers()
    game.drawBoard(board)
    window.mainloop()
