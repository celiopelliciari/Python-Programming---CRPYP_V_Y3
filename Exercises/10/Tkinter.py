#! /usr/bin/env python3

# ============================================ #
# //             Module imports             // #
# ============================================ #

from tkinter import (Tk, Label, Button, IntVar, Radiobutton, Checkbutton, Entry, Frame)

# ============================================ #
# //                GUI Class               // #
# ============================================ #


class Gui:

    def __init__(self, master):
        self.master = master

        # Title for window topbar
        master.title('Tkinter in Python3')

        # Adjust geometry----------------------------------------#
        master.geometry("800x400")
        # ------------------------------------------------------ #

        # Title label using grid-------------------------------- #

        self.label = Label(self.master,
                           text="Python3 course questionnaire",
                           font=("TkDefaultFont", "14", "bold"),
                           fg="red",
                           padx=0, pady=10)  # Pack with padding for relative positioning
        self.label.pack()
        # ------------------------------------------------------ #

        # Entry name box---------------------------------------- #
        self.entry_frame = Frame(self.master)
        self.entry_frame.pack(padx=0, pady=5)  # Pack with padding for relative positioning

        self.entry_name_box = Entry(master)
        self.entry_name_box.insert(0, 'Student name')
        self.entry_name_box.pack()
        # ------------------------------------------------------ #

        # "Are you enjoying this course?" label----------------- #
        self.enjoy_label = Label(self.master,
                                 text="Are you enjoying this course?",
                                 font=("TkDefaultFont", "10", "bold"),
                                 fg="black",
                                 padx=20, pady=5)
        self.enjoy_label.pack(anchor="w")
        # ------------------------------------------------------ #

        # Choices buttons--------------------------------------- #
        self.radio_frame = Frame(self.master)
        self.radio_frame.pack(anchor="w", padx=20)  # Pack the frame for radio buttons

        self.rb_choices = [("It is very good", 1),
                           ('It is somewhat good', 2),
                           ("Neutral", 3),
                           ("It is not very good", 4),
                           ("It is not at all good", 5)]

        self.rb_var = IntVar()
        self.rb_var.set(3)  # Initialize choice

        for i, (lang, val) in enumerate(self.rb_choices):
            self.rb = Radiobutton(self.radio_frame,
                                  text=lang,
                                  variable=self.rb_var,
                                  value=val,
                                  padx=0, pady=5)
            self.rb.pack(side="left", anchor="w")  # Pack to the left, anchored west
        # ------------------------------------------------------ #

        # "The sections most interesting for me are" label------ #
        self.enjoy_label = Label(self.master,
                                 text="The sections most interesting for me are:",
                                 font=("TkDefaultFont", "10", "bold"),
                                 fg="black",
                                 padx=20, pady=5)
        self.enjoy_label.pack(anchor="w")
        # ------------------------------------------------------ #

        # Check buttons----------------------------------------- #
        self.checkbutton_frame = Frame(self.master)
        self.checkbutton_frame.pack(anchor="w", padx=20)  # Pack the frame for check buttons

        self.cb_list = ['Basics', 'Interaction', 'Functions', 'RE', 'Files & Db', 'Networking', 'OOP', 'Graphics',
                        'Web']

        self.cb_intvar = []  # List for each button choice

        for row, value in enumerate(self.cb_list):
            self.cb_intvar.append(IntVar())
            self.cb = Checkbutton(self.checkbutton_frame, text=value,
                                  variable=self.cb_intvar[-1],
                                  padx=0, pady=5)
            self.cb.pack(side='left', anchor='w')
        # ------------------------------------------------------ #

        # "Would you recommend this course to others?" label---- #
        self.recommend_label = Label(self.master,
                                     text="Would you recommend this course to others?",
                                     font=("TkDefaultFont", "10", "bold"),
                                     fg="black",
                                     padx=20, pady=5)
        self.recommend_label.pack(anchor="w")
        # ------------------------------------------------------ #

        # Yes/No Choices buttons-------------------------------- #
        self.radio_frame = Frame(self.master)
        self.radio_frame.pack(anchor="w", padx=20)  # Pack the frame for radio buttons

        self.rb_yn = [("Yes", 1), ('No', 2)]

        self.rb_yn_var = IntVar()
        self.rb_yn_var.set(1)  # Initialize choice

        for i, (lang, val) in enumerate(self.rb_yn):
            self.rb = Radiobutton(self.radio_frame,
                                  text=lang,
                                  variable=self.rb_yn_var,
                                  value=val,
                                  padx=0, pady=5)
            self.rb.pack(side="left", anchor="w")  # Pack to the left, anchored west
        # ------------------------------------------------------ #

        # "Have you additional comments" box-------------------- #
        self.entry_comments_box_frame = Frame(self.master)
        self.entry_comments_box_frame.pack(anchor="w", pady=20)  # Pack with padding for relative positioning

        self.entry_comments_box = Entry(self.entry_comments_box_frame, width=500)
        self.entry_comments_box.insert(0, 'Have you additional comments')
        self.entry_comments_box.pack(side="left", anchor="w")
        # ------------------------------------------------------ #

        # Submit button ---------------------------------------- #
        self.hello_button = Button(master, text='Submit',
                                   command=self.submit,
                                   padx=0, pady=0,
                                   width=8, height=2)
        self.hello_button.pack(anchor="s")
        # ------------------------------------------------------ #

        # Quit button ------------------------------------------ #
        self.close_button = Button(master, text='Quit',
                                   command=master.quit,
                                   bg="green",
                                   fg="white",
                                   padx=0, pady=0,
                                   width=6, height=2)
        self.close_button.pack(anchor="s")
        # ------------------------------------------------------ #

        # // Function to print output //

    def submit(self):
        # Get name
        student_name = self.entry_name_box.get()

        # Get enjoyment level
        enjoying_level = self.rb_choices[self.rb_var.get() - 1][0]

        # Get list of interesting sections
        interested_sections = [self.cb_list[i] for i in range(len(self.cb_list)) if self.cb_intvar[i].get()]

        # Get recommendation choice
        recommends = self.rb_yn[self.rb_yn_var.get() - 1][0]

        # Get additional comments
        comments = self.entry_comments_box.get()

        # Print
        print(f"Student name:          {student_name}\n"
              f"Enjoying the course:   {enjoying_level}\n"
              f"Sections of interest:  {interested_sections}\n"
              f"Recommend this course: {recommends}\n"
              f"Comments:              {comments}")

# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #


if __name__ == '__main__':
    tk = Tk()
    Gui(tk)
    tk.mainloop()
