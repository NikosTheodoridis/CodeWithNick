#Simple Calculator 
#Tkinter Module Python 
#CodeWithNick
#Modules
import tkinter
from tkinter import *
from tkinter import messagebox


#Screen
wn = Tk()
wn.title("Calculator")
wn.geometry("340x440")
#python.ico type of image
wn.iconbitmap("C:/Users/...")

val = ""
A=0
operator = ""

#Functions 
def but1clicked():
    global val
    val = val + "1"
    data.set(val)
def but2clicked():
    global val
    val = val + "2"
    data.set(val)
def but3clicked():
    global val
    val = val + "3"
    data.set(val)
def but4clicked():
    global val
    val = val + "4"
    data.set(val)
def but5clicked():
    global val
    val = val + "5"
    data.set(val)
def but6clicked():
    global val
    val = val + "6"
    data.set(val)
def but7clicked():
    global val
    val = val + "7"
    data.set(val)
def but8clicked():
    global val
    val = val + "8"
    data.set(val)
def but9clicked():
    global val
    val = val + "9"
    data.set(val)
def but0clicked():
    global val
    val = val + "0"
    data.set(val)


def btn_plus_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
def btn_minus_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
def btn_mult_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)
def btn_div_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)


data = StringVar()

#Label
lbl = Label(wn,text = "0",anchor = NE,font = ("Roboto Bold", 40),textvariable = data,background = "white",fg = "grey28",)
lbl.pack(expand = True, fill = "both")

photo_equal = PhotoImage(file = r"C:/Users/...")
photo_ce = PhotoImage(file = r"C:/Users/...")
#Buttons
but1=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="1",font=("Courier New",16,"bold"),border=0,command =but1clicked)
but2=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="2",font=("Courier New",16,"bold"),border=0,command =but2clicked)
but3=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="3",font=("Courier New",16,"bold"),border=0,command =but3clicked)
but4=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="4",font=("Courier New",16,"bold"),border=0,command =but4clicked)
but5=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="5",font=("Courier New",16,"bold"),border=0,command =but5clicked)
but6=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="6",font=("Courier New",16,"bold"),border=0,command =but6clicked)
but7=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="7",font=("Courier New",16,"bold"),border=0,command =but7clicked)
but8=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="8",font=("Courier New",16,"bold"),border=0,command =but8clicked)
but9=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="9",font=("Courier New",16,"bold"),border=0,command =but9clicked)
but0=Button(wn,padx=79,pady=14,bd=4,bg="white",fg = "grey28",text="0",font=("Courier New",16,"bold"),border=0,command =but0clicked)
butpl=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="+",font=("Courier New",16,"bold"),border=0,command=btn_plus_clicked)
butsub=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="-",font=("Courier New",16,"bold"),border=0,command=btn_minus_clicked)
butml=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="*",font=("Courier New",16,"bold"),border=0,command=btn_mult_clicked)
butdiv=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="/",font=("Courier New",16,"bold"),border=0,command=btn_div_clicked)
butclear=Button(wn,padx=14,pady=119,bd=4,image =photo_ce,text="CE",font=("Courier New",16,"bold"),border=0,command=btn_c_pressed)
butequal=Button(wn,padx=151,pady=14,bd=4,image = photo_equal,text="=",font=("Courier New",16,"bold"),border=0,command=result)

but1.place(x=10,y=240)  
but2.place(x=75,y=240)  
but3.place(x=140,y=240)  
but4.place(x=10,y=170)  
but5.place(x=75,y=170)  
but6.place(x=140,y=170)  
but7.place(x=10,y=100) 
but8.place(x=75,y=100) 
but9.place(x=140,y=100) 

but0.place(x=10,y=310)
butpl.place(x=205,y=100)
butsub.place(x=205,y=170)
butml.place(x=205,y=240)
butdiv.place(x=205,y=310)
butclear.place(x=270,y=100)
butequal.place(x=10,y=380)
#####
wn.mainloop()
