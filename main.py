#Simple Calculator 
#Tkinter Module Python 
#CodeWithNick
#Part I

#Modules
from tkinter import *

#Screen
wn=Tk()
wn.title("Calculator")
wn.geometry("350x452")
#Entry box 
box = Entry(wn,width=53,borderwidth=5) 
box.grid(row=0,column=0,columnspan=3,padx=10,pady=30)

#Functions
 
#Buttons 
but1=Button(wn,padx=14,pady=14,bd=4,bg='white',text="1",font=("Courier New",16,'bold'))
but2=Button(wn,padx=14,pady=14,bd=4,bg='white',text="2",font=("Courier New",16,'bold'))
but3=Button(wn,padx=14,pady=14,bd=4,bg='white',text="3",font=("Courier New",16,'bold'))
but4=Button(wn,padx=14,pady=14,bd=4,bg='white',text="4",font=("Courier New",16,'bold'))
but5=Button(wn,padx=14,pady=14,bd=4,bg='white',text="5",font=("Courier New",16,'bold'))
but6=Button(wn,padx=14,pady=14,bd=4,bg='white',text="6",font=("Courier New",16,'bold'))
but7=Button(wn,padx=14,pady=14,bd=4,bg='white',text="7",font=("Courier New",16,'bold'))
but8=Button(wn,padx=14,pady=14,bd=4,bg='white',text="8",font=("Courier New",16,'bold'))
but9=Button(wn,padx=14,pady=14,bd=4,bg='white',text="9",font=("Courier New",16,'bold'))
but0=Button(wn,padx=14,pady=14,bd=4,bg='white',text="0",font=("Courier New",16,'bold'))
butdot=Button(wn,padx=47,pady=14,bd=4,bg='white',text=".",font=("Courier New",16,'bold'))
butpl=Button(wn,padx=14,pady=14,bd=4,bg='white',text="+",font=("Courier New",16,'bold'))
butsub=Button(wn,padx=14,pady=14,bd=4,bg='white',text="-",font=("Courier New",16,'bold'))
butml=Button(wn,padx=14,pady=14,bd=4,bg='white',text="*",font=("Courier New",16,'bold'))
butdiv=Button(wn,padx=14,pady=14,bd=4,bg='white',text="/",font=("Courier New",16,'bold'))
butclear=Button(wn,padx=14,pady=119,bd=4,bg='white',text="CE",font=("Courier New",16,'bold'))
butequal=Button(wn,padx=151,pady=14,bd=4,bg='white',text="=",font=("Courier New",16,'bold'))


but1.place(x=10,y=100)
but2.place(x=10,y=170)
but3.place(x=10,y=240)
but4.place(x=75,y=100)
but5.place(x=75,y=170)
but6.place(x=75,y=240)
but7.place(x=140,y=100)
but8.place(x=140,y=170)
but9.place(x=140,y=240)
but0.place(x=10,y=310)
butdot.place(x=75,y=310)
butpl.place(x=205,y=100)
butsub.place(x=205,y=170)
butml.place(x=205,y=240)
butdiv.place(x=205,y=310)
butclear.place(x=270,y=100)
butequal.place(x=10,y=380)
wn.mainloop()
