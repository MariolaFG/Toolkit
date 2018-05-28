#!/usr/bin/env python3

"""
Module to create a PDF report.
Author: Marijke
"""

import time
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa


def write_header(rep_name, title="SAVI"):
    """ Returns HTML file with header.

    rep_name -- string, name of report
    title -- string, title of report
    """
    template = env.get_template("header.html")
    variables = {"title" : title,
                 "report_name" : rep_name}
    html_out = template.render(variables)
    return(html_out)


def write_statistic(stat_meth, fig, alt_name):
    """ Returns HTML file with statistcal output.

    stat_meth -- string, specifies stastical analysis
    fig -- string ###SHOULD BE CHANGED!
    alt_name -- string, name if image cannot be displayed
    """
    template = env.get_template("stat_meth.html")
    variables = {"statistical_method" : stat_meth,
                 "figure" : fig,
                 "alt_name" : alt_name}
    html_out = template.render(variables)
    return(html_out)


if __name__ == '__main__':
    report_name = "SAVI Analytics Report {}.pdf".format(time.strftime("%Y%m%d")) # .pdf
    
    # get template :
    env = Environment(loader=FileSystemLoader('C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML')) # to local folder
    #env = Environment(loader=FileSystemLoader('.')) #current directory
    # write start of file to template
    html_file = write_header(report_name)
    # write body to template
    html_file += write_statistic("Stastical Method",
                                 "C:\\Users\\marij\\Dropbox\\Wageningen\\ACT\\Toolkit_Work\\Toolkit\\HTML\\test_fig.png",
                                 "Marijke")
    # write end of file to template :
    temp_EOF = env.get_template("EOF.html")
    html_file += temp_EOF.render()
    print(html_file)

    # generate PDF :
    report = open(report_name, "w+b")
    pisa_status = pisa.CreatePDF(html_file, dest=report)
    report.close()
    print(pisa_status.err) #True on succes, False on error

    
