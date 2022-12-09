from logic.director import Director
import tkinter as tk
from tkinter import ttk
import sys


def _p1(): 
# Function to make sure the mouse and WASD keys can be used
    _begin(Director('mouse'))

def _p2(): 
# Function to make sure ASL can be used
    _begin(Director('asl'))

def _p3():
    sys.exit()

def _begin(start): 
# Function to take the info from either _p1 or _p2 and start the actual program
    root.destroy()
    start.run()


if __name__ == '__main__': # Start here
    x = 1
    root = tk.Tk()   # Setting up the GUI
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Selection')

    # Button to choose mouse movement and WASD keys
    p1_button = ttk.Button(
        root,
        text='Mouse Movement and WASD',
        command=_p1
    )

    p1_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # Button to choose to sign letters using ASL
    p2_button = ttk.Button(
        root,
        text='Sign Letters',
        command=_p2
    )

    p2_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # Button to end the program
    p3_button = ttk.Button(
        root,
        text='Quit',
        command=_p3
    )

    p3_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop() # Open the GUI window and wait for input