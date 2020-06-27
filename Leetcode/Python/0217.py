nums = [1,1,1,3,3,4,3,2,4,2]

dict = {}
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        print(True)

print(False)