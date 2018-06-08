#MT - implementing product_type from function.py in function 5
# resultfile = pd.read_excel("prove_18.xlsx", sheetname=0)

#MT - added import:
from write_report import make_pdf # takes list of tuples [(title, fig)]
from function import product_type

## Create the main window
root.title("SATAlytics")
root.geometry("500x400")
width_of_window = 500
height_of_window = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2) ## Make it pop up at the center of the screen
y_coordinate = (screen_height/2) - (height_of_window/2)
root.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))
label = tkinter.Label(root,text="Welcome to SATAlytics")
label.config(font=("Comic", 20))
label.grid(row=0, column=3, columnspan=4)
# so I can also fill the screen with the GUI
# changed name to SATAlytics

# FUNCTIONS OF HELP TO OTHER FUNCTIONS
def create_global_curr_fig(fig):
    """ Creates global of current figure.

    fig -- string, name of figure
    """
    global current_figure
    current_figure = fig

## USE THIS FOR FAKE REPORT
# def final_saved():
#     """ Returns list of saved function with image [fig]

#     """
#     saved_list = []
#     saved_list = [
#                 ("Function 1", 
#                 "..\\HTML\\Images\\bp.png"),
#                 ("Function 2",
#                 "..\\HTML\\Images\\dp.png"),
#                 ("Function 3",
#                 "..\\HTML\\Images\\pc.png")
#                 ]
#     return(saved_list)

## FUNCTIONS OF EXCEL BUTTONS


## FUNCTIONS OF STATISTIC BUTTONS
def act_button5():
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



## FUNCTIONS OF SUPPORT BUTTONS
def act_download():
    """ Downloads PDF report. 

    saved_list -- list of tuples [(title, functions)]
    """
    try:
        # saved_list = final_save() #USE THIS FOR FAKE REPORT
        make_pdf(saved_list)
    except:
        tkinter.messagebox.showinfo("Download report",
                "Unable to download report.")

def act_go():
    tkinter.messagebox.showinfo("Your selection is:", value61 )
    

def act_add():
    selection = current_figure.partition(".")[0]

    if not 'saved_list' in globals():
        global saved_list
        saved_list = [(selection, "..\\{}".format(current_figure))]
    else:
        saved_list += [(selection, "..\\{}".format(current_figure))]

    print(saved_list)

    tkinter.messagebox.showinfo("Add figure to report", 
        "\"{}\" is added to the report.".format(selection))

## CREATE BUTTONS CODE



###############################################
#CHANGED CODE OF FUNCTION.PY
def product_type(resultfile, function):
    """ This function produces a pie chart with the total percentages of 
    compounds.
    No variables needed. Not used.

    function -- string, describes function
    """

    labels = {}
    for element in resultfile["Prova"]:
        if not element in labels.keys():
            labels[element] = 1
        if element in labels.keys():
            prev = labels[element]
            labels[element] = prev + 1
    # labels dictionary structure-> Compound: Amount of times it has been analyzed
    
    sizes = []
    explode = []
    max_labels = heapq.nlargest(10, labels, key=labels.get) # Selects the 10 largest values
    
    # Create pie chart:
    other = 0
    for element in max_labels:
            sizes.append(int((labels[element]/len(labels))*100))
            explode.append(0.1)    
    for element in labels:
        if not element in max_labels:
            other = other + labels[element]
      
    explode.append(0.1)
    sizes.append(other/len(labels)*100)
    explode = tuple(explode) 
    max_labels.append("Other")
    colors = ['lightskyblue', 'lightblue', 'cyan', "coral", "gold",\
              "lightcoral", "lavender", "cyan", "lime", "lightgreen","aquamarine"]
    fig = plt.figure() #MT - changed
    plt.xticks(rotation='vertical')
    plt.pie(np.array(sizes), labels=max_labels, shadow=True, explode=explode, \
            startangle=120, autopct='%1.1f%%', pctdistance=0.8, colors=colors)
    plt.title("Total percentage of Compounds", fontsize= 16)
    # plt.show() - MT - changed
    fig_name = "{}.png".format(function)
    fig.savefig(fig_name) #MT - changed
    fig.close()
    return(fig_name)


###give print statements brackets


if __name__ == '__main__':
    pass