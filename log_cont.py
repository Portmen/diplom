from tkinter import *
from tkinter import ttk
import tk
import subprocess



def click_btn6(tree):
    global cont_name, log_cont, listbox
    from main import get_name_cont
    log_cont = Tk()
    log_cont.title("Logs")
    log_cont.geometry("900x700")

    scrollbar = ttk.Scrollbar(log_cont, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(log_cont, yscrollcommand=scrollbar.set)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    cont_name = get_name_cont(tree)
    logs_container()
    

def logs_container():
    global full_logs
    full_logs = subprocess.run(["sudo", "journalctl", "-M", cont_name], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\n")
    for i in range(len(full_logs)):
        listbox.insert(END, full_logs[i])
    listbox.after(5000, reset_logs)

def reset_logs():
    global full_logs
    new_logs = subprocess.run(["sudo", "journalctl", "-M", cont_name], stdout=subprocess.PIPE).stdout.decode("utf-8").split("\n")
    if len(new_logs) > len(full_logs):
        for i in range(len(full_logs), len(new_logs)):
            listbox.insert(END, new_logs[i])
        full_logs = new_logs    
