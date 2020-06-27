N = 5

output = []
output.append(0)
output.append(1)
output.append(1)
output.append(2)
output.append(3)
output.append(5)
output.append(8)
output.append(13)
output.append(21)
output.append(34)
for i in range(10, 31):
    output.append(output[i-1] + output[i-2])
    
print(output[N])


