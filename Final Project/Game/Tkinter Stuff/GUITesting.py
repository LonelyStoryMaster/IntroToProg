import tkinter

class MyGui:
    def __init__(self):
        self.test_column = 0
        self.window = tkinter.Tk()

        self.test_button = tkinter.Button(self.window, text="H")
        self.quit_button = tkinter.Button(self.window, text='Quit', command=self.window.quit)
        self.increment_button = tkinter.Button(self.window, text='+', command=self.increment)
        self.decrement_button = tkinter.Button(self.window, text='-', command=self.decrement)

        self.test_button.grid(row=0, column=self.test_column, sticky='W')
        self.increment_button.grid(row=3, column=0, sticky='W')
        self.decrement_button.grid(row=3, column=1, sticky='W')
        self.quit_button.grid(row=4, column=0, columnspan=1, sticky='W')
    
        tkinter.mainloop()

    def increment(self):
        self.test_column += 1
        self.test_button.grid(row=0, column=self.test_column)

    def decrement(self):
        self.test_column -= 1
        if self.test_column < 0:
            self.test_column = 0
        self.test_button.grid(row=0, column=self.test_column)

my_gui = MyGui()