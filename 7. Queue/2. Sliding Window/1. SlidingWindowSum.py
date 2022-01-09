"""
Sliding Window... when it comes to sliding window, it is best to use queue!!! u can consider the window as a queue itself
and then perform operations as u like...
One such question that we will be solving is  -
Given an array of integers A, find the sum of sliding windows of size N. For example: if A = [2,3,5,6,2,1]

Sliding Window Sums:
[2,3,5,6,2,1] => 10 (2+3+5)
[2,3,5,6,2,1] => 14 (3+5+6)
[2,3,5,6,2,1] => 13 (5+6+2)
[2,3,5,6,2,1] => 9  (6+2+1)


"""



print('Enter the array - ')
arr = [int(x) for x in input().split()]
n = int(input('Enter the window size'))

q = []

newSum = 0
resultArr = []
for i in arr:

    if len(q) < n:
        q.append(i)
        newSum += i
    elif len(q) == n:

        elem = q.pop(0)
        resultArr.append(newSum)
        newSum = newSum - elem + i
        q.append(i)
resultArr.append(newSum)

print(resultArr)

