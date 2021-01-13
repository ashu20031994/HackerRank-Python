"""
Task
You are given three integers: , , and , respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format
The first line contains , the second line contains , and the third line contains .
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    print(pow(a, b))
    print(pow(a, b, m))
