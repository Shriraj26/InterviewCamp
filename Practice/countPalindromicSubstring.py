"""


"""
s = input()
n = len(s)
def countFromi(left, right):

    count = 0
    while left >= 0 and right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1

    return count

def countAll():

    total = 0
    for i in range(len(s)):

        # count odd
        countOdd = countFromi(i, i)

        # count even
        countEven = countFromi(i, i+1)

        print('Odd and even and i',countOdd, countEven, i)

        total += countOdd + countEven

    print('Final Total - ', total)

countAll()