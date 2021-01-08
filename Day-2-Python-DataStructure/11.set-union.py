"""
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

Input Format

The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Constraints


Output Format

Output the total number of students who have at least one subscription.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def count(set1, set2):
    print(len(set1.union(set2)))
    
if __name__ == "__main__":
    n = int(input())
    set1 = set(map(int, input().split()))
    m = int(input())
    set2 = set(map(int, input().split()))
    count(set1, set2)
