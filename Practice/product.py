arr = [int(x) for x in input().split()]

ans = [None] * len(arr)
ans[0] = 1

for i in range(1, len(arr)):
    ans[i] = ans[i-1] * arr[i-1]

rightProd = 1

for i in range(len(arr)-1, -1, -1):
    ans[i] = ans[i] * rightProd
    rightProd = rightProd * arr[i]

print(ans)

