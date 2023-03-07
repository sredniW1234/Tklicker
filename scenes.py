import tkinter as tk



def scene1(root, func):
    root.config()
    s1 = tk.Frame(root).pack()
    tk.Label(s1, text="Tklicker", font=("Lemon", 75)).pack(pady=(75, 25))
    tk.Label(s1, text="The best clicker\nfor your tk's", font=("Lemon", 20)).pack(pady=(0, 25))
    tk.Button(s1, text="Play", width=10, font=("Arial", 20), command=func, bg="beige").pack()

def scene2(root):
    s2 = tk.Frame(root).pack()
    tk.Button("")