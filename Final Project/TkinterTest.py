from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_quit)

        quitButton.place(x=200, y=150)

    def client_quit(self):
        exit()

root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()