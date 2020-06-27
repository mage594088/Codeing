n = 3

output = []
output.append(0)
output.append(1)
output.append(4)
output.append(9)
output.append(16)
output.append(25)
output.append(36)
output.append(49)
output.append(64)
output.append(81)
output.append(100)
output.append(121)
output.append(144)
output.append(169)
output.append(196)
output.append(225)
output.append(256)
output.append(289)
output.append(324)
output.append(361)
output.append(400)

for i in range(21):
    if n == output[i]:
        print(True)
        break   
for i in range(21, 46341):
    output.append(i*i)
    if n == output[i]:
        print(True)
        break        

print(output)
print(False)


