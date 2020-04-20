# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:00:41 2018

@author: jeffp

main.py
"""

from buying_list import Frequent
from buying_list import sort_buying
from build_tree import BuildTree
from build_tree import findpatternlist
from true_round import TrueRound
import sys
#import time

def mainnn(sup,input_file,output_file):
    min_support = float(sup)
    #min_support = 0.1
    #input_file = "sample2.in"
    #input_file = "test.txt"
    #output_file = "outtest.txt"
    
    freq_dictionary, sort_list, file_len = Frequent(input_file,min_support)
    buying_table = sort_buying(input_file,freq_dictionary)
    #print(sort_list)
    #print(buying_table)
    rootTree,header_list = BuildTree(buying_table, sort_list)
    pattern_list = []
    pattern_list = findpatternlist(rootTree,header_list,(file_len*min_support),set([]),pattern_list)
    #print(pattern_list)
    #need transfer into total_table, key:length of pattern, value:[ [pattern], count ]
    #print(header_list)
    total_table = {}
    for now_pat in pattern_list:
        now_pat[0] = sorted(now_pat[0])
        if(len(now_pat[0]) in total_table):
            total_table[len(now_pat[0])].append(now_pat)
        else:
            total_table[len(now_pat[0])] = [now_pat]
    #print(total_table)
    
    #print(file_len*min_support)
    """
    f = open(output_file, 'w', encoding = 'UTF-8')
    sort_list = sorted(sort_list, key = lambda x : int(x[0]))
    #print(sort_list)
    for i in sort_list:
        f.write("{0}:{1}\n".format(i[0],TrueRound(i[1]/file_len,4)))
    f.close()
    """
    #total_table = findPattern(header_list, min_support*file_len)
    #print("------------------\n")
    #cnt = 0
    f = open(output_file, 'w', encoding = 'UTF-8')
    for i in total_table:
        total_table[i] = sorted(total_table[i], key = lambda x : x[0])
        #print(total_table[i])
        for j in total_table[i]:
            #cnt=cnt+1
            f.write(str(j[0][0]))
            for k in range(1,len(j[0])):
                #print(',{0}'.format(str(j[0][k])))
                f.write(',{0}'.format(str(j[0][k])))
            #print(":{:.4f}\n".format((TrueRound(int(j[1])/file_len,4)),4))
            f.write(":{:.4f}\n".format((TrueRound(int(j[1])/file_len,4)),4))
            #print("{0}:{1}".format((','.join(str(j[0]))),TrueRound(int(j[1])/file_len,4)))
    #print(cnt)
    f.close()
#print(total_table)
#mainnn(0.1,"sample2.in","outtest.txt")
#mainnn(0.1,"testttt.txt","qqqqq.txt")
if __name__ == "__main__":
    #start_time = time.time()
    mainnn(sys.argv[1],sys.argv[2],sys.argv[3])
    #print("--- %s seconds ---" % (time.time() - start_time))
