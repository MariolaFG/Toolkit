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

def clients_graph(resultfile, date = "all"):
    #Graph on clients always, sometimes and never exceeding the limit. 
    
    if date != "all":
        data = resultfile[resultfile["ANNO"] == str(date)]
    if date == "all":
        data = resultfile

    client_dic = {1: [], 2: [], 3: []}
    client_list = []
    for element in data["Cliente"].tolist():
        reduced_data = data[data["Cliente"] == element]
        if not element in client_list:
            client_list.append(element)
            percentages = reduced_data["Ris_Lim_perc"].dropna().tolist()
            
            per2 = []
            count = 0
            for number in percentages:
                if number != "nan":
                    per2.append(number)
                    if number > 100:
                        count = count + 1
                        
            if len(per2) > 0:
                if count == len(per2):                                
                    client_dic[1].append(element)
                if count != 0 and count != len(per2):
                    client_dic[2].append(element)
                if count == 0:
                    client_dic[3].append(element)
    
    explode = (0.1, 0.05, 0.05) 
    labels = ["All samples over threshold", "Some samples over threshold",\
              "No samples over threshold"]
    colors = ['coral', 'gold', 'lightgreen']
    plt.pie(np.array([len(client_dic[1]), len(client_dic[2]), len(client_dic[3])]),\
            labels=labels, shadow=True, explode=explode, autopct='%1.1f%%',\
            pctdistance=0.6, colors=colors)
    plt.title("Clients grouped by threshold", fontsize= 16)
    plt.show()
    

    return client_dic


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
# Graph on number of samples per product/cultivar.        
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
    del prod['NON NORMATO']
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
    


def threshold_pie(resultfile, date="all"):
#Graph on percentage of samples that exceeds the limit in timeline.
    
    if date != "all":
        resultfile = resultfile[resultfile["ANNO"] == str(date)]
    
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

def compound_product(resultfile, date, client = "all", product="all", area="all", compound="none"):
    
    resultfile = resultfile[resultfile["ANNO"]== str(date)]
    
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
    
    prod_dataframe = pd.DataFrame(prod, index= ["Average"], columns=prod.keys())
    prod_dataframe = pd.DataFrame.transpose(prod_dataframe)
    
    if compound == "none":
        return prod_dataframe, None
    if compound != "none":
        return prod_dataframe, prod[compound]


def residues_graph(resultfile, client, crop, date = "all"):
    # Graph on average amount of residues per client for a single
    # crop in a certain time span, including the limit. 

    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Cliente"] == client]
    dates = list(set(data["ANNO"].tolist()))
    
    if date != "all":
        data[data["ANNO"] == str(date)]
    
    
    for date in dates:
        prod = {}
        err_val = {}
        data2 = data[data["ANNO"] == date]
        for element in data["Prova"]:
            name = element + "_" + date
            prev = data2[data2["Prova"] == element]
            prev2 = prev["Risultato"].astype(str).str.replace(',','.')
            if len(prev["Limite"].tolist()) > 0:
                threshold = prev["Limite"].tolist()[0]
            if len(prev["Limite"].tolist()) == 0:
                threshold = "nan"
            try:
                threshold = float(str(threshold).replace(",", "."))
                prod[name] = [np.mean(map(float, prev2.tolist())), threshold]
            except ValueError:
                err_val[name] = prev2.tolist()
    
        
        sizes_0 = []
        labels_0 = []
        limits_0 = []
        count_0 = 0
        
        sizes_1 = []
        labels_1 = []
        limits_1 = []
        count_1 = 0
        
        sizes_5 = []
        labels_5 = []
        limits_5 = []
        count_5 = 0
        
        for element in prod:
            if prod[element][0] <= 1:
                sizes_0.append(prod[element][0])
                labels_0.append(element)
                if prod[element][0] > prod[element][1] and prod[element][1] != float("nan"):
                    limits_0.append(count_0)
                count_0 = count_0 + 1
            if prod[element][0] > 1 and prod[element][0] < 5:
                sizes_1.append(prod[element][0])
                labels_1.append(element)
                if prod[element][0] > prod[element][1] and prod[element][1] != float("nan"):
                    limits_1.append(count_1)
                count_1 = count_1 + 1
            if prod[element][0] >= 5:
                sizes_5.append(prod[element][0])
                labels_5.append(element)
                if prod[element][0] > prod[element][1] and prod[element][1] != float("nan"):
                    limits_5.append(count_5)
                count_5 = count_5 + 1
        
        if len(sizes_0) > 0:
            plt.xticks(rotation='vertical')
            barlist = plt.bar(range(len(sizes_0)), sizes_0, width=0.4, \
                              tick_label = labels_0)
            for element in limits_0:
                barlist[element].set_color('indianred')
            plt.title("Compounds analyzed in " + crop + " from " + client, fontsize= 16)
            plt.show()
        if len(sizes_1) > 0:
            plt.xticks(rotation='vertical')
            barlist = plt.bar(range(len(sizes_1)), sizes_1, width=0.4, \
                              tick_label = labels_1)
            for element in limits_1:
                barlist[element].set_color('indianred')
            plt.title("Compounds analyzed in " + crop + " from " + client, fontsize= 16)
            plt.show()
        if len(sizes_5) > 0:
            plt.xticks(rotation='vertical')
            barlist = plt.bar(range(len(sizes_5)), sizes_5, width=0.4, \
                              tick_label = labels_5)
            for element in limits_5:
                barlist[element].set_color('indianred')
            plt.title("Compounds analyzed in " + crop + " from " + client, fontsize= 16)
            plt.show()

def residues_graph_esp(resultfile, client, crop, compound, date = "all"):    
    
    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Cliente"] == client]
    data = data[data["Prova"] == compound]
    dates = list(set(data["ANNO"].tolist()))
    
    if date != "all":
        data[data["ANNO"] == str(date)]
    
    prod = {}
    err_val = {}
    for date in dates:
        data2 = data[data["ANNO"] == date]
        for element in data2["Prova"]:
            name = element + "_" + date
            prev = data2["Risultato"].astype(str).str.replace(',','.')
            if len(prev["Limite"].tolist()) > 0:
                threshold = prev["Limite"].tolist()[0]
            if len(prev["Limite"].tolist()) == 0:
                threshold = "nan"
            try:
                threshold = float(str(threshold).replace(",", "."))
                prod[name] = [np.mean(map(float, prev.tolist())), threshold]
            except ValueError:
                err_val[name] = prev.tolist()

    
    labels = prod.keys()
    sizes = []
    limits = []
    x = range(len(prod))
    count = 0
    for element in prod:
        sizes.append(prod[element][0])
        if prod[element][0] > prod[element][1] and prod[element][1] != float("nan"):
            limits.append(count)
        count = count + 1
    
    plt.xticks(rotation='vertical')
    barlist = plt.bar(x, sizes, width=0.4, tick_label = labels)
    for element in limits:
        barlist[element].set_color('indianred')
    plt.show()

def bar_per_sample(resultfile, client, crop, compound, date = "all"):
    
    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Cliente"] == client]
    data = data[data["Prova"] == compound]
    dates = list(set(data["ANNO"].tolist()))
    
    if date != "all":
        data[data["ANNO"] == str(date)]
    
    for date in dates:
        prod = {}
        data2 = data[data["ANNO"] == date]
        name = compound + "_" + date
        prev = map(float, data2["Risultato"].astype(str).str.replace(',','.').tolist())
        labels = map(int, data2["N_campione"].tolist())
        labels = map(str, labels)
        if len(data2["Limite"].tolist()) > 0:
            threshold = data2["Limite"].tolist()[0]
            threshold = float(str(threshold).replace(",", "."))
        if len(data2["Limite"].tolist()) == 0:
            threshold = "nan"
        prod[name] = prev, threshold
        
        label = []
        sizes = []
        limits = []
        x = range(len(prod[name][0]))
        count = 0
        for element in prod[name][0]:
            sizes.append(element)
            label.append("Sample_" + labels[count])
            if element > prod[name][1] and prod[name][1] != float("nan"):
                limits.append(count)
            count = count + 1
        
        plt.xticks(rotation='vertical')
        barlist = plt.bar(x, sizes, width=0.4, tick_label = label)
        for element in limits:
            barlist[element].set_color('indianred')
        maxim = (max(prod[name][0])) + threshold/2
        plt.ylim(0, maxim)
        plt.title("Samples of " + name + " in " + crop +\
                  " from " + client, fontsize= 16)
        plt.show()
        

    
#Graph on average of compound per crop over a certain time span. 
#Graph on average number of molecules per crop over a certain time span.
#Graph on average concentration of compound in a product in time.
#Graph on total number of products for a client.


 
if __name__ == "__main__":
    
    resultfile = pd.read_excel("prove_16-17.xlsx", sheetname=0)
    infofile = pd.read_excel("campioni-16-18.xlsx", sheetname=0)
    date = 2018
    product = "Riso"
    area="Pavia"
    compound = "Clorato"
    client = "AGRIEUROPA SOC.COOP.AGR."
    
#    threshold_pie(resultfile, date = 2017)
#    product_type(resultfile)
#    print number_clients(infofile, date)  
#    a, b = compound_product(resultfile, date, product, area, compound)
#    samples_product_type(resultfile)
#    clients_graph(resultfile, date=2016)
    residues_graph(resultfile, client, crop = "Carote", date = "all")
#    residues_graph_esp(resultfile, client, crop = "Carote", compound= compound, date = "all")
    bar_per_sample(resultfile, client, crop="Carote", compound=compound, date = "all")

