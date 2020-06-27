nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

i = 0
j = 0
output = []
for k in range(n+m):
    if i<m and j<n:
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i+=1
        else:
            output.append(nums2[j])
            j+=1
    elif j<n:
        output.append(nums2[j])
        j+=1
    else:
        output.append(nums1[i])
        i+=1

for k in range(n+m):
    nums1[k] = output[k]

print(nums1)