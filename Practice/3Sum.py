"""
Sort the array,
hold first elem,
apply 2 sum using 2 pointers on the from second elem to last
Continue this loop until u process n-2 elems....

Things to take care off -
1. repeated elems - if arr[i]  == arr[i-1], then dont do 2 sum again, just continue ex - -1, -1, 0 2 3 ..
    process for index 0, then ignore the index 1 as both their values are same
2. inside the 2 sum, proceed till u get diff elems, .. see the code for more details

"""

arr = [int(x) for x in input().split()]

def threeSum():

    arr.sort()
    newArr = []

    for i in range(len(arr)-2):

        if i == 0 or (i>0 and arr[i] != arr[i-1]):

            start = i+1
            end = len(arr)-1

            while start < end:

                # print(i, start, end)
                currSum = arr[start] + arr[end] + arr[i]
                if currSum == 0:
                    newArr.append([arr[start], arr[end], arr[i]])

                    # ignore the duplicate elements in the inner 2 sum
                    while start < end and arr[start] == arr[start + 1]:
                        start += 1

                    # ignore the duplicate elements in the inner 2 sum
                    while start < end and arr[end] == arr[end - 1]:
                        end -= 1

                    # just last increment start and end to point to next elem other than dupes
                    start += 1
                    end -= 1

                elif currSum > 0:
                    end -= 1
                else:
                    start += 1




    return newArr

print(threeSum())






print(threeSum())