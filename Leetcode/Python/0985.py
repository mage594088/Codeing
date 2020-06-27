A = [3,2]
queries = [[4,0],[3,0]]

output = []
sum = 0

for i in range(len(A)):
    if A[i]%2 == 0:
        sum += A[i]
        
for i in range(len(queries)):
    if queries[i][1] >= 0 and queries[i][1] < len(A):
        if (A[queries[i][1]] + queries[i][0]) % 2 == 0:            
            if A[queries[i][1]] % 2 == 0:
                A[queries[i][1]] += queries[i][0]
                sum += queries[i][0]
            else:                
                A[queries[i][1]] += queries[i][0]
                sum += A[queries[i][1]]

        else:
            if A[queries[i][1]]%2 == 0:
                sum -= A[queries[i][1]]
                A[queries[i][1]] += queries[i][0]
            else:
                A[queries[i][1]] += queries[i][0]

    output.append(sum)

print(output)
