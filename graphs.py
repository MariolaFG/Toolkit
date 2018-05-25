#!/usr/bin/env python3

"""
Module to display several types of graphs: pie chart, bar plot
Author: Marijke
"""

import matplotlib.pyplot as plt
import numpy as np
from sys import argv


def pie_chart(labels, sizes):
    """ Displays an pie chart.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of pie piece
    """
    patches, texts = plt.pie(sizes, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def bar_plot(labels, sizes):
    """ Displays a bar plot.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of bars
    """
    y_pos = np.arange(len(labels))
    
    plt.bar(y_pos, sizes, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Product group')
    plt.title('Unique samples per product group')
     
    plt.show()
