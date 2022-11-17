#Will create a GUI for the game to make to easier to visualize how good my AI is

import tkinter as tk

class GameWindow:
    
    def __init__(self, window):
        self.window = window
        self.window.title('YINSH')
        self.xSpacing = 75
        self.ySpacing = 42
        
        
    def drawNumbers(self):
        for i in range(0, 11):
            self.number = tk.Label(self.window, text = i)
            self.number.place(x = self.xSpacing*i + 50, y = 5)
        for i in range(0, 19):
            self.number = tk.Label(self.window, text = i)
            self.number.place(x = 10, y = self.ySpacing*i + 50)
    
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
                    self.ring = tk.Canvas(self.window, width = 50, height = 50)
                    self.ring.create_oval(10, 10, 50, 50, width = 5, outline = 'red')
                    self.ring.place(x = self.xSpacing*j + 25, y = self.ySpacing*i + 25)
                elif self.block == 4:
                    self.ring = tk.Canvas(self.window, width = 50, height = 50)
                    self.ring.create_oval(10, 10, 50, 50, width = 5, outline = 'blue')
                    self.ring.place(x = self.xSpacing*j + 25, y = self.ySpacing*i + 25)
                elif self.block == 3:
                    self.marker = tk.Canvas(self.window, width = 50, height = 50)
                    self.marker.create_oval(10, 10, 50, 50, fill = 'red', outline = 'red')
                    self.marker.place(x = self.xSpacing*j + 25, y = self.ySpacing*i + 25)
                elif self.block == 5:
                    self.marker = tk.Canvas(self.window, width = 50, height = 50)
                    self.marker.create_oval(10, 10, 50, 50, fill = 'blue', outline= 'blue')
                    self.marker.place(x = self.xSpacing*j + 25, y = self.ySpacing*i + 25)
    
    def clearBoard(self):
        for item in self.window.winfo_children():
            item.destroy()
            
board = [[1 for i in range(18)] for j in range(10)]

if __name__ == '__main__':
    #testing code to only run if this file is run directly
    window = tk.Tk()
    window.geometry('1000x1000')
    game = GameWindow(window)
    game.drawBoard(board)
    window.mainloop()
