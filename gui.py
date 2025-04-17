from tkinter import *
from tkinter import ttk
from geo import *  # Assuming this is your custom geometry logic

root = Tk()
root.title("autoDraw")
root.geometry("300x269")
icon = PhotoImage(file="pencil.png")
root.iconphoto(True, icon)
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

fr = ttk.Frame(root, padding=10)
fr.pack(fill="both", expand=True)

############### Variable Definitions ###################
en2var = StringVar()
en3var = StringVar()
chkvar1 = IntVar(value=0)
chkvar3 = IntVar(value=0)
comVar = StringVar()
lbl2Text = StringVar()
lbl3Text = StringVar()

################ Functions ################
def updateLabel(*args):
    shape = comVar.get()
    if shape == "Rectangle":
        en3.config(state="normal")
        lbl2Text.set("Length:")
        lbl3Text.set("Height:")
    elif shape == "Square":
        lbl2Text.set("Side:")
        lbl3Text.set("-")
        en3.config(state="disabled")
    else:
        lbl2Text.set("")
        lbl3Text.set("")

def updateCheck(*args):
    if chkvar3.get() == 1:
        scl.config(state="normal", troughcolor="lightgray", fg="black")
        obtn.config(state="normal")
    else:
        scl.config(state="disabled", troughcolor="gray", fg="gray")
        obtn.config(state="disabled")
    if chkvar1.get() == 1:
        cbtn.config(state="normal")
    elif chkvar1.get() == 0:
        cbtn.config(state="disabled")

comVar.trace_add("write", updateLabel)
chkvar3.trace_add("write", updateCheck)
chkvar1.trace_add("write", updateCheck)

################ Widget Creation ################
# Dropdown
lbl = ttk.Label(fr, text="Shape:")
com = ttk.Combobox(fr, textvariable=comVar, values=["Rectangle", "Square"])
com.current(0)
com.config(state="readonly")

# Entry labels and boxes
lbl2 = ttk.Label(fr, textvariable=lbl2Text)
en2 = ttk.Entry(fr, textvariable=en2var)

lbl3 = ttk.Label(fr, textvariable=lbl3Text)
en3 = ttk.Entry(fr, textvariable=en3var)

# Outline size
lbl4 = ttk.Label(fr, text="Outline Size:")
scl = Scale(fr, from_=0, to=20, orient="horizontal", showvalue=True, state="disabled")

# Checkbox frame
check_frame = ttk.Frame(fr)
chk1 = ttk.Checkbutton(check_frame, text="Fill", variable=chkvar1)
chk3 = ttk.Checkbutton(check_frame, text="Outline", variable=chkvar3)

# Buttons
cbtn = ttk.Button(fr, text="🎨 Fill Color", state="disabled")
obtn = ttk.Button(fr, text="🖊 Outline Color", state="disabled")
dbtn = ttk.Button(fr, text="🖌 Draw !")
########################Traces#########################
comVar.trace_add("write", updateLabel)
chkvar3.trace_add("write", updateCheck)
chkvar1.trace_add("write", updateCheck)
################ Layout ################
lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)
com.grid(row=0, column=1, columnspan=2, sticky="ew", pady=5)

lbl2.grid(row=1, column=0, sticky="w", padx=5)
en2.grid(row=1, column=1, columnspan=2, sticky="ew", pady=3)

lbl3.grid(row=2, column=0, sticky="w", padx=5)
en3.grid(row=2, column=1, columnspan=2, sticky="ew", pady=3)

lbl4.grid(row=3, column=0, sticky="w", padx=5)
scl.grid(row=3, column=1, columnspan=2, sticky="ew", pady=3)

check_frame.grid(row=4, column=0, columnspan=3, pady=5)
chk1.grid(row=0, column=0, padx=10)
chk3.grid(row=0, column=1, padx=10)

cbtn.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
obtn.grid(row=5, column=2, sticky="ew", padx=5, pady=5)
dbtn.grid(row=6, column=0, columnspan=3, sticky="ew", pady=5)
# Make entries and combo expand
fr.columnconfigure(1, weight=1)
fr.columnconfigure(2, weight=1)

# Initialize labels and states
updateLabel()
updateCheck()

root.mainloop()
