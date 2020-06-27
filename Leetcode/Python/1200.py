arr = [3,8,-10,23,19,-4,-14,27]
 
arr.sort()

output1 = []
output2 = []

for i in range(len(arr)-1):
    output1.append(arr[i+1]-arr[i])
    output2.append([arr[i], arr[i+1]])
ans = []
m = 10000000
for i in range(len(output1)):
    if m > output1[i]:
        m = output1[i]
for i in range(len(output1)):
    if m == output1[i]:
        ans.append(output2[i])
        
print(ans)