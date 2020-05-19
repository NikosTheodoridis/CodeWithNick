#Simple Calculator 
#Tkinter Module Python 
#CodeWithNick

from tkinter import *
import tkinter

#Screen 
wn = Tk()
wn.title("Calculator")
wn.geometry("340x440")
wn.iconbitmap("C:/Users/theod/Downloads/Tutorials/window.ico")

val = ""
A=0

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
#Register the images 
photo_equal = PhotoImage(file = r"C:/Users/theod/Downloads/Tutorials/equal.png")
photo_ce = PhotoImage(file = r"C:/Users/theod/Downloads/Tutorials/CE.png")


data = StringVar()
#Label 
lbl = Label(wn,text="0",anchor=NE,textvariable = data , font = ("Roboto Bold",40),background="white",fg="grey28")
lbl.pack(expand=True,fill ="both")

#Buttons 
but1 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="1",font=("Courier New",16,"bold"),command =but1clicked,border = 0)
but2 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="2",font=("Courier New",16,"bold"),command =but2clicked,border = 0)
but3 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="3",font=("Courier New",16,"bold"),command =but3clicked,border = 0)
but4 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="4",font=("Courier New",16,"bold"),command =but4clicked,border = 0)
but5 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="5",font=("Courier New",16,"bold"),command =but5clicked,border = 0)
but6 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="6",font=("Courier New",16,"bold"),command =but6clicked,border = 0)
but7 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="7",font=("Courier New",16,"bold"),command =but7clicked,border = 0)
but8 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="8",font=("Courier New",16,"bold"),command =but8clicked,border = 0)
but9 = Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="9",font=("Courier New",16,"bold"),command =but9clicked,border = 0)
but0 = Button(wn,padx=79,pady=14,bg="white",fg="grey28",text="0",font=("Courier New",16,"bold"),command =but0clicked,border = 0)
butpl= Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="+",font=("Courier New",16,"bold"),border = 0)
butsub= Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="-",font=("Courier New",16,"bold"),border = 0)
butml= Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="*",font=("Courier New",16,"bold"),border = 0)
butdiv= Button(wn,padx=14,pady=14,bg="white",fg="grey28",text="/",font=("Courier New",16,"bold"),border = 0)
butclear= Button(wn,padx=14,pady=119,bg="white",fg="grey28",image =photo_ce,font=("Courier New",16,"bold"),border = 0)
butequal= Button(wn,padx=151,pady=14,bg="white",fg="grey28",image =photo_equal,font=("Courier New",16,"bold"),border = 0)

#place the buttons 
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
wn.mainloop()
