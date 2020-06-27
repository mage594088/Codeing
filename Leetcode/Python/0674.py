nums = []

output = 1
list = []
if len(nums) == 0:
    print(0)
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        output += 1
    else:
        list.append(output)
        output = 1
list.append(output)

max = 0
for i in range(len(list)):
    if list[i] > max:
        max = list[i]

print(max)