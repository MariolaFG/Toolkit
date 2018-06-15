#!usr/bin/env python3
"""
"""

from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import heapq


def residues_graph(resultfile, client, crop, date = "all", hide = False): ## n.1
    """ This function creates a graph on average amount of residues per client 
    for a single crop in a certain time span, including the limit. 
    Variables:
        - Client: Compulsory (Column Cliente)
        - Crop: Compulsory (Column Gruppo_Prodotto)
        - Date: Optional. 
    Returns list of figures as strings.
    """
    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Cliente"] == client]
    dates = list(set(data["ANNO"].tolist()))
    
    if date != "all":
        data[data["ANNO"] == str(date)]
        dates = [date]
    
    fig_list = []
    
    client_count = 1
    client_dic = {}
    for year in dates: # Will produce a graph for each date.
        prod = {}
        err_val = {}
        data2 = data[data["ANNO"] == year]
        list_check = []
        for element in data["Prova"]:
            # This will hide the compound names if hide == True
            if hide == False:
                name = element + "_" + str(year)
            if hide == True:
                name = client_count
                client_dic["Compound: " + str(name)] = element+ "_" + str(year) # MT - changed
                
            prev = data2[data2["Prova"] == element]
            # prev contains the data from a single year, client, crop and compound
            prev2 = prev["Risultato"].astype(str).str.replace(',','.')
            # prev2 contains the concentration stored in prev
            if len(prev["Limite"].tolist()) > 0:
                threshold = prev["Limite"].tolist()[0]
            if len(prev["Limite"].tolist()) == 0:
                threshold = "nan"
            try:
                if not element + "_" + str(year) in list_check:
                    list_check.append(element + "_" + str(year))
                    threshold = float(str(threshold).replace(",", "."))
                    client_count = client_count + 1
                    prod[name] = [np.mean(list(map(float, prev2.tolist()))), threshold]
            except ValueError:
                err_val[name] = prev2.tolist() # This is just to store the weird values
        
        sizes = []
        label = []
        limits = []
        count = 0
        for element in sorted(prod.keys()):
            sizes.append(prod[element][0])
            label.append("Compound: " + str(element))
            bool_th =  prod[element][0] > prod[element][1]
            if bool_th == True and prod[name][1] != float("nan"):
                limits.append(count)
            count = count + 1
        

        start = 0
        limits1 = limits            
        while start < len(sizes):
            fig = plt.figure()
            fig.set_size_inches(18.0, 18.0)
            sizes2 = list(map(float, sizes[start:start+30]))
            label2 = label[start:start+30]

            x2 = range(len(sizes2))
            plt.xticks(rotation='vertical')
            barlist = plt.bar(x2, sizes2, width=0.4, tick_label = label2, \
                              align='center')
            
            limits2 = []
            for element in limits1:
                if element < 30:
                    barlist[element].set_color('indianred')
                else:
                    limits2.append(element-30)
                    
            limits1 = limits2 

            # titles of graphs
            if date == "all":
                year1 = dates[0]
                year2 = dates[-1]
                if year1 == year2:
                    fig_title = "Average concentration of all compounds found in " + crop + " from " + client + " in " + str(year1) + "(" + str(int(1+(start/30))) + ")"
                else:
                    fig_title = "Average concentration of all compounds found in " + crop + " from " + client + " in {}-{}".format(year1, year2) + "(" + str(int(1+(start/30))) + ")"
            else:
                fig_title = "Average concentration of all compounds found in " + crop + " from " + client + " in " + str(date) + "(" + str(int(1+(start/30))) + ")"
            plt.title(fig_title, fontsize= 24)
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%f mg/kg'))
            
            fig_name = "{}.png".format(fig_title)
            fig.savefig(fig_name, dpi=100)
            fig_list.append(fig_name)
            
            start = start + 30

        data_client = pd.DataFrame.from_dict(client_dic, orient="index")
        writer = pd.ExcelWriter('Compound_index.xlsx', engine='xlsxwriter')
        data_client.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        
        print(fig_list)
        return(fig_list)


def compound_per_client(resultfile, compound, crop, date ="all", hide=False): ## n.2 
    """This function creates a graph on average amount of residues in a single 
    crop for a single client in a certain time span, including the limit.
    Variables:
        - Compound: compulsory (column Prova)
        - Crop: compulsory (column Gruppo_prodotto
        - Date: optional"""
    fig_list = []

    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Prova"] == compound]
    dates = list(set(data["ANNO"].tolist()))
    
    if date != "all":
        data[data["ANNO"] == str(date)]
        dates = [date]
    
    client_count = 1
    client_dic = {}
    for year in dates: #Creates a graph per year
        prod = {}
        err_val = {}
        data2 = data[data["ANNO"] == year]
        list_check = []
        # data2 contains the information for single crop, year and compound.
        for element in data["Cliente"]:
            if hide == False:
                name = element + "_" + str(year)
            if hide == True:
                name = client_count
                client_dic["Client " + str(name)] = element+ "_" + str(year)
                
            prev = data2[data2["Cliente"] == element]
            # prev contains the information for single crop, year, compound and client.
            prev2 = prev["Risultato"].astype(str).str.replace(',','.')
            if len(prev["Limite"].tolist()) > 0:
                threshold = prev["Limite"].tolist()[0]
            if len(prev["Limite"].tolist()) == 0:
                threshold = "nan"
            try:
                if not element + "_" + str(year) in list_check:
                    list_check.append(element + "_" + str(year))
                    client_count = client_count + 1
                    threshold = float(str(threshold).replace(",", "."))
                    prod[name] = [np.mean(list(map(float, prev2.tolist()))), threshold]
            except ValueError:
                err_val[name] = prev2.tolist()
                
        # Creates bar charts in groups of 30 clients:
        label = []
        sizes = []
        limits = []
        x = range(len(prod))
        count = 0
        for element in sorted(prod.keys()):
            sizes.append(prod[element][0])
            label.append("Client " + str(element))
            bool_th =  prod[element][0] > prod[element][1]
            if bool_th == True and prod[name][1] != float("nan"):
                limits.append(count)
            count = count + 1
        
        if len(sizes) <= 30:
            fig = plt.figure()
            fig.set_size_inches(18.0, 18.0)
            plt.xticks(rotation='vertical')
            barlist = plt.bar(x, sizes, width=0.4, tick_label = label)
            for element in limits:
                barlist[element].set_color('indianred')

            # titles of graphs
            if date == "all":
                year1 = dates[0]
                year2 = dates[-1]
                if year1 == year2:
                    fig_title = "Average concentration of " + compound + " in " + crop + " in " + str(year1)
                else:
                    fig_title = "Average concentration of " + compound + " in " + crop + " in {}-{}".format(year1, year2)
            else:
                fig_title = "Average concentration of " + compound + " in " + crop + " in " + str(date)

            plt.title(fig_title, fontsize= 16)
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%f mg/kg'))
            fig_name = "{}.png".format(fig_title)
            # fig_name = "Function21.png"
            fig.savefig(fig_name, dpi=100)
            fig_list.append(fig_name)  

        if len(sizes) > 30:
            start = 0
            limits1 = limits            
            while start < len(sizes):
                fig = plt.figure()
                fig.set_size_inches(18.0, 18.0)

                sizes2 = list(map(float, sizes[start:start+30]))
                label2 = label[start:start+30]

                x2 = range(len(sizes2))
                plt.xticks(rotation='vertical')
                barlist = plt.bar(x2, sizes2, width=0.4, tick_label = label2, \
                                  align='center')
                
                limits2 = []
                for element in limits1:
                    if element < 30:
                        barlist[element].set_color('indianred')
                    else:
                        limits2.append(element-30)
                        
                limits1 = limits2 
                
                # titles of graphs
                if date == "all":
                    year1 = dates[0]
                    year2 = dates[-1]
                    if year1 == year2:
                        fig_title = "Average concentration of " + compound + " in " + crop + " in " + str(year1) + "(" + str(int(1+(start/30))) + ")"
                    else:
                        fig_title = "Average concentration of " + compound + " in " + crop + " in {}-{}".format(year1, year2) + "(" + str(int(1+(start/30))) + ")"
                else:
                    fig_title = "Average concentration of " + compound + " in " + crop + " in " + str(date) + "(" + str(int(1+(start/30))) + ")"

                plt.title(fig_title, \
                          fontsize= 16)
                plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%f mg/kg'))
                
                fig_name = "{}.png".format(fig_title)   
                fig.savefig(fig_name, dpi=100)
                fig_list.append(fig_name)  

                start = start + 30
                
    data_client = pd.DataFrame.from_dict(client_dic, orient="index")
    writer = pd.ExcelWriter('Client_index.xlsx', engine='xlsxwriter')
    data_client.to_excel(writer, sheet_name='Sheet1')
    writer.save()

    print(fig_list)
    return(fig_list)


def samples_product_type(resultfile, client = "all", detail = False,\
                         date = "all"): # n.3 and n.6
    """ This function creates a graph on number of samples per product/cultivar
    Variables:
        - Client = optional"""
    
    fig_list = []

    if client != "all":
        resultfile = resultfile[resultfile["Cliente"] == str(client)]
    years = list(set(resultfile["ANNO"].tolist()))
    
    if date != "all":
        resultfile = resultfile[resultfile["ANNO"] == date]
        years = [str(date)]
    
    # This is to choose if we want the pie chart for product detail:
    if detail == True:
        product_detail = "dettaglio_prodotto"
    if detail == False:
        product_detail = "Gruppo_prodotto"   
    
    for year in years:
        prod = {}
        explode = []
        for element in resultfile[product_detail]:
            if not element in prod:
                data = resultfile[resultfile[product_detail] == element]
                samples = list(set(data["N_campione"].tolist()))
                # Creates a list without repetitions
                prod[element] = len(samples)
        # Prod dictionary structure -> Product: Amount of times it has been analyzed
        
        # Create pie chart:
        sizes = []
        labels = []
        
        if "..." in prod.keys():
            del prod["..."]
        
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
        
        if other != 0:
            labels.append("Other")
            sizes.append(other)
            explode.append(0.1)
        fig = plt.figure()
        fig.set_size_inches(18.0, 18.0)
        if client == "all":
            fig_title = "Amount of samples for all clients in " + str(year)
        elif date == "all":
            year1 = years[0]
            year2 = years[-1]
            if year1 == year2:
                fig_title = "Amount of samples for " + client + " in " + str(year1)
        else:
            fig_title = "Amount of samples for " + client + " in {}-{}".format(year1, year2)
        plt.title(fig_title)
        plt.pie(np.array(sizes), labels=labels, shadow=True, colors=colors, \
                explode=explode, autopct='%1.1f%%', pctdistance=0.8, startangle=150)
        
        fig_name = "{}.png".format(fig_title)   
        fig.savefig(fig_name, dpi=100)
        fig_list.append(fig_name)  

    print(fig_list)
    return(fig_list)


def residues_graph_esp(resultfile, client, crop, compound):  ## 4 
    """ This function creates a graph with the average concentration of a compound 
    through the year for a single client.
    Variables:
        - Client: Compulsory (column Cliente)
        - Crop: Compulsory (column Gruppo_prodotto)
        - Compound: Compulsory (column Prova)
    Things to do: 
        - Make client optional and use this function to give an average
        concentration.
        - Order dates chronologicaly
        """
    fig_list = []

    data = resultfile[resultfile["Gruppo_prodotto"] == crop]
    data = data[data["Cliente"] == client]
    data = data[data["Prova"] == compound]
    dates = list(set(data["Data_Arrivo"].tolist()))
    
    prod = {}
    err_val = {}
    for date in dates:
        data2 = data[data["Data_Arrivo"] == date]
        
        for element in data2["N_campione"]:
            name = "Sample_" + str(int(element)) + "_" + str(date)[:-9]
            prev = data2["Risultato"].astype(str).str.replace(',','.')
            if len(data2["Limite"].tolist()) > 0:
                threshold = data2["Limite"].tolist()[0]
            if len(data2["Limite"].tolist()) == 0:
                threshold = "nan"
            try:
                threshold = float(str(threshold).replace(",", "."))
                prod[name] = [np.mean(list(map(float, prev.tolist()))), threshold, date]
                
            except ValueError:
                err_val[name] = prev.tolist()
    
    # Create bar chart:
    labels = []
    sizes = []
    limits = []
    x = range(len(prod))
    count = 0
    for el in sorted(prod.items(), key=lambda prod: prod[1][2]): # This sorts the dates
        element = el[0] # This is necessary because previous function produces a tuple
        labels.append(element)
        sizes.append(prod[element][0])
        if prod[element][0] > prod[element][1] and prod[element][1] != float("nan"):
            limits.append(count)
        count = count + 1

    fig = plt.figure()
    if len(sizes) <= 20:  
        fig = plt.figure()
        fig.set_size_inches(18.0, 18.0)  
        plt.xticks(rotation='vertical')
        barlist = plt.bar(x, sizes, width=0.4, tick_label = labels)
        for element in limits:
            barlist[element].set_color('indianred')

        # titles of graphs
        if date == "all":
            year1 = dates[0]
            year2 = dates[-1]
            if year1 == year2:
                fig_title = "Average concentration of " + compound + " in " + crop + " from " + client + " in " + str(year1)
            else:
                fig_title = "Average concentration of " + compound + " in " + crop + " from " + client + " in {}-{}".format(year1, year2)
        else:
            fig_title = "Average concentration of " + compound + " in " + crop + " from " + client + " in " + str(date)
            # fig_title = "Average concentration of " + compound + " in " + crop + " from " + client + "_low" ## Y-D-M H-M-S gives error

        plt.title(fig_title, fontsize= 16)
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%f mg/kg'))
        fig_name = "{}.png".format(fig_title)   
        fig.savefig(fig_name, dpi=100)
        fig_list.append(fig_name)  
    
    if len(sizes) > 20:
        ind = 20
        limits1 = limits
        while ind < len(sizes):
            sizes1 = sizes[ind-20:ind]
            labels1 = labels[ind-20:ind]

            fig = plt.figure()
            fig.set_size_inches(18.0, 18.0)        
            plt.xticks(rotation='vertical')
            barlist = plt.bar(range(len(sizes1)), sizes1, width=0.4, \
                              tick_label = labels1)
            
            limits2 = []
            for element in limits1:
                if element < 20:
                    barlist[element].set_color('indianred')
                else:
                    limits2.append(element-20)
                    
            limits1 = limits2    
            
            # titles of graphs
            if date == "all":
                year1 = dates[0]
                year2 = dates[-1]
                if year1 == year2:
                    fig_title = "Average concentration of " + compound + " in " + crop + " from " + client + " in " + str(year1) + "(" + str(int(1+(start/30))) + ")"
                else:
                    fig_title = "Average concentration of " + compound + " in " + crop + "from " + client + " in {}-{}".format(year1, year2) + "(" + str(int(1+(start/30))) + ")"
            else:
                fig_title = "Average concentration of " + compound + " in " + crop + "from " + client + " in " + str(date) + "(" + str(int(1+(start/30))) + ")"
            plt.title(fig_title, fontsize= 16)
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%f mg/kg'))
            
            ind = ind + 20
        fig_name = "{}.png".format(fig_title)   
        fig.savefig(fig_name, dpi=100)
        fig_list.append(fig_name)  
        
    print(fig_list)
    return(fig_list)


def number_of_molecules(infofile, client = "all", date = "all"): ## n.5
    """ This function creates a graph on average number of molecules per crop
    over a certain time span.
    Variables:
        Date: optional"""   
    fig_list = []

    if date != "all":
        infofile = infofile[infofile["ANNO"] == str(date)]
    if date != "all":
        infofile = infofile[infofile["Cliente"] == client]
    years = []
    for i in list(set(infofile["ANNO"].tolist())):
        if i != "Totale":
            years.append(i) 
        
    
    for year in years: # Produces a graph per year
        data2 = infofile[infofile["ANNO"] == year]
        prod = {}
        for element in data2["Gruppo_prodotto"]:
            if not element in prod:
                data = data2[data2["Gruppo_prodotto"] == element]
                # data contains the information for a single crop in a year
                prev = list(set(data["N_Molecole"].tolist()))
                # prev contains a list with all the trials to that especific crop
                if prev != []:
                    prod[element] = np.mean(prev)
                    # It is storing the average

        # Create bar chart:
        sizes = []
        labels = []
        explode = [0.1]

        max_labels = heapq.nlargest(20, prod, key=prod.get)
        # It selects the 20 greatest averages
        
        for element in max_labels:
            sizes.append(prod[element])
            labels.append(element)
            explode.append(0.1)

        fig = plt.figure()
        fig.set_size_inches(18.0, 18.0)  
        plt.xticks(rotation='vertical')

        if client == "all":
            fig_title = "Amount of analyses per product for all clients in " + str(year)
        elif date == "all":
            year1 = years[0]
            year2 = years[-1]
            if year1 == year2:
                fig_title = "Amount of analyses for " + client + " in " + str(year1)
            else:
                fig_title = "Amount of analyses for " + client + " in {}-{}".format(year1, year2)
        else:
            fig_title = "Amount of analyses for " + client + " in " + str(year)

        plt.title(fig_title)
        plt.bar(range(len(sizes)), sizes, width=0.4, tick_label = labels, color="aquamarine")
        fig_name = "{}.png".format(fig_title)   
        fig.savefig(fig_name, dpi=100)
        fig_list.append(fig_name) 

    print(fig_list)
    return(fig_list) 


def threshold_pie(resultfile, infofile, date="all", client="all", detail = False): ## 7
    """ This function creates a graph on percentage of samples that exceeds 
    the limit in timeline.
    Variables:
        - Date: optional"""
    fig_list = []

    if date != "all":
        resultfile = resultfile[resultfile["ANNO"] == date]
        years = []
        for i in list(set(resultfile["ANNO"].tolist())):
            if i != "Totale":
                years.append(i)
    if client != "all":
        resultfile = resultfile[resultfile["Cliente"] == str(client)]
    
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
    # List2 contains know all the class of the sample acording to the percentage
    # with the threshold
    
    list3 = np.array([list2.count("Tra 0 e 30"), list2.count("Tra 30 e 50"), \
             list2.count("Tra 50 e 80"),list2.count("Tra 80 e 100"), \
             list2.count("Maggiore o uguale a 100")])
    # This creates an array with the number of elements in each class
    
    # Create pie chart:
    labels = ["Tra 0 e 30", "Tra 30 e 50", "Tra 50 e 80", "Tra 80 e 100",\
              "Maggiore o uguale a 100"]
    colors = ['lightskyblue', 'lightblue', 'cyan',"aquamarine", "coral"]
    explode = (0.05, 0.05, 0.05, 0.05, 0.2)

    fig = plt.figure()
    fig.set_size_inches(18.0, 18.0)
    plt.xticks(rotation='vertical')
    plt.pie(list3, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, \
            pctdistance=0.7, explode=explode)
    
    # title of graph
    if client == "all":
        fig_title = "Occurence of exceeding the limit for all clients in " + str(date)
    elif date == "all":
        year1 = years[0]
        year2 = years[-1]
        if year1 == year2:
            fig_title = "Occurence of exceeding the limit for " + client + " in " + str(year1)
        else:
            fig_title = "Occurence of exceeding the limit for " + client + " in {}-{}".format(year1, year2)
    else:
        fig_title = "Occurence of exceeding the limit for " + client + " in " + str(date)
    plt.title(fig_title, fontsize=16)
    
    
    if detail == True:
        sample_count = {}
        list_samples = infofile["Gruppo_prodotto"].tolist()
        for element in set(list_samples):
            if not element in sample_count:
                sample_count[element] = list_samples.count(element)
                
        over_threshold(resultfile[resultfile['Classi_Ris_Lim_perc'] == \
                                  "Maggiore o uguale a 100"], sample_count,\
                                    client, date)

    fig_name = "{}.png".format(fig_title)   
    fig.savefig(fig_name, dpi=100)
    fig_list.append(fig_name)  

    print(fig_list)
    return(fig_list)

def clients_graph(resultfile, date = "all"): ## 8
    """ This function produces a Graph on clients always, sometimes and never 
    exceeding the limit. 
    
    Variables needed: None, date is optional."""
    fig_list = []

    if date != "all":
        data = resultfile[resultfile["ANNO"] == date]
    if date == "all":
        data = resultfile

    client_dic = {1: [], 2: [], 3: []}
    # This dictionary will store the names of the clients. 1: All samples over
    # over the threshold; 2: Some samples over the threshold; 3: No samples
    # over the threshold.
    client_list = [] # This list is just to make sure that no clients are repeated
    for element in data["Cliente"].tolist():
        reduced_data = data[data["Cliente"] == element]
        if not element in client_list:
            client_list.append(element)
            percentages = reduced_data["Ris_Lim_perc"].dropna().tolist()
            # At this point, we have a list that contains all the percentages
            # (higher than 100 means over the threshold)
            
            per2 = []
            count = 0
            for number in percentages:
                if number != "nan":
                    per2.append(number)
                    if number > 100:
                        count = count + 1
            # This is for each client, count will be the way to see if none, 
            # some, or all elements of per are above the threshold
                        
            if len(per2) > 0:
                if count == len(per2):                                
                    client_dic[1].append(element)
                if count != 0 and count != len(per2):
                    client_dic[2].append(element)
                if count == 0:
                    client_dic[3].append(element)


    # Create the plot:
    explode = (0.1, 0.05, 0.05) 
    labels = ["All samples over threshold", "Some samples over threshold",\
              "No samples over threshold"]
    colors = ['coral', 'gold', 'lightgreen']

    fig = plt.figure()
    fig.set_size_inches(18.0, 18.0)
    plt.pie(np.array([len(client_dic[1]), len(client_dic[2]), len(client_dic[3])]),\
            labels=labels, shadow=True, explode=explode, autopct='%1.1f%%',\
            pctdistance=0.6, colors=colors)

    fig_title = "Occurence of samples exceeding the limit for clients in " + str(date)
    plt.title(fig_title, fontsize= 16)
    
    fig_name = "{}.png".format(fig_title)   
    fig.savefig(fig_name, dpi=100)
    fig_list.append(fig_name)  
    
    print(fig_list)
    return(fig_list)
    #return client_dic


        
def products_of_client(resultfile, client, date = "all"):
    """ This function creates a graph on total number of products for a client.
    Variables:
        - Client: compulsory (column Cliente)
        - Date: Optional."""
    fig_list = []

    if date != "all":
        resultfile = resultfile[resultfile["ANNO"] == str(date)]
        years = list(set(resultfile["ANNO"].tolist()))
    
    resultfile = resultfile[resultfile["Cliente"] == str(client)]
    
    prod = {}
    for element in resultfile["Gruppo_prodotto"]:
        if not element in prod:
            data = resultfile[resultfile["Gruppo_prodotto"] == element]
            # data contains the information for single client and product
            prev = list(set(data["Prova"].tolist())) # This are the trials
            samples = list(set(data["N_campione"].tolist())) # This is the number of samples
            prod[element] = [len(samples), len(prev)]
    
    #Create bar chart: 
    sizes = []
    labels = []
    for element in prod:
        sizes.append(prod[element][0])
        labels.append(element)
    
    fig = plt.figure()
    fig.set_size_inches(18.0, 18.0)
    plt.xticks(rotation='vertical')
    plt.bar(range(len(sizes)), sizes, width=0.4, tick_label = labels,\
            color = "lightgreen")

    # title of graph
    if date == "all":
        year1 = years[0]
        year2 = years[-1]
        if year1 == year2:
            fig_title = "Crops analyzed from " + client + " in " + str(year1)
        else: 
            fig_title = "Crops analyzes from " + client + " in {}-{}".format(year1, year2)
    else:
        fig_title = "Crops analyzed from " + client + " in " + str(date)    

    plt.title(fig_title, fontsize= 16)
    fig_name = "{}.png".format(fig_title)   
    fig.savefig(fig_name, dpi=100)
    fig_list.append(fig_name)  

    print(fig_list)
    return(fig_list)
             
def over_threshold(reducedfile, sample_count, client, date):
    """This function creates detailed information about the samples that are 
    over the threshold. It only apears if detail == True"""
    fig_list = []

    prod = {}
    for element in reducedfile["Prova"]:
        if not element in prod:
            prod[element] = 1
        if element in prod:
            prev = prod[element]
            prod[element] = prev + 1
            
    sizes = []
    labels = []
    sample_sizes = []
    explode = []
    max_labels = heapq.nlargest(20, prod, key=prod.get)
        # It selects the 20 greatest averages
        
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
    
    if other != 0:
        labels.append("Other")
        sizes.append(other)
        explode.append(0.1)
    
    fig = plt.figure()
    fig.set_size_inches(18.0, 18.0)     
    plt.pie(np.array(sizes), labels=labels, shadow=True, colors=colors, \
            explode=explode, autopct='%1.1f%%', pctdistance=0.8, startangle=150)
    fig_title = "Occurences exceeding the limit per compound for " + client + " in " + str(date) 
    plt.title(fig_title, fontsize= 16)
    fig_name = "{}.png".format(fig_title)   
    fig.savefig(fig_name, dpi=100)
    fig_list.append(fig_name)  
    
    prod = {}
    for element in reducedfile["Gruppo_prodotto"]:
        if not element in prod:
            prod[element] = 1
        if element in prod:
            prev = prod[element]
            prod[element] = prev + 1
            
    sizes = []
    labels = []
    max_labels = heapq.nlargest(15, prod, key=prod.get)
        # It selects the 20 greatest averages
    
    for element in max_labels:
        sizes.append(prod[element])
        labels.append(element)
        if element in sample_count:
            sample_sizes.append(sample_count[element])
    
    fig = plt.figure()
    fig.set_size_inches(18.0, 18.0)       
    plt.xticks(rotation='vertical')
    plt.bar(range(len(sizes)), sizes, width=0.4, tick_label = labels,\
            color = "lightgreen")
    for i, v in enumerate(sizes):
        plt.text(i, v+0.25, str(sample_sizes[i]), horizontalalignment='center', \
                 color='darkgreen', fontweight='bold', fontsize = 8)
    plt.ylim(0, max(sizes) + 1)
    plt.ylabel("Number of samples", fontsize = 14)
    fig_title = "Occurences exceeding the limit per product for " + client + " in " + str(date)
    plt.title(fig_title, fontsize= 16)
    fig_name = "{}.png".format(fig_title)   
    fig.savefig(fig_name, dpi=100)
    fig_list.append(fig_name)  
    
    print(fig_list)
    return(fig_list)


def drop_rows(resultfile):

    dic_todrop = {"Prova":["Grado Rifrattometrico", "Acidita", "Acidità", \
    "Acidita (espr. in ac.citrico)", "Acidità (espr. in ac.citrico)", "Calibro medio",\
    "Durezza", "Durezza totale"], "Gruppo_prodotto": ["NON NORMATO"], "ANNO": ["Totale"]}
    # Contains what we want to erase from the database

    for key in dic_todrop:
        for element in dic_todrop[key]:
            #For all the elements and keys in the dictionary
            if element in resultfile[key].tolist():
                # Checks if it is on the file and erase it
                resultfile = resultfile[resultfile[key] != element]
    
    return resultfile
 
if __name__ == "__main__":
    
    # resultfile = pd.read_excel("prove_16-17.xlsx", sheetname=0)
    # infofile = pd.read_excel("campioni-16-18.xlsx", sheetname=0)
    date = 2016
    # compound = "Clorpirifos"
    # client = "CONAD SOC. COOP."
    # # crop = "Pesche"
    # crop = "Albicocche"
    resultfile = pd.read_excel("test_analysis_18.xlsx", sheet_name=0)
    client = "AZIENDA AGRICOLA PONZIO S.R.L. -  SOCIETA' AGRICOLA"
    crop = "Rucola"
    compound = "Spinosyn A"

    hide = False
    detail = False

    residues_graph(resultfile, client=client, crop=crop)
    
    # compound_per_client(resultfile, compound=compound, crop=crop, date = "all", hide=hide)   

    # samples_product_type(resultfile, client=client, date=date, detail=True)
   
    # residues_graph_esp(resultfile, client=client, crop = crop, compound= compound)

    # number_of_molecules(resultfile, client= client)
    
    # threshold_pie(resultfile, date = 2016, client=client, detail = True)
    
    # clients_graph(resultfile, date= date)
     
    # products_of_client(resultfile, client=client)
