# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:35:03 2018

@author: jeffp
"""

def TrueRound(x,n):
    #print(str(x[n+2]))
    
    #print(str(x*(10**(n+1)))[4])
    s = str(x)
    if(len(s)<(n+3)):
        return x
    else:
       if((s[n+2] == '5')):
           if((int(s[n+1])+1)>=10):
               return round(x,n-1)
               """
               a = 1
               for i in range(0,n):
                   a = a/10
               num = float(s[0:n+2])+a
               """
           else:
               num = float(s[0:n+1]+str(int(s[n+1])+1))
           
           
           return num
       else:
           #return float(s[0:n+2])
           return round(x,n)
    """
    d = (x*(10**(n+1)))
    #b = int((x)*(10**(n)))*10
    if((str(d)[n] == '5')or(str(d)[n] == '6')or(str(d)[n] == '7')or(str(d)[n] == '8')or(str(d)[n] == '9')):
        num = (int(str(d)[0:n])+1)/(10**(n))
    else:
        num = (int(str(d)[0:n]))/(10**(n))
    """
    """
    a = x
    for i in range(0,n+1):
        a = a*10
        print(a)
    a = int(a)
    #a = int(x*(10**(n+1)))
    print("a: ",a)
    b = x
    for j in range(0,n):
        b = b*10
        print(b)
    b = int(b)*10
    #b = int((x)*(10**(n)))*10
    print("b: ",b)
    c = a-b
    if(c<5):
        num = b/(10**(n+1))
    else:
        num = ((b/10)+1)/(10**(n))
    """
    
    return num
