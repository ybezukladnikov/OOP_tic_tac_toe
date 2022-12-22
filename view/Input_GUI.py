from view.Abstract_Input import Abstract_Input
import tkinter as tk


class Input_GUI(Abstract_Input):

    res = 'test'


    def get_step(self, name):
        return input(f"{name} enter the cell number => ")

    def get_name(self, order):

        def clicked():
            self.res = txt.get()
            window.destroy()
            # lbl.configure(text="Добро пожаловать в приложение PythonRu")

        window = tk.Tk()
        window.title("Добро пожаловать в приложение PythonRu")
        window.geometry('400x250')
        lbl = tk.Label(text=f"Input name {order} player =>")
        lbl.grid(column=0, row=0)
        txt = tk.Entry(width=10)
        txt.grid(column=1, row=0)

        btn = tk.Button(text="Submit", command=clicked)
        btn.grid(column=2, row=0)
        window.mainloop()

        return self.res
        # return input(f"Input name {order} player => ")