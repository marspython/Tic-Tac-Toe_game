import tkinter as tk
from tkinter import messagebox

def display_message(message):
    messagebox.showinfo("Information", message)

message = "Ok! Thank you for playing!"

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        # Create buttons for the game grid
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Helvetica", 24), width=6, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.display_winner()
            elif self.check_draw():
                self.display_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw (all cells are filled)
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def display_winner(self):
        winner = self.current_player
        result = messagebox.askquestion("Game Over", f"Player {winner} wins! Do you want to play again?")
        if result == "yes":
            self.reset_game()
        else:
            display_message(message)
            self.window.close()

    def display_draw(self):
        result = messagebox.askquestion("Game Over", "It's a draw! Want to play again?")
        if result == "yes":
            self.reset_game()
        else:
            display_message(message)
            self.window.close()



    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
