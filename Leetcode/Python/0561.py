nums = [1,2,3,2]

b = sorted(nums)
sum = 0
print(b)
for i in range(0, len(nums), 2):
    sum = sum + b[i]

print(sum)