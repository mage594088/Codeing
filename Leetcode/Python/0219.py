nums = [1,0,1,1]
k = 1

t = 0
dict = {}
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        for j in range(i):
            if nums[j] == nums[i]:
                if i-j <= k:
                    t = 1
                    break
if t == 0:
    print(False)
else:
    print(True)