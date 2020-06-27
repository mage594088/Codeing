n = 11

temp = []
temp.append(n)
a = str(n)
k = 1
    
while(a != "1"):
    if a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "8":
        print(False)
        break
    a = str(a)
    b = []
    c = 0
    for i in range(len(a)):
        b.append(int(a[i]))
        c = c + b[i]*b[i]
        
    temp.append(c)
    a = str(temp[k])
    k+=1
    
        
print(True)

print(temp)

