'''
You are given a string .
Your task is to print all possible permutations of size S of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S and the integer value k.

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    (s, r) = tuple(input().split())
    r = int(r)
    result = permutations(sorted(s), r)
    for item in result:
        print(("").join(item))
