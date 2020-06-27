flowerbed = [1,0,0,0,1]
n = 2

count = 0
if len(flowerbed) == 1 and flowerbed[0] == 0:
    count += 1
else:    
    if flowerbed[0] ==0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        count += 1
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i-1] ==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    if flowerbed[-1] ==0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        count += 1   
print(count)        
if count < n:
    print(False)
else:
    print(True)