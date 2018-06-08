#!/usr/bin/env python3

"""
Module to display several types of graphs: pie chart, bar plot
"""

import datetime
import matplotlib.pyplot as plt
import numpy as np
from sys import argv 

def set_colors(sizes):
    """ Set color theme. Returns colors.
    
    sizes -- list, for determining number of colors needed
    """
    # useful website: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
    cmap = plt.cm.winter
    colors = cmap(np.linspace(0., 1., len(sizes)))
    return(colors)

def pie_chart(labels, sizes, donut=0, title="pc"):
    """ Displays and saves a pie chart.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of pie piece
    donut -- integer, indicate pie chart (0) or donut chart (1), default: 0
    title -- integer, title of plot, default: pc
    """
    colors = set_colors(sizes)
    
    # draw pie chart :
    fig = plt.figure()
    patches, texts = plt.pie(sizes, startangle=90,
                     colors=colors
#                    labels=sizes
#                    shadow=True
                    )
    plt.legend(patches, labels, loc="best")
    
    # draw donut chart :
    if donut == 1:
        center_circle = plt.Circle((0,0), 0.70, fc="white")
        fig1 = plt.gcf()
        fig1.gca().add_artist(center_circle)
    
    plt.axis("equal")
    plt.tight_layout()
    plt.title(title)
    plt.show()
    fig.savefig("{}.png".format(title))
    


def bar_plot(labels, sizes, title, ylabel, vert=0):
    """ Displays and saves a bar plot.

    labels -- list of strings, indicates labels
    sizes -- list of integers, indicates size of bars
    ylabel -- string, label at y-axis (x-axis if vert = 1)
    title -- string, title of plot
    vert -- integer, indicates a vertical (0) or horizontal plot (1), default: 0
    """
    colors = set_colors(sizes)
    
    fig = plt.figure()
    y_pos = np.arange(len(labels))

    if vert == 0:
        plt.bar(y_pos, sizes, align="center", alpha=0.5, color=colors)
        plt.xticks(y_pos, labels)
        plt.ylabel(ylabel)
    elif vert == 1:
        plt.barh(y_pos, sizes, align="center", alpha=0.5, color=colors)
        plt.yticks(y_pos, labels)
        plt.xlabel(ylabel)
    else:
        raise ValueError("vert can have value 0 or 1.")
    plt.title(title)
     
    plt.show()
    fig.savefig("bp.png")
