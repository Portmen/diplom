import time

from tkinter import *
from tkinter import ttk
from os import listdir, system
from os.path import isdir, join



def craete_btn(state_btn):
    global btn_1,  btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9
    btn_1 = ttk.Button(text="Создать контейнер", command=click_btn1)
    btn_2 = ttk.Button(text="Запуск",  state=state_btn)
    btn_3 = ttk.Button(text="Остановить", state=state_btn)
    btn_4 = ttk.Button(text="Удалить", state=state_btn)
    btn_5 = ttk.Button(text="Информация о контейнере",
                       command=click_btn5, state=state_btn)
    btn_6 = ttk.Button(text="Журнал событий",
                       command=click_btn6, state=state_btn)
    btn_7 = ttk.Button(text="Управление ресурсами",
                       command=click_btn7, state=state_btn)
    btn_8 = ttk.Button(text="Консоль контейнера",
                       command=click_btn8, state=state_btn)
    btn_9 = ttk.Button(text="Обновить список", command=reset_list_cont)
    btn_1.grid(row=1, ipadx=20, ipady=10, padx=[
               10, 20], pady=[50, 10], sticky=NSEW)
    btn_2.grid(row=2, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_3.grid(row=3, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_4.grid(row=4, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_5.grid(row=5, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_6.grid(row=6, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_7.grid(row=7, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_8.grid(row=8, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)
    btn_9.grid(row=9, ipadx=20, ipady=10, padx=[10, 20], pady=10, sticky=NSEW)


def reset_list_cont():
    list_cont = [cont for cont in listdir(PATH) if isdir(join(PATH, cont))]
    list_cont_var = StringVar(value=list_cont)
    cont_list = Listbox(listvariable=list_cont_var, font=8, bd=3)
    cont_list.grid(row=1, rowspan=9, column=1, pady=[
                   50, 10], padx=[10, 30], sticky=NSEW)
    cont_list.yview_scroll(number=1, what="units")


def click_btn1():
    create_cont = Tk()
    create_cont.title("Create container")
    create_cont.geometry("700x800+600+100")


def click_btn5():
    info_cont = Tk()
    info_cont.title("Information")
    info_cont.geometry("700x800+600+100")
    cont_name = cont_list.curselection() #Выбранный контейнер в списке
    label = ttk.Label(text="Информация о контейнере", background="#FFFFFF")
    label.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)



#Разобраться с выводом логов и их обновлением в реальном времени

def click_btn6():
    log_cont = Tk()
    log_cont.title("Logs")
    log_cont.geometry("700x800+600+100")
    log_var = " "
    log_list = log_var.split("\n")
    label = ttk.Label(text="Логи контейнера", background="#FFFFFF")
    label.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)
    while True:
        time.sleep(5)
        log_var = " "
        log_list2 = log_var.split("\n")
        log_list.append(log_list2[-1])
        label = ttk.Label(text="Логи контейнера", background="#FFFFFF")
        label.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)

        

    #logs_list = system("")


def click_btn7():
    control_resourses = Tk()
    control_resourses.title("Control resourses")
    control_resourses.geometry("700x800+600+100")


def click_btn8():
    console_cont = Tk()
    console_cont.title("Console container")
    console_cont.geometry("700x800+600+100")


def change_state_btn(event):
    craete_btn("enable")


if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    app.geometry("1200x800+350+80")
    PATH = '/var/lib/machines/'
    state_btn = "disable"

    #icon =  PhotoImage(file="./icon.png")
    #app.iconphoto(False, icon)
    craete_btn(state_btn)

    #btn.bind("<Enter>", create_container)
    for r in range(11):
        app.rowconfigure(index=r, weight=1)
    for c in range(2):
        if c == 0:
            app.columnconfigure(index=c, weight=1)
        else:
            app.columnconfigure(index=c, weight=8)

    list_cont = [cont for cont in listdir(PATH) if isdir(join(PATH, cont))]
    list_cont_var = StringVar(value=list_cont)
    cont_list = Listbox(listvariable=list_cont_var, font=8, bd=3)
    cont_list.grid(row=1, rowspan=9, column=1, pady=[
                   50, 10], padx=[10, 30], sticky=NSEW)
    cont_list.bind("<<ListboxSelect>>", change_state_btn)
    cont_list.yview_scroll(number=1, what="units")

    app.mainloop()
