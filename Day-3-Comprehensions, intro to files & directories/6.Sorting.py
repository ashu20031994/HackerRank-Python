"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string .

Output Format

Output the sorted string .
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort(arr):
    lower, upper, even, odd = [], [], [], []

    for item in arr:
        if item.isalpha():
            if item.islower():
                lower.append(item)
            else:
                upper.append(item)
        else:
            if int(item) % 2==0:
                even.append(item)
            else:
                odd.append(item)
    print(("").join(lower+upper+odd+even) )   
    
if __name__ == "__main__":
    arr = sorted(input())
    sort(arr)
