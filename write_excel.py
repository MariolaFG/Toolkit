#!/usr/bin/env python3

"""
Module to write to an Excel(.xls) file.
"""

from sys import argv
import xlwt

def write_xls(file_name, my_dict):
    """ Writes to the first sheet of an Excel (.xls) file and saves it.

    file_name -- string, name of Excel file
    my_dict -- dict, indicates content of first column and second
    """
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("Sheet 1")
    counter = 0
    # worksheet.write(0, 0, "Test Value")
    for key in my_dict:
        worksheet.write(counter, 0, key)
        worksheet.write(counter, 1, my_dict[key])
        counter += 1
    workbook.save("{}.xls".format(file_name))
    #return(workbook)

if __name__ == '__main__':
    # check if name of file is provided
    # if not argv[1]:
        # print("Name of Excel file needs to be entered.")

    name_of_file = "Test"
    test_dict = {"Marijke" : 1234,
                "Thijssen" : 4567}
    write_xls(name_of_file, test_dict)
