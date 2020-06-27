A = [1,2,3,3]

dict = {}
for i in range(int(len(A)/2)+2):
    if A[i] not in dict:
        dict[A[i]] = 1
    else:
        print(A[i])
