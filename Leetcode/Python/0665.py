nums = [3,4,2,3]

n1 = []
n2 = []
for i in range(len(nums)):
    n1.append(nums[i])
    n2.append(nums[i])
    
for i in range(len(nums)-1):
    if n1[i] > n1[i+1]:
        n1[i] = n1[i+1]
        break

for i in range(len(nums)-1):
    if n2[i] > n2[i+1]:
        n2[i+1] = n2[i]
        break

k = 0
for i in range(len(nums)-1):
    if n1[i] > n1[i+1]:
        k += 1
        break

for i in range(len(nums)-1):
    if n2[i] > n2[i+1]:
        k += 1
        break

if k == 2:
    print(False)
else:
    print(True)