"""
Word Break Problem: Given a String S, which contains letters and no spaces, determine if you
can break it into valid words. Return one such combination of words.
You can assume that you are provided a dictionary of English words.
For example:
S = "ilikemangotango"
Output:
Return any one of these:
"i like mango tango"
"i like man go tan go"
"i like mango tan go"
"i like man go tango"
"""

""" ********* This code does not work as of now because the dictionary to find whether a word is a valid word in python
is giving valid word true even for single letter say - x or u therefore once I find the resource for the valid dictionaty,
then I will come and visit this problem again..."""

"""
from nltk.corpus import words
from nltk.corpus import wordnet
print(wordnet.synsets('l'))
from spellchecker import SpellChecker
spell = SpellChecker()
spell.correction(word)

if not wordnet.synsets('l'):
    print('not an eng word')
else:
    print('An english word')
"""

"""
The basic idea is to check this - check if a words is a valid word from 0 to i
IF it is valid, check if i+1 to len of string is a valid word, if that is also true, 
then add the current string to the result string
If not, then remove it from the result string, and check for 0 to i+1
Base cases - 
1. If we reach the end of the string it means that we have got a valid word, then we return
2. if we encounter an index from where valid word would not exist, then it will return from that too
"""


myStr = input()
memo = ['UNVISITED' for i in range(len(myStr))]
result = []

def findValidString(start):
    
    
    #base case- if u reach end it means that we got a valid string
    if start == len(myStr):
        return True
    
    # if u reach certain index from no valid string exists, then we return False
    if memo[start] == 'NOT_FOUND':
        return False
    
    # iterate from start to end of string and check if valid string exists from 0 to i
    for i in range(start, len(myStr)):
        
        stringToCheck = myStr[start: i+1] 
        print(stringToCheck)
        #First check if this string is a vali string, 
        if stringToCheck in words.words():
            
            result.append(stringToCheck)
            #print(result)
            # Now check if valid string exists from i+1 till len of string
            if findValidString(i+1):
                return True
            else:
                result.pop()
                memo[i+1] = 'NOT_FOUND'
    
    # If u reach here it means that u didnot get a valid string yet thus we return False
    return False
            
            
    


#print('age' in words.words())
print('l' in words.words())
print(findValidString(0))
print(result)
print(memo)

