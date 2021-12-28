"""
Given a String, find the longest substring with unique characters.
For example: "whatwhywhere" --> "atwhy"
"""

a = input()
start = 0
end = 0
maxSubstr = ''
mydict = {}
for i in range( ord('a'), ord('z')+1):
    mydict[chr(i)] = None

print(mydict)

while start < len(a):

    print(start, end, maxSubstr)
    if end == len(a):
        break
    if mydict[a[end]] is not None:

        start = mydict[ a[end]] + 1
        mydict[a[end]] = None


    else:
        mydict[a[end]] = end
        if len(maxSubstr) < len(a[start: end+1]):
            maxSubstr = a[start: end+1]

        end += 1

print(maxSubstr)