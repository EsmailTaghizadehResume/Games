import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.score_X = 0
        self.score_O = 0
        
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda r=i, c=j: self.make_move(r, c))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
        
        self.score_label = tk.Label(self.window, text="Score - X: 0   O: 0")
        self.score_label.grid(row=3, columnspan=3)
        
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, columnspan=3)
        
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.score_X += 1
                else:
                    self.score_O += 1
                self.update_score_label()
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        
    def check_win(self, player):
        for i in range(3):
            if all(cell == player for cell in self.board[i]):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
    
    def check_tie(self):
        return all(cell != "" for row in self.board for cell in row)
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="")
        self.update_score_label()
        
    def update_score_label(self):
        self.score_label.config(text=f"Score - X: {self.score_X}   O: {self.score_O}")
        
    def start(self):
        self.window.mainloop()

game = TicTacToe()
game.start()
