#!/usr/bin/env python3

"""
Module to import an Excel .xlsx file into Python using pandas
Author: Marijke
"""

from sys import argv
import pandas as pd

def import_xlsx(file_name):
    """ Imports first sheet of Excel file.

    file_name -- string, name of Excel file
    """
    xlsx = pd.ExcelFile(file_name)
    sheet_names = xlsx.sheet_names #sheet names depend on language
    df1 = xlsx.parse(sheet_names[0])
    print(df1.shape) #gives number of rows and columns
    return(df1)
    

if __name__ == '__main__':
    # check if name of file is provided
    if not argv[1]:
        print("Name of Excel file needs to be entered.")

    xlsx_samples = argv[1]
#   xlsx_inf = argv[2]
    import_xlsx(xlsx_samples)

