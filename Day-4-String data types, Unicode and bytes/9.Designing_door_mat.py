"""

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
row,width=input().split()
row=int(row)
width=int (width)
c='.|.'
for i in range(int(row/2)):
    print ((c*i).rjust(int(width/2)-1,'-') + c +(c*i).ljust(int(width/2)-1,'-'))
print("WELCOME".center(width,'-'))
for i in range(int(row/2)):
    print ((c*(int(row/2)-i-1)).rjust(int(width/2)-1,'-') + c + (c*(int(row/2)-i-1)).ljust(int(width/2)-1,'-')) 
