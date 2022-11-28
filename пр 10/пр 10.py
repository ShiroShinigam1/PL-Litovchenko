from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()
window.title("Litovchenko A.R. UB-23")
window.geometry('800x600')
window.wm_resizable(0, 0)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.add(tab2, text="Вторая")
tab_control.add(tab3, text="Третья")

lbl = Label(tab2)
lbl.grid(column=2, row=1)
lbl1 = Label(tab1, text="2", font=(16))
lbl1.grid(column=0, row=0)
lbl2 = Label(tab1, text="2", font=(16))
lbl2.grid(column=2, row=0)
lbl_gl = Label(tab1)
lbl_gl.grid(column=4, row=0)

txt = scrolledtext.ScrolledText(tab3, height=14, width=70, bg='#009900')
txt.grid(column=0, row=0)

combo = Combobox(tab1, justify="center", width=5)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)
combo.grid(column=1, row=0)

def calculator():
    if combo.get()=="+":
        label1.configure(text=int(spin.get())+int(spin1.get()))
    elif combo.get()=="-":
        label1.configure(text=int(spin.get())-int(spin1.get()))
    elif combo.get()=="*":
        label1.configure(text=int(spin.get())*int(spin1.get()))
    elif combo.get()=="/" and spin1.get()=="0":
        label1.configure(text="00")
    else:
        label1.configure(text=int(spin.get())/int(spin1.get()))

var =IntVar()
var.set(0)
spin=Spinbox(tab1,from_=-100000,to=100000,width=10,justify="center",textvariable=var)
spin.grid(column=0,row=0)
var1 =IntVar()
var1.set(0)
spin1=Spinbox(tab1,from_=-100000,to=100000,width=10,justify="center",textvariable=var1)
spin1.grid(column=2,row=0)
btn1= Button(tab1,text="=",command=calculator)
btn1.grid(column=3,row=0)
label1 = ttk.Label(tab1,text="0")
label1.grid(column=4,row=0)

chkst1 = BooleanVar()
chkst2 = BooleanVar()
chkst3 = BooleanVar()
chk1 = Checkbutton(tab2, text="Первый", var=chkst1)
chk2 = Checkbutton(tab2, text="Второй", var=chkst2)
chk3 = Checkbutton(tab2, text="Третий", var=chkst3)
chk1.grid(column=0, row=0)
chk2.grid(column=0, row=1)
chk3.grid(column=0, row=2)

def button():
    if chk1.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали первый вариант')
        if chk2.instate(['selected']) == True:
            messagebox.showinfo('Text', 'Вы выбрали второй вариант')
            if chk3.instate(['selected']) == True:
                messagebox.showinfo('Text', 'Вы выбрали третий вариант')
    elif chk2.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали второй вариант')
        if chk3.instate(['selected']) == True:
            messagebox.showinfo('Text', 'Вы выбрали третий вариант')
    elif chk3.instate(['selected']) == True:
        messagebox.showinfo('Text', 'Вы выбрали третий вариант')
    else:
        lbl.configure(text="Вы ничего не выбрали :(", font=("Times New Roman", 16))

btn = Button(tab2, text="нажми!", command=button)
btn.grid(column=1, row=1)

def file():
    file = filedialog.askopenfilename()
    with open(file, "r+", encoding='utf-8-sig') as f:
        line = f.read()
        txt.insert('1.0', line)
        txt.place(x=0,y=0)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label="Открыть", command=file)
new_item.add_separator()
menu.add_cascade(label="Файл", menu=new_item)
window.config(menu=menu)

tab_control.pack(expand=1, fill="both")
window.mainloop()