'''
Let's use decorators to build a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. Print their 
names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print 
them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids
For Mary George, the output should be:

Ms. Mary George
Input Format

The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Output Format

Output  names on separate lines in the format described above in ascending order of age.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle'''



def person_lister(f):
    def inner(people):
        # complete the function
        people = sorted(people, key = lambda x : int(x[2]))
        
        return [f(item) for item in people]
    return inner

