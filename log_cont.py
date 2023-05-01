from tkinter import *
from tkinter import ttk
import subprocess



def click_btn6(tree):
    global label, cont_name, log_cont
    from main import get_name_cont
    log_cont = Tk()
    log_cont.title("Logs")
    cont_name = get_name_cont(tree)
    label = ttk.Label(log_cont, background="#FFFFFF")
    label.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)
    logs_container()
    

def logs_container():
    full_logs = subprocess.run(["sudo", "journalctl", "-M", cont_name], stdout=subprocess.PIPE).stdout.decode("utf-8")
    label.config(text=full_logs)
    label.after(5000, logs_container)