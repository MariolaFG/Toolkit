#!/usr/bin/env python3

"""
Module to display several types of graphs: pie chart, bar plot
Author: Marijke
"""

import datetime
import matplotlib.pyplot as plt
import numpy as np
from sys import argv


def pie_chart(labels, sizes, title):
    """ Displays and saves a pie chart.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of pie piece
    title -- integer, title of plot
    """
    fig = plt.figure()
    patches, texts = plt.pie(sizes, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis("equal")
    plt.tight_layout()
    plt.title(title)
    plt.show()
    fig.savefig("pc.png")


def bar_plot(labels, sizes, title, ylabel, vert=0):
    """ Displays and saves a bar plot.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of bars
    ylabel -- string, label at y-axis (x-axis if vert = 1)
    title -- string, title of plot
    vert -- integer, indicates a vertical (0) or horizontal plot (1), default: 0
    """
    fig = plt.figure()
    y_pos = np.arange(len(labels))

    if vert == 0:
        plt.bar(y_pos, sizes, align="center", alpha=0.5)
        plt.xticks(y_pos, labels)
        plt.ylabel(ylabel)
    elif vert == 1:
        plt.barh(y_pos, sizes, align="center", alpha=0.5)
        plt.yticks(y_pos, labels)
        plt.xlabel(ylabel)
    else:
        raise ValueError("vert can have value 0 or 1.")
    plt.title(title)
     
    plt.show()
    fig.savefig("bp.png")
