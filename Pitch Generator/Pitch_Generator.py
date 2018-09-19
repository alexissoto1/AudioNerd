#Python 3.5

import numpy as np
import simpleaudio as sa
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

Range = list(range(20, 20000))

class Generator(object):

    def __init__(self,root):
        self.root = root

        root.title('Pitch Generator')
        root.resizable(False, False)
        root.configure(background = 'black')

        self.frame_header = ttk.Frame(root)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = 'Enter a digit (Root Frequency) from 20 to 20,000:').grid(row = 0, columnspan = 1)
        self.entry_number = ttk.Entry(self.frame_header, width = 20, font = ('Arial', 10))
        self.entry_number.grid(row = 1, column = 0)

        ttk.Button(self.frame_header, text = 'Use',
                   command = self.GetFreq).grid(row = 2, column = 0)

    #Create the frame_content atribute for buttons

        self.frame_content = ttk.Frame(root)
        self.frame_content.pack()

     #Specific notes buttons.

        ttk.Button(self.frame_content, text = 'A',
                   command = self.A).grid(row = 1, column = 0)

        ttk.Button(self.frame_content, text = 'A#',
                   command = self.Ash).grid(row = 1, column = 1)

        ttk.Button(self.frame_content, text = 'B',
                   command = self.B).grid(row = 1, column = 2)

        ttk.Button(self.frame_content, text = 'C',
                   command = self.C).grid(row = 2, column = 0)

        ttk.Button(self.frame_content, text = 'C#',
                   command = self.Csh).grid(row = 2, column = 1)

        ttk.Button(self.frame_content, text = 'D',
                   command = self.D).grid(row = 2, column = 2)

        ttk.Button(self.frame_content, text = 'D#',
                   command = self.Dsh).grid(row = 3, column = 0)

        ttk.Button(self.frame_content, text = 'E',
                   command = self.E).grid(row = 3, column = 1)

        ttk.Button(self.frame_content, text = 'F',
                   command = self.F).grid(row = 3, column = 2)

        ttk.Button(self.frame_content, text = 'F#',
                   command = self.Fsh).grid(row = 4, column = 0)

        ttk.Button(self.frame_content, text = 'G',
                   command = self.G).grid(row = 4, column = 1)

        ttk.Button(self.frame_content, text = 'G#',
                   command = self.Gsh).grid(row = 4, column = 2)

    def InitVars(self, frequency):
        self.A_freq = int(frequency)
        self.Ash_freq = self.A_freq * 2 ** (1 / 12)
        self.B_freq = self.A_freq * 2 ** (2 / 12)
        self.C_freq = self.A_freq * 2 ** (3 / 12)
        self.Csh_freq = self.A_freq * 2 ** (4 / 12)
        self.D_freq = self.A_freq * 2 ** (5 / 12)
        self.Dsh_freq = self.A_freq * 2 ** (6 / 12)
        self.E_freq = self.A_freq * 2 ** (7 / 12)
        self.F_freq = self.A_freq * 2 ** (8 / 12)
        self.Fsh_freq = self.A_freq * 2 ** (9 / 12)
        self.G_freq = self.A_freq * 2 ** (10 / 12)
        self.Gsh_freq = self.A_freq * 2 ** (11/12)

        # get timesteps for each sample, T is note duration in seconds
        self.sample_rate = 96000
        T = 2
        t = np.linspace(0, T, T * self.sample_rate, False)

    # generate sine wave notes
        self.A_note = np.sin(self.A_freq * t * np.pi)
        self.Ash_note = np.sin(self.Ash_freq * t * np.pi)
        self.B_note = np.sin(self.B_freq * t * np.pi)
        self.C_note = np.sin(self.C_freq * t * np.pi)
        self.Csh_note = np.sin(self.Csh_freq * t * np.pi)
        self.D_note = np.sin(self.D_freq * t * np.pi)
        self.Dsh_note = np.sin(self.Dsh_freq * t * np.pi)
        self.E_note = np.sin(self.E_freq * t * np.pi)
        self.F_note = np.sin(self.F_freq * t * np.pi)
        self.Fsh_note = np.sin(self.Fsh_freq * t * np.pi)
        self.G_note = np.sin(self.G_freq * t * np.pi)
        self.Gsh_note = np.sin(self.Gsh_freq * t * np.pi )

        #Button functions (Each one is called at specific button):

    def A(self):
        # concatenate notes
        audio = self.A_note
        # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
        # convert to 16-bit data
        audio = audio.astype(np.int16)

        # start playback
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)

        # wait for playback to finish before exiting
        play_obj.wait_done()

    def Ash(self):

        audio = self.Ash_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'A# is at: {} Hz.'.format(str(self.Ash_freq)))

    def B(self):

        audio = self.B_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'B is at: {} Hz.'.format(str(self.B_freq)))

    def C(self):

        audio = self.C_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'C is at: {} Hz.'.format(str(self.C_freq)))

    def Csh(self):

        audio = self.Csh_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'C# is at: {} Hz.'.format(str(self.Csh_freq)))

    def D(self):

        audio = self.D_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'D is at: {} Hz.'.format(str(self.D_freq)))

    def Dsh(self):

        audio = self.Dsh_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'D# is at: {} Hz.'.format(str(self.Dsh_freq)))

    def E(self):

        audio = self.E_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'E is at: {} Hz.'.format(str(self.E_freq)))

    def F(self):

        audio = self.F_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'F is at: {} Hz.'.format(str(self.F_freq)))

    def Fsh(self):

        audio = self.Fsh_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'F# is at: {} Hz.'.format(str(self.Fsh_freq)))

    def G(self):

        audio = self.G_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'G is at: {} Hz.'.format(str(self.G_freq)))

    def Gsh(self):

        audio = self.Gsh_note
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, self.sample_rate)
        play_obj.wait_done()
        messagebox.showinfo(title = 'Pitch Generator', message = 'G# is at: {} Hz.'.format(str(self.Gsh_freq)))

# Get integer from User
    def GetFreq(self):

        if self.entry_number.get() == '':
            messagebox.showinfo(title = 'Pitch Generator', message = 'Please enter a frequency value.')
        elif self.entry_number.get().isalpha():
            messagebox.showinfo(title = 'Pitch Generator', message = 'Please enter a numeric value.')
            self.entry_number.delete(0, 'end')
        else:
            if self.entry_number.get().isdigit():
                print('Frequency: {} Hz'.format(self.entry_number.get()))
                messagebox.showinfo(title = 'Pitch Generator', message = 'Using: {} Hz.'.format(self.entry_number.get()))
                self.InitVars(self.entry_number.get())
            
def main():

    root = tk.Tk()
    app = Generator(root)
    root.mainloop()

if __name__ == "__main__": main()
