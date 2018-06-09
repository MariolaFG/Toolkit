#!/usr/bin/env python3

"""
Module to count the number of samples in a column.
Author: Marijke
"""

from import_xlsx import import_xlsx, write_xls
from graphs import bar_plot, pie_chart
import numpy as np
from operator import itemgetter
import pandas as pd
from sys import argv


def counter(sheet, col_name, unique=0):
    """ Counts number per group in a column as a dict {group: count}. 

    sheet -- pandas df, sheet from .xlsx file
    unique -- integer, indicates unique samples (0) or not (1), default: 0
    """
    prod_dict = {}
    
    col_group = pd.Series(sheet[col_name].astype("str"))
    # counts unique samples :
    if unique == 0:
        col_N_sample = pd.Series(sheet["N_campione"].astype("str"))
        for i in range(len(col_group)):
            if i == 0:  # pandas Series can't count negatively
                if col_group[i] not in prod_dict:
                    prod_dict[col_group[i]] = 1
                else:
                    prod_dict[col_group[i]] += 1
            elif col_N_sample[i-1] != col_N_sample[i]: #sample is different from following
                if col_group[i] not in prod_dict:
                    prod_dict[col_group[i]] = 1
                else:
                    prod_dict[col_group[i]] += 1
                    
    # counts all samples :
    elif unique == 1:
        for j in range(len(col_group)):
            if col_group[j] not in prod_dict:
                prod_dict[col_group[j]] = 1
            else:
                prod_dict[col_group[j]] += 1
    else:
        raise ValueError("unique can be 0 (unique) or 1 (not unique)")
    
    return(prod_dict)
  
 
def give_graphs(prod_dict):
    """ Produces graphs. 
    
    prod_dict -- dict {prod : count}
    """
    # get labels and sizes :
    labels = list(prod_count.keys())
    sizes = list(prod_count.values())
    N_diff_samples = sum(sizes)
    # calculates sizes as percentages (total 100%)
    if len(labels) == len(sizes):
        relative_sizes = [(sizes[i] / N_diff_samples * 100) for i in range(len(labels))]
    
    # make list of tuples to sort while label and size comined :
    count_prod_tuple = list(zip(sizes, labels))
    sorted_high = sorted(count_prod_tuple, key=itemgetter(0,1), reverse=True)
    # show bar plot in descending order :
    ylabel = "Product group"
    title = "Unique samples per product group"
    count_prod_list = [list(t) for t in zip(*sorted_high)]
    count_list = count_prod_list[0]
    prod_list = count_prod_list[1]

    bar_plot(prod_list, count_list, title, ylabel)
    # prints product and unique samples per line
    print("PRODUCT\tN_UNIQUE_SAMPLES")
    for i in range(len(sorted_high)):
        print("{}\t{}".format(sorted_high[i][0], sorted_high[i][1]))
    
    # create figures:
    pie_chart(labels, relative_sizes, 1, title)
    # bar_plot(labels, sizes, title, ylabel) # not readable but one can zoom in
    # bar_plot(labels, relative_sizes, title, ylabel, 1)
    # bar_plot(labels, relative_sizes, title, ylabel, 3) # to check if raises ValueError


   

if __name__ == '__main__':
    # imports Excel file:
    sheet = import_xlsx(argv[1])

    # counts unique samples per product group:
    col_group = "Gruppo_prodotto"
    #col_group = "Cliente"
    prod_count = counter(sheet, col_group)
    #prod_count = counter(sheet, col_group, 1) # to test no uniqueness
    #write_xls("Samples_per_client", prod_count)
    
    give_graphs(prod_count)
    
