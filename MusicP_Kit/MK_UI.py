#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:15:26 2018

@author: alexissoto
"""

import Librosa1 as lib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Generator(object):

    def __init__(self,root):
        self.root = root

        root.title('Music Production Kit')
        root.resizable(False, False)
# =============================================================================
#         root.configure(background = 'black')
# =============================================================================

        self.frame_header = ttk.Frame(root)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = 'Select the Path of your song:').grid(row = 0, columnspan = 1)
        self.entry_number = ttk.Entry(self.frame_header, width = 20, font = ('Arial', 10))

    #Create the frame_content atribute for buttons

        self.frame_content = ttk.Frame(root)
        self.frame_content.pack()

     #Specific notes buttons.

        ttk.Button(self.frame_content, text = 'Tempo',
                   command = lib.Tempo).grid(row = 1, column = 0)

        ttk.Button(self.frame_content, text = 'ChangeTempo',
                   command = lib.TempoChange).grid(row = 1, column = 1)

        ttk.Button(self.frame_content, text = 'Step',
                   command = lib.Steps).grid(row = 1, column = 2)

        ttk.Button(self.frame_content, text = 'Harmonic',
                   command = lib.Harmonics).grid(row = 2, column = 0)

        ttk.Button(self.frame_content, text = 'Percussive',
                   command = lib.Percussive).grid(row = 2, column = 1)

        ttk.Button(self.frame_content, text = 'Both',
                   command = lib.Both).grid(row = 2, column = 2)

        ttk.Button(self.frame_content, text = 'Quit',
                   command = self._quit).grid(row = 3, column = 1)
  
    def _quit(self):
        self.root.quit()
        self.root.destroy()
        exit()
        

def main():

    root = tk.Tk()
    app = Generator(root)
    root.mainloop()

if __name__ == "__main__": main()

