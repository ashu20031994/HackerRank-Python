"""
TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.



Output Format

Output the sum of elements in set .
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":
    n = int(input())
    setA = set(map(int, input().split()))
    for i in range(int(input())):
        command = (input().split())[0]
        
        if command == "intersection_update":
            setB = set(map(int, input().split()))
            setA.intersection_update(setB)
        elif command == "update":
            setB = set(map(int, input().split()))
            setA.update(setB)
        elif command =="symmetric_difference_update":
            setB = set(map(int, input().split()))
            setA.symmetric_difference_update(setB)
        else:
            setB = set(map(int, input().split()))
            setA.difference_update(setB)
    
    print(sum(setA))
