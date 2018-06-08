#!/usr/bin/env python2

"""
Module to create a PDF report with ReportLab.
"""

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
# from reportlab.pdfbase.ttfonts import TTFont  # other fonts
import os.path
import time

####### PRACTICE ######################
# def hello(c):
#     c.drawString(0,0, "0, 0")
#     c.drawString(100, 100, "100, 100")
#     c.drawString(100, 200, "100, 200")
#     c.drawString(100, 300, "100, 300")
#     c.drawString(100, 400, "100, 400")
#     c.drawString(100, 500, "100, 500")
#     c.drawString(100, 600, "100, 600")
#     c.drawString(100, 700, "100, 700")
#     c.drawString(100, 800, "100, 800")
#     c.drawString(100, 900, "100, 900")
#     c.drawString(200, 100, "200, 100")
#     c.drawString(300, 100, "300, 100")
#     c.drawString(400, 100, "400, 100")
#     c.drawString(500, 100, "500, 100")
#     c.drawString(550, 100, "550, 100")
#     c.drawString(600, 100, "600, 100")

# if __name__ == '__main__':

#     c = canvas.Canvas("hello.pdf")
#     hello(c)
#     c.showPage()    # to stop drawing in current page
#     c.save()        # to save page


# ####### OWN STUFF ####################
########## COLORS FROM LOGO ##########
# divide by 256
# (70, 165, 66) - green
# (31, 79, 116) - blue

def make_pdf(saved_list, title="SATAlytics Report"):
    """ Creates a PDF from a HTML template with date of today.

    saved_list -- list of tuples (strings), saved images from GUI (title, fig)
    title -- string, title of report, default: SAVI Analytics Report 
    """   

    # give unique report name:
    version = 0
    report_name = "{} {}.pdf".format(title, time.strftime("%Y%m%d"))
    while os.path.isfile(report_name):
        version += 1
        report_name = "{} {} ({}).pdf".format(title, time.strftime("%Y%m%d"), version)

    c = canvas.Canvas(report_name)
    # c.setAuthor() #how does this work?
    c.setTitle(title)
    title_page(c)
    c.showPage()
    toc_page(c, saved_list)
    c.showPage()
    for i in range(len(saved_list)):
        regular_page(c, saved_list[i][0], saved_list[i][1])
        c.showPage()
    c.save()
    os.startfile(report_name)


def title_page(c, logo="HTML\\Images\\Logo.png"):
    """ Creates title page. 

    c -- canvas
    logo -- string, path to logo - default: "HTML\\Images\\Logo.png"
    """

    # code for title page
    ## HERE ##
    # code for image
    c.drawImage(logo, 60, 580, width=525, height=187.5, mask=None)

    # code for colored block:
    # c.setStrokeColorRGB(0.4, 0.5, 0.3)
    # c.setFillColorRGB(0.4, 0.5, 0.3) #lighter darkgreen)   
    # c.rect(0, 0, 600, 300, stroke=1, fill=1)

    # code colored band with text:
    c.setFillColorRGB(70/256, 165/256, 66/256)  
    c.rect(0, 300, 600, 100, stroke=0, fill=1)
    c.setFont("Times-BoldItalic", 40, leading=None)
    c.setFillGray(1.0) # white text
    c.drawString(50, 335, "SATAlytics Report")


def toc_page(c, saved_list):
    """ Creates table of contents page. 

    saved_list -- list of tuples (strings), (title, fig)
    c -- canvas
    """
    styles = getSampleStyleSheet()
    info = []
    # styles["ToC_info"] = ParagraphStyle("Normal", 
    #     parent=styles["Normal"],
    #     fontSize=12,
    #     fontName="Times-Roman")

    INFO_TXT = "This report was generated by SATAlytics on {}. The software tool SATAlytics summarizes, analyzes and visualizes chemical analysis data.".format(time.strftime("%B %d, %Y"))

    # display title of page
    c.setFont("Helvetica-Bold", 20, leading=None)
    c.drawCentredString(325, 750, "Table of Contents")

    # display table of contents
    c.setFont("Helvetica-Oblique", 16, leading=None)
    # c.setLineWidth(1)
    # c.setDash(1, 2) #dots
    y = 660
    for i in range(len(saved_list)):
        y -= 30
        c.drawString(65, y, saved_list[i][0]) # text
        # c.line(x1, y1, x2, y2)
        c.drawRightString(580, y, "{}".format(i+3)) #page number
#### WHAT TO DO IF PAGE ENDS? ###########
    watermark(c)

    # draw line
    c.setLineWidth(1)
    c.line(65, 60, 565, 60)   

    info.append(Paragraph(INFO_TXT, styles["Normal"]))
    f = Frame(65, 50, 515, 50, leftPadding=0, bottomPadding=0,
        rightPadding=0, topPadding=0, id=None, showBoundary=0)
    f.addFromList(info, c)
    ## use text object for that

    side_bar(c)
    footer(c)


def regular_page(c, title, fig):
    """ Creates regular page. 

    title -- string, title of figure
    fig -- string, path to figure
    c -- canvas
    """   
    
    # display title
    c.setFont("Helvetica-Bold", 20, leading=None)
    c.drawCentredString(325, 700, title)

    #display box with image
    c.setStrokeColorRGB(0.3, 0.4, 0.2)
    c.setFillColorRGB(0.3, 0.4, 0.2)
    c.rect(120, 270, 400, 400, stroke=0, fill=0)
    c.drawImage(fig, 120, 280, width=390, height=390, mask=None,
        preserveAspectRatio=True)   
   
    # ## check if this is faster for func images: 
    # ## c.drawInlineImage(self, image, x, y, width=None, height=None) 
   
    watermark(c)
    footer(c)
    side_bar(c)


def watermark(c, watermark="HTML\\Images\\watermark.png"):
    """ Sets watermark.

    c -- canvas
    watermark -- string, path to watermark
    """
    c.drawImage(watermark, 350, 10, width=250, height=200, mask=None) 
    

def footer(c, pages=1):
    """ Sets footer. Displays copyright and page number (True of False).
    
    c -- canvas
    pages -- integer, displays page number (True=0, False=1) - default: 1
    """

    # display copyright
    c.setFont("Courier", 9, leading=None)
    page = c.getPageNumber() ## use?
    c.drawString(65, 20, 
        "(c) SATAlytics by SATA s.l.r.")

    # display page numers
    if pages == 0:
        c.drawRightString(580, 20, "page {}".format(page))


def side_bar(c):
    """Sets side_bar

    c -- canvas
    """
    c.setFillColorRGB(70/256, 165/256, 66/256)
    c.setStrokeColorRGB(70/256, 165/256, 66/256)
    c.rect(20, 0, 25, 850, stroke=1, fill=1)

# # ####
# # What is bookmarkpage()

if __name__ == '__main__':
    fake_list = [("Marijke", "HTML\\Images\\dp.png"), 
                ("Marijke Thijssen", "HTML\\Images\\dp.png")]
    make_pdf(fake_list)