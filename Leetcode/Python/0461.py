x = 3
y = 1

a = str(bin(x)[2:])
b = str(bin(y)[2:])
c = ""
if len(a) < len(b):
    for i in range(len(b)-len(a)):
        c += "0"
    c += a
else:
    for i in range(len(a)-len(b)):
        c += "0"
    c += b

output = 0
for i in range(len(c)):
    if len(a) < len(b):
        if c[i] != b[i]:
            output += 1
    else:
        if c[i] != a[i]:
            output += 1
        
print(output)