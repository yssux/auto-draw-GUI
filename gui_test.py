from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x250")
fr = ttk.Frame(root)
fr.pack()

###############Var Definitions###################
en2var = StringVar()
en3var = StringVar()
chkvar1 = IntVar(value=0)
chkvar3 = IntVar(value=0)
comVar = StringVar()
lbl2Text = StringVar()
lbl3Text = StringVar()

##########################Functions###########################
def update_label_from_combobox(*args):
    shape = comVar.get()
    if shape == "Rectangle":
        en3.config(state="normal")
        lbl2Text.set("Length:")
        lbl3Text.set("Height:")
    elif shape == "Square":
        lbl2Text.set("Side:")
        lbl3Text.set("")  # Or set to "-" or hide the label if needed
        en3.config(state="disabled")
    else:
        lbl2Text.set("")
        lbl3Text.set("")

comVar.trace_add("write", update_label_from_combobox)

#######################Widget Creation########################
# Entries
en2 = Entry(fr, textvariable=en2var)
en3 = Entry(fr, textvariable=en3var)
# CheckButtons
chk1 = ttk.Checkbutton(fr, text="Fill", variable=chkvar1, onvalue=True, offvalue=False)
chk3 = ttk.Checkbutton(fr, text="Outline", variable=chkvar3)
# Labels and scale
scl = Scale(fr, from_=0, to=20, orient="horizontal", showvalue=True)
lbl = ttk.Label(fr, text="Shape:")
lbl2 = ttk.Label(fr, textvariable=lbl2Text)
lbl3 = ttk.Label(fr, textvariable=lbl3Text)
lbl4 = ttk.Label(fr, text="Outline Size:")
# Combobox
com = ttk.Combobox(fr, textvariable=comVar)
com["values"] = ["Rectangle", "Square"]
# Buttons
btn = ttk.Button(fr, text="Draw")
cbtn = ttk.Button(fr, text="Open color chooser")

######################Grid Placement#####################
com.grid(row=0, column=1, columnspan=3, sticky="we", pady=5)
en2.grid(row=2, column=1, sticky="we", columnspan=3, pady=5)
en3.grid(row=3, column=1, sticky="we", columnspan=3, pady=5)
scl.grid(row=4, column=1, columnspan=4, sticky="nsew")
chk1.grid(row=5, column=0, padx=5)
chk3.grid(row=5, column=3, sticky="w")
lbl.grid(row=0, column=0)
lbl2.grid(row=2, column=0)
lbl3.grid(row=3, column=0)
lbl4.grid(row=4, column=0)
btn.grid(row=7, column=1)
cbtn.grid(row=6, column=1, pady=5, ipadx=10)

####################################################
root.wm_attributes("-topmost", 1)
root.resizable(0, 0)
root.mainloop()
