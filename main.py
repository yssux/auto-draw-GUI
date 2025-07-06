import turtle
from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import colorchooser
from geo.basic import *
from geo.triangles import *
from tkinter import messagebox as msg

#Setup
blk = (0, 0, 0)
root = Tk()
try:
    root.iconbitmap("pencil.ico")
    root.title("autoDraw")
    root.geometry("300x340")
    root.resizable(0, 0) # type: ignore
    root.wm_attributes("-topmost", 1)
    screen = turtle.Screen()
    window = screen.getcanvas().winfo_toplevel()
    window.protocol("WM_DELETE_WINDOW", window.withdraw) #type: ignore
    screen.setup(500, 500)
    screen.title("autoDraw")
    window.withdraw() #type: ignore
    turtle.hideturtle()
    fr = ttk.Frame(root, padding=10)
    fr.pack(fill="both", expand=True)
    ############### Variable Definitions ###################
    en2var = IntVar(value=None)
    en3var = IntVar(value=None)
    chkvar1 = IntVar()
    chkvar3 = IntVar()
    comVar = StringVar()
    comVarType = StringVar()
    lbl2Text = StringVar()
    lbl3Text = StringVar()
    sclVar = IntVar(value=0)

    ################ Functions ################
    def updateLabel(*args):
        shape = comVar.get()
        type = comVarType.get()
        if shape == "Rectangle":
            en3.config(state="normal")
            comType.config(state="disabled")
            lbl2Text.set("Length:")
            lbl3Text.set("Height:")
        elif shape == "Square":
            en3.config(state="disabled")
            comType.config(state="disabled")
            lbl2Text.set("Side:")
            lbl3Text.set("-")
        elif shape == "Triangle":
                comType.config(state="normal")
                if type == "Equilateral":
                    lbl2Text.set("Side:")
                    lbl3Text.set("-")
                    en3.config(state="disabled")
                elif type in ("Isosceles", "Right"):
                    lbl2Text.set("Base:")
                    lbl3Text.set("Height:")
                    en3.config(state="normal")
        elif shape is None or shape == "":
            lbl2Text.set("-")
            lbl3Text.set("-")
            en3.config(state="disabled")
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
            self.tri_iso = tri_iso
            self.tri_rect = tri_rect
            self.outColored = None
            self.outliner = turtle.Turtle()
        def cChooser(self, outline, fillcolor):
            gui_chooser = colorchooser.askcolor()
            if gui_chooser[1] is not None:
                if outline:
                    self.outColor = gui_chooser[1]
                    self.outColored
                elif outline == False:
                    self.chosen_c = gui_chooser[1]
            elif gui_chooser[1] is None:
                no_color = msg.showwarning("Error", "No color selected, please select a color")
                if no_color == "ok":
                    pass
        def logicGetter(self):
            self.shape = comVar.get()
            self.shapeType = comVarType.get()
            self.outline = chkvar3.get()
            self.filled = chkvar1.get()
            self.m1 = int(en2var.get())
            self.m2 = int(en3var.get())
            self.outSize = float(sclVar.get())
            while True:
                if self.shape == "Square" and self.m1 <= 0:
                    msg.showerror("Error", "Please enter a valid size")
                    break
                elif self.shape == "Rectangle" and (self.m1 <= 0 or self.m2 <= 0):
                    msg.showerror("Error", "Please enter a valid size")
                    break
                elif self.shape == "Triangle" and self.m1 <= 0:
                    msg.showerror("Error", "Please enter a valid size")
                    break
                else:
                    self.logicCaller()
        def logicCaller(self):           
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
                    window.deiconify() #type: ignore
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
                    window.deiconify() #type: ignore
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
                    match self.shapeType:
                        case "Equilateral":
                            window.deiconify() #type: ignore
                            if filling:
                                self.tri_equi(self.m1, True, self.chosen_c)
                            elif not filling and not outlined:
                                self.tri_equi(self.m1, False, None)
                            if outlined and self.outColored:
                                self.outDraw(self.tri_equi, self.outSize, self.outColor)
                            elif outlined and not self.outColored:
                                self.outDraw(self.tri_equi, self.outSize, None)
                            turtle.done()
                        case "Isosceles":
                            window.deiconify()
                            if filling:
                                self.tri_iso(self.m1, self.m2, True, self.chosen_c)
                            elif not filling and not outlined:
                                self.tri_iso(self.m1, self.m2, False, None)
                            if outlined and self.outColored:
                                self.outDraw(self.tri_iso, self.outSize, self.outColor)
                            elif outlined and not self.outColored:
                                self.outDraw(self.tri_iso, self.outSize, None)
                            turtle.done()                                                    
                        case "Right":
                            window.deiconify()
                            if filling:
                                self.tri_rect(self.m1, self.m2, True, self.chosen_c)                            
                            elif not filling and not outlined:
                                self.tri_rect(self.m1,self.m2, False, None)
                            if outlined and self.outColored:
                                self.outDraw(self.tri_rect, self.outSize, self.outColor)
                            elif outlined and not self.outColored:
                                self.outDraw(self.tri_rect, self.outSize, None)
                            turtle.done()
        def outDraw(self, shape, size, src):
            self.outliner.pensize(size)
            self.outliner.penup()
            self.outliner.setheading(0)
            self.outliner.pendown()
            self.outliner.speed(0)
            self.outliner.hideturtle()
            if bool(src) == True:
                self.outliner.color(src)
            elif bool(src) == False:
                self.outliner.color(self.outColor)
            if shape == self.tri_equi:
                self.outTriEqui(self.m1)
            elif shape == self.rect:
                self.outRect(self.m1, self.m2)
            elif shape == self.carr:
                self.outSq(self.m1)
            elif shape == self.tri_rect:
                self.outTriRect(self.m1, self.m2)
            elif shape == self.tri_iso:
                self.outTrIso(self.m1, self.m2)
            elif shape == self.tri_equi:
                self.outTriEqui(self.m1)
        def outSq(self, size):
            for x in range(4):
                self.outliner.forward(size)
                self.outliner.left(90)
        def outRect(self, height, width):
            for _ in range(2):
                self.outliner.forward(width)
                self.outliner.left(90)
                self.outliner.forward(height)
                self.outliner.left(90)
        def outTriEqui(self, side):
            for _ in range(3):
                self.outliner.forward(side)
                self.outliner.left(120)
        def outTrIso(self, side, base):
            height = (side ** 2 - (base / 2) ** 2) ** 0.5
            # Draw the isosceles triangle
            angle = math.degrees(math.atan(height / (base / 2)))
            self.outliner.forward(base)  # Draw the base
            self.outliner.left(180 - angle)  # Turn to draw the first equal side
            self.outliner.forward(side)  # Draw the first equal side
            self.outliner.left(2 * angle)  # Turn to draw the second equal side
            self.outliner.forward(side)
        def outTriRect(self, a, b):
            # Calculate hypotenuse
            c = math.sqrt(a ** 2 + b ** 2)
            angle = math.degrees(math.atan2(b, a))
            # Move to starting position (optional)
            self.outliner.penup()
            self.outliner.goto(-a // 2, -b // 2)  # Centering the triangle
            self.outliner.pendown()
            # Draw the triangle correctly
            self.outliner.forward(a)  # Base
            self.outliner.left(90)
            self.outliner.forward(b)  # Height
            self.outliner.left(90 + angle)
            self.outliner.forward(c)  # Hypotenuse
    logic = Logic()
    def cAsk(src: str):
        if src == "outline":
            logic.cChooser(True, False)
        elif src == "fill":
            logic.cChooser(False, True)
    ################ Widget Creation ################
    # ShapeDropdown
    lbl = ttk.Label(fr, text="Shape:")
    com = ttk.Combobox(fr, textvariable=comVar, values=["Rectangle", "Square", "Triangle"])
    com.current(0)
    com.config(state="readonly")
    #ShapeType Dropdown
    lblType = ttk.Label(fr, text="Shape Type:")
    comType = ttk.Combobox(fr, textvariable=comVarType, values=["Equilateral", "Isosceles", "Right"])
    com.current(0)
    comType.config(state="readonly")
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
    dbtn = ttk.Button(fr, text="🖌 Draw !", command=logic.logicGetter)
    ebtn = ttk.Button(fr, text="⬇️ Export", command=lambda: msg.showinfo("Info", "This feature is not implemented yet."))
    ########################Traces#########################
    comVar.trace_add("write", updateLabel)
    comVarType.trace_add("write", updateLabel)
    chkvar3.trace_add("write", updateCheck)
    chkvar1.trace_add("write", updateCheck)
    ################ Layout ################
    lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    com.grid(row=0, column=1, columnspan=2, sticky="ew", pady=5)
    comType.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)
    lblType.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    lbl2.grid(row=2, column=0, sticky="w", padx=5)
    en2.grid(row=2, column=1, columnspan=2, sticky="ew", pady=3)

    lbl3.grid(row=3, column=0, sticky="w", padx=5)
    en3.grid(row=3, column=1, columnspan=2, sticky="ew", pady=3)

    lbl4.grid(row=4, column=0, sticky="w", padx=5)
    scl.grid(row=4, column=1, columnspan=2, sticky="ew", pady=3)

    check_frame.grid(row=5, column=0, columnspan=3, pady=5)
    chk1.grid(row=0, column=0, padx=10)
    chk3.grid(row=0, column=1, padx=10)

    cbtn.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5,  ipady=4)
    obtn.grid(row=6, column=2, sticky="ew", padx=5, pady=5, ipady=4)
    dbtn.grid(row=7, column=0, columnspan=3, sticky="ew", pady=5, ipady=5)
    ebtn.grid(row=8, column=0, columnspan=3, sticky="ew", pady=5, ipady=5)
    # Make entries and combo expand
    fr.columnconfigure(1, weight=1)
    fr.columnconfigure(2, weight=1)

    # Initialize labels and states
    updateLabel()
    updateCheck()

    root.bind("<Return>", lambda event: logic.logicGetter())
    root.mainloop()
except Exception as e:
    err = msg.showerror("Error", f"An error occurred: {e}")
    if err == "ok":
        root.quit()
#Window Icon made by Freepik from www.flaticon.com