A = [3,1,2,4]

output = []
for i in range(len(A)):
    if A[i]%2 == 0:
        output.append(A[i])

for i in range(len(A)):
    if A[i]%2 == 1:
        output.append(A[i])

print(output)