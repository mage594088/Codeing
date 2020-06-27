nums = [2, 7, 11, 15]
target = 9

dict = {}
       
for i in range(len(nums)):
    if target - nums[i] not in dict:
        dict[nums[i]] = i
    else:
        print(dict[target - nums[i]]+1, i+1)