"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

import string
def print_rangoli(size):
    # your code goes here
    alphabets = string.ascii_lowercase
    
    result = []
    for i in range(size):
        
        mid = ("-".join(alphabets[size-i-1:size]))
        mid = mid[::-1][:-1] + mid
        result.append(mid.center(4*n-3,'-'))
    temp = result[::-1]
    temp = temp[1:]
    
    for item in temp:
        result.append(item)
    print("\n".join(result))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
