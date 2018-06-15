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
#import mp3play
import winsound

bgcolor = "white"
fgcolor = "black"
root = Tk()
root.state()
root.configure(background=bgcolor)
#FOR LOGO:
# root.iconbitmap(r"Images\GUIlogo.ico")
# root.iconbitmap(r"Images\LogoIco.ico")

## Create the main window
root.title("SATAlytics")
# root.geometry("800x600")
# width_of_window = 800
# height_of_window = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (screen_width, screen_height))
# x_coordinate = (screen_width/2) - (width_of_window/2) ## Make it pop up at the center of the screen
# y_coordinate = (screen_height/2) - (height_of_window/2)
# root.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))
label = tkinter.Label(root,text="Welcome to SATAlytics")
label.config(font=("Comic", 20), bg=bgcolor, fg=fgcolor)
label.grid(row=0, column=2, columnspan=8)

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

check_excel_1_exist = False

check_excel_2_exist = False

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
    create_global_curr_fig(fig)


imagelist = []
back_next_counter = -1
def list(item):
    global imagelist
    print ("List is reached this time")
    imagelist.append(item)

def listcounter(x):
    global back_next_counter
    print ("The number of listcounter is:",back_next_counter)
    if x == True:
        back_next_counter = back_next_counter - 1
        print (x)
    else:
        back_next_counter = back_next_counter + 1
        print(x)


def create_global_curr_fig(fig):
    """ Creates global of current figure.
    fig -- string, name of figure
    """
    global current_figure
    current_figure = fig

hidecounter = False
def act_hide():
    global hidecounter
    if hidecounter == False:
        hidecounter = True
    else:
        hidecounter = False
    if hidecounter == False:
        buttonHide.config(bg = "blue", text= "Show Client")
    else:
        buttonHide.config(bg = "red", text= "Hide Client")

def act_details():
    img_list = over_threshold(reduced1, reduced2, reduced3, reduced4)
    for img in img_list:
        draw_image(img)
        imagelist.append(img)
        listcounter(False)
    print (imagelist)
    timed_msgbox("Function was executed successfully ({} graphs were drawn)".format(len(img_list)),
            "Created graphs", 1500)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



## FUNCTIONS OF EXCEL BUTTONS
        
def ex1_button():
    global filename ## should be changed
    global excel1
    # global excel1_columns
    global splitfilename11

    filename = askopenfilename() # open selection of files
    splitfilename11 = filename.rsplit('/', 1)
    excel1 = pd.read_excel(filename, sheet_name=0)
    excel1 = drop_rows(excel1)
    if filename:        
        # excel1_columns = excel1.columns.values.tolist()

        ## Button to confirm that the program have the file
        buttonshow1 = Button(root, text=splitfilename11[1], bg="blue")
        buttonshow1.grid(row=1, column=1, sticky="ew")
        print (splitfilename11[1])
        global check_excel_1_exist
        check_excel_1_exist = True
    else:
        print ("File not selected")
    
    ## Some pre-process to the excel1 file. It is connected with help functions
    global excel1_specific_column_uniq_Cliente
    excel1_specific_column_uniq_Cliente = pre_proc(excel1,'Cliente')

    global excel1_specific_column_uniq_Gruppo_prodotto
    excel1_specific_column_uniq_Gruppo_prodotto = pre_proc(excel1,'Gruppo_prodotto')

    global excel1_specific_column_uniq_ANNO
    excel1_specific_column_uniq_ANNO = pre_proc(excel1,'ANNO')


def ex2_button():
    global filename2
    global excel2
    # global excel2_columns
    global splitfilename2

    filename2 = askopenfilename()
    splitfilename2 = filename2.rsplit('/',1)
    excel2 = pd.read_excel(filename2, sheet_name=0)
    excel2.drop(excel2.index[len(excel2) - 1], inplace=True) #drop total row
    # excel2 = drop_rows(excel2)
    if filename2:
        print ("selected: ", filename2)
        buttonshow2 = Button(root, text=splitfilename2[1], bg="blue")
        buttonshow2.grid(row=1, column=3, sticky="ew")
        global check_excel_2_exist
        check_excel_2_exist = True
    else:
        print ("File not selected")

## FUNCTIONS OF STATISTIC BUTTONS
### actions for button 1
def act_button1():
    global most_recent_function
    most_recent_function = 1

    if check_excel_1_exist == True:
        lb11 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb11.grid(row=2, column=1, sticky="nsew")
        ## Adding scrollbar for lb71
        scroll_fun(lb11)

        for i in excel1_specific_column_uniq_Cliente:
            lb11.insert(END, i)

        def cur_selection11(*x):
            global value11
            value11 = (lb11.get(lb11.curselection()))

        lb11.bind("<<ListboxSelect>>", cur_selection11)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)

def act_button2():
    global most_recent_function
    most_recent_function = 2
    print (check_excel_2_exist)
    print (check_excel_1_exist)
    if check_excel_1_exist == True and check_excel_2_exist == True:

        lb21 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb21.grid(row=3, column=1, sticky="nsew")
        ## Adding scrollbar for lb81
        scroll_fun(lb81)

        for i in excel1_specific_column_uniq_ANNO:
            lb21.insert(END, i)

        def cur_selection21(*x):
            global value21
            value21 = (lb21.get(lb21.curselection()))

        lb21.bind("<<ListboxSelect>>", cur_selection21)
    elif check_excel_2_exist == False and check_excel_1_exist == False:
        timed_msgbox("Both excel files are missing", top_title="ERROR", duration=1500)
    elif check_excel_1_exist == False and check_excel_2_exist == True:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)
    else:
        timed_msgbox("Excel file 2 is missing", top_title="ERROR", duration=1500)
        winsound.Beep("")

def act_button3():    
    """ Shows listboxes for client, product and year 
    to select from for function 1.  
    """   
    global most_recent_function
    most_recent_function = 3

    if check_excel_1_exist == True:
        lb31 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb31.grid(row=4, column=1, sticky="nsew")
        # Adding scrollbar for lb31
        scroll_fun(lb31)
        # Put the data into the listbox
        for i in excel1_specific_column_uniq_Cliente:
            lb31.insert(END, i)

        def cur_selection31(*x):
            global value31
            value31 = (lb31.get(lb31.curselection()))

            act_lb32()
        lb31.bind("<<ListboxSelect>>", cur_selection31)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)

def act_lb12():
    """ Changes selection for Listbox 2 of function 1.

    """ 
    lb32 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb32.grid(row=4, column=2, sticky="nsew")
    ## Adding scrollbar for lb32
    scroll_fun(lb32)

    adjusted_excel = excel1.loc[excel1["Cliente"] == value31]
    unique_gruppo_prodotto = pre_proc(adjusted_excel, "Gruppo_prodotto")
    for y in unique_gruppo_prodotto:
        lb32.insert(END, y)

    def cur_selection32(*y):
        global value32
        value32 = lb32.get(lb32.curselection())

        act_lb33()
    lb32.bind("<<ListboxSelect>>", cur_selection32)

def act_lb33():
    """ Changes selection for Listbox 3 of function 1.
    """    
    lb33 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb33.grid(row=4, column=3, sticky="nsew")
    # ## Adding scrollbar for lb33
    # scroll_fun(lb33)
    adjusted_excel = excel1.loc[(excel1["Cliente"] == value31) & (excel1["Gruppo_prodotto"] == value32)]
    unique_anno = pre_proc(adjusted_excel, "ANNO")
    for z in excel1_specific_column_uniq_ANNO:
        lb33.insert(END, z)
    lb33.insert(END, "all")

    def cur_selection33(*z):
        global value33
        value33 = (lb33.get(lb33.curselection()))

    lb33.bind("<<ListboxSelect>>", cur_selection33)

def act_button4():
    global most_recent_function
    most_recent_function = 4

    if check_excel_1_exist == True:
        lb41 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb41.grid(row=5, column=1, sticky="nsew")
        ## Adding scrollbar for lb51
        scroll_fun(lb41)

        for i in excel1_specific_column_uniq_ANNO:
            lb41.insert(END, i)

        def cur_selection41(*x):
            global value41
            value41 = (lb41.get(lb41.curselection()))

        lb41.bind("<<ListboxSelect>>", cur_selection41)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)
    
def act_button5():
    """ Shows listboxes for product, compound and year 
    to select from for function 2.  
    """
    global most_recent_function
    most_recent_function = 5

    if check_excel_1_exist == True:
    # create Listbox
        lb51 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb51.grid(row=6, column=1, sticky="nsew")
        ## Adding scrollbar for lb21
        scroll_fun(lb51)

        for i in excel1_specific_column_uniq_Gruppo_prodotto:
            lb51.insert(END, i)

        def cur_selection51(*x):
            # global selected_value51
            global value51
            value51 = lb51.get(lb51.curselection())
            # selected_value51 = True

            act_lb52()
        lb51.bind("<<ListboxSelect>>", cur_selection51)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)



def act_lb52():
    """ Changes selection for Listbox 2 of function 5.
    """ 
    # create Listbox 
    lb52 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb52.grid(row=6, column=2, sticky="nsew")
    ## Adding scrollbar for lb52
    scroll_fun(lb52)

    adjusted_excel = excel1.loc[excel1["Gruppo_prodotto"] == value51]
    unique_prova = pre_proc(adjusted_excel, "Prova")
    for y in unique_prova:
        lb52.insert(END, y)

    def cur_selection52(*y):
        global value52
        value52 = lb52.get(lb52.curselection())

        act_lb53()
    lb52.bind("<<ListboxSelect>>", cur_selection52)

def act_lb53():
    """ Changes selection for Listbox 3 of function 5.
    """    
    lb53 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb53.grid(row=6, column=3, sticky="nsew")
    # ## Adding scrollbar for lb53
    # scroll_fun(lb53)

    adjusted_excel = excel1.loc[(excel1["Gruppo_prodotto"] == value51) & (excel1["Prova"] == value52)]
    unique_anno = pre_proc(adjusted_excel, "ANNO")
    for z in unique_anno:
        lb53.insert(END, z)
    lb53.insert(END, "all")

    def cur_selection53(*z):
        global value53
        value53 = (lb53.get(lb53.curselection()))
    lb53.bind("<<ListboxSelect>>", cur_selection53)

def act_button6():
    global most_recent_function
    most_recent_function = 6

    if check_excel_1_exist == True:
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
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)


def act_button7():
    """ Shows listboxes for product, client and year 
    to select from for function 3.  
    """
    global most_recent_function
    most_recent_function = 7

    if check_excel_1_exist == True:
        lb71 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb71.grid(row=8, column=1, sticky="nsew")
        ## Adding scrollbar for lb31
        scroll_fun(lb71)

        for i in excel1_specific_column_uniq_Gruppo_prodotto:
            lb71.insert(END, i)
        a = lb71.curselection()

        def cur_selection71(*x):
            global value71
            value71 = (lb71.get(lb71.curselection()))

            act_lb72()
        lb71.bind("<<ListboxSelect>>", cur_selection71)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)


def act_lb72():
    """ Changes selection for Listbox 2 of function 7.

    """    
    lb72 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb72.grid(row=8, column=2, sticky="nsew")
    ## Adding scrollbar for lb72
    scroll_fun(lb72)

    adjusted_excel = excel1.loc[excel1["Gruppo_prodotto"] == value71]
    unique_cliente = pre_proc(adjusted_excel, "Cliente")
    for y in unique_cliente:
        lb72.insert(END, y)

    def cur_selection72(*y):
        global value72
        value72 = lb72.get(lb72.curselection())

        act_lb73()
    lb72.bind("<<ListboxSelect>>", cur_selection72)

def act_lb73():
    """ Changes selection for Listbox 3 of function 7.

    """        
    lb73 = Listbox(root, selectmode=SINGLE, exportselection=0)
    lb73.grid(row=8, column=3, sticky="nsew")
    # ## Adding scrollbar for lb73
    # scroll_fun(lb73)
    
    adjusted_excel = excel1.loc[(excel1["Gruppo_prodotto"] == value71) & (excel1["Cliente"] == value72)]
    unique_prova = pre_proc(adjusted_excel, "Prova")
    for z in unique_prova:
        lb73.insert(END, z)

    def cur_selection73(*z):
        global value73
        value73 = (lb73.get(lb73.curselection()))
    lb73.bind("<<ListboxSelect>>", cur_selection73)    

def act_button8():
    global most_recent_function
    most_recent_function = 8

    if check_excel_1_exist == True:
        lb81 = Listbox(root, selectmode=SINGLE, exportselection=0)
        lb81.grid(row=9, column=3, sticky="nsew")
        ## Adding scrollbar for lb81
        scroll_fun(lb81)

        for i in excel1_specific_column_uniq_ANNO:
            lb81.insert(END, i)

        def cur_selection81(*x):
            global value81
            value81 = (lb81.get(lb81.curselection()))

        lb81.bind("<<ListboxSelect>>", cur_selection81)
    else:
        timed_msgbox("Excel file 1 is missing", top_title="ERROR", duration=1500)
        winsound.Beep("")

def act_button9():
    # works but GUI can't close
    # resultfile = pd.read_excel("test_analysis_18.xlsx", sheetname=0) #TEMP!
    # fig = product_type(resultfile,"Function_5" )
    # fig = "cat.png"
    # canvas = Canvas(root)
    # canvas.grid(row=1,column=4,rowspan=9,columnspan=10)
    # img = PhotoImage( file=fig)
    # canvas.create_image(100,100, image=img)
    # list(img)
    # listcounter(False)
    # create_global_curr_fig(fig)
    # winsound.PlaySound("Feeling Happy Sound Effect", winsound.SND_FILENAME)
    # winsound.PlaySound(None, winsound.SND_PURGE)
    pass



    

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
        play = lambda: PlaySound("Error_sound.wmv", SND_FILENAME)
 
    
def act_go():
    # try:
    if most_recent_function == 0:
        tkinter.messagebox.showinfo("Error","Pick a graph first")
    elif most_recent_function == 3:
        img_list = residues_graph(excel1, value31, value32, value33)
    elif most_recent_function == 5:
        img_list = compound_per_client(excel1, compound=value52, crop=value51, date = value53, hide=hidecounter)
    elif  most_recent_function == 7:
        img_list = residues_graph_esp(excel1, client=value72, crop = value71, compound= value73)
    elif most_recent_function == 4:
        img_list = number_of_molecules(excel1, client= value41)
    elif most_recent_function == 6:
        img_list = samples_product_type(excel1, client="all", date=value61, detail=True)
    elif most_recent_function == 1:
        img_list = samples_product_type(excel1, client=value11, date="all", detail=True)
    elif most_recent_function == 2:
        global reduced1
        global reduced2
        global reduced3
        global reduced4
        img_list, reduced1, reduced2, reduced3, reduced4 = threshold_pie(excel1, excel2, date = value81, client="all", detail=True)
        buttonDetails = Button(root, text="Details", bg="blue", command= act_details)
        buttonDetails.grid(row=10, column=7, sticky="ew")
    elif most_recent_function == 8:
        img_list = clients_graph(excel1, date= value81)

    for img in img_list:
        draw_image(img)
        imagelist.append(img)
        listcounter(False)
    print (imagelist)
    timed_msgbox("Function was executed successfully ({} graphs were drawn)".format(len(img_list)),
            "Created graphs", 1500)
    # except:
    #     tkinter.messagebox.showinfo("Error","Pick a function first")


def act_add():
    selection = current_figure.partition(".")[0]

    if not 'saved_list' in globals():
        global saved_list
        saved_list = [(selection, current_figure)]
    else:
        saved_list += [(selection, current_figure)]

    print(saved_list)

    timed_msgbox("\"{}\" is added to the report.".format(selection), "Added figure to report")


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

button1 = Button(root,text="1. Graph on total number of samples \n per product for one client", command=act_button1, bg=bgcolor, fg=fgcolor)
button1.grid(row=2, column=0, sticky="nsew")

button2 = Button(root,text="2. Pie Chart of one crop samples by one client \n categorised into groups based on \n their concetration relative to their threshold", command=act_button2, bg=bgcolor, fg=fgcolor)
button2.grid(row=3, column=0, sticky="nsew")

button3 = Button(root,text="3. Average concetrations of all compounds \n found in one crop from one client \n in a certain span", command=act_button3, bg=bgcolor, fg=fgcolor)
button3.grid(row=4, column=0, sticky="nsew")

button4 = Button(root,text="4. Distribution of a certain compound \n throughout one year \n for one client for one crop ", command = act_button4, bg=bgcolor, fg=fgcolor)
button4.grid(row=5, column=0, sticky="nsew")

button5 = Button(root,text="5. Average concetration of one compound \n found in one crop \n by clients in a certain time span", command=act_button5, bg=bgcolor, fg=fgcolor)
button5.grid(row=6, column=0, sticky="nsew")

button6 = Button(root,text="6. Chart of average number of molecules \n per crop collected by SATA \n per year", command=act_button6, bg=bgcolor, fg=fgcolor) #command= lambda: [f() for f in [selection61, selection62]])
button6.grid(row=7, column=0, sticky="nsew")

button7 = Button(root,text="7. Chart on number of samples per product \n collected by SATA in a certain year", command=act_button7, bg=bgcolor, fg=fgcolor)
button7.grid(row=8, column=0, sticky="nsew")

button8 = Button(root,text="8. Chart on occurence of clients \n exceeding the limit per year", command=act_button8, bg=bgcolor, fg=fgcolor)
button8.grid(row=9, column=0, sticky="nsew")

button9 = Button(root, text="Dummy Button to be removed", command=act_button4, bg=bgcolor, fg=fgcolor)
button9.grid(row=9, column=2, sticky="nsew")

backbutton = Button(root, text= "Previous Screen", command = backbutton, bg=bgcolor, fg=fgcolor)
backbutton.grid(row=10, column=4, sticky="ewsn")

forwardbutton = Button(root, text= "Next Screen", command = forwardbutton, bg=bgcolor, fg=fgcolor)
forwardbutton.grid(row=10, column=5, sticky="ewsn")

addbutton = Button(root, text="Add Item", bg="blue", command=act_add)
addbutton.grid(row=10, column=10, sticky="ewsn")

buttonDownload = Button(root, text="Download Summary", bg="green", command=act_download, fg=fgcolor)
buttonDownload.grid(row=10, column=0, columnspan=2, sticky="nsew")

buttonGo = Button(root, text="GO!", bg="blue", command= act_go, fg=fgcolor)
buttonGo.grid(row=10, column=3, sticky="nsew")

buttonHide = Button(root, text="Show Client", bg="blue", command= act_hide, fg=fgcolor)
buttonHide.grid(row=10, column=8, sticky="ew")

buttonex1 = Button(root, text="Excel file 1", command=ex1_button, bg=bgcolor, fg=fgcolor)
buttonex1.grid(row=1, column=0, sticky="ew")

buttonex2 = Button(root, text="Excel file 2", command=ex2_button, bg=bgcolor, fg=fgcolor)
buttonex2.grid(row=1, column=2, sticky="ew")

textBox=Text(root)
infophoto = PhotoImage( file="infobutton.png")
buttoninfo = Button(root, image=infophoto, height=20, width=20, command=openInstrucktion, bg="blue", fg=fgcolor)
buttoninfo.grid(row=0, column=9, sticky="ew")

# buttonInfo = CustomButton(root, 100, 25, "blue", command=openInstrucktion)
# buttonInfo.grid(row=0, column=9)

canvas = Canvas(root, bg="black")
canvas.grid(row=1,column=4,rowspan=9,columnspan=10 , sticky="nwes")

quit = Button(root, text="Quit", command=_quit, bg=bgcolor, fg=fgcolor)
quit.grid(row=0, column=10, sticky="ew")

root.mainloop()

# 
