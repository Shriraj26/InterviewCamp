


x = int(input())
y = int(input())

def getSumOfdigits(num, y):


    if num == 0:
        return 0

    strNum = str(num)
    sum = 0
    for i in strNum:
        sum += int(i)


    return sum

Totalsum = 0
for i in range(x):

    if y == getSumOfdigits(i, y):
        Totalsum = Totalsum + 1

        print(Totalsum, i)

print(Totalsum)

