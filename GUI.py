import tkinter
import tkinter.messagebox
from tkinter import *
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

def helloCallBack():
    tkinter.messagebox.showinfo("Statistic 1","Give us the money")
## Buttons 
button1 = Button(root,text="Statistic 1", command=helloCallBack)
button1.grid(row=2, column=0, sticky="nsew")
entry11 = Entry(root)
entry11.grid(row=2, column=1, sticky="ew")
entry12 = Entry(root)
entry12.grid(row=2, column=2, sticky="ew")

button2 = Button(root,text="Statistic 2")
button2.grid(row=3, column=0, sticky="nsew")
entry21 = Entry(root)
entry21.grid(row=3, column=1, sticky="ew")
entry22 = Entry(root)
entry22.grid(row=3, column=2, sticky="ew")
entry32 = Entry(root)
entry32.grid(row=3, column=3, sticky="ew")

button3 = Button(root,text="Statistic 3")
button3.grid(row=4, column=0, sticky="nsew")
entry31 = Entry(root)
entry31.grid(row=4, column=1, sticky="ew")
entry32 = Entry(root)
entry32.grid(row=4, column=2, sticky="ew")

button4 = Button(root,text="Statistic 4")
button4.grid(row=5, column=0, sticky="nsew")
entry41 = Entry(root)
entry41.grid(row=5, column=1, sticky="ew")
entry42 = Entry(root)
entry42.grid(row=5, column=2, sticky="ew")
entry42 = Entry(root)
entry42.grid(row=5, column=3, sticky="ew")

button5 = Button(root,text="Statistic 5")
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

addbutton = Button(root, text="Add Item")
addbutton.grid(row=10, column=10, sticky="ewsn")

buttonDownload = Button(root, text="Download Summary", bg="green")
buttonDownload.grid(row=10, column=0, columnspan=2, sticky="nsew")

canvas = Canvas(root, bg="red")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10, sticky="nwes")


root.mainloop()
