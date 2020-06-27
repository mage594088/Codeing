n = 8
output = []
output.append(0)
output.append(1)
output.append(2)
output.append(3)
output.append(5)
for i in range(5, n+1):
    output.append(output[i-1] + output[i-2])

print(output[n])
            
        