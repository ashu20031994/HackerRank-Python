"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .
"""


def count_substring(string, sub_string):
    count = 0
    lst = []
    for i in range(len(string)-len(sub_string)+1):
        lst.append(string[i:i+len(sub_string)])
    return (lst.count(sub_string))

def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    vowel = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowel:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
        
    if kevin > stuart:
        print( "{} {}".format("Kevin", kevin))
    elif stuart > kevin:
        print( "{} {}".format("Stuart", stuart))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
