nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

dict1 = {}
dict2 = {}
output = []

for i in range(len(nums1)):
    if nums1[i] not in dict1:
        dict1[nums1[i]] = 1

print(dict1)
        
for i in range(len(nums2)):   
    if nums2[i] not in dict2:
        if nums2[i] in dict1:
            output.append(nums2[i])
            dict2[nums2[i]] = 1

print(output)