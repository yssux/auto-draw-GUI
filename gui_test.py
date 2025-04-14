from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x240")
fr = ttk.Frame(root)
fr.pack()

com = ttk.Combobox(fr,values=["a", "b", "c"])
btn = ttk.Button(fr, text="Dummy")
chkvar1 = IntVar(value=0)
chkvar2 = IntVar(value=0)
chkvar3 = IntVar(value=0)

en2 = Entry(fr)
en3 = Entry(fr)
chk1 = ttk.Checkbutton(fr, text="Check1",variable=chkvar1)
chk3 = ttk.Checkbutton(fr, text="Check3",variable=chkvar3)
scl = Scale(fr, from_=0, to=20, orient="horizontal", showvalue=True)
lbl = Label(fr, text="Combobox").grid(row=0, column=0)
lbl2 = Label(fr, text="Entry1").grid(row=2, column=0)
lbl3 = Label(fr, text="Entry2").grid(row=3, column=0)
lbl4 = Label(fr, text="Outline Size:").grid(row=4, column=0)

def debug():
    chk1d = chkvar1.get()
    chk3d = chkvar3.get()
    if en2.get() == 1:
        en2d = True
    else:
        en2d = False
    if en3.get() == 1:
        en3d = True
    else:
        en3d = False

    comd = com.get()

    print("Check1 : ", chk1d)
    print("Check3 : ", chk3d)
    print("Entry1 : ", en2d)
    print("Entry2 : ", en3d)
    print("Combobox : ", comd)
    print("Scale : ", scl.get())

com.grid(row=0, column=1, columnspan=3, sticky="we", pady=5)
en2.grid(row=2, column=1, sticky="we", columnspan=3, pady=5)
en3.grid(row=3, column=1, sticky="we", columnspan=3, pady=5)
scl.grid(row=4, column=1, columnspan=4, sticky="nsew")
chk1.grid(row=5, column=0, sticky="e")
chk3.grid(row=5, column=3, sticky="w")
btn.grid(row=6, column=1)
dbtn = ttk.Button(fr, text="States", command=debug)
dbtn.grid(row=7, column=1, pady=5)

###################Debug####################


root.wm_attributes("-topmost", 1)
root.resizable(0, 0)
root.mainloop()
