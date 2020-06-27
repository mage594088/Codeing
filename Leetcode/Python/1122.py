arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

dict1 = {}
for i in range(len(arr2)):
    dict1[arr2[i]] = 0

output = []
tmp = []
dict2 = dict1

for i in range(len(arr1)):
    if arr1[i] not in dict1:
        tmp.append(arr1[i])
    else:
        dict2[arr1[i]] += 1
        
tmp.sort()

for i in range(len(arr2)):
    for j in range(dict2[arr2[i]]):
        output.append(arr2[i])
        
for i in range(len(tmp)):
    output.append(tmp[i])

print(output)