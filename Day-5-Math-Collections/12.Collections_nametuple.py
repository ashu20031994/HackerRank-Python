"""
Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    Student = namedtuple("Student", ",".join(input().split()))
    average = 0
    for i in range(N):
        lst = list(map(str, input().split()))
        x = Student(lst[0], lst[1], lst[2], lst[3])
        
        average += int(x.MARKS)
    print("{:.2f}".format(average/N))
