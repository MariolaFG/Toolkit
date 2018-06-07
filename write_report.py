#!/usr/bin/env python3

"""
Module to create a PDF report.
"""

from jinja2 import Environment, FileSystemLoader
import os.path
import time
from xhtml2pdf import pisa


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    

def write_header(rep_name="SATAlytics Report", title="SATAlytics",
                 alt_name="Logo SATAlytics"):
    """ Returns HTML file with header.

    rep_name -- string, name of report, default: SAVI Analytics Report
    title -- string, title of report, default: SAVI
    figure -- string, logo of SAVI, default: #have to find out how
    """
    template = env.get_template("header.html")
    fig_path = "..\\HTML\\Images\\Logo.png" 
    variables = {"title" : title,
                 "report_name" : rep_name,
                 "figure" : fig_path,
                 "alt_name" : alt_name,
                 # "width" : "300",
                 # "height" : "250",
                 "align" : "right",
                 "date" : "{}".format(time.strftime("%B %d, %Y")),
                }
    html_out = template.render(variables)
    return(html_out)
    

def write_toc():
    """ Returns HTML file with table of contents.
    
    """
    template = env.get_template("table_of_contents.html")
    html_out = template.render()
    return(html_out)


    
def write_function(title, fig):
    """ Returns HTML file with statistcal output.

    title -- string, name of function
    fig -- string, path to fig
    """
    template = env.get_template("function.html")
    variables = {"title" : title,
                 "figure" : fig
                 # "text" : txt
                 }
    html_out = template.render(variables)
    return(html_out)


def write_EOF():
    """ Returns HTML file with end of file and footer.

    """
    template = env.get_template("EOF.html")
    html_out = template.render()
    return(html_out)


def write_test():
    """ Returns HTML file with end of file and footer.

    """
    template = env.get_template("interior.html")
    html_out = template.render()
    return(html_out)


# def make_pdf(html_temp, title="SATAlytics Report"):    
def make_pdf(list_of_funct, title="SATAlytics Report"):
    """ Creates a PDF from a HTML template with date of today.

    html_temp -- html, template
    title -- string, title of report, default: SAVI Analytics Report 
    """   
    version = 0
    report_name = "{} {}.pdf".format(title, time.strftime("%Y%m%d"))

    #get unique file names based on version:
    while os.path.isfile(report_name):
        # os.remove(report_name) #figure out better solution
        report_name = "{} {} ({}).pdf".format(title, time.strftime("%Y%m%d"), version)
        version += 1
    
    html_temp = create_temp(list_of_funct)

    # print(html_temp)

    # generate PDF :
    report = open(report_name, "w+b")
    pisa_status = pisa.CreatePDF(html_temp, dest=report)
    report.close()
    os.startfile(report_name)
    return(pisa_status.err) #True on succes, False on error
    

def create_temp(list_of_funct):
    """ Returns HTML template.
    
    list_of_funct -- list of tuples of strings [(title, fig, alt)]
    """

    create_global_env()

    # write start of file to template
    html_file = write_header()
    html_file += write_toc()
    # write body to template
    for i in range(len(list_of_funct)):
        html_file += write_function(list_of_funct[i][0],
                     list_of_funct[i][1])   

    html_file += write_EOF()

    # html_file = write_test()
    
    return (html_file)


def create_global_env():
    global env
    # env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    env = Environment(
    loader=FileSystemLoader(
    resource_path('HTML'))) # to local folder
    print(resource_path('HTML'))


if __name__ == '__main__':
    func_list = [
                ("Function 1", 
                "..\\HTML\\Images\\bp.png"),
                ("Function 2",
                "..\\HTML\\Images\\dp.png"),
                ("Function 3",
                "..\\HTML\\Images\\pc.png")
                ]

    make_pdf(func_list)
    # make_pdf(create_temp())
    

    
