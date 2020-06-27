A = [1,2,1]

A.sort(reverse = True)

for i in range(len(A)-2):
    if A[i] < A[i+1] + A[i+2]:
        print(A[i]+A[i+1]+A[i+2])

print(0)
        