import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
#command
def tarea():
     length, height = int(my_entry.get()), int(my_entry2.get())
     area = (length * height)/2
     result=tk.Text(root,height=5,width=10,padx=15,pady=15)
     result.insert(1.0,area)
     result.grid(column=1,row=4)
            
def sarea():
    s=int(my_entry.get())
    ar1=int(s*s) 
    #text box
    result=tk.Text(root,height=5,width=10,padx=15,pady=15)
    result.insert(1.0,ar1)
    result.grid(column=1,row=4)
    
    
def carea(): 
    r=int(my_entry.get())
    #r=eval(input("enter the radius"))
    ar2=float(3.14*r*r )      
    #print(ar2)
    #text box
    result=tk.Text(root,height=5,width=10,padx=15,pady=15)
    result.insert(1.0,ar2)
    result.grid(column=1,row=4)

root= tk.Tk()

canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)
#logo
logo=Image.open("logo.jpg")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)
#selecting an option
select= tk.Label(root, text ="Select a shape to find its area",font="Releway")
select.grid(columnspan=3, column=0, row=1)


my_entry=Entry(root)
my_entry.grid(row=2,column=1,padx=20,pady=5)
my_entry2=Entry(root)
my_entry2.grid(row=2,column=2,padx=20,pady=5)
#making buttons
end_text=tk.StringVar()
end_button=tk.Button(root,textvariable=end_text,font="Raleway",bg="#20bebe",fg="white",height=1,width=4,command=root.quit)
end_text.set("End")
end_button.grid(column=2,row=0)

triangle_text=tk.StringVar()
triangle_button=tk.Button(root,textvariable=triangle_text,font="Raleway",bg="#20bebe",fg="white",height=2,width=15,command=tarea)
triangle_text.set("Triangle")
triangle_button.grid(column=0,row=3)

square_text=tk.StringVar()
square_button=tk.Button(root,textvariable=square_text,font="Raleway",bg="#20bebe",fg="white",height=2,width=15,command=sarea)
square_text.set("Square")
square_button.grid(column=1,row=3)

circle_text=tk.StringVar()
circle_button=tk.Button(root,textvariable=circle_text,font="Raleway",bg="#20bebe",fg="white",height=2,width=15,command=carea)
circle_text.set("Circle")
circle_button.grid(column=2,row=3)

canvas=tk.Canvas(root,width=600,height=250)
canvas.grid(columnspan=3)

root.mainloop()
