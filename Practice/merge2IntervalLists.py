"""
This is the FB question to merge 2 interval lists
"""

# n1 = int(input('Enter len of input 1'))
# print('Enter arr 1')
# arr1 = [[int(x) for x in input().split()] for j in range(n1)]
# n2 = int(input('Enter len of input 2'))
# print('Enter arr 2')
# arr2 = [[int(x) for x in input().split()] for j in range(n2)]

arr1 = [[1,5],[10,14],[16,18]]
arr2 = [[2,6],[8,10],[11,20]]

i = 0
j = 0
res = []
while i < len(arr1) or j < len(arr2):

    print(i, j)
    if i == len(arr1):
        curr = arr2[j]
        j += 1

    elif j == len(arr2):
        curr = arr1[i]
        i += 1

    elif arr1[i][0] < arr2[j][0]:
        curr = arr1[i]
        i += 1
    else:
        curr = arr2[j]
        j += 1

    # Merging condition
    if res and res[-1][1] >= curr[0]:
        res[-1][1] = max(res[-1][1], curr[1])
    else:
        res.append(curr)

print(res)




