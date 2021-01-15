"""
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression 
to cube each fibonacci number and print the list.
"""

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        lst = [0, 1]
        for i in range(2, n):
            lst.append(lst[i-1] + lst[i-2])
        return lst
    

