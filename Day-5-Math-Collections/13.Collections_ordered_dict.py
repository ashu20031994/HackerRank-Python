"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
if __name__ == "__main__":
    N = int(input())
    item =  OrderedDict()
    for i in range(N):
        x = input().split()
        item_name = (" "). join(x[:-1])
        price = x[-1]
        if item_name in item.keys():
            item[item_name] += int(price)
        else:
            item[item_name] = int(price)
    
    for key in item.keys():
            print(key, item[key], sep=" ")
    
