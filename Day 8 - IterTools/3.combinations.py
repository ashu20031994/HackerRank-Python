'''
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    (s, r) = tuple(input().split())
    r = int(r)
    s = sorted(s)
    for i in range(1, r+1):
        result = combinations(s, i)
        for item in result:
            print(("".join(item)))
