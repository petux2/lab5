import requests
from tkinter import *
from PIL import ImageTk, Image

url = "https://aws.random.cat/meow"

#объявление окна
window = Tk()
window.title("Рандомный котик")
window.geometry('400x500')
window.resizable(height=False, width=False)
panel = Label(window)
panel.pack(pady=10)

#генерация нового кота
def meow():
    #обращение к api
    r = requests.get(url)
    r1 = requests.get(r.json()['file'])

    #скачивание картинки
    file = 'cat.jpg'
    with open(file, 'wb') as f:
        f.write(r1.content)

    #изменение размера картинки под окно
    img = Image.open('cat.jpg')
    size = img.size
    img = img.resize((380, int(380 * size[1] / size[0])))

    #отображение картинки
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img

#кнопка
btn = Button(text='Новый котик!', command=meow)
btn.place(x=120, y=440, width=160, height=30)

meow() #первая генерация

window.mainloop()
