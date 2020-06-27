A = [[1,2,3],[4,5,6]]

row = len(A)
col = len(A[0])
num = []
output = []
for i in range(row):
    for j in range(col):
        num.append(A[i][j])
        
print(num)

for i in range(col):
    tmp = []
    for j in range(row):
        tmp.append(num[i+j*col])
    output.append(tmp)
    
print(output)