nums1 = [1,2,2,1]
nums2 = [2,2]

dict1 = {}
output = []

for i in range(len(nums1)):
    if nums1[i] not in dict1:
        dict1[nums1[i]] = 1
    else:
        dict1[nums1[i]] += 1

print(dict1)
        
for i in range(len(nums2)):  
    if nums2[i] in dict1:
        if dict1[nums2[i]] > 1:
            if nums2[i] in dict1:
                output.append(nums2[i])
                dict1[nums2[i]] -= 1
        elif dict1[nums2[i]] == 1:
            if nums2[i] in dict1:
                output.append(nums2[i])
                del dict1[nums2[i]]

print(output)