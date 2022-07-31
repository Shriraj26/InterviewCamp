ipPhoneNo = input()

phoneNo = ''
for i in ipPhoneNo:

    if i != '0' and i != '1':
        # print(i, i != '1')
        phoneNo += i


# print(phoneNo)
buff = [None] * len(phoneNo)

myDict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def generateCombos(startINdex, buffINdex):

    if buffINdex == len(buff):
        print(buff)
        return

    if startINdex == len(phoneNo):
        return

    for letter in myDict[phoneNo[startINdex]]:

        buff[buffINdex] = letter
        generateCombos(startINdex + 1, buffINdex + 1)

generateCombos(0, 0)

