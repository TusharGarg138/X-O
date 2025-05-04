import tkinter as tk
from tkinter import messagebox

# Initial setup
root = tk.Tk()
root.title("Tic Tac Toe")

# Global variables
player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for winner or draw
def check_winner():
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

