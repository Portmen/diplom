from tkinter import *
from tkinter import ttk
import subprocess
from create_cont import total_kernels, total_memmory 



def click_btn7(tree):
    global resource_management
    cont_name = tree

    resource_management = Tk()
    resource_management.title("Resource management")
    # create_cont.geometry("815x450+600+100")
    

    state_1 = "image"
    state_2 = "archive"
    

    header_2 = ttk.Label(resource_management, text="Укажите объём выделяемой оперативной памяти для контейнера(DEFAULT=512МБ):", font=("Arial", 10))
    header_2.grid(row=3, column=0, columnspan=3, padx=5, pady=[0,25], sticky=W)
    
    memory_var = IntVar(resource_management, value=512)
    tot_memmory = total_memmory()   #TEST
    memmory_scale = ttk.Scale(resource_management, orient="horizontal", length=300, from_=512.0, to=5000.0, variable=memory_var, command=change_label_memmory)
    memmory_scale.configure(to=tot_memmory)
    memmory_scale.grid(row=4, column=0, columnspan=2, padx=5, pady=[0, 15], sticky=W)
    memmory_label = ttk.Label(resource_management)
    memmory_label.grid(row=4, column=1, padx=5, pady=[0, 15], sticky=W)

    #memory_entry = ttk.Entry(create_cont, textvariable=memory_var, width=25)
    #memory_entry.grid(row=4, column=0, padx=10, pady=[0, 15], sticky=W)
    cpu_var = IntVar(resource_management)
    cpu_checkbtn = ttk.Checkbutton(resource_management, text="Ограничить число виртуальных ядер", variable=cpu_var, command=create_combobox_management_ct )
    cpu_checkbtn.grid(row=5, column=0, padx=5, pady=[10, 5], sticky=W)
    
    ip_var = IntVar(resource_management)
    ip_checkbtn = ttk.Checkbutton(resource_management, text="Ограничить диапозон ip адресов", variable=ip_var, command=create_ip_create_ct)
    ip_checkbtn.grid(row=6, column=0, padx=5, pady=[0, 5], sticky=W)
    
    process_var = IntVar(resource_management)
    process_checkbtn = ttk.Checkbutton(resource_management, text="Ограничить максимальное число процессов в контейнере", variable=process_var, command=create_entry_management_ct )
    process_checkbtn.grid(row=7, column=0, padx=5, pady=[0, 15], sticky=W)


    create_btn = ttk.Button(resource_management, text="Изменить", state="disable")
    create_btn.grid(row=9, column=2, padx=5, pady=[70, 5], sticky=SE) 

    #proc = subprocess.Popen([archive_path, image_name, state_create, disk_size], stdout=subprocess.PIPE)
    #output = proc.stdout.read() #Вывод запуска скрипта
    resource_management.mainloop()


def create_combobox_management_ct():
    global combobox_var_kernel
    combobox_var_kernel = StringVar(resource_management)
    list_kernel = [str(i) for i in range(1, total_kernels() + 1)]
    combobox_kernel = ttk.Combobox(resource_management, values=list_kernel, textvariable=combobox_var_kernel, state="readonly", font=("Arial",8), width=2)
    combobox_kernel.current(0)
    combobox_kernel.grid(row=5, column=1, padx=5, pady=[10, 5], sticky=W)

    
def create_entry_management_ct():
    global entry_proc, message_fail_proc
    entry_proc = ttk.Entry(resource_management, width=4, validate="focusout", validatecommand=validate_proc)
    entry_proc.grid(row=7, column=1, padx=5, pady=[0, 15], sticky=W)

    message_fail_proc = ttk.Label(resource_management, text="")
    message_fail_proc.grid(row=7, column=2, padx=5, pady=[0, 15], sticky=W)    


def validate_proc():
    
    if entry_proc.get() != '':
        try:
            if 1 <= int(entry_proc.get()) <= 1000:
                return True
        except:
            message_fail_proc.config(text="Ошибка", foreground="red")
            return False     
    else:
        message_fail_proc.config(text="Ошибка", foreground="red")
        return False