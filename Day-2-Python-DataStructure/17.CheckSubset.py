"""
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

Input Format

The first line will contain the number of test cases, .
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ =="__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        setA = set(map(int, input().split()))
        m = int(input())
        setB = set(map(int, input().split()))
        
        if setA.issubset(setB):
            print(True)
        else:
            print(False)
