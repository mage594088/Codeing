nums1 = [4,1,2]
nums2 = [1,3,4,2]

n1 = len(nums1)
n2 = len(nums2)
dict = {}

if len(nums1) == 0:
    print([])
    
for i in range(n1):
    for j in range(n2):
        if nums1[i]==nums2[j]:
            if nums1[i] not in dict:
                dict[nums1[i]] = j

output = []
for i in range(n1):
    found = 0
    for j in range(dict[nums1[i]], n2):
        if nums1[i] < nums2[j]:
            output.append(nums2[j])
            found = 1
            break
    if found == 0:
        output.append(-1)
        
print(output)