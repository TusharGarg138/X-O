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

# Check if draw
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Handle button click
def click(row, col):
    global player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        buttons[row][col]["state"] = "disabled"

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

# Reset the game
def reset_game():
    global player
    player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""
            btn["state"] = "normal"

# Create 3x3 buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('Helvetica', 32), width=5, height=2,
                                  command=lambda r=i, c=j: click(r, c))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()