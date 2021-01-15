"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()
    for i in range(N):
        x = input().split()
        method = x[0]
        
        if method == "append":
            value = int(x[1])
            d.append(value)
        elif method == "appendleft":
            value = int(x[1])
            d.appendleft(value)
        elif method == "pop":
            d.pop()
        else:
            d.popleft()
    
    for items in d:
        print(items, end=" ")
