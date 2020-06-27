nums = [0,0,3,2]

output1 = 0
output2 = 0
k = 0

for i in range(len(nums)):
    if nums[i] > output1:
        output1 = nums[i]
        k = i

for i in range(len(nums)):
    if nums[i] > output2 and nums[i] != output1:
        output2 = nums[i]

if output1 >= output2 * 2:
    print(k)
else:
    print(-1)