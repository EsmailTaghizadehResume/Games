import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Initialize game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.score_X = 0
        self.score_O = 0

        # Create game board
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5,
                                   command=lambda r=i, c=j: self.make_move(r, c))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Create score label and reset button
        self.score_label = tk.Label(self.window, text="Score - X: 0   O: 0")
        self.score_label.grid(row=3, columnspan=3)
        self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, columnspan=3)

        # Create level dropdown menu
        self.levels = tk.StringVar(self.window)
        self.levels.set("Easy")
        level_dropdown = tk.OptionMenu(self.window, self.levels, "Easy", "Medium", "Hard")
        level_dropdown.grid(row=5, columnspan=3)

    def make_move(self, row, col):
        # Check if move is valid
        if self.board[row][col] == "":
            # Update board and button with player's move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check if game is over
            if self.check_win(self.current_player):
                # Show winner message and update score
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                if self.current_player == "X":
                    self.score_X += 1
                else:
                    self.score_O += 1
                self.update_score_label()
                self.reset_game()
            elif self.check_tie():
                # Show tie message and reset game
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                # Switch to next player's turn
                if self.current_player == "X":
                    self.current_player = "O"
                    self.computer_move()
                else:
                    self.current_player = "X"

    def computer_move(self):
        # Get current level
        level = self.levels.get()

        # Call appropriate computer move function based on level
        if level == "Easy":
            self.computer_random_move()
        elif level == "Medium":
            self.computer_medium_move()
        elif level == "Hard":
            self.computer_hard_move()

    def computer_random_move(self):
        # Get list of available moves
        available_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    available_moves.append((i, j))

        # Make a random move from available moves
        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)

    def computer_medium_move(self):
        # Check if computer can win in the next move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    if self.check_win("O"):
                        self.buttons[i][j].config(text="O")
                        self.current_player = "X"
                        if self.current_player == "X":
                            self.score_X += 1
                        else:
                            self.score_O += 1
                        self.update_score_label()
                        self.reset_game()
                        return
                    self.board[i][j] = ""

        # Check if player can win in the next move and block them
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "X"
                    if self.check_win("X"):
                        self.board[i][j] = "O"
                        self.buttons[i][j].config(text="O")
                        self.current_player = "X"
                        return
                    self.board[i][j] = ""

        # If no winning moves, make a random move
        self.computer_random_move()

    def computer_hard_move(self):
        # TODO: Implement hard computer move
        pass

    def check_win(self, player):
        # Check horizontal lines
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True

        # Check vertical lines
        for j in range(3):
            if self.board[0][j] == player and self.board[1][j] == player and self.board[2][j] == player:
                return True

        # Check diagonal lines
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True

        # If no winning line found, return False
        return False

    def check_tie(self):
        # Check if all board positions are filled
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        # If all positions are filled, return True for tie
        return True

    def reset_game(self):
        # Reset game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Clear board buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

    def update_score_label(self):
        # Update score label with new scores
        self.score_label.config(text=f"Score - X: {self.score_X}   O: {self.score_O}")

    def play(self):
        self.window.mainloop()

game = TicTacToe()
game.play()