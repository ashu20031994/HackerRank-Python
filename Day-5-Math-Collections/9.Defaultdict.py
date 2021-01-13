"""
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each  words, 
check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
if __name__ == "__main__":
    word = defaultdict(list)
    
    (n, m) = tuple(map(int, input().split()))
    
    for i in range(n):
        word[input()].append(i+1)
    
    for i in range(m):
        x = input()
        if x in word.keys():
            print(" ".join(map(str, word[x])))
        else: 
            print(-1)
        
