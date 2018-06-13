from updated_function import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.backends.tkagg as tkagg
import numpy as np
import os.path
import pandas as pd
import PIL.Image
import PIL.ImageTk
from reportlab_report import make_pdf
import sys
import tkinter.messagebox
from functools import partial
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


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

global most_recent_function
most_recent_function = 0

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
        tkinter.messagebox.showinfo("Missing column", "The column \"{}\" is missing.".format(column_name))

 
def timed_msgbox(msg, top_title="Results", duration=1000):
    """ Display messagebox that closes after specified time.
    
    msg -- string, message to display
    top_title -- string, title of msgbox -default: "Results"
    duration -- integer, number of milliseconds -default: 1000
    """        
    top = Toplevel()
    top.title(top_title)
    Message(top, text=msg, padx=20, pady=20).pack()
    top.after(duration, top.destroy)
        # # show timed messagebox
        # select_msg = "You selected \"{}\".".format(value21)
        # timed_msgbox(select_msg)


def draw_image(fig):
    """ Displays image in canvas.

    img -- string, image to display
    """
    # canvas = Canvas(root)
    # canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    img = PIL.Image.open(fig)
    # img = PhotoImage( file=fig)
    img = img.resize((500, 500), PIL.Image.ANTIALIAS)
    resized = PIL.ImageTk.PhotoImage(img)
    label = Label(image=resized)
    label.img = resized
    label.grid(row=1,column=4,rowspan=9,columnspan=10 , sticky="nwes")
    list(fig)
    listcounter(False)
    create_global_curr_fig(fig)
    return(0)




imagelist = []
back_next_counter = -1
def list(item):
    global imagelist    
    imagelist.append(item)

def listcounter(x):
    global back_next_counter
    if x == True:
        back_next_counter = back_next_counter - 1
    else:
        back_next_counter = back_next_counter + 1


def create_global_curr_fig(fig):
    """ Creates global of current figure.

    fig -- string, name of figure
    """
    global current_figure
    current_figure = fig


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



## FUNCTIONS OF EXCEL BUTTONS
        
def ex1_button():
    global filename ## should be changed
    global excel1
    global excel1_columns
    global splitfilename11

    filename = askopenfilename() # open selection of files
    splitfilename11 = filename.rsplit('/', 1)
    excel1 = pd.read_excel(filename)
    if filename:        
        excel1_columns = excel1.columns.values.tolist()

        ## Button to confirm that the program have the file
        buttonshow1 = Button(root, text=splitfilename11[1], bg="blue")
        buttonshow1.grid(row=1, column=1, sticky="ew")
        print (splitfilename11[1])
    else:
        print ("File not selected")
    
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
        print ("File not selected")

## FUNCTIONS OF STATISTIC BUTTONS
### actions for button 1
def act_button1():    
    """ Shows listboxes for client, product and year 
    to select from for function 1.  
    """   
    global most_recent_function
    most_recent_function = 1

    lb11 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb11.grid(row=2, column=1, sticky="nsew")
    # Adding scrollbar for lb11
    scroll_fun(lb11)
    # Put the data into the listbox
    for i in excel1_specific_column_uniq_Cliente:
        lb11.insert(END, i)

    def cur_selection11(*x):
        global value11
        value11 = (lb11.get(lb11.curselection()))

        act_lb12()
    lb11.bind("<<ListboxSelect>>", cur_selection11)

def act_lb12():
    """ Changes selection for Listbox 2 of function 1.

    """ 
    lb12 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb12.grid(row=2, column=2, sticky="nsew")
    ## Adding scrollbar for lb12
    scroll_fun(lb12)

    adjusted_excel = excel1.loc[excel1["Cliente"] == value11]
    unique_gruppo_prodotto = pre_proc(adjusted_excel, "Gruppo_prodotto")
    for y in unique_gruppo_prodotto:
        lb12.insert(END, y)

    def cur_selection12(*y):
        global value12
        value12 = lb12.get(lb12.curselection())

        act_lb13()
    lb12.bind("<<ListboxSelect>>", cur_selection12)

def act_lb13():
    """ Changes selection for Listbox 3 of function 1.
    """    
    lb13 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb13.grid(row=2, column=3, sticky="nsew")
    # ## Adding scrollbar for lb13
    # scroll_fun(lb13)
    adjusted_excel = excel1.loc[(excel1["Cliente"] == value11) & (excel1["Gruppo_prodotto"] == value12)]
    unique_anno = pre_proc(adjusted_excel, "ANNO")
    for z in excel1_specific_column_uniq_ANNO:
        lb13.insert(END, z)

    def cur_selection13(*z):
        global value13
        value13 = (lb13.get(lb13.curselection()))

    lb13.bind("<<ListboxSelect>>", cur_selection13)
###
    
### actions for button 2    
def act_button2():
    """ Shows listboxes for product, compound and year 
    to select from for function 2.  
    """
    global most_recent_function
    most_recent_function = 2

    # create listboxes
    lb21 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb21.grid(row=3, column=1, sticky="nsew")
    ## Adding scrollbar for lb21
    scroll_fun(lb21)

    for i in excel1_specific_column_uniq_Gruppo_prodotto:
        lb21.insert(END, i)

    def cur_selection21(*x):
        # global selected_value21
        global value21
        value21 = lb21.get(lb21.curselection())
        # selected_value21 = True

        act_lb22()
    lb21.bind("<<ListboxSelect>>", cur_selection21)


def act_lb22():
    """ Changes selection for Listbox 2 of function 2.
    """ 
    # create Listbox 
    lb22 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb22.grid(row=3, column=2, sticky="nsew")
    ## Adding scrollbar for lb22
    scroll_fun(lb22)

    # if selected_value21 == False:
    #     for y in excel1_specific_column_uniq_Prova:
    #         lb22.insert(END, y)
    # elif selected_value21 == True:
    adjusted_excel = excel1.loc[excel1["Gruppo_prodotto"] == value21]
    unique_prova = pre_proc(adjusted_excel, "Prova")
    for y in unique_prova:
        lb22.insert(END, y)

    def cur_selection22(*y):
        global value22
        value22 = lb22.get(lb22.curselection())

        act_lb23()
    lb22.bind("<<ListboxSelect>>", cur_selection22)

def act_lb23():
    """ Changes selection for Listbox 3 of function 2.
    """    
    lb23 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb23.grid(row=3, column=3, sticky="nsew")
    # ## Adding scrollbar for lb23
    # scroll_fun(lb23)

    adjusted_excel = excel1.loc[(excel1["Gruppo_prodotto"] == value21) & (excel1["Prova"] == value22)]
    unique_anno = pre_proc(adjusted_excel, "ANNO")
    for z in unique_anno:
        lb23.insert(END, z)

    def cur_selection23(*z):
        global value23
        value23 = (lb23.get(lb23.curselection()))
    lb23.bind("<<ListboxSelect>>", cur_selection23)
###

### actions for button 3    
def act_button3():
    """ Shows listboxes for product, client and year 
    to select from for function 3.  
    """
    global most_recent_function
    most_recent_function = 3
    lb31 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb31.grid(row=4, column=1, sticky="nsew")
    ## Adding scrollbar for lb31
    scroll_fun(lb31)

    for i in excel1_specific_column_uniq_Gruppo_prodotto:
        lb31.insert(END, i)
    a = lb31.curselection()

    def cur_selection31(*x):
        global value31
        value31 = (lb31.get(lb31.curselection()))

        act_lb32()
    lb31.bind("<<ListboxSelect>>", cur_selection31)

def act_lb32():
    """ Changes selection for Listbox 2 of function 3.

    """    
    lb32 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb32.grid(row=4, column=2, sticky="nsew")
    ## Adding scrollbar for lb32
    scroll_fun(lb32)

    adjusted_excel = excel1.loc[excel1["Gruppo_prodotto"] == value31]
    unique_cliente = pre_proc(adjusted_excel, "Cliente")
    for y in unique_cliente:
        lb32.insert(END, y)

    def cur_selection32(*y):
        global value32
        value32 = lb32.get(lb32.curselection())

        act_lb33()
    lb32.bind("<<ListboxSelect>>", cur_selection32)

def act_lb33():
    """ Changes selection for Listbox 3 of function 3.

    """        
    lb33 = Listbox(root, selectmode=EXTENDED, exportselection=0)
    lb33.grid(row=4, column=3, sticky="nsew")
    # ## Adding scrollbar for lb33
    # scroll_fun(lb33)
    
    adjusted_excel = excel1.loc[(excel1["Gruppo_prodotto"] == value31) & (excel1["Cliente"] == value32)]
    unique_prova = pre_proc(adjusted_excel, "Prova")
    for z in unique_prova:
        lb33.insert(END, z)

    def cur_selection33(*z):
        global value33
        value33 = (lb33.get(lb33.curselection()))
    lb33.bind("<<ListboxSelect>>", cur_selection33)    
###
    

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
    global most_recent_function
    most_recent_function = 5
    lb51 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb51.grid(row=6, column=1, sticky="nsew")
    ## Adding scrollbar for lb51
    scroll_fun(lb51)

    for i in excel1_specific_column_uniq_ANNO:
        lb51.insert(END, i)

    def cur_selection51(*x):
        global value51
        value51 = (lb51.get(lb51.curselection()))

    lb51.bind("<<ListboxSelect>>", cur_selection51)


def act_button6():
    global most_recent_function
    most_recent_function = 6
    lb61 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb61.grid(row=7, column=1, sticky="nsew")
    ## Adding scrollbar for lb61
    scroll_fun(lb61)

    for i in excel1_specific_column_uniq_ANNO:
        lb61.insert(END, i)

    def cur_selection61(*x):
        global value61
        value61 = (lb61.get(lb61.curselection()))

    lb61.bind("<<ListboxSelect>>", cur_selection61)


def act_button7():
    global most_recent_function
    most_recent_function = 7
    lb71 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb71.grid(row=8, column=1, sticky="nsew")
    ## Adding scrollbar for lb71
    scroll_fun(lb71)

    for i in excel1_specific_column_uniq_Cliente:
        lb71.insert(END, i)

    def cur_selection71(*x):
        global value71
        value71 = (lb71.get(lb71.curselection()))

    lb71.bind("<<ListboxSelect>>", cur_selection71)


def act_button8():
    global most_recent_function
    most_recent_function = 8
    lb81 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb81.grid(row=9, column=1, sticky="nsew")
    ## Adding scrollbar for lb81
    scroll_fun(lb81)

    for i in excel1_specific_column_uniq_ANNO:
        lb81.insert(END, i)

    def cur_selection81(*x):
        global value81
        value81 = (lb81.get(lb81.curselection()))

    lb81.bind("<<ListboxSelect>>", cur_selection81)


def act_button9():
    global most_recent_function
    most_recent_function = 9
    lb91 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb91.grid(row=9, column=3, sticky="nsew")
    ## Adding scrollbar for lb91
    scroll_fun(lb91)

    for i in excel1_specific_column_uniq_ANNO:
        lb91.insert(END, i)

    def cur_selection91(*x):
        global value91
        value91 = (lb91.get(lb91.curselection()))

    lb91.bind("<<ListboxSelect>>", cur_selection91)


    

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
    # try:
    if most_recent_function == 0:
        tkinter.messagebox.showinfo("Error","Pick a graph first")
    elif most_recent_function == 1:
        # img_list = residues_graph(pd.read_excel(splitfilename11[1], sheet_name=0), value11, value12, value13)
        img_list = residues_graph(excel1, value11, value12)
    elif most_recent_function == 2:
        img_list = compound_per_client(excel1, compound=value22, crop=value21, date = "all", hide=True)
    elif  most_recent_function == 3:
        img_list = residues_graph_esp(excel1, client=value32, crop = value31, compound= value33)
    elif most_recent_function == 5:
        img_list = number_of_molecules(excel1, client= value51)
    elif most_recent_function == 6:
        img_list = samples_product_type(excel1, client="all", date=value61, detail=True)
    elif most_recent_function == 7:
        img_list = samples_product_type(excel1, client=value71, date="all", detail=True)
    elif most_recent_function == 8:
        img_list = threshold_pie(excel1, date = value81, client="all", detail=True)
    elif most_recent_function == 9:
        img_list = clients_graph(excel1, date= value91)

    for img in img_list:
        draw_image(img)
    print (imagelist)
    timed_msgbox("Function was executed successfully ({} graphs were drawn)".format(len(img_list)))
    # except:
    #     tkinter.messagebox.showinfo("Error","Pick a function first")



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
        draw_image(imagelist[back_next_counter - 1])
        listcounter(True)
    else:
        draw_image(imagelist[back_next_counter])
        tkinter.messagebox.showinfo("ERROR","No more graphs")
    
def forwardbutton():
    try:
        draw_image(imagelist[back_next_counter + 1])
        listcounter(False)
    except IndexError:
        draw_image(imagelist[back_next_counter])
        tkinter.messagebox.showinfo("ERROR","No more graphs")

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
buttoninfo.grid(row=0, column=9, sticky="ew")

canvas = Canvas(root, bg="black")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10 , sticky="nwes")

quit = Button(root, text="Quit", command=_quit)
quit.grid(row=0, column=10, sticky="ew")

root.mainloop()

# 
