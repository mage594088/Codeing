nums = [1, 1]

dict = {}
output = []
max = 1
if nums == []:
    output = []
else:
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    if len(nums) > max:
        max = len(nums)
        output.append(max)
            
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
    
    for i in range(1, max):
        if i not in dict:
            output.append(i)
        
print (output)
