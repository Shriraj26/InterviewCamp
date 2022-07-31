"""
Given a string, return a longest Palindromic Substring that is present in that string...

We apply a expand from the middle procedure in this, for every char in the string,
we take left and right pointer, and expand left to left and right to right,
and record the longest length and string found till now
"""

s = input()

def longestPalindromicSubstring():

    resultLen = [0]
    resultString = ''

    def calculateLongestPalindrome(left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if right - left + 1 > resultLen[0]:
                print(s[left: right+1])
                resultString = s[left: right + 1]
                resultLen[0] = right - left + 1
                # print(left - right + 1, resultLen[0])

            left -= 1
            right += 1


    for i in range(len(s)):

        # odd length palindrome
        calculateLongestPalindrome(i, i)
        # print(resultLen)
        # print(resultString)
        # even length palindrome
        calculateLongestPalindrome(i, i+1)
        # print(resultLen)
        # print(resultString)

    print(resultString)
    print(resultLen)

longestPalindromicSubstring()