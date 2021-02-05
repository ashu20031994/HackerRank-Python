'''
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    s = input().split()
    k = int(input())
    
    pairs = list(combinations((range(n)), k))
    index = []
    for i in range(len(s)):
        if s[i] == 'a':
            index.append(i)
    count = 0
    for item in pairs:
        for key in index:
            if key in item:
                count += 1
                break
    
    print(count / len(pairs))
