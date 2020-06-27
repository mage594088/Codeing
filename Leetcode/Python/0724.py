nums = [-1,-1,0,1,1,0]

output = []
sum = 0

output.append(0)
for i in range(len(nums)):
    sum = sum + nums[i]
    output.append(sum)

print(output[5], sum, nums[5])

for i in range(len(nums)):
    if 2 * output[i] == sum - nums[i]:
        print(i)

print(-1)
print(output)