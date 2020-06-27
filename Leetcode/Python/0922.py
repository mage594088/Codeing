A = [3,1,2,4]

output = []
output1 = []
output2 = []
for i in range(len(A)):
    if A[i]%2 == 0:
        output1.append(A[i])
    else:
        output2.append(A[i])

for i in range(len(output1)):
    output.append(output1[i])
    output.append(output2[i])

print(output)