#!usr/bin/env python3
"""

"""
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import heapq

def number_clients(infofile, date):
    
    return len(infofile[infofile["ANNO"]==str(date)])

def product_type(resultfile):
    
    labels = {}
    for element in resultfile["Prova"]:
        if not element in labels.keys():
            labels[element] = 1
        if element in labels.keys():
            prev = labels[element]
            labels[element] = prev + 1
    
    sizes = []
    explode = []
    max_labels = heapq.nlargest(10, labels, key=labels.get)
    
    other = 0
    for element in max_labels:
            sizes.append(int((labels[element]/len(labels))*100))
            explode.append(0.1)    
    for element in labels:
        if not element in max_labels:
            other = other + labels[element]
            
    explode.append(0.1)
    sizes.append(other/len(labels)*100)
    explode = tuple(explode) 
    max_labels.append("Other")
    colors = ['lightskyblue', 'lightblue', 'cyan', "coral", "gold",\
              "lightcoral", "lavender", "cyan", "lime", "lightgreen","aquamarine"]
    plt.xticks(rotation='vertical')
    plt.pie(np.array(sizes), labels=max_labels, shadow=True, explode=explode, \
            startangle=120, autopct='%1.1f%%', pctdistance=0.8, colors=colors)
    plt.title("Total percentage of Compounds", fontsize= 16)
    plt.show()

def samples_product_type(resultfile):
        
    prod = {}
    explode = [0.1]
    for element in resultfile["Gruppo_prodotto"]:
        if not element in prod:
            prod[element] = 1
        if element in prod:
            prev = prod[element]
            prod[element] = prev + 1
    
    sizes = []
    labels = []
    max_labels = heapq.nlargest(10, prod, key=prod.get)
    for element in max_labels:
        sizes.append(prod[element])
        labels.append(element)
        explode.append(0.1)
        
        
    other = 0
    for element in prod:
        if not element in max_labels:
            other = other + prod[element]
    
    colors = ['lightskyblue', 'lightblue', 'cyan', "coral", "gold",\
              "lightcoral", "lavender", "cyan", "lime", "lightgreen","aquamarine"]
    labels.append("Other")
    sizes.append(other)
    plt.pie(np.array(sizes), labels=labels, shadow=True, colors=colors, \
            explode=explode, autopct='%1.1f%%', pctdistance=0.8, startangle=120)
    plt.show
    


def threshold_pie(resultfile):

    list2 = []
    for element in resultfile['Classi_Ris_Lim_perc']:
        element = str(element)
        if "Tra 0 e 30" in element:
            list2.append("Tra 0 e 30")
        if "Tra 30 e 50" in element:
            list2.append("Tra 30 e 50")
        if "Tra 50 e 80" in element:
            list2.append("Tra 50 e 80")
        if "Tra 80 e 100" in element:
            list2.append("Tra 80 e 100")
        if "Maggiore o uguale a 100" in element:
            list2.append("Maggiore o uguale a 100")
    
    list3 = np.array([list2.count("Tra 0 e 30"), list2.count("Tra 30 e 50"), \
             list2.count("Tra 50 e 80"),list2.count("Tra 80 e 100"), \
             list2.count("Maggiore o uguale a 100")])  
    
    result_count = len(list2)
    labels = ["Tra 0 e 30", "Tra 30 e 50", "Tra 50 e 80", "Tra 80 e 100",\
              "Maggiore o uguale a 100"]
    colors = ['lightskyblue', 'lightblue', 'cyan',"aquamarine", "coral"]
    explode = (0.05, 0.05, 0.05, 0.05, 0.2)
    plt.xticks(rotation='vertical')
    plt.pie(list3, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, \
            pctdistance=0.7, explode=explode)
    plt.title("Samples grouped by threshold", fontsize= 16)
    
    plt.show()
    
    return result_count, list2.count("Maggiore o uguale a 100")

def compound_product(resultfile, product="all", area="all"):
    
    if area == "all" and product != "all":
        data = resultfile[resultfile["Gruppo_prodotto"]==product]
    if area != "all"and product != "all":
        data2 = resultfile[resultfile["Gruppo_prodotto"]==product]
        data = data2[data2["Location"]==area]
    if area == "all" and product == "all":
        data = resultfile
    if area != "all"and product == "all":
         data = resultfile[resultfile["Location"]==area]

    prod = {}
    err_val = {}
    for element in data["Prova"]:
        prev = data[data["Prova"] == element]
        prev2 = prev["Risultato"].astype(str).str.replace(',','.')        
        try:
            prod[element] = np.mean(map(float, prev2.tolist()))
        except ValueError:
            err_val[element] = prev2.tolist()
    
    prod_dataframe = pd.DataFrame(prod, index= ["Average"])

    return pd.DataFrame.transpose(prod_dataframe)

 
if __name__ == "__main__":
    
    resultfile = pd.read_excel("prove_18.xlsx", sheetname=0)
    infofile = pd.read_excel("campioni-16-18.xlsx", sheetname=0)
    date = 2018
    product = "Riso"
    area="Pavia"
    
    threshold_pie(resultfile)
    product_type(resultfile)
    print number_clients(infofile, date)  
    print compound_product(resultfile, product, area)
    samples_product_type(resultfile)
    