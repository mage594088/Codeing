nums = [1, 2]
k = 3

dig = len(nums)

if dig > k:
    tmp = []
    for i in range(k):
        tmp.append(nums[dig-i-1])

    for j in range(dig - k):
        nums[dig - 1 - j] = nums[dig - 1 - k - j]

    for i in range(k):
        nums[i] = tmp[k - 1 - i]
else:
    while(k > dig):
        k = k - dig
    tmp = []
    for i in range(k):
        tmp.append(nums[dig-i-1])

    for j in range(dig - k):
        nums[dig - 1 - j] = nums[dig - 1 - k - j]

    for i in range(k):
        nums[i] = tmp[k - 1 - i]

print(nums)