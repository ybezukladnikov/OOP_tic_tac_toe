from tkinter import *

count = 0
def clicked():
    global count
    if not count%2:
        btn.configure(text="Х")
    else:
        btn.configure(text="O")
    count+=1

def clicked_1():
    global count
    if not count%2:
        btn1.configure(text="Х")
    else:
        btn1.configure(text="O")
    count+=1






window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('120x120')
# lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
btn = Button(window, height = 1, width = 1, text="", command=clicked)
btn.grid(column=0, row=0)

btn1 = Button(window, text="", command=clicked_1)
btn1.grid(column=1, row=0)
btn2 = Button(window, text="")
btn2.grid(column=0, row=1)
window.mainloop()


