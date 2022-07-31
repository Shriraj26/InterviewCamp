# def count(s):
#     cnt = 0
#
#     for c in s:
#         if c == 'a':
#             cnt += 1
#     if cnt % 3 != 0:
#         return 0
#
#     res = 0
#     k = cnt // 3
#     sum = 0
#
#     mp = {}
#
#     for i in range(len(s)):
#
#         if s[i] == 'a':
#             sum += 1
#
#         if sum == 2 * k and k in mp and len(s) - 1 > i > 0:
#             res += mp[k]
#
#         # Insert sum in map
#         if sum in mp:
#             mp[sum] += 1
#         else:
#             mp[sum] = 1
#
#     return res
#

import math

def getBitsFromDecimal(number):
    number = -number
    result = []
    while number != 0:
        result.append(number % 2)
        number /= -2
    return result


def getDecimalFromBits(bits):
    result = 0;
    for index, bit in enumerate(bits):
        result += bit * int(math.pow(-2, index))
    return result


def solution(A, B):
    decA = getDecimalFromBits(A)
    decB = getDecimalFromBits(B)
    sum = decA + decB
    print(getBitsFromDecimal(sum))
    return getBitsFromDecimal(sum)


# s = input()
# print(count(s))

# print(bin(2))
print(format(30, 'b'))
print(bin(30)[2:].zfill(8))

# solution([0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1])