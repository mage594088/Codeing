N = 8

a = str(bin(N)[2:])

output = []
for i in range(len(a)):
    if a[i] == '1':
        output.append(i)
        
c = 0
dig = len(output)
for i in range(dig-1):
    if c < output[i+1] - output[i]:
        c = output[i+1] - output[i]
        
print(c)