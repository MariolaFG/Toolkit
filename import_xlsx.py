#!/usr/bin/env python3

"""
Module to import and write to an Excel(.xlsx) file.
"""

from sys import argv
import pandas as pd
import xlwt


def import_xlsx(file_name):
    """ Returns first sheet of .xlsx file as pandas dataframe.

    file_name -- string, name of Excel file
    """
    xlsx = pd.ExcelFile(file_name)
    sheet_names = xlsx.sheet_names #sheet names depend on language
    df1 = xlsx.parse(sheet_names[0])
    #df1.fillna("None")
    df1.drop(df1.index[len(df1) - 1], inplace=True) #drop total row
    #print("columns, rows -" , df1.shape) #gives number of rows and columns
    return(df1)
    

def write_xls(file_name, list_cols):
    """ Writes to the first sheet of an Excel (.xls) file and saves it.

    file_name -- string, name of Excel file
    list_cols -- list, indicates content of columns in Excel file
    """
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("Sheet 1")
    # worksheet.write(0, 0, "Test Value")
    for row in range(len(list_cols)):
        for col in range(len(list_cols[row])):
            worksheet.write(row, col, list_cols[col][row])
    workbook.save("{}.xls".format(file_name))
    #return(workbook)
    
    
if __name__ == '__main__':
    # check if name of file is provided
    if not argv[1]:
        print("Name of Excel file needs to be entered.")

    xlsx_samples = argv[1]
    import_xlsx(xlsx_samples)
    
    name_of_file = "Test"
    list_of_two = [["Marijke", "Thijssen"],[1234, 4567]]
    write_xls(name_of_file, list_of_two)

