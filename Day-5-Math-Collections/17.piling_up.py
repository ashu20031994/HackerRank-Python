"""
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube_i is on top
of cube_j then sideLength_j >= sideLength_i.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not
print the quotation marks.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
if __name__ == "__main__":
    d = deque()
    for case in range(int(input())):
        n = int(input())
        d.extend(list(map(int, input().split())))
        
        result = []
        for i in range(len(d)):
            if len(d) == 1:
                result.append(d.pop())
            else:
                x = d.popleft()
                y = d.pop()
                if x > y:
                    result.append(x)
                    d.append(y)
                else: 
                    result.append(y)
                    d.appendleft(x)
        
        res = True
        for i in range(len(result)-1):
            if result[i] < result[i+1]:
                res = False
        if res:
            print("Yes")
        else:
            print("No")
        
        d.clear()
            
