from tkinter import *
from tkinter import ttk
from geo.basic import *

screen = turtle.Screen()
screen.cv._rootwindow.withdraw()
root = Tk()
root.geometry("300x250")
fr = ttk.Frame(root)
fr.pack()

en2var = StringVar()
en3var = StringVar()
chkvar1 = IntVar(value=0)
chkvar3 = IntVar(value=0)


en2 = Entry(fr, textvariable=en2var)
en3 = Entry(fr, textvariable=en3var)
chk1 = ttk.Checkbutton(fr, text="Fill",variable=chkvar1)
chk3 = ttk.Checkbutton(fr, text="Outline",variable=chkvar3)
scl = Scale(fr, from_=0, to=20, orient="horizontal", showvalue=True)
lbl = Label(fr, text="Shape:").grid(row=0, column=0)
lbl2 = Label(fr, text="").grid(row=2, column=0)
lbl3 = Label(fr, text="").grid(row=3, column=0)
lbl4 = Label(fr, text="Outline Size:").grid(row=4, column=0)
com = ttk.Combobox(fr,values=["Rectangle","Square"])
btn = ttk.Button(fr, text="Draw")

com.grid(row=0, column=1, columnspan=3, sticky="we", pady=5)
en2.grid(row=2, column=1, sticky="we", columnspan=3, pady=5)
en3.grid(row=3, column=1, sticky="we", columnspan=3, pady=5)
scl.grid(row=4, column=1, columnspan=4, sticky="nsew")
chk1.grid(row=5, column=0, padx=5)
chk3.grid(row=5, column=3, sticky="w")
btn.grid(row=7, column=1)
dbtn = ttk.Button(fr, text="Open color chooser")
dbtn.grid(row=6, column=1, pady=5, ipadx=10)


root.wm_attributes("-topmost", 1)
root.resizable(0, 0)
root.mainloop()
