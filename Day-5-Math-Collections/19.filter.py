"""
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.
"""

import re
def fun(s):
    # return True if s is a valid email, else return False
    return re.search(r"^[\w-]+@[0-9a-zA-Z]+\.[a-z]{1,3}$", s)

