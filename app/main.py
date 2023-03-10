from tkinter import *
from tkinter import ttk
from os import *

#def create_container()


if __name__ == "__main__":
    app = Tk()
    app.title('ContainerAPP')
    app.geometry("800x800+500+100")
    icon =  PhotoImage(file="./icon.png")

    app.iconphoto(False, icon)
    btn = ttk.Button(text="CREATE")
    btn.pack(anchor="e", side="bottom", ipadx=8, ipady=8, padx=10, pady=10)
    #btn.bind("<Enter>", create_container)

    entry_arch= ttk.Entry(justify=CENTER)
    entry_arch.pack(anchor=NE, padx=10, pady= 10)

    app.mainloop()

