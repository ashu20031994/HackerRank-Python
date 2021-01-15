"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    words = OrderedDict()
    for i in range(N):
        x = input()
        if x in words.keys():
            words[x] += 1
        else:
            words[x] = 1
    
    print(len(words.keys()))
    for key in words.keys():
        print(words[key] , end=" ")
