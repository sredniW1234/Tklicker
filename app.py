# Imports
import json
import scenes
import tkinter as tk
from tkinter import font

# variables
state = 0  # State of the app: 1 = main menu, 2 = main app, 3 = minimized app


# Functions
# Deletes all widgets in root window
def delete_all_widgets():
    # Iterate over the widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()


# Updates the root window to new scene:
def update_scene():
    global state
    state += 1
    if state == 1:
        delete_all_widgets()
        scenes.scene1(root, update_scene)
    if state == 2:
        delete_all_widgets()
        scenes.scene2(root)

# Initialize Window
root = tk.Tk()
root.state("zoomed")

# Logic
update_scene()




# Run the app
root.mainloop()
