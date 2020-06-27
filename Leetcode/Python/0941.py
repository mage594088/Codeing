A = [0,1,2,3,4,5,6,7,8,9]

s = 0
if len(A) < 3:
    s = 1
elif A[0] >= A[1]:
    s = 1
else:
    for i in range(len(A)-1):
        if A[i] >= A[i+1]:   #i = 2成立
            for j in range(i, len(A)-1):  #j = 3開始
                s = 0
                if A[j] <= A[j+1]:
                    s = 1
                    break
            break
        s = 2    
if s != 0:
    print(False)
else:
    print(True)