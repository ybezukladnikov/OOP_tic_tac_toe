from view.Abstract_Input import Abstract_Input
from tkinter import *


class Input_GUI(Abstract_Input):

    res = 'test'


    def get_step(self, name):
        return input(f"{name} enter the cell number => ")



    def get_name(self, order):



        def clicked():
            self.res = txt.get()
            lbl.configure(text="Добро пожаловать в приложение PythonRu")

        window = Tk()
        window.title("Добро пожаловать в приложение PythonRu")
        window.geometry('400x250')
        lbl = Label(window, text=f"Input name {order} player =>")
        lbl.grid(column=0, row=0)
        txt = Entry(window, width=10)
        txt.grid(column=1, row=0)

        btn = Button(window, text="Submit", command=clicked)
        btn.grid(column=2, row=0)
        window.mainloop()

        return self.res
        # return input(f"Input name {order} player => ")