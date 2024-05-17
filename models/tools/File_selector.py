# [File_selector.py]

import os
import tkinter as tk
from tkinter import filedialog


def print_debug(message):
    print("[Minizinc.py]: {}".format(str(message)))


class File_selector:
    @staticmethod
    def select(initial_folder=None):
        if initial_folder is None:
            initial_folder = os.getcwd()
        else:
            initial_folder = os.path.abspath(initial_folder)

        root = tk.Tk()
        root.withdraw()

        archivo = filedialog.askopenfilename(initialdir=initial_folder)

        root.destroy()

        return archivo
