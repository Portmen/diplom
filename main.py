import time
import subprocess       #Для Linux
from tkinter import *
from tkinter import ttk
from create_cont import *

'''
*********************************************************
***************ФУНКЦИИ ГЛАВНОГО ОКНА*********************
*********************************************************
'''

def create_btn(state_btn):
    global btn_1,  btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9
    from log_cont import click_btn6
    from info_cont import click_btn5
    from resource_management import click_btn7
    btn_1 = ttk.Button(text="Создать контейнер", command=click_btn1)
    btn_2 = ttk.Button(text="Запуск",  state=state_btn)
    btn_3 = ttk.Button(text="Остановить", state=state_btn, command=power_off)
    btn_4 = ttk.Button(text="Удалить", state=state_btn, command=power_off)
    btn_5 = ttk.Button(text="Информация о контейнере",
                       command=lambda: click_btn5(tree), state=state_btn)
    btn_6 = ttk.Button(text="Журнал событий",
                       command=lambda: click_btn6(tree), state=state_btn)
    btn_7 = ttk.Button(text="Управление ресурсами",
                       command=lambda: click_btn7(tree), state=state_btn)
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
    global tree
    list_cont = subprocess.run(["machinectl", "list"], stdout=subprocess.PIPE).stdout.decode("utf-8").split()
    head_tree = ("machines", "class", "service", "os", "version", "addresses")
    tree = ttk.Treeview(columns=head_tree, show="headings")
    tree.grid(row=1, rowspan=9, column=1, pady=[
                   50, 10], padx=[10, 30], sticky=NSEW)
    for i in head_tree:
        tree.heading(i, text=i)
    if len(list_cont) > 2:
        add_list = []
        count = 0
        for i in range(6, len(list_cont)):
            count += 1
            if count == 6:
                if validate_list_cont(list_cont[i]):
                    add_list.append(list_cont[i]) 
                    tree.insert("", END, values=add_list)
                    count = 0
                    add_list.clear()
                else:
                    tree.insert("", END, values=add_list)
                    count = 0
                    add_list.clear()
                    count += 1
                    add_list.append(list_cont[i])                       
            elif count < 6:
                add_list.append(list_cont[i])
    else:
        none_list = ["(пусто)" for i in range(6)]
        tree.insert("", END, values=none_list)                 
    tree.bind("<<TreeviewSelect>>", change_state_btn)       


def get_name_cont(tree):
    cont_id = tree.selection()  #id выбранного контейнера
    item = tree.item(cont_id)
    cont_name = item["values"][0]
    return cont_name


def change_state_btn(event):
    create_btn("enable")


def validate_list_cont(ip):
    if validate_ip(ip):
        return True
    else:
        return False


def power_off():
    cont_name = get_name_cont(tree)
    subprocess.run(["machinectl", "poweroff", cont_name])
    reset_list_cont()


'''
************************************************************
***************ФУНКЦИИ ОКНА КОНСОЛИ КОНТЕЙНЕРА**************
************************************************************
'''

def click_btn8():
    console_cont = Tk()
    console_cont.title("Console container")
    console_cont.geometry("700x800+600+100")


if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    PATH = '/var/lib/machines/'
    state_btn = "disable"

    icon = PhotoImage(file = "./icon/icon.png")
    app.iconphoto(True, icon)
    
    for r in range(11):
        app.rowconfigure(index=r, weight=1)
    for c in range(2):
        if c == 0:
            app.columnconfigure(index=c, weight=1)
        else:
            app.columnconfigure(index=c, weight=8)

    reset_list_cont()
    create_btn(state_btn)    

    app.mainloop()
