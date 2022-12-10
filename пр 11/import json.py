import json
import requests
from tkinter import *
from tkinter import scrolledtext

def zapros():
    repo = txt.get() #переменная через которую мы получаем значение от пользователя

url = f"https://api.github.com/repos/{repo}"
rep = requests.get(url).json() #переменная в которую делается запрос request и преобразует в json файл

try: #обработка ошибки (выводит none вместо ошибки)
    rep['company']
    rep['email']
    rep['created_at']
    rep['id']
    rep['name']
    rep['url']
except KeyError:
    rep['company'] = None
    rep['email'] = None
    rep['created_at'] = None
    rep['id'] = None
    rep['name'] = None
    rep['url'] = None
with open("File.txt", "a+") as f:
    f.write(f"'company': '{rep['company']}'\n")
    f.write(f"'created_at': '{rep['created_at']}'\n")
    f.write(f"'email': '{rep['email']}'\n")
    f.write(f"'id': '{rep['id']}'\n")
    f.write(f"'name': '{rep['name']}'\n")
    f.write(f"'url': '{rep['url']}'\n")
    f.write("\n") #ключи значения
with open("File.txt", "r+") as f1:
    line = f1.read()
    txt1.insert('1.0', line)

window = Tk()
window.title("GH_Rep")
window.geometry('600x500')
txt = Entry(window)
txt.grid(column="0", row="0")
btn = Button(window, text="Нажать", command=zapros)
btn.grid(column="1", row="0")
txt1 = scrolledtext.ScrolledText(window)
txt1.grid(column="2", row="0")
window.mainloop()
