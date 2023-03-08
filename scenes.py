import tkinter as tk
import json


def scene1(root, func):
    s1 = tk.Frame(root).pack()
    tk.Label(s1, text="Tklicker", font=("Lemon", 75)).pack(pady=(75, 25))
    tk.Label(s1, text="The best clicker\nfor your tk's", font=("Lemon", 20)).pack(pady=(0, 25))
    tk.Button(s1, text="Play", width=10, font=("Arial", 20), command=func, bg="beige").pack()


def scene2(root):
    if json.load(open("save_1_data.json")) == {}:
        save1_ = "New Game"
        save1 = False
    else:
        save1_ = "Load Game"
        save1 = True
    if json.load(open("save_2_data.json")) == {}:
        save2_ = "New Game"
        save2 = False
    else:
        save2_ = "Load Game"
        save2 = True
    if json.load(open("save_3_data.json")) == {}:
        save3_ = "New Game"
        save3 = False
    else:
        save3_ = "Load Game"
        save3 = True
    s2 = tk.Frame(root).pack()
    tk.Button(s2, text=save1_).pack()
    tk.Button(s2, text=save2_).pack()
    tk.Button(s2, text=save3_).pack()