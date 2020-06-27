n = 7

a = str(bin(n)[2:])

for i in range(len(a)-1):
    if a[i]=='1' and a[i+1]=='1':
        print(False)
        break
    if a[i]=='0' and a[i+1]=='0':
        print(False)
        break
        
print(True)