matrix = [[58,25,63],[30,17,36],[90,62,21]]

row = len(matrix)       #3
col = len(matrix[0])    #4
num = []
output = []
m = min(row, col)

if row != col:
    for i in range(m):
        num.append(i+1)
    for i in range(abs(row-col)-1):
        num.append(m)
    for i in range(m):
        num.append(m-i)
else:
    for i in range(m):
        num.append(i+1)
    for i in range(m-1):
        num.append(m-i-1)
            
for i in range(row, -col, -1):
    for j in range(row):
        for k in range(col):
            if j-k == i:
                output.append(matrix[j][k])

print(num)
print(output)

same = 0
i = 0
j = 0
k = 0
while i < len(output):
    for j in range(num[k]):
        print(output[i], output[i+j], i, j, k)
        if output[i] != output[i+j]:
            same = 1
            break
    if same == 1:
        break
    k+=1
    i+=num[j]
    
if same == 0:
    print(True)
else:
    print(False)
    
        