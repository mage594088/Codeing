nums = [1,5,3,2,2,7,6,4,8,9]

dict = {}
dig = len(nums)
output1 = 0
output2 = dig
k = 0

for i in range(dig):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        k = i
output1 = nums[k]

for i in range(1, dig):
    if i not in dict:
        output2 = i
        
if dig == 2 and nums[0] == 1:
    output2 = 2
elif dig == 2 and nums[0] == 2:
    output2 = 1

ret = []
ret.append(output1)
ret.append(output2)
print(ret)