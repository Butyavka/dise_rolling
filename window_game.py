from tkinter import *
from tkinter import messagebox as mb
import random


class Window:
    def __init__(self, width, height, title="Вход", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable = (resizable[0], resizable[1])
        self.ran_one = 0
        self.ran_two = 0

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Бросай кубики", height=2).grid(row=0, column=1, columnspan=2)

        Button(self.root, text="Бросить", width=10, command=self.random_num).grid(row=1, column=1, columnspan=2)

        Button(self.root, text="Выйти", width= 10, command=self.exit).grid(row=6, column=1, columnspan=2)

    def random_num(self):
        self.ran_one = random.randint(1, 6)
        self.ran_two = random.randint(1, 6)
        Label(self.root, text=self.ran_one, height=2, width=4, relief=GROOVE).grid(row=2, column=0, columnspan=2)
        Label(self.root, text=self.ran_two, height=2, width=4, relief=GROOVE).grid(row=2, column=2, columnspan=2)
        if self.ran_one == 1 and self.ran_two == 1:
            mb.showinfo('*_*', "Глаза змеи!!")



    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(500, 500)
    window.run()