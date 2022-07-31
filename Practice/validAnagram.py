"""
isAnagram question - Create an array of length 26,
for char a, the index is = 0 and for index z the index is 25, increment the count wherever char at s
is found and decrement the count at t
Thus if there is an anagram, the final counts will be 0 after incrementing and decrementing!!!
Thus return False and True depending on that!!
"""

s = input()
t = input()


def validAnagram():
    if len(s) != len(t):
        return False

    arr = [0] * 26

    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1

    for i in range(len(arr)):
        if arr[i] != 0:
            return False

    return True


validAnagram()


