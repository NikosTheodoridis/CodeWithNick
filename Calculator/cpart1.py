#Simple Calculator 
#Tkinter Module Python 
#CodeWithNick

import tkinter
from tkinter import *
from tkinter import messagebox

#Screen
wn = Tk()
wn.title("Calculator")
wn.geometry("340x440")
#python.ico type of image
wn.iconbitmap("C:/Users/...")



#Label
lbl = Label(wn,text = "0",anchor = NE,font = ("Roboto Bold", 40),background = "white",fg = "grey28",)
lbl.pack(expand = True, fill = "both")

photo_equal = PhotoImage(file = r"C:/Users/...")
photo_ce = PhotoImage(file = r"C:/Users/...")
#Buttons
but1=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="1",font=("Courier New",16,"bold"),border=0)
but2=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="2",font=("Courier New",16,"bold"),border=0)
but3=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="3",font=("Courier New",16,"bold"),border=0)
but4=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="4",font=("Courier New",16,"bold"),border=0)
but5=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="5",font=("Courier New",16,"bold"),border=0)
but6=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="6",font=("Courier New",16,"bold"),border=0)
but7=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="7",font=("Courier New",16,"bold"),border=0)
but8=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="8",font=("Courier New",16,"bold"),border=0)
but9=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="9",font=("Courier New",16,"bold"),border=0)
but0=Button(wn,padx=79,pady=14,bd=4,bg="white",fg = "grey28",text="0",font=("Courier New",16,"bold"),border=0)
butpl=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="+",font=("Courier New",16,"bold"),border=0)
butsub=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="-",font=("Courier New",16,"bold"),border=0)
butml=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="*",font=("Courier New",16,"bold"),border=0)
butdiv=Button(wn,padx=14,pady=14,bd=4,bg="white",fg = "grey28",text="/",font=("Courier New",16,"bold"),border=0)
butclear=Button(wn,padx=14,pady=119,bd=4,image =photo_ce,text="CE",font=("Courier New",16,"bold"),border=0)
butequal=Button(wn,padx=151,pady=14,bd=4,image = photo_equal,text="=",font=("Courier New",16,"bold"),border=0)

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
