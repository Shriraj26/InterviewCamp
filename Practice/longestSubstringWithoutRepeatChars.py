"""


"""

s = input()

def func():

    start = 0
    end = 1
    myDict = {s[start]: 1}
    longest = 1
    while end < len(s)-1:

        currLetter = s[end]

        if myDict.get(currLetter) is not None and start <= myDict[currLetter]:
            start = myDict[currLetter] + 1

        myDict[currLetter] = end

        if end - start + 1> longest:
            longest = end - start + 1
            newStr = s[start: end+1]
            print(newStr)

        end += 1

    return longest

print(func())