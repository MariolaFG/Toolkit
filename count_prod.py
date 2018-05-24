#!/usr/bin/env python3

"""
Module to count the number of different products
Author: Marijke
"""

from import_xlsx import import_xlsx
import matplotlib.pyplot as plt
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
    

def pie_chart(count_dict):
    """ Displays an pie chart.

    count_dict -- dict{product, count as integer}
    """
    count_list = list(count_dict.values())
    N_diff_samples = sum(count_list)
    labels = list(count_dict.keys())
    # calculates sizes as percentages (max. 100%)
    sizes = [(count_list[i] / N_diff_samples * 100) for i in range(len(labels))]

    patches, texts = plt.pie(sizes, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    

if __name__ == '__main__':
    sheet = import_xlsx(argv[1])
    #prod_bar_graph(sheet)
    prod_count = counter(sheet)
    pie_chart(prod_count)
