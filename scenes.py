import tkinter as tk
import json


def scene1(root, func):
    s1 = tk.Frame(root).pack()
    tk.Label(s1, text="Tklicker", font=("Lemon", 75)).pack(pady=(75, 25))
    tk.Label(s1, text="The best clicker\nfor your tk's", font=("Lemon", 20)).pack(pady=(0, 25))
    tk.Button(s1, text="Play", width=10, font=("Arial", 20), command=func, bg="beige").pack()


def scene2(root, func):
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
    tk.Button(s2, text=save1_, font=("Arial", 30), width=10, command=lambda: func(save1)).pack()
    tk.Button(s2, text=save2_, font=("Arial", 30), width=10, command=lambda: func(save2)).pack()
    tk.Button(s2, text=save3_, font=("Arial", 30), width=10, command=lambda: func(save3)).pack()


def scene3(root, data={}):
    s3 = tk.Frame(root).grid(row=0, column=0)
    if data == {}:
        pass
    else:
        pass

    general_info = tk.Frame(s3).grid(row=0, column=0, columnspan=1)
    shop = tk.Frame(s3).grid(row=1, column=0)
    tk_button = tk.Frame(s3).grid(row=1, column=1)
    tk.button(general_info).grid()
