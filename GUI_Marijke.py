#MT - added import:
from write_report import make_pdf # takes list of tuples [(title, fig)]

## Create the main window
    ### NO CHANGES

# FUNCTIONS OF HELP TO OTHER FUNCTIONS
global temp_curr_tuple #temporarily holds (title, fig)

def final_save():
    """ Returns list of saved function with image [(title, fig)]

    """
    global saved_list
    saved_list = [
                ("Function 1", 
                "..\\HTML\\Images\\bp.png"),
                ("Function 2",
                "..\\HTML\\Images\\dp.png"),
                ("Function 3",
                "..\\HTML\\Images\\pc.png")
                ]
    return(saved_list)

## FUNCTIONS OF EXCEL BUTTONS


## FUNCTIONS OF STATISTIC BUTTONS


## FUNCTIONS OF SUPPORT BUTTONS
def act_download():
    """ Downloads PDF report. 

    saved_list -- list of tuples [(title, functions)]
    """
    try:
        a = final_save()
        make_pdf(a)
    except:
        tkinter.messagebox.showinfo("Download report",
                "Unable to download report.")
    

## CREATE BUTTONS CODE


