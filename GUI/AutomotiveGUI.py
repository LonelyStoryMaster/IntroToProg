import tkinter
import tkinter.messagebox

class JoesAuto:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.check_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.cb1_val = tkinter.IntVar()
        self.cb2_val = tkinter.IntVar()
        self.cb3_val = tkinter.IntVar()        
        self.cb4_val = tkinter.IntVar()
        self.cb5_val = tkinter.IntVar()
        self.cb6_val = tkinter.IntVar()
        self.cb7_val = tkinter.IntVar()

        self.cb1_val.set(0)
        self.cb2_val.set(0)
        self.cb3_val.set(0)
        self.cb4_val.set(0)
        self.cb5_val.set(0)
        self.cb6_val.set(0)
        self.cb7_val.set(0)

        self.cb1 = tkinter.Checkbutton(self.check_frame, \
                    text='Oil Change', variable=self.cb1_val)
        self.cb2 = tkinter.Checkbutton(self.check_frame, \
                    text='Lube Job', variable=self.cb2_val)
        self.cb3 = tkinter.Checkbutton(self.check_frame, \
                    text='Radiator Flush', variable=self.cb3_val)
        self.cb4 = tkinter.Checkbutton(self.check_frame, \
                    text='Transmission Flush', variable=self.cb4_val)
        self.cb5 = tkinter.Checkbutton(self.check_frame, \
                    text='Inspection', variable=self.cb5_val)
        self.cb6 = tkinter.Checkbutton(self.check_frame, \
                    text='Muffler Replacement', variable=self.cb6_val)
        self.cb7 = tkinter.Checkbutton(self.check_frame, \
                    text='Tire Rotation', variable=self.cb7_val)

        self.cb1.pack(side='top')
        self.cb2.pack(side='top')
        self.cb3.pack(side='top')
        self.cb4.pack(side='top')
        self.cb5.pack(side='top')
        self.cb6.pack(side='top')
        self.cb7.pack(side='top')

        self.ok_button = tkinter.Button(self.button_frame, \
                    text='Make Selections', command=self.show_selections)
        self.quit_button = tkinter.Button(self.button_frame, \
                    text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.check_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show_selections(self):
        self.message = "You selected:\n"
        self.total = 0

        if self.cb1_val.get() == 1:
            self.message += 'Oil change—$30.00\n'
            self.total += 30
        if self.cb2_val.get() == 1:
            self.message += 'Lube job—$20.00\n'
            self.total += 20
        if self.cb3_val.get() == 1:
            self.message += 'Radiator flush—$40.00\n'
            self.total += 40
        if self.cb4_val.get() == 1:
            self.message += 'Transmission flush—$100.00\n'
            self.total += 100
        if self.cb5_val.get() == 1:
            self.message += 'Inspection—$35.00\n'
            self.total += 35
        if self.cb6_val.get() == 1:
            self.message += 'Muffler replacement—$200.00\n'
            self.total += 200
        if self.cb7_val.get() == 1:
            self.message += 'Tire rotation—$20.00\n'
            self.total += 20

        self.message += '\nTotal: %d' % self.total

        tkinter.messagebox.showinfo('Selections', self.message)

joes_auto = JoesAuto()