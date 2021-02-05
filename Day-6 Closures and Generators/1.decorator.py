'''
The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer , the number of mobile phone numbers.
 lines follow each containing a mobile number.

Output Format

Print  mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
'''


import re


def wrapper(f):
    def fun(l):
        # complete the function
        rules = (("^91", '+91'), ("^0", "+91"))
        for i in range(len(l)):
            item = l[i]
            if len(item) == 10:
                l[i] = "+91 " + item[0:5] + " " + item[5:10] 
            else:
                l[i] = "+91 " + item[len(item)-10:len(item)-5] + " " + item[len(item)-5:]
        
        return f(l)
    return fun


