'''
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with  (X, c)
in the string.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == "__main__":
    s = list(map(int, list(input())))
    result = []
    for k, g in groupby(s):
        result.append((len(list(g)), k))
    
    for item in result:
        print(item, end=" ")
