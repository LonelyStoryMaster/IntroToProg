import tkinter

class Application(tkinter.Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = tkinter.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_var = tkinter.IntVar()

        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there["variable"] = self.hi_var

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
