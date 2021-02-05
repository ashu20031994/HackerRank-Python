'''
You are given a string s.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == "__main__":
    (s, r) = tuple(input().split())
    r = int(r)
    
    result = combinations_with_replacement(sorted(s), r)
    for item in result:
        print(("".join(item)))
