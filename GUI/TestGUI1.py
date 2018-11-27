from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master, combo_list):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.combo_list = combo_list

    def greet(self):
        # print("Greetings!")
        for ch in self.combo_list:
            ch = Tk()
            MyFirstGUI(ch, self.combo_list)

alphabet = ['a', 'b','c','d','e', 'f','g','h','i', 'j','k','l','m','n','o', 'p','q','r','s','t','u', 'v','w','x','y','z']
combo_list = []
for letter in alphabet:
    for i in range(len(alphabet)):
        # for j in range(len(alphabet)):
        #     new_letter = letter + alphabet[i] + alphabet[j]
        #     combo_list.append(new_letter)
        new_letter = letter + alphabet[i]
        combo_list.append(new_letter)
        # combo_list.append(new_letter)

root = Tk()
my_gui = MyFirstGUI(root, combo_list)
root.mainloop()
