"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.
Constraints


Output Format

Output the total number of distinct country stamps on a single line.
"""

def count_stamps(arr):
    print(len(set(arr)))
    
if __name__ =="__main__":
    n = int(input())
    arr = [input() for i in range(n)]
    count_stamps(arr)
