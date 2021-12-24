"""
Given a sentence - "i live in a house" convert it to -  "house a in live i".
This is very similar to the string reversal problem made using 2 pointers start and end, decrement
end adn increment start till start <= end...
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


