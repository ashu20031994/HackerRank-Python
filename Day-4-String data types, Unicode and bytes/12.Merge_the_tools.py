"""
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at 
a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Example


There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . 
The third substring has  different characters, so . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence 
shown is important.
"""

def merge_the_tools(string, k):
    # your code goes here
    substr = [string[i:i+k] for i in range(0,len(string), k)]
    result = []
    for item in substr:
        temp = ''
        for i in range(len(item)):
            if item[i] not in temp:
                temp += item[i]
        result.append(temp)
    
    for item in result:
        print(item)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
