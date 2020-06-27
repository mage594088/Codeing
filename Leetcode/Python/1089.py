arr = [0,0,0,0,0,0,0]

i = 0
while(i < len(arr)):
    if arr[i] == 0:
        if i+1 != len(arr):
            for j in range(len(arr)-i-2):
                arr[-j-1] = arr[-2-j]
            arr[i+1] = 0
            i+=1
    i+=1
        
print(arr)