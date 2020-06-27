A = [0,2,1,0]

max = len(A)-1   
for i in range(len(A)-1):
    if A[i]> A[i+1]:
        max = i
        break
        
print(max)