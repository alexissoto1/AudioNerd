#Python 2.7

import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from tkinter import messagebox

class Recognizer(object):
    
    def __init__(self,root):
        self.root = root
        
        root.title('Speech Recognizer')
        root.resizable(False, False)
        root.configure(background = 'royal blue')
        self.data = ''
        
    # create a Frame for the Text and Scrollbar
        txt_frm = tk.Frame(self.root, width = 400, height = 200)
        txt_frm.pack(fill = "both", expand = True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        txt_frm.configure(background = 'royal blue')

    # create first Text label
        self.lbl1 = tk.Label(txt_frm, text = "You just said: ")
        self.lbl1.grid(row = 1,column = 2,padx = 3,pady = 2)
        self.lbl1.configure(font = ('Arial', 14, 'bold'))  
        
    #Entry text box and scrollbar to it
        self.entry_text = tk.Text(txt_frm, borderwidth = 4, relief = "sunken", height = 8, width = 20)
        self.entry_text.config(font = ("consolas", 12), undo = True, wrap = 'word')
        self.entry_text.grid(row = 25, column = 7, sticky = "nsew", padx=2, pady=2)
        
        self.frame_content = ttk.Frame(root)
        self.frame_content.pack()
        
     #Submit and Clear buttons.
     
        ttk.Button(self.frame_content, text = 'Record',
                   command = self.record).grid(row = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'e')
     
        ttk.Button(self.frame_content, text = 'Info',
                   command = self.info).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')

        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
        
        ttk.Button(self.frame_content, text = 'Exit',
                   command = self._quit).grid(row = 4, column = 2, padx = 5, pady = 5, sticky = 'w')
     
        #Recordign Up and Down press commands

    def record(self):

         self.r = sr.Recognizer()
         self.mic = sr.Microphone()
         self.mic.list_microphone_names()
 
         with self.mic as source:
             self.audio = self.r.listen(source)
         try:
            self.data = (self.r.recognize_google(self.audio))
            print('You just said: ' + self.data)
            self.entry_text.insert(0.0, '\n' + self.data)              
            return (self.data)
     
         except LookupError:                            
             self.data = "Could not understand audio"
             messagebox.showinfo(title = 'Speech Recognizer', message = 'Try again, please!.')

    def info(self):
        messagebox.showinfo(title = 'Speech Recognizer', message = 'Use "Record" button to use your mic and' 
                     + ' speak to the computer. Use "Clear" to erase everything in the text box.' 
                     + '\n' + '\nBe connected to internet to use the app.')

    def clear(self):
        self.entry_text.delete('1.0', 'end')
        
    def _quit(self):
        self.root.quit()
        self.root.destroy()
        exit()
        
def main():  
    
    root = tk.Tk()
    app = Recognizer(root)
    root.mainloop()
    
if __name__ == "__main__": main()
