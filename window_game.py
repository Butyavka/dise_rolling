from tkinter import *
from tkinter import messagebox as mb
import random


class Window:
    def __init__(self, width, height, title="Вход", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable = (resizable[0], resizable[1])
        self.ran = 0
        self.amount = 1

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Число кубиков:", height=2).grid(row=0, column=1, columnspan=2)
        Button(self.root, text="1", width=4, command=self.amount_dise_1).grid(row=2, column=0)
        Button(self.root, text="2", width=4, command=self.amount_dise_2).grid(row=2, column=1)
        Button(self.root, text="3", width=4, command=self.amount_dise_3).grid(row=2, column=2)
        Button(self.root, text="4", width=4, command=self.amount_dise_4).grid(row=2, column=3)
        Label(self.root, text="", height=2).grid(row=3 , column=1, columnspan=2)
        Button(self.root, text="Бросить", width=10, command=self.random_num).grid(row=5, column=1, columnspan=2)

        Button(self.root, text="Выйти", width=10, command=self.exit).grid(row=6, column=1, columnspan=2)

    def amount_dise_1(self):
        self.amount = 1

    def amount_dise_2(self):
        self.amount = 2

    def amount_dise_3(self):
        self.amount = 3

    def amount_dise_4(self):
        self.amount = 4

    def random_num(self):
        for i in range(4):
            self.ran = random.randint(1, 6)
            Label(self.root, text='', height=2, width=4, relief=GROOVE).grid(row=4, column=i)
        for i in range(self.amount):
            self.ran = random.randint(1, 6)
            Label(self.root, text=self.ran, height=2, width=4, relief=GROOVE).grid(row=4, column=i)

    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(500, 500)
    window.run()