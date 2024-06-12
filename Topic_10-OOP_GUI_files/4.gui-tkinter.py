#! /usr/bin/env python3

from tkinter import (Tk, Label, Button, IntVar, Radiobutton, 
                    Checkbutton, Scale, Entry, X, HORIZONTAL)

class Tkinter_app():
    ''' Hello World Application Class '''

    def __init__(self, master):
        self.master = master
        master.title('Place window title here')  # Title for window topbar

        # Set size of application window
        master.geometry('320x450')

        # ------------------------------------------------------ #
        # Window label
        self.label = Label(master, text='Message here',
                           fg='red', font='Helvetica 14 bold')
        self.label.pack()

        # ------------------------------------------------------ #
        Label(master, bg='black', font=(3), height=0).pack(fill=X)
        # ------------------------------------------------------ #
        # Radio buttons

        self.rb_choices = [('Choice #1',1),
                           ('Choice #2',2),
                           ('Choice #3',3)]

        self.rb_var = IntVar()
        self.rb_var.set(1)  # initialise choice

        # Function to show Radiobutton choice
        for lang, val in self.rb_choices:
            self.rb = Radiobutton(master, 
                                  text=lang,
                                  #indicatoron = 0,
                                  #width = 20,
                                  #padx = 20, 
                                  variable=self.rb_var, 
                                  #command=self.rb_show_choice,
                                  value=val)
            self.rb.pack()

        # ------------------------------------------------------ #
        Label(master, bg='black', font=(3), height=0).pack(fill=X)
        # ------------------------------------------------------ #
        # Checkbuttons

        self.cb_list = ['Check1',
                        'Check2',
                        'Check3']

        self.cb_intvar = []   # List for each button choice

        # Function to show Checkbutton choice
        for row, value in enumerate(self.cb_list):
            self.cb_intvar.append(IntVar()) 
            self.cb = Checkbutton(master,text=value,
                                  variable=self.cb_intvar[-1])
            self.cb.pack()

        # ------------------------------------------------------ #
        # Entry box
        self.entry_box = Entry(master)
        self.entry_box.insert(20, 'Name')
        self.entry_box.pack()

        # ------------------------------------------------------ #
        # Slider

        self.scale1 = Scale(master, from_=0, to=20)
        self.scale2 = Scale(master, from_=0, to=100, 
                            orient=HORIZONTAL)
        self.scale1.pack()
        self.scale2.pack()

        # ------------------------------------------------------ #
        # Working button
        self.submit_button = Button(master, text='Submit', 
                                   command=self.show_choices)
        self.submit_button.pack()

        # ------------------------------------------------------ #
        # Quit the window
        self.close_button = Button(master, text='Quit', 
                                   bg='green',fg='white',
                                   relief='raised', bd=2,
                                   activebackground='red', 
                                   command=master.quit)
        self.close_button.pack()

    # ------------------------------------------------------ #
    # Action functions

    # Function to extract and print Radiobutton message
    def rb_show_choice(self):
        pos = (self.rb_var.get() - 1)
        print(f'{self.rb_choices[pos][0]}: selected')

    # Function to extract and print Checkbutton message
    def cb_show_choice(self):
        for count, var in enumerate(self.cb_intvar):
            if var.get():
                print(f'{self.cb_list[count]}: checked')

    # Function to extract and print entrybox message
    def eb_show_choice(self):
        eb_text = self.entry_box.get()
        print(f"'{eb_text}' is in the entry box")

    # Function to extract and print scale numbers
    def sc_show_choice(self):
        sc1_text = self.scale1.get()
        sc2_text = self.scale2.get()
        print(f'Scale vertical: {sc1_text}')
        print(f'Scale horizontal: {sc2_text}')

    # Function to display choices
    def show_choices(self):
        print('')
        self.rb_show_choice()
        self.cb_show_choice()
        self.eb_show_choice()
        self.sc_show_choice()

# create and run an Application object
if __name__ == '__main__':
    tk = Tk()
    Tkinter_app(tk)
    tk.mainloop()


