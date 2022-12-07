from logic.director import Director
import tkinter as tk
from tkinter import ttk


def _p1():
    _begin(Director('mouse'))

def _p2():
    _begin(Director('asl'))

def _begin(start):
    root.quit()
    start.run()

# root window

# import multiprocessing as mp

if __name__ == '__main__':
    # start = Director()
    root = tk.Tk()
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Selection')

    # exit button
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

    root.mainloop()
    # processes = [mp.Process(target=start.run, args=()), mp.Process(target=start.run, args=())]
    # processes.append(mp.Process(target=start.run, args=()), mp.Process(target=start.run, args=()))
    # p = mp.Process(target=start.run, args=())
    # p = mp.Process(target=start.run, args=())
    # for p in processes:
        # print('time')
        # p.start()
    # for p in processes:
        # p.join()
    # start.run()