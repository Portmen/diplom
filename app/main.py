from tkinter import *
from tkinter import ttk
from os import *

#def create_container()


if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    app.geometry("1200x800+350+80")

    icon =  PhotoImage(file="./icon.png")
    app.iconphoto(False, icon)

    btn_1 = ttk.Button(text="Создать контейнер")
    btn_2 = ttk.Button(text="Запуск")
    btn_3 = ttk.Button(text="Остановить")
    btn_4 = ttk.Button(text="Удалить")
    btn_5 = ttk.Button(text="Информация о контейнере")
    btn_6 = ttk.Button(text="Журнал событий")
    btn_7 = ttk.Button(text="Управление ресурсами")
    btn_8 = ttk.Button(text="Консоль контейнера")
    #btn.bind("<Enter>", create_container)
  
    btn_1.grid(row=1, ipadx=50, ipady=10, padx=[15, 30], pady=[70, 10])
    btn_2.grid(row=2, ipadx=76, ipady=10, padx=[15, 30], pady=10)
    btn_3.grid(row=3, ipadx=72, ipady=10, padx=[15, 30], pady=10)
    btn_4.grid(row=4, ipadx=76, ipady=10, padx=[15, 30], pady=10)
    btn_5.grid(row=5, ipadx=26, ipady=10, padx=[15, 30], pady=10)
    btn_6.grid(row=6, ipadx=58, ipady=10, padx=[15, 30], pady=10)
    btn_7.grid(row=7, ipadx=38, ipady=10, padx=[15, 30], pady=10)
    btn_8.grid(row=8, ipadx=46, ipady=10, padx=[15, 30], pady=10)


    app.mainloop() 

