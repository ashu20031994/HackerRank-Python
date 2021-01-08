"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def superset(setA, setB):
    return setA.issuperset(setB)

if __name__ == "__main__":
    result = True
    setA = set(map(int, input().split()))
    for i in range(int(input())):
        setB = set(map(int, input().split()))
        result = superset(setA, setB)
        if result == True:
            continue
        else:
            break
    print(result)


