#!/usr/bin/env python3

"""
Module to create a PDF report.
"""

from jinja2 import Environment, FileSystemLoader
import os.path
import time
from xhtml2pdf import pisa


def write_header(rep_name="SATAlytics Report", title="SATAlytics",
                 alt_name="Logo SATAlytics"):
    """ Returns HTML file with header.

    rep_name -- string, name of report, default: SAVI Analytics Report
    title -- string, title of report, default: SAVI
    figure -- string, logo of SAVI, default: #have to find out how
    """
    # env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    template = env.get_template("header.html")
    fig_path = "C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML\\Images\\Logo.png" #Should be changed
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
    # env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    template = env.get_template("table_of_contents.html")
    html_out = template.render()
    return(html_out)


    
def write_function(title, fig, alt_name):
    """ Returns HTML file with statistcal output.

    title -- string, describes function
    fig -- string ###SHOULD BE CHANGED!
    alt_name -- string, name if image cannot be displayed
    txt -- string, text describing figure
    """
    # env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    template = env.get_template("function.html")
    variables = {"title" : title,
                 "figure" : fig,
                 "alt_name" : alt_name
                 # "text" : txt
                 }
    html_out = template.render(variables)
    return(html_out)


def make_pdf(html_temp, title="SATAlytics Report"):
    """ Creates a PDF from a HTML template with date of today.

    html_temp -- html, template
    title -- string, title of report, default: SAVI Analytics Report 
    """   
    report_name = "{} {}.pdf".format(title, time.strftime("%Y%m%d"))

    env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    #env = Environment(loader=FileSystemLoader('.')) #current directory
    if os.path.isfile(report_name):
        os.remove(report_name) #figure out better solution
    ## this would be better: 
    #os.path.exists(file_path)
    ## have to know file path
    
    # write end of file to template :
    temp_EOF = env.get_template("EOF.html")
    html_temp += temp_EOF.render()
    # print(html_file)

    # generate PDF :
    report = open(report_name, "w+b")
    pisa_status = pisa.CreatePDF(html_temp, dest=report)
    report.close()
    print(pisa_status.err) #True on succes, False on error
    os.startfile(report_name)


##def write_to_template(var1, var2, var3)
##    """ Returns HTML file of header, statistical method with figure
##
##    var1 -- string, variable 1
##    var2 -- string, variable 2
##    var3 -- string, variable 3
##    """
##    #use case ... if ...


def create_global_env():
    global env
    env = env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    


if __name__ == '__main__':
    create_global_env()

    # write start of file to template
    html_file = write_header()
    # html_file += write_toc()
    # write body to template
    html_file += write_function("Function 1",
                                 "C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML\\Images\\test_fig.png",
                                 "Marijke")
    html_file += write_function("Function 2",
                                 "C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML\\Images\\test_fig.png",
                                 "Marijke")
    
    make_pdf(html_file)
    

    
