#!/usr/bin/env python3

"""
Module to count the number of different products
Author: Marijke
"""

from import_xlsx import import_xlsx
from graphs import bar_plot
from graphs import pie_chart
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
from sys import argv


def counter(sheet):
    """ Counts number of products per group

    sheet -- pandas df, sheet from .xlsx file
    """
    prod_dict = {}
    total_count = 0
    col_group = sheet["Gruppo_prodotto"].tolist()
    col_N_sample = sheet["N_campione"].tolist()
    for i in range(len(col_group)):
        if col_N_sample[i-1] != col_N_sample[i]: #only if sample is different from following
            if col_group[i] not in prod_dict:
                prod_dict[col_group[i]] = 1
            else:
                prod_dict[col_group[i]] += 1
    return(prod_dict)
    
    

if __name__ == '__main__':
    sheet = import_xlsx(argv[1])
    prod_count = counter(sheet)

    # get labels and sizes :
    labels = list(prod_count.keys())
    sizes = list(prod_count.values())
    N_diff_samples = sum(sizes)
    # calculates sizes as percentages (max. 100%)
    if len(labels) == len(sizes):
        relative_sizes = [(sizes[i] / N_diff_samples * 100) for i in range(len(labels))]

    # make list of tuples to sort while label and size comined :
    count_prod_tuple = list(zip(sizes, labels))
    print(count_prod_tuple)
    sorted_high = sorted(count_prod_tuple, key=itemgetter(0,1), reverse=True)
    # show bar plot in descending order :
    count_prod_list = [list(t) for t in zip(*sorted_high)]
    count_list = count_prod_list[0]
    prod_list = count_prod_list[1]
    bar_plot(prod_list, count_list)
    # prints product and unique samples per line
    print("PRODUCT\tN_UNIQUE_SAMPLES")
    for i in range(len(sorted_high)):
        print("{}\t{}".format(sorted_high[i][0], sorted_high[i][1]))
    
    # create figures:
    pie_chart(labels, relative_sizes)
    #bar_plot(labels, sizes) # not readable but one can zoom in
    #bar_plot(labels, relative_sizes)
