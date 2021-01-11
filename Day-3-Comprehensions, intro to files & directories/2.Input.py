"""
Task

You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Constraints
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    (x, k) = tuple(map(int, input().split()))
    print(True if eval(input()) == k else False)
