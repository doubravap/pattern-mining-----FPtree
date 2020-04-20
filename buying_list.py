# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:46:22 2018

@author: jeffp

buying_list.py
"""


def Frequent(filename,minsupport):
    total = {}
    f = open(filename,'r', encoding = 'utf8')
    file = f.readlines()
    for line in file:
        single_line = line.split(',')
        if(single_line[-1][-1] == '\n'):
            single_line[-1]=single_line[-1][:-1]
        #print(single_line)
        for single_buy in single_line:
            if(single_buy in total):
                total[single_buy] = total[single_buy]+1
            else:
                total[single_buy] = 1
    #print(total)
    del_list = []
    for i in total:
        #print(i)
        if(total[i]<(len(file)*minsupport)):
            del_list.append(i)
    for i in del_list:
        del total[i]
    #print(total)
    sort_list = sorted(total.items(), key=lambda d: d[1], reverse=True)
    #print(sort_list)
    return total, sort_list, len(file)

def sort_buying(filename,dictionary):
    buying_table = []
    f = open(filename,'r', encoding = 'utf8')
    file = f.readlines()
    for line in file:
        single_line = line.split(',')
        if(single_line[-1][-1] == '\n'):
            single_line[-1]=single_line[-1][:-1]
        single_list = []
        #print(single_line)
        for single_buy in single_line:
            #print(single_buy)
            if(single_buy in dictionary):
                insert_place = 0
                for i in range(0,len(single_list)):
                    if(dictionary[single_buy]<=dictionary[single_list[i]]):
                        insert_place = i+1
                single_list.insert(insert_place,single_buy)
        if(len(single_list)>0):
            buying_table.append(single_list)
        #print(single_list)
    
    return buying_table
#freq_dictionary, sort_list = Frequent("sample2.in",0.2)
#buying_table = sort_buying("sample2.in",freq_dictionary)



