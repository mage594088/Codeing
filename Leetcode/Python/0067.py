a = "1010"
b = "1011"

x = int(a, base=2)
y = int(b, base=2)
z = x+y

tmp = str(bin(z))
print(tmp[2:])

