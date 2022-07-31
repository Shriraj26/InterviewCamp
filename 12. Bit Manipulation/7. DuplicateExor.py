"""
In exor, the same element cancels itself!! so if there is a question to find the unique elem in qrray or duplicates,
u can ex-or all the elements and then get the unique one!!

Function 1 - find the missing number in the array that is from 0 to n

Function 2 0 find the unique number in array where all other numbers are repeated.
"""

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

def findTheMissingNumber():

    # get the exor from 0 to n
    myExor = 0
    for i in range(1,len(arr1)+1):
        myExor ^= i

    # Now, the numbers that are there in array will cancel out other numbers and only the missing one will remain
    for i in range(len(arr1)):
        myExor ^= arr1[i]

    return myExor

def findTheUniqueNumber():

    myExor = arr2[0]
    for i in range(1,len(arr2)):
        myExor ^= arr2[i]

    return myExor

print(findTheMissingNumber())
print(findTheUniqueNumber())