from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import colorchooser
from geo.basic import *
from geo.triangles import *
from tkinter import messagebox as msg

blk = (0, 0, 0)
root = Tk()
root.title("autoDraw")
root.geometry("300x265")
icon = PhotoImage(file="win_icon.png")
root.iconphoto(True, icon)
root.resizable(0, 0) # type: ignore
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
sclVar = IntVar(value=0)

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
    elif shape == "Triangle":
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
class Logic:
    def __init__(self) -> None:
        self.rect = rect
        self.carr = carr
        self.tri_equi = tri_equi
        self.outColored = None
    def cChooser(self, outline, fillcolor):
        gui_chooser = colorchooser.askcolor()
        if gui_chooser[1] is not None:
            if outline:
                self.outColor = gui_chooser[1]
                self.outColored
            elif outline == False:
                self.chosen_c = gui_chooser[1]
        elif gui_chooser[1] is None:
            no_color = msg.showwarning("Please select a color")
            if no_color == "ok":
                pass
    def logicCaller(self):
        self.shape = comVar.get()
        self.outline = chkvar3.get()
        self.filled = chkvar1.get()
        self.m1 = float(en2var.get())
        self.m2 = float(en3var.get())
        self.outSize = float(sclVar.get())
        if self.outline and self.filled:
            self.logic(True, True)
        elif self.outline and not self.filled:
            self.logic(False, True)
        elif not self.outline and self.filled:
            self.logic(True, False)
        elif not self.outline and not self.filled:
            self.logic(False, False)
    def logic(self, filling, outlined):
        match self.shape:
            case "Square":
                if filling:
                    self.carr(self.m1, True, self.chosen_c)
                if outlined and self.outColored:
                    self.outDraw(self.carr, self.outSize, self.chosen_c)
                elif outlined and not self.outColored:
                    self.outDraw(self.carr, self.outSize, None)
                elif not outlined and not filling and not self.outColored:
                    self.carr(self.m1, False, None)
                turtle.done()
            case "Rectangle":
                if filling:
                    self.rect(self.m1, self.m2, True, self.chosen_c)
                elif not filling:
                    self.rect(self.m1, self.m2, False, None)
                if outlined and self.outColored:
                    self.outDraw(self.rect, self.outSize, self.outColor)
                elif outlined and not self.outColored:
                    self.outDraw(self.rect, self.outSize, None)
                elif not outlined and not filling and not self.outColored:
                    self.rect(self.m1, self.m2, False, None)
                turtle.done()
            case "Triangle":
                if filling:
                    self.tri_equi(self.m1, True, self.chosen_c)
                elif not filling and not outlined:
                    self.tri_equi(self.m1, False, None)
                if outlined and self.outColored:
                    self.outDraw(self.tri_equi, self.outSize, self.outColor)
                elif outlined and not self.outColored:
                    self.outDraw(self.tri_equi, self.outSize, None)
                turtle.done()
    def outDraw(self, shape, size, src):
        turtle.pensize(size)
        turtle.penup()
        turtle.setheading(0)
        turtle.pendown()
        if bool(src) == True:
            turtle.color(src)
        else:
            turtle.color(blk)
        if shape == self.tri_equi:
            self.outTriEqui(self.m1)
        elif shape == self.rect:
            self.outRect(self.m1, self.m2)
        elif shape == self.carr:
            self.outSq(self.m1)
    def outSq(self, size):
        for x in range(4):
            turtle.forward(size)
            turtle.left(90)
    def outRect(self, height, width):
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
    def outTriEqui(self, side):
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)

logic = Logic()
def cAsk(src: str):
    if src == "outline":
        logic.cChooser(True, False)
    elif src == "fill":
        logic.cChooser(False, True)
################ Widget Creation ################
# Dropdown
lbl = ttk.Label(fr, text="Shape:")
com = ttk.Combobox(fr, textvariable=comVar, values=["Rectangle", "Square", "Triangle"])
com.current(0)
com.config(state="readonly")

# Entry labels and boxes
lbl2 = ttk.Label(fr, textvariable=lbl2Text)
en2 = ttk.Entry(fr, textvariable=en2var)

lbl3 = ttk.Label(fr, textvariable=lbl3Text)
en3 = ttk.Entry(fr, textvariable=en3var)

# Outline size
lbl4 = ttk.Label(fr, text="Outline Size:")
scl = Scale(fr, from_=0, to=20, orient="horizontal", showvalue=True, state="disabled", variable=sclVar)

# Checkbox frame
check_frame = ttk.Frame(fr)
chk1 = ttk.Checkbutton(check_frame, text="Fill", variable=chkvar1, onvalue=True, offvalue=False)
chk3 = ttk.Checkbutton(check_frame, text="Outline", variable=chkvar3, onvalue=True, offvalue=False)
# Buttons
cbtn = ttk.Button(fr, text="🎨 Fill Color", state="disabled", command= lambda: cAsk("fill"))
obtn = ttk.Button(fr, text="🖊 Outline Color", state="disabled", command= lambda: cAsk("outline"))
dbtn = ttk.Button(fr, text="🖌 Draw !", command = logic.logicCaller)
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

#Icon made by Freepik from www.flaticon.com