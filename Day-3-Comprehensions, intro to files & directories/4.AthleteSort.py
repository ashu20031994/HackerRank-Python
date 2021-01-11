"""
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th 
attribute and print the final resulting table. Follow the example given below for better understanding.

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def sort(arr, k):
    result = sorted(arr, key = lambda x : x[k])
    for item in result:
        for ele in item:
            print(ele, end=' ')
        print(end='\n')
        

if __name__ == '__main__':
    (n, m) = tuple(map(int, input().split()))
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sort(arr, k)
