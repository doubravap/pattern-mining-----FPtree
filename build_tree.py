# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:19:56 2018

@author: jeffp

build_tree.py
"""

class TreeNode:
    def __init__(self, now_name,now_count,parentNode):
        self.name = now_name
        self.count = now_count
        self.parent = parentNode
        self.children = {}
        self.linktoNext = None
        
    def plus(self,num):
        self.count = self.count + num
    def show(self,ind=1):
        print(' '*ind,self.name,' ', self.count)
        for child in self.children.values():
            child.show(ind+1)

def BuildTree(buying_list, sort_list):
    header_list = {}
    for now in sort_list:
        header_list[now[0]] = [now[1],None]
    
    rootTree = TreeNode('Null root', 1, None)
    for single_buy in buying_list:
        addTree(single_buy, rootTree, header_list, 1)
    #print(header_list)
    #rootTree.show()
    #print("RRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOTTTTTTTTT")
    return rootTree,header_list
    
    
def addTree(single_buy, now_node, header_list, count):
    if(single_buy[0] in now_node.children):
        #First object exists in children
        now_node.children[single_buy[0]].plus(count)
    else:
        #We need to build a new child
        now_node.children[single_buy[0]] = TreeNode(single_buy[0],count,now_node)
        
        if(header_list[single_buy[0]][1] == None):
            #point to this node
            header_list[single_buy[0]][1] = now_node.children[single_buy[0]]
        else:
            #start with head until None, and point to this node
            addHeader(header_list[single_buy[0]][1], now_node.children[single_buy[0]])
    if(len(single_buy) > 1):
        addTree(single_buy[1:], now_node.children[single_buy[0]], header_list, count)

def addHeader(start_node, now_node):
    while(start_node.linktoNext != None):
        start_node = start_node.linktoNext
    start_node.linktoNext = now_node


def BuildconTree(data, min_support):
    header_list = {}
    for single_buy in data:
        for single_item in single_buy:
            header_list[single_item] = header_list.get(single_item,0)+data[single_buy]
    del_list=[]
    for check in header_list.keys():
        if(header_list[check]<min_support):
            del_list.append(check)
    for i in del_list:
        del(header_list[i])
    
    head = set(header_list.keys())
    if(len(head)==0):
        return None, None
    
    for i in header_list:
        header_list[i]=[header_list[i],None]
    rootTree = TreeNode("Null root",1,None)
    for settt, count in data.items():
        forsorting = []
        for single_item in settt:
            if(single_item in header_list):
                insert_place = 0
                for i in range(0,len(forsorting)):
                    if(header_list[forsorting[i]][0]>header_list[single_item][0]):
                        insert_place = i+1
                    if(header_list[forsorting[i]][0]==header_list[single_item][0]):
                        check_list = list(header_list)
                        if(check_list.index(forsorting[i])<check_list.index(single_item)):
                            insert_place=i+1
                forsorting.insert(insert_place,single_item)
                #forsorting[single_item]=header_list[single_item][0]
        if(len(forsorting)>0):
            #aftersorting = [a[0] for a in sorted(forsorting.items(), key=lambda x: x[1], reverse=True)]
            #print("aftersorting : ", forsorting)
            addConTree(forsorting,rootTree,header_list,count)
    #print("---------------")
    #print(header_list)
    #rootTree.show()
    #del del_list,head,aftersorting,forsorting
    return rootTree, header_list
def addConTree(single_buy, now_node, header_list, count):
    if(single_buy[0] in now_node.children):
        #First object exists in children
        now_node.children[single_buy[0]].plus(count)
    else:
        #We need to build a new child
        now_node.children[single_buy[0]] = TreeNode(single_buy[0],count,now_node)
        
        if(header_list[single_buy[0]][1] == None):
            #point to this node
            header_list[single_buy[0]][1] = now_node.children[single_buy[0]]
        else:
            #start with head until None, and point to this node
            addHeader(header_list[single_buy[0]][1], now_node.children[single_buy[0]])
    if(len(single_buy) > 1):
        addTree(single_buy[1::], now_node.children[single_buy[0]], header_list, count)
    


def findcondPattern(now_node):
    pattern = {}
    while(now_node != None):
        parent_list = []
        if(now_node.name !="Null root"):
            #print(now_node.name)
            parent_list.append(now_node.name)
            Parent = now_node
            while(Parent.parent.name !="Null root"):
                Parent = Parent.parent
                #print(Parent.name)
                parent_list.append(Parent.name)
        parent_list = parent_list[1:]
        if(len(parent_list)>0):
            #print(frozenset(parent_list))
            pattern[frozenset(parent_list)] = now_node.count
        now_node = now_node.linktoNext
        #print("freq pattern : ", pattern)
    return pattern

def findpatternlist(tree,header_list,min_support,pre_seq,pattern_list):
    #print(header_list.items())
    #print(list(header_list))
    """
    head = []
    for i in header_list:
        head.append([i,header_list[i][0]])
    header = sorted(head, key=lambda x:x[1]) 
    del head
    header_listsss = []
    for i in header:
        header_listsss.append(i[0])
    del header
    """
    #print(header_listsss)
    #print(header_listsss)
    for single in header_list:
        
        new_seq = pre_seq.copy()
        new_seq.add(int(single))
        #print(single,pre_seq,new_seq)
        #print("HHHHHEas:",header_list)
        pattern_list.append([list(new_seq),int(header_list[single][0])])
        #print("THIS IS PATTERN :",pattern_list, "len: ", len(pattern_list))
        cond_pat = findcondPattern(header_list[single][1])
        #print(cond_pat)
        #***********建新的樹的時候，樹的node順序要跟原本一樣?
        cond_tree, cond_head = BuildconTree(cond_pat,min_support)
        #print(cond_head)
        if(cond_head != None):
            findpatternlist(cond_tree,cond_head,min_support,new_seq,pattern_list)
    del header_list,tree
    return pattern_list


            
            