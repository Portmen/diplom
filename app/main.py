from tkinter import *
from tkinter import ttk
from os import listdir
from os.path import isdir, join

def reset_list_cont():
    path = '/var/lib/machines/'
    list_cont = [cont for cont in listdir(path) if isdir(join(path, cont))]
    list_cont_var = StringVar(value=list_cont)
    return list_cont_var

def click_btn1():
    create_cont = Tk()


def click_btn5():
    info_cont = Tk()




def click_btn6():
    log_cont = Tk()



def click_btn7():
    control_resourses = Tk()



def click_btn8():
    consol_cont = Tk()






if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    app.geometry("1200x800+350+80")

    #icon =  PhotoImage(file="./icon.png")
    #app.iconphoto(False, icon)
    
    btn_1 = ttk.Button(text="Создать контейнер",command=click_btn1)
    btn_2 = ttk.Button(text="Запуск")
    btn_3 = ttk.Button(text="Остановить")
    btn_4 = ttk.Button(text="Удалить")
    btn_5 = ttk.Button(text="Информация о контейнере")
    btn_6 = ttk.Button(text="Журнал событий")
    btn_7 = ttk.Button(text="Управление ресурсами")
    btn_8 = ttk.Button(text="Консоль контейнера")
    #btn.bind("<Enter>", create_container)
    for r in range(10):
        app.rowconfigure(index=r, weight=1)
    for c in range(2):
        if c == 0:
            app.columnconfigure(index=c, weight=1)
        else:
            app.columnconfigure(index=c, weight=8)
    btn_1.grid(row=1, ipadx=20, ipady=10, padx=[10, 20], pady=[50, 10], sticky=NSEW)
    btn_2.grid(row=2, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_3.grid(row=3, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_4.grid(row=4, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_5.grid(row=5, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_6.grid(row=6, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_7.grid(row=7, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_8.grid(row=8, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)

    
    list_cont_var = reset_list_cont()
    cont_list = Listbox(listvariable=list_cont_var)
    cont_list.grid(row=1 ,rowspan=8, column=1, sticky=NSEW, pady=[50, 10], padx=[10, 30])
    cont_list.yview_scroll(number=1, what="units")



    app.mainloop() 

