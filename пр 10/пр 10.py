from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()
window.title("Litovchenko UB-23")
window.geometry('1920x1080')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.add(tab2, text="Вторая")
tab_control.add(tab3, text="Третья")

lbl = Label(tab2)
lbl.grid(column=2, row=1)
lbl1 = Label(tab1, text="10", font=(16))
lbl1.grid(column=0, row=0)
lbl2 = Label(tab1, text="10", font=(16))
lbl2.grid(column=2, row=0)
lbl_gl = Label(tab1)
lbl_gl.grid(column=4, row=0)

txt = scrolledtext.ScrolledText(tab3, height=14, width=70)
txt.grid(column=0, row=0)

combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.grid(column=1, row=0)

cs1 = BooleanVar()
cs2 = BooleanVar()
cs3 = BooleanVar()
c1 = Checkbutton(tab2, text="Первый", var=cs1)
c2 = Checkbutton(tab2, text="Второй", var=cs2)
c3 = Checkbutton(tab2, text="Третий", var=cs3)
c1.grid(column=0, row=0)
c2.grid(column=0, row=1)
c3.grid(column=0, row=2)

def calculator():
    if combo.get() == '+':
        lbl_gl.configure(text="20")
    elif combo.get() == '-':
        lbl_gl.configure(text="0")
    elif combo.get() == '*':
        lbl_gl.configure(text="100")
    elif combo.get() == '/':
        lbl_gl.configure(text="1")

def button():
    if c1.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый вариант')
    elif c2.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали второй вариант')
    elif c3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали третий вариант')
    elif ((c1.instate(['selected']) == True) and (c2.instate(['selected']) == True)):
        messagebox.showinfo('Text', 'Вы выбрали первый и второй вариант')
    else:
        lbl.configure(text="Вы ничего не выбрали :(", font=("Times New Roman", 14))

btn = Button(tab2, text="нажми!", command=button)
btn.grid(column=1, row=1)
btn1 = Button(tab1, text="Посчитать", command=calculator)
btn1.grid(column=3, row=0)

def open():
    file = filedialog.askopenfilename()
    with open(file, "r+", encoding='utf-8-sig') as f:
        line = f.read()
        txt.insert('1.0', line)
        txt.place(x=0,y=0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="Открыть", command=open)
new_item.add_separator()
menu.add_cascade(label="Файл", menu=new_item)
window.config(menu=menu)

tab_control.pack(expand=1, fill="both")
window.mainloop()