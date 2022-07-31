"""
Traverse the matrix in spiral order...
Mantain 4 pointers t, b, r, l and then follow this order
First from left to right until u reach right, decrease top pointer
From right to bottom until u reach bot, decrease the right pointer
then from bot right to left till u reach left, decrease the bot pointer,
then top, till u reach top, decrease the left ptr,
"""

row = int(input())
col = int(input())
board = [[int(x) for x in input().split()] for y in range(row)]

top = 0
left = 0
right = col
bot = row
res = []
while top < bot and left < right:

    #finish from left --> right
    for i in range(left, right):
        res.append(board[top][i])
    top += 1

    # finish from right to bot
    for i in range(top, bot):
        res.append(board[i][right-1])
    right -= 1

    if not (left < right and top < bot):
        break

    # finish from right bot to left bot
    for i in range(right-1, left-1, -1):
        res.append(board[bot-1][i])
    bot -= 1

    # finish bot left to top
    for i in range(bot-1, top-1, -1):
        res.append(board[i][left])
    left += 1

print(res)