import time
#import subprocess
import tkinter.filedialog
import re
from tkinter import *
from tkinter import ttk
from os import listdir, system
from os.path import isdir, join




def create_btn(state_btn):
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
    #list_cont = [cont for cont in listdir(PATH) if isdir(join(PATH, cont))]
    #list_cont_var = StringVar(value=list_cont)
    cont_list = Listbox(listvariable=list_cont_var, font=8, bd=3)
    cont_list.grid(row=1, rowspan=9, column=1, pady=[
                   50, 10], padx=[10, 30], sticky=NSEW)
    cont_list.bind("<<ListboxSelect>>", change_state_btn)
    cont_list.yview_scroll(number=1, what="units")

#Разобраться с отображением
def click_btn1():
    global create_cont, archive_btn, header_2
    create_cont = Tk()
    create_cont.title("Create container")
    create_cont.geometry("700x800+600+100")
    #for r in range(14):
    #    create_cont.rowconfigure(index=r, weight=1)
    #for c in range(2):
    #    create_cont.columnconfigure(index=0, weight=1)

    state_list = ["archive", "image"]
    state = StringVar()
    memory_var = StringVar()
    cpu_var = IntVar()
    ip_var = IntVar()

    header_1 = ttk.Label(create_cont, text="Выберите способ создания:", font=("Arial", 10))
    header_1.grid(row=0, column=0, columnspan=2, padx=5, pady=[25, 25], sticky=W)

    image_btn = ttk.Radiobutton(create_cont, text="Создание контейнера из имеющихся образов", value=state_list[1], variable=state, command=create_combobox_create_ct)
    image_btn.grid(row=1, column=0, padx=10, pady=[0,10], sticky=W)

    archive_btn = ttk.Radiobutton(create_cont, text="Создание контейнера из архива с ФС", value=state_list[0], variable=state, command=create_path_create_ct)
    archive_btn.grid(row=2, column=0, padx=10, pady=[0, 25], sticky=W)

    header_2 = ttk.Label(create_cont, text="Укажите объём выделяемой оперативной памяти для контейнера(Гб):", font=("Arial", 10))
    header_2.grid(row=3, column=0, padx=5, columnspan=2, pady=[0,25], sticky=W)

    memory_entry = ttk.Entry(create_cont, textvariable=memory_var, width=25)
    memory_entry.grid(row=4, column=0, padx=10, pady=[0, 15], sticky=W)

    cpu_checkbtn = ttk.Checkbutton(create_cont, text="Ограничить число виртуальных ядер", variable=cpu_var, command=create_scale_create_ct)
    cpu_checkbtn.grid(row=5, column=0, padx=5, pady=[10, 5], sticky=W)
    
    ip_checkbtn = ttk.Checkbutton(create_cont, text="Ограничить диапозон ip адресов", variable=ip_var, command=create_ip_create_ct)
    ip_checkbtn.grid(row=6, column=0, padx=5, pady=[0, 15], sticky=W)

    if state.get() == state_list[1]:
        state_create = state_list[1]
        image_name = sel_image

    elif state.get() == state_list[0]:
        state_create = state_list[0]    

    archive_path = ""
    image_name = ""
    disk_size = ""
    #proc = subprocess.Popen([archive_path, image_name, state_create, disk_size], stdout=subprocess.PIPE)
    #output = proc.stdout.read() #Вывод запуска скрипта

def create_ip_create_ct():
    global ip_entry, message_fail
    ip_entry = ttk.Entry(create_cont, width=18)  #Настроить проверку корректности
    ip_entry.grid(row=6, column=1, padx=5, pady=[0,15], sticky=W)
    message_fail = ttk.Label(create_cont, text="A")
    message_fail.grid(row=6, column=2, padx=5, pady=[0, 15], sticky=W)
    message_fail_ip()   #Сделать проверку в реальном времени
  

def message_fail_ip():
    if validate_ip():
        message_fail.config(text="Ок")
    else:
        message_fail.config(text="Неверно: xxx.xxx.xxx.xxx/xx")


def validate_ip():
    pattern = r"^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$"
    ip_addr = ip_entry.get()
    if re.match(pattern, ip_addr):
        return True
    else:
        return False

def create_scale_create_ct():
    global num_cpu
    num_cpu = IntVar(value=1)
    scale_cpu = ttk.Scale(create_cont, orient="horizontal", length=200, from_=1, to=8, variable=num_cpu)
    cpu_label = ttk.Label(create_cont, textvariable=num_cpu)
    cpu_label.grid(row=5, column=2, padx=[0, 3], pady=[10, 5], sticky=W) #??? отображение
    scale_cpu.grid(row=5, column=1, padx=[5, 0], pady=[10, 5], sticky=W)


def create_combobox_create_ct():
    global sel_image
    combobox_var = StringVar()
    combobox = ttk.Combobox(create_cont, textvariable=combobox_var, state="readonly", font=("Arial", 8), width=30)  # Для Win
    #combobox = ttk.Combobox(create_cont, values=list_cont, textvariable=combobox_var, state="readonly", font=("Arial", 8), width=30) #Для Linux
    combobox.grid(row=1, column=1, padx=[5,10], pady=[0, 10], sticky=W)
    sel_image = combobox.get()


def create_path_create_ct():
    btn_path = ttk.Button(create_cont, text="Выбрать", command=open_path)
    btn_path.grid(row=2, column=1, padx=[5, 10], pady=[0,25], sticky=W)

    #entry = ttk.Entry(create_cont, textvariable=entry_var, width=30) #проверку добавить
    #entry.grid(row=2, column=1, columnspan=2, padx=[5,10], pady=[0, 25], sticky= W)

def open_path():
    global path_file
    path_file = tkinter.filedialog.askopenfilename()
    show_path()
    

def show_path():
    path_label = ttk.Label(create_cont, text=path_file)
    path_label.grid(row=2, column=2, padx=[5, 10], pady=[0, 25], sticky=W)


def click_btn5():
    info_cont = Tk()
    info_cont.title("Information")
    info_cont.geometry("700x800+600+100")
    cont_name = cont_list.curselection() #Выбранный контейнер в списке
    label_info = ttk.Label(info_cont, text="Информация о контейнере", background="#FFFFFF")
    label_info.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)



#Разобраться с выводом логов и их обновлением в реальном времени

def click_btn6():
    log_cont = Tk()
    log_cont.title("Logs")
    log_cont.geometry("700x800+600+100")
    log_var = " "
    log_list = log_var.split("\n")
    label = ttk.Label(log_cont, text="Логи контейнера", background="#FFFFFF")
    label.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)
    while True:
        time.sleep(5)
        log_var = " "
        log_list2 = log_var.split("\n")
        log_list.append(log_list2[-1])
        label = ttk.Label(log_cont, text="Логи контейнера", background="#FFFFFF")
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
    create_btn("enable")


if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    app.geometry("1200x800+350+80")
    PATH = '/var/lib/machines/'
    state_btn = "disable"

    #icon =  PhotoImage(file="./icon.png")
    #app.iconphoto(False, icon)
    create_btn(state_btn)

    #btn.bind("<Enter>", create_container)
    for r in range(11):
        app.rowconfigure(index=r, weight=1)
    for c in range(2):
        if c == 0:
            app.columnconfigure(index=c, weight=1)
        else:
            app.columnconfigure(index=c, weight=8)

    #list_cont = [cont for cont in listdir(PATH) if isdir(join(PATH, cont))]  #Раскоментить для Linux
    #list_cont_var = StringVar(value=list_cont)
    list_cont_var = StringVar()    # Для Win
    cont_list = Listbox(listvariable=list_cont_var, font=8, bd=3)
    cont_list.grid(row=1, rowspan=9, column=1, pady=[
                   50, 10], padx=[10, 30], sticky=NSEW)
    cont_list.bind("<<ListboxSelect>>", change_state_btn)
    cont_list.yview_scroll(number=1, what="units")

    app.mainloop()
