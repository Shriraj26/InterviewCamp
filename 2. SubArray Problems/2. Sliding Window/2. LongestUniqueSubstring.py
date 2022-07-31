"""
Given a String, find the longest substring with unique characters.
For example: "whatwhywhere" --> "atwhy"
"""

a = input()
start = 0
end = 1
longest = 1
myDict = {}
myDict[a[start]]= 0
newStr = ''

def longSubStrWithoutRepeat(start, end, newStr, longest):
    while end < len(a):

        toAdd = a[end]

        if myDict.get(toAdd) is not None and myDict[toAdd] >= start:
            start = myDict[toAdd] + 1

        myDict[toAdd] = end

        if end - start + 1 > longest:
            longest = end - start + 1
            newStr = a[start: end + 1]

        # print(newStr)
        end += 1
    print(newStr)
    return longest


print(longSubStrWithoutRepeat(start, end, newStr, longest))












