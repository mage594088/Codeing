import operator
nums = [2,2,1,1,1,2,2, 3]

output = 0
dict = {}

for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        dict[nums[i]] += 1
    
output = max(dict.items(), key=operator.itemgetter(1))[0]

print(output)