import tkinter
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
label.grid(row=0, column=1, columnspan=3)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=3)
root.rowconfigure(4, weight=3)
root.rowconfigure(5, weight=3)
root.rowconfigure(6, weight=3)
root.rowconfigure(7, weight=3)
root.rowconfigure(8, weight=3)





root.mainloop()
