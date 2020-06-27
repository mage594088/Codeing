A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

row = len(A)
col = len(A[0])
for i in range(row):
    for j in range(col//2):
        k = A[i][j]
        A[i][j] = A[i][col-1-j]
        A[i][col-1-j] = k

print(A)

for i in range(row):
    for j in range(col):
        if A[i][j] == 1:
            A[i][j] = 0
        elif A[i][j] == 0:
            A[i][j] = 1
            
print(A)