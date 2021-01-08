"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.
"""


def symmeteric_difference(set1, set2):
    result = sorted(list(set1.symmetric_difference(set2)))
    for item in result:
        print(item)
        
if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int, input().split()))
    n = int(input())
    set2 = set(map(int, input().split()))
    symmeteric_difference(set1, set2)
    
