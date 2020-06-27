L = 15
R = 16

output = 0
for num in range(L, R+1):
    nums = str(bin(num)[2:])
    numi = int(nums)

    num1 = 0
    for i in range(len(nums)):
        if nums[i] == '1':
            num1 += 1

    nump1 = 0
    for i in range(2, num1):
        if num1%i == 0:
            nump1 += 1
            
    if num1 == 1:
        nump1 = 1
        
    #print(numi, num1)
    
    if nump1 == 0:
        output += 1
        
print(output)

