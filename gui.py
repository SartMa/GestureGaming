import tkinter as tk
from tkinter import ttk, messagebox
import subprocess, os
import time
# env = 'eval "$(/home/$USER/anaconda3/bin/conda shell.bash hook)"'

def destroy(window):
    window.destroy()

style = {"font": ("Helvetica", 18), "bg": "#f0f0f0", "fg": "#333", "borderwidth": 2, "relief": "solid"}

def show_controls():
    # Create a new window for the controls
    control_window = tk.Toplevel(window)
    control_window.title("Controls")
    
    # Create a Text widget to display the controls
    controls_text = """
    Controls:
    - Lane Game: Show 'fist' to attack, 'two' to move up, 'five' to move down.
    - Flappy Bird: Show 'two' to move up.
    """
    button_control = tk.Button(control_window, **style, text="close", command=lambda: destroy(control_window), pady=10)
    controls_label = tk.Label(control_window, text=controls_text, justify="left", font=("Helvetica", 20))
    controls_label.pack(padx=10, pady=10)
    button_control.pack()

style = {"font": ("Helvetica", 18), "bg": "#f0f0f0", "fg": "#333", "borderwidth": 2, "relief": "solid"}


tuts = 'python3 Tutorial.py'
tuts_process = subprocess.Popen(tuts, shell=True, stdout=subprocess.DEVNULL)


def lane_game():
    time.sleep(5)
    os.chdir('./Game')
    main = 'python3 main.py'
    lane_process = subprocess.Popen(main, shell=True, stdout=subprocess.DEVNULL)
    destroy(window)


def flappy_bird():
    os.chdir('./flappy')
    main = 'python3 flappy.py'
    subprocess.Popen(main, shell=True, stdout=subprocess.DEVNULL)
    destroy(window)

window = tk.Tk()

# Set the title of the window
window.title("Serpents: Gaming Gaming")

# Set the size of the window
window.geometry("1000x800")

greet_text = """
Welcome to Gesture Gaming:
Unleash your inner gamer and play games using hand gesture detection!
"""

instructions_text = """
Instructions:
- Press Lane Game : Medium
- Press Flappy Bird : Hard
- For controls, click 'Controls' button

*After you finish playing press 'q' to exit object detection window*

"""

select_game = '''Select a game:
'''
# Create a label widget
label = tk.Label(window, text=greet_text+instructions_text+select_game, font=("Helvetica", 20), pady=10)

# Pack the label widget into the window
label.pack()

button1 = tk.Button(window, text="Lane Game", **style, command=lane_game, width=20, pady=10)
button2 = tk.Button(window, text="Flappy Bird", **style, command=flappy_bird, width=20, pady=10)
button3 = tk.Button(window, text="Controls", **style, command=show_controls, width=20, pady=10)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
# Run the Tkinter event loop
window.mainloop()