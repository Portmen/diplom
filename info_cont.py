from tkinter import *
from tkinter import ttk
import subprocess





def click_btn5(tree):
    from main import get_name_cont
    info_cont = Tk()
    info_cont.title("Information")
    info_cont.geometry("700x450+600+100")
    
    info_cont.rowconfigure(index=0, weight=1)
    info_cont.columnconfigure(index=0, weight=1)

    cont_name = get_name_cont(tree)
    info_var = info_container(cont_name)


    label_info = ttk.Label(info_cont, text=info_var, background="#FFFFFF", anchor=NW, padding=5)
    label_info.grid(ipady=20, ipadx=20, padx=10,  pady=10, sticky=NSEW)
    

def info_container(name):
    full_info = subprocess.run(['machinectl', 'status', name], stdout=subprocess.PIPE).stdout.decode("utf-8")
    return full_info    