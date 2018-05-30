import tkinter
import sys
import tkinter.messagebox
from functools import partial
from tkinter import *
#import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
#import numpy as np
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.figure import Figure




root = Tk()

## Create the main window
root.title("Savi Analytics")
root.geometry("1000x800")
width_of_window = 1000
height_of_window = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2) ## Make it pop up at the center of the screen
y_coordinate = (screen_height/2) - (height_of_window/2)
root.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))



label = tkinter.Label(root,text="Welcome to SAVI Analytics")
label.grid(row=0, column=3, columnspan=4)

root.columnconfigure(0, weight=20)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=20)
root.columnconfigure(4, weight=20)
root.columnconfigure(5, weight=20)
root.columnconfigure(6, weight=20)
root.columnconfigure(7, weight=20)
root.columnconfigure(8, weight=20)
root.columnconfigure(9, weight=20)
root.columnconfigure(10, weight=20)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)
root.rowconfigure(10, weight=1)

## Functions 

# List to go next and previous 
imagelist = []
i = -1
def list(item):
    global imagelist    
    imagelist.append(item)

def listcounter(x):
    global i
    if x == True:
        i = i -1

    else:
        i = i + 1
    
## Create the main button functions 
def act_button1():
    try:
        a = int(entry11.get())
        b = int(entry12.get())
        c = a+b
        tkinter.messagebox.showinfo("Your value is:",c)
    except ValueError:
        tkinter.messagebox.showinfo("ERROR","Not numbers in the correct place. Try again idiot")
        pass
def act_button2():
    #novi = Toplevel()
    canvas = Canvas(root)
    canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    gif1 = PhotoImage( file="dog1.gif")
    canvas.create_image(100,100, image=gif1)
    list(gif1)
    listcounter(False)

    
def act_button3():
    canvas = Canvas(root)
    canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    gif2 = PhotoImage( file="dog2.gif")
    canvas.create_image(100,100, image=gif2)
#    canvas.gif2 = gif2
    list(gif2)
    listcounter(False)
    
def act_button4():
    canvas = Canvas(root)
    canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    gif3 = PhotoImage( file="cat.png")
    canvas.create_image(100,100, image=gif3)
    list(gif3)
    listcounter(False)

def act_button5():
    canvas = Canvas(root)
    canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    gif4 = PhotoImage( file="cat1.png")
    canvas.create_image(100,100, image=gif4)
    list(gif4)
    listcounter(False)
    
def act_download():
    tkinter.messagebox.showinfo("Statistic 1","No download for you money-boy")
def act_add():
    tkinter.messagebox.showinfo("Statistic 1","No add for you. I don't like your face")

def backbutton():
    if i >= 1:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[i - 1])
        listcounter(True)
    else:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[i])
        tkinter.messagebox.showinfo("ERROR","No more graphs")
    
def forwardbutton():
    try:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[i + 1])
        listcounter(False)
    except IndexError:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[i])
        tkinter.messagebox.showinfo("ERROR","No more graphs")
        pass

    
##Create the Buttons 
button1 = Button(root,text="Calculation", command=act_button1)
button1.grid(row=2, column=0, sticky="nsew")
entry11 = Entry(root)
entry11.grid(row=2, column=1, sticky="ew")
entry12 = Entry(root)
entry12.grid(row=2, column=2, sticky="ew")

button2 = Button(root,text="DOG", command=act_button2)
button2.grid(row=3, column=0, sticky="nsew")
entry21 = Entry(root)
entry21.grid(row=3, column=1, sticky="ew")
entry22 = Entry(root)
entry22.grid(row=3, column=2, sticky="ew")
entry32 = Entry(root)
entry32.grid(row=3, column=3, sticky="ew")

button3 = Button(root,text="Statistic 3", command=act_button3)
button3.grid(row=4, column=0, sticky="nsew")
entry31 = Entry(root)
entry31.grid(row=4, column=1, sticky="ew")
entry32 = Entry(root)
entry32.grid(row=4, column=2, sticky="ew")

button4 = Button(root,text="Statistic 4", command=act_button4)
button4.grid(row=5, column=0, sticky="nsew")
entry41 = Entry(root)
entry41.grid(row=5, column=1, sticky="ew")
entry42 = Entry(root)
entry42.grid(row=5, column=2, sticky="ew")
entry42 = Entry(root)
entry42.grid(row=5, column=3, sticky="ew")

button5 = Button(root,text="Statistic 5", command=act_button5)
button5.grid(row=6, column=0, sticky="nsew")
entry51 = Entry(root)
entry51.grid(row=6, column=1, sticky="ew")
entry52 = Entry(root)
entry52.grid(row=6, column=2, sticky="ew")


button6 = Button(root,text="Statistic 6")
button6.grid(row=7, column=0, sticky="nsew")
entry61 = Entry(root)
entry61.grid(row=7, column=1, sticky="ew")
entry62 = Entry(root)
entry62.grid(row=7, column=2, sticky="ew")
entry62 = Entry(root)
entry62.grid(row=7, column=3, sticky="ew")

button7 = Button(root,text="Statistic 7")
button7.grid(row=8, column=0, sticky="nsew")
entry71 = Entry(root)
entry71.grid(row=8, column=1, sticky="ew")
entry72 = Entry(root)
entry72.grid(row=8, column=2, sticky="ew")

button8 = Button(root,text="Statistic 8")
button8.grid(row=9, column=0, sticky="nsew")
entry81 = Entry(root)
entry81.grid(row=9, column=1, sticky="ew")
entry82 = Entry(root)
entry82.grid(row=9, column=2, sticky="ew")
entry82 = Entry(root)
entry82.grid(row=9, column=3, sticky="ew")

backbutton = Button(root, text= "Previous Screen", command = backbutton)
backbutton.grid(row=10, column=4, sticky="ewsn")

forwardbutton = Button(root, text= "Next Screen", command = forwardbutton)
forwardbutton.grid(row=10, column=5, sticky="ewsn")

addbutton = Button(root, text="Add Item", command=act_add)
addbutton.grid(row=10, column=10, sticky="ewsn")

buttonDownload = Button(root, text="Download Summary", bg="green", command=act_download)
buttonDownload.grid(row=10, column=0, columnspan=2, sticky="nsew")

canvas = Canvas(root, bg="black")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10, sticky="nwes")



root.mainloop()
