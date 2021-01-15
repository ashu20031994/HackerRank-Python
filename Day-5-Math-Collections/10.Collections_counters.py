"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x_i amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and , the price of the shoe.
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
    
    
