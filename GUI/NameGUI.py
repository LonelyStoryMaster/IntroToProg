import tkinter

class Name:
    def __init__(self, master):
        self.master = master
        master.title("Buttons")

        # Creating buttons
        self.name_button = tkinter.Button(self.master, text='Name', command=self.display_name, height=1)
        self.address_button = tkinter.Button(self.master, text='Address', command=self.display_address)
        self.course_button = tkinter.Button(self.master, text='Course List', command=self.display_courses)
        self.quit_button = tkinter.Button(self.master, text='Quit', command=master.quit)

        self.labelframe = tkinter.LabelFrame(self.master, height=28, width=10)

        self.name_button.grid(row=0, column=0, columnspan=2)
        self.address_button.grid(row=0, column=5, columnspan=2)
        self.course_button.grid(row=0, column=8, columnspan=2)
        self.quit_button.grid(row=2, column=4, columnspan=2)
        self.labelframe.grid(row=0, column=3)

    def display_name(self):
        print("My name is Jared Menze")

    def display_address(self):
        print("I live at 2319 Monster Inc. Drive")

    def display_courses(self):
        print("I am taking:\n - Intro to Programming\n - College Comp 1\n - American Gov.\n - Ethics")

root = tkinter.Tk()
my_gui = Name(root)
root.mainloop()