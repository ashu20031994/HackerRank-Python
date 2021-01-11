"""
zip([iterable, ...])

This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

Task

The National University conducts an examination of  students in  subjects.
Your task is to compute the average scores of each student.

Input Format

The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by students in a particular subject.

Output Format

Print the averages of all students on separate lines.

The averages must be correct up to  decimal place.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def average_score(subject_marks_each_students):
    students_marks_each_subject = list(zip(*subject_marks_each_students.values()))
    
    for item in students_marks_each_subject:
        print(sum(item)/ len(item))
    
    
if __name__ == "__main__":
    (N, X) = tuple(map(int, input().split()))
    subject_marks_each_students = {i:list(map(float, input().split())) for i in range(X)}
    
    average_score(subject_marks_each_students) 
