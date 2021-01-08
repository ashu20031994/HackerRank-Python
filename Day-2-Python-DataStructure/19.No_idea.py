"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    initial_happiness = 0
    
    (n, m) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    
    for item in arr:
        if item in setA:
            initial_happiness += 1
        if item in setB:
            initial_happiness -= 1
        
    print(initial_happiness)
