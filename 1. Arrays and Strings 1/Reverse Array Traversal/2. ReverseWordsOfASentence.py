"""
Given a sentence - "i live in a house" convert it to -  "house a in live i".
end will point to len(str) and start will point to len(str) - 1, then decrease start, if u encounter
a space, then push a new word from s[start:end]
"""

s = input()
start = len(s)-1
end = len(s)
newStr = ''

while start >= 0:
    if s[start] == ' ':
        if len(newStr) > 0:
            newStr += ' '
        word = s[start+1 : end]
        newStr += word
        end = start
    start -= 1

if len(newStr) > 0:
    newStr += ' '
word = s[start+1 : end]
newStr += word
print(newStr)

#print(start)


