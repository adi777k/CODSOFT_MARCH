import tkinter as tk
from tkinter import messagebox
import math

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]  # Represents the 3x3 board
        self.current_winner = None
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Helvetica', 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(button)

    def make_move(self, row, col):
        if self.buttons[row*3 + col]["text"] == '' and not self.current_winner:
            self.buttons[row*3 + col]["text"] = 'X'
            self.board[row*3 + col] = 'X'
            if self.winner('X'):
                self.current_winner = 'X'
                messagebox.showinfo("Winner", "You win!")
                self.reset_board()
                return
            if self.empty_squares():
                self.ai_move()
                if self.winner('O'):
                    self.current_winner = 'O'
                    messagebox.showinfo("Winner", "AI wins!")
                    self.reset_board()
                    return
            else:
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
                return

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.buttons[best_move]["text"] = 'O'
        self.board[best_move] = 'O'

    def minimax(self, board, depth, is_maximizing):
        if self.winner('O'):
            return 1
        elif self.winner('X'):
            return -1
        elif self.empty_squares() == 0:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def winner(self, player):
        for i in range(0, 9, 3):
            if all([self.board[i+j] == player for j in range(3)]):  # Check rows
                return True
        for i in range(3):
            if all([self.board[i+j*3] == player for j in range(3)]):  # Check columns
                return True
        if self.board[0] == player and self.board[4] == player and self.board[8] == player:  # Check diagonal
            return True
        if self.board[2] == player and self.board[4] == player and self.board[6] == player:  # Check diagonal
            return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def reset_board(self):
        for button in self.buttons:
            button["text"] = ''
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


if __name__ == "__main__":
    root = tk.Tk()
    ttt = TicTacToeGUI(root)
    root.mainloop()
