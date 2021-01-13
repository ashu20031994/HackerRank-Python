"""
Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
number = complex(input())

print(abs(number))
print(cmath.phase(number))


