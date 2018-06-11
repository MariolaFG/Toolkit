from function import product_type
from reportlab_report import make_pdf
import sys
import tkinter.messagebox
from tkinter import *
from functools import partial
import numpy as np
import os.path
import pandas as pd


root = Tk()

## Create the main window
root.title("SATAlytics")
root.geometry("800x600")
width_of_window = 800
height_of_window = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2) ## Make it pop up at the center of the screen
y_coordinate = (screen_height/2) - (height_of_window/2)
root.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))
label = tkinter.Label(root,text="Welcome to SATAlytics")
label.config(font=("Comic", 20))
label.grid(row=0, column=3, columnspan=4)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=40)
root.columnconfigure(5, weight=40)
root.columnconfigure(6, weight=40)
root.columnconfigure(7, weight=40)
root.columnconfigure(8, weight=40)
root.columnconfigure(9, weight=40)
root.columnconfigure(10, weight=40)
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


# FUNCTIONS OF HELP TO OTHER FUNCTIONS

def scroll_fun(e): ## Function for adding scrollbars into the listbox
    scrollbar_v = Scrollbar(e, orient= "vertical")
    scrollbar_v.config(command= e.yview)
    scrollbar_v.pack(side= "right", fill="y")
    e.config(yscrollcommand= scrollbar_v.set)

    scrollbar_h = Scrollbar(e, orient = "horizontal")
    scrollbar_h.config(command= e.xview)
    scrollbar_h.pack(side= "bottom", fill= "x")
    e.config(xscrollcommand= scrollbar_h.set)


def pre_proc(excel_file,column_name):  
    """ Returns column with unique values.

    excel_file -- pandas df, dataframe from Excel file
    column_name -- string, name of column
    """
    try:
        specific_column = excel_file[column_name]  # Here we chose the column that we want to choose a value from
        without_nan = specific_column[pd.isna(specific_column) == FALSE] # Here we keep the column without the NaN values
        unique_values = np.unique(without_nan) # Here we keep only the unique values
        return(unique_values)
    except KeyError:
        tkinter.messagebox.showinfo("Missing column", "The column {} is missing.".format(column_name))
        pass
        

imagelist = []
back_next_counter = -1
def list(item):
    global imagelist    
    imagelist.append(item)

def listcounter(x):
    global back_next_counter
    if x == True:
        back_next_counter = back_next_counter -1
    else:
        back_next_counter = back_next_counter + 1


def create_global_curr_fig(fig):
    """ Creates global of current figure.

    fig -- string, name of figure
    """
    global current_figure
    current_figure = fig


## FUNCTIONS OF EXCEL BUTTONS
        
def ex1_button():
    global filename
    global excel1
    global excel1_columns

    filename = askopenfilename() #Import information file about rice
    splitfilename = filename.rsplit('/',1)
    excel1 = pd.read_excel(filename)
    if filename:        
        excel1_columns = excel1.columns.values.tolist()

        ## Button to confirm that the program have the file
        buttonshow1 = Button(root, text=splitfilename[1], bg="blue")
        buttonshow1.grid(row=1, column=1, sticky="ew")    
    else:
        print ("file not selected")
    
    ## Some pre-process to the excel1 file. It is connected with help functions
    global excel1_specific_column_uniq_Cliente
    excel1_specific_column_uniq_Cliente = pre_proc(excel1,'Cliente')

    global excel1_specific_column_uniq_Gruppo_prodotto
    excel1_specific_column_uniq_Gruppo_prodotto = pre_proc(excel1,'Gruppo_prodotto')

    global excel1_specific_column_uniq_ANNO
    excel1_specific_column_uniq_ANNO = pre_proc(excel1,'ANNO')

    global excel1_specific_column_uniq_Prova
    excel1_specific_column_uniq_Prova = pre_proc(excel1,"Prova")



def ex2_button():
    global filename1
    filename1 = askopenfilename()
    splitfilename1 = filename1.rsplit('/',1)
    if filename1:
        print ("selected:", filename1)
        buttonshow2 = Button(root, text=splitfilename1[1], bg="blue")
        buttonshow2.grid(row=1, column=3, sticky="ew")
    else:
        print ("file not selected")

## FUNCTIONS OF STATISTIC BUTTONS

def act_button1():       
    lb11 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb11.grid(row=2, column=1, sticky="nsew")
    # Adding scrollbar for lb11
    scroll_fun(lb11)
    # Put the data into the listbox
    global value11
    for i in excel1_specific_column_uniq_Cliente:
        lb11.insert(END, i)
    a = lb11.curselection()
    for i in a:
        print(lb11.get(i))
    def cur_selection11(*x):
        global value11
        value11 = (lb11.get(lb11.curselection()))
        print (value11)
    lb11.bind("<<ListboxSelect>>", cur_selection11)

   
    lb12 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb12.grid(row=2, column=2, sticky="nsew")
    ## Adding scrollbar for lb12
    scroll_fun(lb12)
    
    for y in excel1_specific_column_uniq_Gruppo_prodotto:
        lb12.insert(END, y)
    b = lb12.curselection()
    for y in a:
        print (lb12.get(y))
    def cur_selection12(*y):
        global value12
        value12 = lb12.get(lb12.curselection())
        print (value12)
    lb12.bind("<<ListboxSelect>>", cur_selection12)
    
    lb13 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb13.grid(row=2, column=3, sticky="nsew")
    # ## Adding scrollbar for lb13
    # scroll_fun(lb13)

    for z in excel1_specific_column_uniq_ANNO:
        lb13.insert(END, z)
    b = lb13.curselection()
    for z in a:
        print (lb13.get(z))
    def cur_selection13(*z):
        global value13
        value13 = (lb13.get(lb13.curselection()))
        print (value13)
    lb13.bind("<<ListboxSelect>>", cur_selection13)
    
def act_button2():
    lb21 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb21.grid(row=3, column=1, sticky="nsew")
    ## Adding scrollbar for lb21
    scroll_fun(lb21)

    for i in excel1_specific_column_uniq_Gruppo_prodotto:
        lb21.insert(END, i)
    a = lb21.curselection()
    for i in a:
        print(lb21.get(i))
    def cur_selection21(*x):
        global value21
        value21 = (lb21.get(lb21.curselection()))
        print (value21)
    lb21.bind("<<ListboxSelect>>", cur_selection21)
   
    lb22 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb22.grid(row=3, column=2, sticky="nsew")
    ## Adding scrollbar for lb22
    scroll_fun(lb22)

    for y in excel1_specific_column_uniq_Prova:
        lb22.insert(END, y)
    b = lb22.curselection()
    for y in a:
        print (lb22.get(y))
    def cur_selection22(*y):
        global value22
        value22 = lb22.get(lb22.curselection())
        print (value22)
    lb22.bind("<<ListboxSelect>>", cur_selection22)
    
    lb23 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb23.grid(row=3, column=3, sticky="nsew")
    # ## Adding scrollbar for lb23
    # scroll_fun(lb23)

    for z in excel1_specific_column_uniq_ANNO:
        lb23.insert(END, z)
    b = lb23.curselection()
    for z in a:
        print (lb23.get(z))
    def cur_selection23(*z):
        global value23
        value23 = (lb23.get(lb23.curselection()))
        print (value23)
    lb23.bind("<<ListboxSelect>>", cur_selection23)

    
def act_button3():
    lb31 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb31.grid(row=4, column=1, sticky="nsew")
    ## Adding scrollbar for lb31
    scroll_fun(lb31)

    for i in excel1_specific_column_uniq_Gruppo_prodotto:
        lb31.insert(END, i)
    a = lb31.curselection()
    for i in a:
        print(lb31.get(i))
    def cur_selection31(*x):
        global value31
        value31 = (lb31.get(lb31.curselection()))
        print (value31)
    lb31.bind("<<ListboxSelect>>", cur_selection31)
   
    lb32 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb32.grid(row=4, column=2, sticky="nsew")
    ## Adding scrollbar for lb32
    scroll_fun(lb32)

    for y in excel1_specific_column_uniq_Cliente:
        lb32.insert(END, y)
    b = lb32.curselection()
    for y in a:
        print (lb32.get(y))
    def cur_selection32(*y):
        global value32
        value22 = lb32.get(lb32.curselection())
        print (value32)
    lb32.bind("<<ListboxSelect>>", cur_selection32)
    
    lb33 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb33.grid(row=4, column=3, sticky="nsew")
    # ## Adding scrollbar for lb33
    # scroll_fun(lb33)

    for z in excel1_specific_column_uniq_Prova:
        lb33.insert(END, z)
    b = lb33.curselection()
    for z in a:
        print (lb33.get(z))
    def cur_selection33(*z):
        global value33
        value33 = (lb33.get(lb33.curselection()))
        print (value33)
    lb33.bind("<<ListboxSelect>>", cur_selection33)    

    

def act_button4():
    # works but GUI can't close
    # resultfile = pd.read_excel("test_analysis_18.xlsx", sheetname=0) #TEMP!
    # fig = product_type(resultfile,"Function_5" )
    fig = "cat.png"
    canvas = Canvas(root)
    canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    img = PhotoImage( file=fig)
    canvas.create_image(100,100, image=img)
    list(img)
    listcounter(False)
    create_global_curr_fig(fig)


def act_button5():
    lb51 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb51.grid(row=6, column=1, sticky="nsew")
    ## Adding scrollbar for lb51
    scroll_fun(lb51)

    for i in excel1_specific_column_uniq_ANNO:
        lb51.insert(END, i)
    a = lb51.curselection()
    for i in a:
        print(lb51.get(i))
    def cur_selection51(*x):
        global value51
        value51 = (lb51.get(lb51.curselection()))
        print (value51)
    lb51.bind("<<ListboxSelect>>", cur_selection51)

def act_button6():
    lb61 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb61.grid(row=7, column=1, sticky="nsew")
    ## Adding scrollbar for lb61
    scroll_fun(lb61)

    for i in excel1_specific_column_uniq_ANNO:
        lb61.insert(END, i)
    a = lb61.curselection()
    for i in a:
        print(lb61.get(i))
    def cur_selection61(*x):
        global value61
        value61 = (lb61.get(lb61.curselection()))
        print (value61)
    lb61.bind("<<ListboxSelect>>", cur_selection61)

def act_button7():
    lb71 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb71.grid(row=8, column=1, sticky="nsew")
    ## Adding scrollbar for lb71
    scroll_fun(lb71)

    for i in excel1_specific_column_uniq_Cliente:
        lb71.insert(END, i)
    a = lb71.curselection()
    for i in a:
        print(lb71.get(i))
    def cur_selection71(*x):
        global value71
        value71 = (lb71.get(lb71.curselection()))
        print (value71)
    lb71.bind("<<ListboxSelect>>", cur_selection71)

def act_button8():
    lb81 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb81.grid(row=9, column=1, sticky="nsew")
    ## Adding scrollbar for lb81
    scroll_fun(lb81)

    for i in excel1_specific_column_uniq_ANNO:
        lb81.insert(END, i)
    a = lb81.curselection()
    for i in a:
        print(lb81.get(i))
    def cur_selection81(*x):
        global value81
        value81 = (lb81.get(lb81.curselection()))
        print (value81)
    lb81.bind("<<ListboxSelect>>", cur_selection81)

def act_button9():
    lb91 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb91.grid(row=9, column=3, sticky="nsew")
    ## Adding scrollbar for lb91
    scroll_fun(lb91)

    for i in excel1_specific_column_uniq_ANNO:
        lb91.insert(END, i)
    a = lb91.curselection()
    for i in a:
        print(lb91.get(i))
    def cur_selection91(*x):
        global value91
        value91 = (lb91.get(lb91.curselection()))
        print (value91)
    lb91.bind("<<ListboxSelect>>", cur_selection91)

    # canvas = Canvas(root)
    # canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    # gif4 = PhotoImage( file="cat1.png")
    # canvas.create_image(100,100, image=gif4)
    # list(gif4)
    # listcounter(False)



    

## FUNCTIONS OF SUPPORT BUTTONS
    
def act_download():
    """ Downloads PDF report. 

    saved_list -- list of tuples [(title, functions)]
    """
    try:
        make_pdf(saved_list)
    except:
        tkinter.messagebox.showinfo("Download report",
                "Unable to download report.")
    
def act_go():
    tkinter.messagebox.showinfo("GO!", "Your selection is: {}".format(value61))
    
    
def act_add():
    selection = current_figure.partition(".")[0]

    if not 'saved_list' in globals():
        global saved_list
        saved_list = [(selection, current_figure)]
        #"{}".format(current_figure)
    else:
        saved_list += [(selection, current_figure)]

    print(saved_list)

    tkinter.messagebox.showinfo("Add figure to report", 
        "\"{}\" is added to the report.".format(selection))


def backbutton():
    if back_next_counter >= 1:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[back_next_counter - 1])
        listcounter(True)
    else:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[back_next_counter])
        tkinter.messagebox.showinfo("ERROR","No more graphs")
    
def forwardbutton():
    try:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[back_next_counter + 1])
        listcounter(False)
    except IndexError:
        canvas = Canvas(root)
        canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
        canvas.create_image(100,100, image=imagelist[back_next_counter])
        tkinter.messagebox.showinfo("ERROR","No more graphs")
        pass

def openInstrucktion():
    os.startfile("Instructions.pdf")




## CREATE BUTTONS CODE

button1 = Button(root,text="1. Graph on average amount of residues \n per client for a single crop \n in a certain time span", command=act_button1)
button1.grid(row=2, column=0, sticky="nsew")

button2 = Button(root,text="2. Graph on average amount of a certain compound \n per crop per year \n for all clients", command=act_button2)
button2.grid(row=3, column=0, sticky="nsew")

button3 = Button(root,text="4. Distribution of a certain compound \n throughout one year \n for one client for one crop ", command=act_button3)
button3.grid(row=4, column=0, sticky="nsew")

button4 = Button(root,text="", command=act_button4)
button4.grid(row=5, column=0, sticky="nsew")

button5 = Button(root,text="5. Chart of average number of molecules \n per crop collected by SATA \n per year", command=act_button5)
button5.grid(row=6, column=0, sticky="nsew")

button6 = Button(root,text="3. Chart on number of samples per product \n collected by SATA in a certain year", command=act_button6) #command= lambda: [f() for f in [selection61, selection62]])
button6.grid(row=7, column=0, sticky="nsew")

button7 = Button(root,text="6. Graph on total number of samples \n per product for one client", command=act_button7)
button7.grid(row=8, column=0, sticky="nsew")

button8 = Button(root,text="7. Chart on percentage of samples \n that exceeds the limit in one year", command=act_button8)
button8.grid(row=9, column=0, sticky="nsew")

button9 = Button(root, text="8. Chart on clients \n always-sometimes-never \n exceeding the limit per year", command=act_button9)
button9.grid(row=9, column=2, sticky="nsew")

backbutton = Button(root, text= "Previous Screen", command = backbutton)
backbutton.grid(row=10, column=4, sticky="ewsn")

forwardbutton = Button(root, text= "Next Screen", command = forwardbutton)
forwardbutton.grid(row=10, column=5, sticky="ewsn")

addbutton = Button(root, text="Add Item", command=act_add)
addbutton.grid(row=10, column=10, sticky="ewsn")

buttonDownload = Button(root, text="Download Summary", bg="green", command=act_download)
buttonDownload.grid(row=10, column=0, columnspan=2, sticky="nsew")

buttonGo = Button(root, text="GO!", bg="blue", command=act_go)
buttonGo.grid(row=10, column=3, sticky="nsew")

buttonex1 = Button(root, text="Excel file 1", command=ex1_button)
buttonex1.grid(row=1, column=0, sticky="ew")

buttonex2 = Button(root, text="Excel file 2", command=ex2_button)
buttonex2.grid(row=1, column=2, sticky="ew")

textBox=Text(root)
infophoto = PhotoImage( file="infobutton.png")
buttoninfo = Button(root, image=infophoto, height=20, width=20, command=openInstrucktion)
buttoninfo.grid(row=0, column=10, sticky="ew")

canvas = Canvas(root, bg="black")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10 , sticky="nwes")


root.mainloop()

# 