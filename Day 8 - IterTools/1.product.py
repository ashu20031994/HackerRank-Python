'''
You are given a two lists A and B. Your task is to compute their cartesian product A X B.
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ =="__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = list((product(a, b)))
    for item in result:
        print(item, end=" ")
