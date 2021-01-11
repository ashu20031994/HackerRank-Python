"""
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer .  is the total number of integers in the list.
The second line contains the space separated list of  integers.

Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    arr = input().split()
    print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))
