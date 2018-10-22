#Python 3.5

import numpy as np
from tkinter import *
from pygame import sndarray, mixer

tempo_1 = 10000 
tempo_2 = 1000 

#The lower the note, the more time the system will take processing the np arrays.

infinite = -1

class Drawing:
    
    def __init__(self, master):
        self.prev = None # previous location 
        self.sound = None # sound array to play
        self.sound_on = False 
    
        master.attributes('-fullscreen', True)
        
        self.canvas = Canvas(master, background = 'white')
        self.canvas.pack(fill = BOTH, expand = True)
        self.canvas.create_text(master.winfo_screenwidth()//2, master.winfo_screenheight()//2, anchor = 's',
                                text = "Music on Canvas", font = ('Helvetica', 40, 'bold'), fill = 'black')
        
        master.bind('<Motion>', self.mouse_move)
        master.bind('<ButtonPress>', self.mouse_down)
        master.bind('<ButtonRelease>', self.mouse_up)
        master.bind('<Escape>', lambda e: master.destroy())
            
        mixer.init(96000, -16, 1)
                
    def mouse_move(self, event):        
        if self.sound_on:
            new_sound = sndarray.make_sound(self.sine_wave(self.calc_freq(event.x)))
            new_sound.play(infinite) #Infinte looping
            self.sound.stop()
            self.sound = new_sound
     
        Red = int(255 * event.x / self.canvas.winfo_width() * (self.canvas.winfo_height() - (event.y + 1)) / self.canvas.winfo_height()) 
        Blues = int(255 * event.x / self.canvas.winfo_width() * (event.y + 1) / self.canvas.winfo_height())   

        if self.prev: # draw line if mouse is down
            self.canvas.create_line(self.prev.x, self.prev.y, event.x, event.y, width = 10, fill = '#{:02x}88{:02x}'.format(Red, Blues))
            self.prev = event
        
    def mouse_down(self, event):
        self.canvas.delete('all')
        self.prev = event       
        self.sound_on = True
        self.sound = sndarray.make_sound(self.sine_wave(self.calc_freq(event.x)))
        self.sound.play(tempo_2) #Works as csound event biding
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height()//7, anchor = 's',
                            text = "Drawing...", font = ('Helvetica', 38, 'bold'), fill = 'black')
        
    def mouse_up(self, event):        
        self.prev = None
        self.canvas.delete('all')
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height()//7, anchor = 's',
                                text = "Music on Canvas", font = ('Helvetica', 38, 'bold'), fill = 'black')
        self.sound_on = False
        self.sound.stop()
        
    def calc_freq(self, y_pos): # calculate key frequency at y_pos     
        pkey = 88 * (self.canvas.winfo_height() - (y_pos + 1)) / self.canvas.winfo_height() + 1
        return 440 * 2**((pkey - 49)/12) # 440Hz is key #49 on a piano
    
    def calc_volume(self, x_pos):
        return x_pos / self.canvas.winfo_width()

    def sine_wave(self, frequency = 440.0, samplerate = 96000):
        samples = samplerate / frequency
        return (32767 * np.tan(np.arange(int(samples)) * (2 * np.pi) / samples)).astype(np.int16)
# =============================================================================
#        np.round, np.sin, np.around, np.sinh, np.cos, np.tan, np.arctan changing the np array 
        # will give a different type of waveform trough the system.
# =============================================================================
    
def main():
    root = Tk()
    gui = Drawing(root)
    root.mainloop()
    
if __name__ == "__main__": main()