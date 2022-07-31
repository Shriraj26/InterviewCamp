
row = int(input())
col = int(input())
# word = input()
# wordLen = len(word)

board = [[x for x in input().split()] for y in range(row)]
print(board)

word = input()
wordLen = len(word)
print(word, wordLen)
visited = set()


def oob(i, j):
    if i >= row or i < 0 or j >= col or j < 0:
        return True
    return False


def travel(i, j, wordPtr):

    if wordPtr == wordLen - 1:
        return True

    if oob(i, j) or wordPtr > wordLen or (i, j) in visited:
        return False

    # print(i, j, wordPtr, word[wordPtr])
    if board[i][j] != word[wordPtr]:
        return False



    visited.add((i, j))

    # process
    pts = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
    for pt in pts:
        if travel(pt[0], pt[1], wordPtr + 1):
            return True

    visited.remove((i, j))

    return False

def findWord():

    for i in range(row):
        for j in range(col):
            if travel(i, j, 0):
                return True

    return False

print(findWord())
