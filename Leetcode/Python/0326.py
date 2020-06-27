n = 531441

output = []
output.append(1)
output.append(3)
output.append(9)
output.append(27)
output.append(81)
output.append(243)
output.append(729)
for i in range(7):
    if n == output[i]:
        print(True)
        break   
for i in range(7, 20):
    output.append(output[i-1]*3)
    if n == output[i]:
        print(True)
        break
        
print(output)
print(False)


