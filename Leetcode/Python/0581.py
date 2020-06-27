nums = [2, 6, 4, 8, 10, 9, 15]

n = []
for i in range(len(nums)):
    n.append(nums[i])
n.sort()

max = len(nums)
k = 0
for i in range(len(nums)):
    if n[i] != nums[i]:
        if k == 0:
            a = i
            k += 1
        else:
            b = i
if k == 0:
    print(0)
else:
    print(b-a+1)