import subprocess
import multiprocessing
import re
from tkinter import *
from tkinter import ttk
import tkinter.filedialog



def click_btn1():
    global create_cont, archive_btn, header_2, memory_var, memmory_label
    create_cont = Tk()
    create_cont.title("Create container")
    create_cont.geometry("700x800+600+100")
    

    state_list = ["archive", "image"]
    state = StringVar()
    memory_var = IntVar(value=512.0)
    cpu_var = IntVar()
    ip_var = IntVar()
    process_var = IntVar()

    header_1 = ttk.Label(create_cont, text="Выберите способ создания:", font=("Arial", 10))
    header_1.grid(row=0, column=0, columnspan=2, padx=5, pady=[25, 25], sticky=W)

    image_btn = ttk.Radiobutton(create_cont, text="Создание контейнера из имеющихся образов", value=state_list[1], variable=state, command=create_combobox_create_ct)
    image_btn.grid(row=1, column=0, padx=10, pady=[0,10], sticky=W)

    archive_btn = ttk.Radiobutton(create_cont, text="Создание контейнера из архива с ФС", value=state_list[0], variable=state, command=create_path_create_ct)
    archive_btn.grid(row=2, column=0, padx=10, pady=[0, 25], sticky=W)

    header_2 = ttk.Label(create_cont, text="Укажите объём выделяемой оперативной памяти для контейнера(DEFAULT=512МБ):", font=("Arial", 10))
    header_2.grid(row=3, column=0, columnspan=3, padx=5, pady=[0,25], sticky=W)
    

    #tot_memmory = total_memmory()   #TEST
    memmory_scale = ttk.Scale(create_cont, orient="horizontal", length=300, from_=512.0, to=5000.0, variable=memory_var, command=change_label_memmory)
    #memmory_scale.configure(to=tot_memmory)
    memmory_scale.grid(row=4, column=0, columnspan=2, padx=5, pady=[0, 15], sticky=W)
    memmory_label = ttk.Label(create_cont)
    memmory_label.grid(row=4, column=1, padx=5, pady=[0, 15], sticky=W)

    #memory_entry = ttk.Entry(create_cont, textvariable=memory_var, width=25)
    #memory_entry.grid(row=4, column=0, padx=10, pady=[0, 15], sticky=W)

    cpu_checkbtn = ttk.Checkbutton(create_cont, text="Ограничить число виртуальных ядер", variable=cpu_var, command=create_spinbox1_create_ct)
    cpu_checkbtn.grid(row=5, column=0, padx=5, pady=[10, 5], sticky=W)
    
    ip_checkbtn = ttk.Checkbutton(create_cont, text="Ограничить диапозон ip адресов", variable=ip_var, command=create_ip_create_ct)
    ip_checkbtn.grid(row=6, column=0, padx=5, pady=[0, 5], sticky=W)

    process_checkbtn = ttk.Checkbutton(create_cont, text="Ограничить максимальное число процессов в контейнере", variable=process_var, command=create_spinbox2_create_ct)
    process_checkbtn.grid(row=7, column=0, padx=5, pady=[0, 15], sticky=W)

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
'''   Для Linux '''
def total_memmory():
    full_memmory = subprocess.run(["free", "-b"], stdout=subprocess.PIPE).stdout.decode("utf-8")
    list_memmory = full_memmory.split()
    return float (list_memmory[7])

def total_kernels():
    total = multiprocessing.cpu_count()
    return total     
''''''

def change_label_memmory(newVal):
    int_var = str(round(float(newVal)))
    memmory_label["text"] = str(int_var) + " Мб" 



def create_ip_create_ct():
    global ip_entry, message_fail
    ip_entry = ttk.Entry(create_cont, width=18, validate="focusout", validatecommand=message_fail_ip)
    ip_entry.grid(row=6, column=1, padx=5, pady=[0,15], sticky=W)
    message_fail = ttk.Label(create_cont, text="Пример: 192.168.1.0/24")
    message_fail.grid(row=6, column=2, padx=5, pady=[0, 15], sticky=W)
  

def message_fail_ip():
    global ip_addr
    ip_addr = ip_entry.get()
    if validate_ip(ip_addr):
        message_fail.config(text="Ок", foreground="green")
        return True
    else:
        message_fail.config(text="Неверно: xxx.xxx.xxx.xxx/xx", foreground="red")
        return False


def validate_ip(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$"
    if re.match(pattern, ip):
        return True
    else:
        return False

def create_spinbox1_create_ct():
    global spinbox_var1
    #total = total_kernels()      #TEST
    spinbox_var1 = StringVar(value=1.0)
    spinbox_kernel = ttk.Spinbox(create_cont, from_=1.0, to=8.0, textvariable=spinbox_var1)
    #spinbox_kernel.configure(to=total)     #TEST
    spinbox_kernel.grid(row=5, column=1, padx=5, pady=[10, 5], sticky=W)
    

def create_spinbox2_create_ct():
    global spinbox_var2
    spinbox_var2 = StringVar(value=1.0)
    spinbox_proc = ttk.Spinbox(create_cont, from_=1.0, to=100.0, textvariable=spinbox_var2)
    spinbox_proc.grid(row=7, column=1, padx=5, pady=[0, 15], sticky=W)

def create_combobox_create_ct():
    global sel_image
    list_images_cmd = subprocess.run(["machinectl", "list-images"], stdout=subprocess.PIPE).stdout.decode("utf-8").split()
    list_img = []
    for i in range( 6, len(list_images_cmd) - 3, 6):
        list_img.append(list_images_cmd[i])

    combobox_var = StringVar()
    #combobox = ttk.Combobox(create_cont, textvariable=combobox_var, state="readonly", font=("Arial", 8), width=20)  # Для Win
    combobox = ttk.Combobox(create_cont, values=list_img, textvariable=combobox_var, state="readonly", font=("Arial", 8), width=20) #Для Linux
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
