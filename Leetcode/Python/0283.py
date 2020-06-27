nums = [0,1,0,3,12]

output = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == 0 and nums[j] != 0:
            k = nums[i]
            nums[i] = nums[j]
            nums[j] = 0
            i = j+1
            break
    print(nums)
