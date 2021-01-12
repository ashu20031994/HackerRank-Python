"""
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""

if __name__ == '__main__':
    s = list(input())
    print(True if any(s[i].isalnum() for i in range(len(s))) else False)
    print(True if any(s[i].isalpha() for i in range(len(s))) else False)
    print(True if any(s[i].isdigit() for i in range(len(s))) else False)
    print(True if any(s[i].islower() for i in range(len(s))) else False)
    print(True if any(s[i].isupper() for i in range(len(s))) else False)
