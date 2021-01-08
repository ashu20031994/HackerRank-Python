"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
"""

def names_second_lowest_grade(arr):
    second_lowest = sorted(set([item[1] for item in arr]))[1]
    result = sorted([item[0] for item in arr if item[1] == second_lowest])
    for item in result:
        print(item)
    
if __name__ == '__main__':
    arr = [[input(), float(input())] for _ in range(int(input()))]
    
    names_second_lowest_grade(arr)
