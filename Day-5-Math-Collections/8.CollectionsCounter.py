"""
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == "__main__":
    X = int(input())
    shoe_size_available = Counter(list(map(int, input().split())))
    N = int(input())
    result = 0
    for i in range(N):
        (size, price) = tuple(map(int, input().split()))
        if shoe_size_available[size] > 0:
            shoe_size_available[size] -= 1
            result += price
        else:
            continue
    print(result)
    
    
