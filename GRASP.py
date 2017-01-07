from random import randint, sample
from itertools import chain, combinations
from time import time

def quicksort(listToSort):
    less = []
    more = []
    equal = []
    if len (listToSort) > 1:
        pivot = listToSort[0]
        for i in listToSort:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                more.append(i)
        return quicksort(more)+equal+quicksort(less)
    else:
        return listToSort 
        
def graspSubsetSum(sortedList,t):
    total = 0
    for i in range(len(sortedList)):
        if total < t:
            total = total + sortedList[i]
            if total > t:
                total = total - sortedList[i]
    return t - total

def random_instance(n,bit=10):
    max_n_bit_number = 2**bit-1
    S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ], reverse=True)
    return S

for n in range(10,70,2):
    total = 0
    for x in range(1,100):
       S = random_instance(n)
       sortedList = quicksort(S)
       total += graspSubsetSum(sortedList, 10000)
    print(total/100)