import tkinter
#import matplotlib, sys
import tkinter.messagebox
from functools import partial
from tkinter import *
#import matplotlib
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
    gif1 = PhotoImage( file="Babis.gif")
    canvas.create_image(100,100, image=gif1)
    canvas.gif1 = gif1
    
def act_button3():
    tkinter.messagebox.showinfo("Statistic 1","BOOM BITCH")
def act_button4():
    tkinter.messagebox.showinfo("Statistic 1","Give us the money SATA snakes")
def act_download():
    tkinter.messagebox.showinfo("Statistic 1","No download for you money-boy")
def act_add():
    tkinter.messagebox.showinfo("Statistic 1","No add for you. I don't like your face")
def act_button5():
    tkinter.messagebox.showinfo("Statistic 1","Give us the money SATAAAAAAAAAA")

##def plot():
##    x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
##    v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
##    p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
##            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
##
##    fig = Figure(figsize=(6,6))
##    a = fig.add_subplot(111)
##    a.scatter(v,x,color='red')
##    a.plot(p, range(2 +max(x)),color='blue')
##    a.invert_yaxis()
##
##    a.set_title ("Estimation Grid", fontsize=16)
##    a.set_ylabel("Y", fontsize=14)
##    a.set_xlabel("X", fontsize=14)
##
##    canvas = FigureCanvasTkAgg(root)
##    canvas.get_tk_widget().pack()
##    canvas.draw()


## Buttons 
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

backbutton = Button(root, text= "Previous Screen")
backbutton.grid(row=10, column=4, sticky="ewsn")

forwardbutton = Button(root, text= "Next Screen")
forwardbutton.grid(row=10, column=5, sticky="ewsn")

addbutton = Button(root, text="Add Item", command=act_add)
addbutton.grid(row=10, column=10, sticky="ewsn")

buttonDownload = Button(root, text="Download Summary", bg="green", command=act_download)
buttonDownload.grid(row=10, column=0, columnspan=2, sticky="nsew")

canvas = Canvas(root, bg="white")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10, sticky="nwes")



root.mainloop()
