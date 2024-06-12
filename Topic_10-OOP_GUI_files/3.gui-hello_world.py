#! /usr/bin/env python3

from tkinter import Tk, Label, Button

class Gui():
    ''' Hello World Application Class '''

    def __init__(self, master):
        self.master = master

        # // Title for window topbar //
        master.title('Hello World')  

        #  // Adjust geometry // 
        master.geometry('320x100')

        #  // Window label // 
        self.label = Label(master, text='Hello World, message')
        self.label.pack()

        #  // Working button // 
        self.hello_button = Button(master, text='Hello World', 
                                   command=self.hello_world)
        self.hello_button.pack()

        #  // Quit the window // 
        self.close_button = Button(master, text='Quit', 
                                   command=master.quit)
        self.close_button.pack()

    # // Function to print message // 
    def hello_world(self):
        print('Hello World, an initial GUI')

# // Create and run an Application object //
if __name__ == '__main__':
    tk = Tk()
    Gui(tk)
    tk.mainloop()

# End


