


arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
A = [[1,2,3],[4,5,6],[7,8,9]]

d1 =[arr[i][len(arr)-1-i] for i in range(len(arr))]
d2 = [arr[i][i] for i in range(len(arr))]

# print(d1)
# print(d2)

row = len(arr)
col = len(arr[0])

# n = [ [arr[i][j] for j in range(col) if (i == j or j == len(arr)-1-i) ] for i in range(row)]
# print(n)

n2 = [arr[i][len(arr)-1-i] for i in range(row) ]

x = [arr[i][row - 1 - i] for i in range(row)]
print(x)



# print([ A[i][j] for i in range(len(A)) for j in range(len(A[i])) if  (A[i][j]==A[i][len(A)-1-i] or A[i][j]== A[i][i]) and A[i][j]%2==0])