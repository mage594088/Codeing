import operator
nums = [2,2,1]

output = 0
dict = {}

for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        del dict[nums[i]]
    
output = max(dict)

print(output)