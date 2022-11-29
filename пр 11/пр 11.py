import json
import requests
from tkinter import *
from tkinter import scrolledtext

def zapros():
    repo = txt.get()

    url = f"https://api.github.com/repos/{repo}"
    repository_url = requests.get(url).json()

    try:
        repository_url['company']
        repository_url['email']
    except KeyError:
            repository_url['company'] = None
            repository_url['email'] = None

    with open("File.txt", "a+") as f:
        f.write(f"'company': '{repository_url['company']}'\n")
        f.write(f"'created_at': '{repository_url['created_at']}'\n")
        f.write(f"'email': '{repository_url['email']}'\n")
        f.write(f"'id': '{repository_url['id']}'\n")
        f.write(f"'name': '{repository_url['name']}'\n")
        f.write(f"'url': '{repository_url['url']}'\n")
        f.write("\n")
    with open("File.txt", "r+") as f1:
        line = f1.read()
        txt1.insert('1.0', line)

win = Tk()
win.title("GitHub_Repositories")
win.geometry('600x500')
lbl = Label(win, text="Введите имя пользователя и репозиторий через /")
lbl1 = Label(win, text="Например: openshift/origin")
lbl.grid(padx=150, pady=15)
lbl1.grid(padx=150, pady=15)
txt = Entry(win, width=50, justify="center")
txt.grid(padx=150, pady=15)
btn = Button(win, text="Нажать", command=zapros)
btn.grid(padx=150, pady=15)
txt1 = scrolledtext.ScrolledText(win, height=10, width=50, bg='#00BFFF', fg='#FFFFFF')
txt1.grid(padx=100, pady=15)
win.mainloop()