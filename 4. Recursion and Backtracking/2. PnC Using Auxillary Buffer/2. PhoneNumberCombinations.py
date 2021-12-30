"""
Phone Number Mnemonic Problem: Given an N digit phone number, print all the strings that can be made from that phone number. Since 1 and 0 don't correspond to any characters, ignore them. For example:
213 => AD, AE, AF, BD, BE, BF, CD, CE, CF
"""

myStr = input()

"""
We create a newString to not include 0s and 1s in it and ignore them
"""
phoneNo = ''
for i in myStr:
    if i == '0' or i == '1':
        continue
    phoneNo += i

# this is our auxillary array to store the letters in the buffer
bufferArr = [None for i in range(len(phoneNo))]

# This is to store the letter combinations
myDict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

"""
String index will iterate from 0 till len of the phone number string say 234 is given value so it will go from 2 till 4
Bufferindex will iterate for the same
"""


def printLetterCombos(stringIndex, bufferIndex):
    if bufferIndex == len(bufferArr):
        print(bufferArr)
        return

    if stringIndex == len(phoneNo):
        return

    for i in range(len(myDict[phoneNo[stringIndex]])):
        bufferArr[bufferIndex] = myDict[phoneNo[stringIndex]][i]

        printLetterCombos(stringIndex + 1, bufferIndex + 1)
    pass


printLetterCombos(0, 0)
