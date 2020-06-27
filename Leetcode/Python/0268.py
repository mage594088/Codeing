nums = [0]

dict = {}
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1

for i in range(len(nums)):
    if i not in dict:
        print(i)
        
if i == len(nums)-1:
    print(i+1)